# education/views.py
from django.shortcuts import render
from .models import Resource  # Changed from EducationalResource to Resource
from django.contrib.auth.decorators import login_required
@login_required
def resources(request):
    resources = Resource.objects.all()
    
    # Pre-process tutorial links by splitting them
    for resource in resources:
        if resource.tutorial_links:  # Changed from tutorial_link to tutorial_links
            resource.tutorial_links_list = [link.strip() for link in resource.tutorial_links.split(',') if link.strip()]
        else:
            resource.tutorial_links_list = []
    
    context = {
        'resources': resources
    }
    return render(request, 'education/resources.html', context)