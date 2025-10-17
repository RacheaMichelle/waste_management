from django import forms
from django.core.exceptions import ValidationError
from .models import DumpingReport
import os

class DumpingReportForm(forms.ModelForm):
    reporter_name = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name (optional)',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )
    reporter_email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email (optional)',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )
    reporter_phone = forms.CharField(
        required=False,
        max_length=15,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your phone (optional)',
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
        })
    )

    class Meta:
        model = DumpingReport
        fields = [
            'reporter_name', 'reporter_email', 'reporter_phone',
            'photo', 'waste_type', 'district', 'description', 'latitude', 'longitude'
        ]
        widgets = {
            'latitude': forms.HiddenInput(attrs={'id': 'id_latitude'}),
            'longitude': forms.HiddenInput(attrs={'id': 'id_longitude'}),
            'photo': forms.FileInput(attrs={
                'class': 'w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe the dumping situation...',
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'waste_type': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'district': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')
        
        # Validate that location was selected
        if not latitude or not longitude:
            raise ValidationError("Please select a location on the map by clicking on your desired location.")
        
        # Basic coordinate validation for Uganda
        try:
            lat_float = float(latitude)
            lng_float = float(longitude)
            
            # Uganda approximate coordinates
            if not (-1.5 <= lat_float <= 4.5 and 29.0 <= lng_float <= 35.5):
                raise ValidationError("Please select a location within Uganda.")
        except (ValueError, TypeError):
            raise ValidationError("Invalid location coordinates.")
        
        return cleaned_data

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            raise ValidationError("Please upload a photo of the dumping site.")
            
        if photo:
            # Validate file size (max 5MB)
            max_size = 5 * 1024 * 1024
            if photo.size > max_size:
                raise ValidationError("Image file too large (max 5MB)")
            
            # Validate file extension
            valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            ext = os.path.splitext(photo.name)[1].lower()
            if ext not in valid_extensions:
                raise ValidationError("Unsupported file format. Please upload a JPG, PNG, or GIF image.")
        
        return photo