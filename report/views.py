from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading
from .forms import DumpingReportForm
from .models import DumpingReport
from .district_contacts import get_district_emails, get_primary_district_contact

def report_dumping(request):
    if request.method == 'POST':
        form = DumpingReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            
            # If user is logged in, associate with their account
            if request.user.is_authenticated:
                report.user = request.user
            
            report.save()
            
            # Send SMS notification
            district_number = get_primary_district_contact(report.district)
            sms_content = (
                f"New dumping report in {report.district}\n"
                f"Type: {report.get_waste_type_display()}\n"
                f"Location: {report.latitude}, {report.longitude}"
            )
            print(f"\nSMS would be sent to {district_number}:\n{sms_content}\n")
            
            # Send email to district authorities in background
            send_report_to_district_authorities_async(report)

            messages.success(request, "Thank you! Your report has been submitted and authorities have been notified.")
            return redirect('report_success', report_id=report.id)
    else:
        # Pre-fill location if available from logged-in user
        initial_data = {}
        if request.user.is_authenticated:
            initial_data['reporter_name'] = f"{request.user.first_name} {request.user.last_name}".strip()
            initial_data['reporter_email'] = request.user.email
        
        form = DumpingReportForm(initial=initial_data)
    
    return render(request, 'report/report_form.html', {'form': form})

def send_report_to_district_authorities_async(report):
    """Send email notification to district authorities in background thread"""
    def send_email():
        try:
            subject = f"🚨 Illegal Dumping Report - {report.get_district_display()} District"
            
            # Build reporter information
            reporter_info = ""
            if report.reporter_name:
                reporter_info = f"Reported by: {report.reporter_name}"
                if report.reporter_email:
                    reporter_info += f" ({report.reporter_email})"
                if report.reporter_phone:
                    reporter_info += f" - Phone: {report.reporter_phone}"
            elif report.user:
                reporter_info = f"Reported by registered user: {report.user.get_full_name() or report.user.username} ({report.user.email})"
            else:
                reporter_info = "Reported anonymously"
            
            # Format the date properly
            formatted_date = report.created_at.strftime('%Y-%m-%d at %H:%M:%S')
            
            # Create email content
            plain_message = f"""
URGENT: Illegal Dumping Report

{reporter_info}

LOCATION DETAILS:
• District: {report.get_district_display()}
• Waste Type: {report.get_waste_type_display()}
• Coordinates: {report.latitude}, {report.longitude}
• Description: {report.description or 'No additional description provided'}

TIMESTAMP: {formatted_date}

DISTRICT CONTACT: {get_primary_district_contact(report.district)}

This report was submitted through the Clean Uganda Platform.
Please take immediate appropriate action.

--
Clean Uganda Environmental Platform
Making Uganda Cleaner, Together
"""
            
            # Get district email addresses
            district_emails = get_district_emails(report.district)
            
            # Create context for HTML email
            context = {
                'report': report,
                'reporter_info': reporter_info,
                'district_contact': get_primary_district_contact(report.district),
                'formatted_date': formatted_date,
            }
            
            # Render HTML content
            html_message = render_to_string('report/email_report.html', context)
            
            # Send email with both plain text and HTML versions
            email = EmailMultiAlternatives(
                subject=subject,
                body=plain_message,  # This is the plain text version
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=district_emails,
                reply_to=[settings.DEFAULT_FROM_EMAIL],
            )
            
            # Attach HTML version
            email.attach_alternative(html_message, "text/html")
            
            # Attach the photo if available
            if report.photo:
                try:
                    email.attach_file(report.photo.path)
                except Exception as attach_error:
                    print(f"⚠️ Could not attach photo: {attach_error}")
            
            email.send(fail_silently=False)
            print(f"✅ Email sent successfully to: {', '.join(district_emails)}")
            
        except Exception as e:
            print(f"❌ Failed to send email to district authorities: {e}")
            # Fallback: try simple email without HTML
            send_fallback_email(report, district_emails, str(e))
    
    # Run email sending in background thread
    thread = threading.Thread(target=send_email)
    thread.daemon = True
    thread.start()

def send_fallback_email(report, district_emails, error_message):
    """Simple fallback email without HTML or attachments"""
    try:
        subject = f"URGENT: Dumping Report - {report.district}"
        
        # Build simple message
        reporter_info = ""
        if report.reporter_name:
            reporter_info = f"Reported by: {report.reporter_name}"
            if report.reporter_phone:
                reporter_info += f" (Phone: {report.reporter_phone})"
        else:
            reporter_info = "Reported anonymously"
        
        plain_message = f"""
ILLEGAL DUMPING REPORT - {report.district.upper()}

{reporter_info}

Location: {report.latitude}, {report.longitude}
Waste Type: {report.get_waste_type_display()}
Description: {report.description or 'No description'}

Time: {report.created_at.strftime('%Y-%m-%d %H:%M')}

Note: Original email with photo failed due to: {error_message}

-- Clean Uganda System
"""
        
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            district_emails,
            fail_silently=False,
        )
        print(f"✅ Fallback email sent to: {', '.join(district_emails)}")
        
    except Exception as e:
        print(f"❌ Fallback email also failed: {e}")

def report_success(request, report_id):
    report = DumpingReport.objects.get(id=report_id)
    return render(request, 'report/report_success.html', {'report': report})

# Test email view (remove in production)
from django.http import HttpResponse

def test_email(request):
    """Test email configuration - remove this in production"""
    try:
        # Test both email methods
        send_mail(
            '✅ Test Email from Clean Uganda',
            'Congratulations! Your email configuration is working correctly.',
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
        # Test HTML email
        html_content = "<h1>HTML Test</h1><p>This is an HTML email test.</p>"
        email = EmailMultiAlternatives(
            subject='✅ HTML Email Test from Clean Uganda',
            body='Plain text version',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.EMAIL_HOST_USER],
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)
        
        return HttpResponse("""
            <div style="text-align: center; padding: 50px; background: #f0f9ff;">
                <h1 style="color: #059669;">✅ Email Test Successful!</h1>
                <p style="font-size: 18px;">Both plain text and HTML emails are working correctly.</p>
                <p>Check your email inbox for the test messages.</p>
                <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #3b82f6; color: white; text-decoration: none; border-radius: 5px;">
                    Return to Homepage
                </a>
            </div>
        """)
    except Exception as e:
        return HttpResponse(f"""
            <div style="text-align: center; padding: 50px; background: #fef2f2;">
                <h1 style="color: #dc2626;">❌ Email Test Failed</h1>
                <p style="font-size: 18px;">Error: {e}</p>
                <p>Check your email settings in settings.py</p>
                <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #3b82f6; color: white; text-decoration: none; border-radius: 5px;">
                    Return to Homepage
                </a>
            </div>
        """)