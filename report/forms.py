from django import forms
from django.core.exceptions import ValidationError
from .models import DumpingReport
import os

class DumpingReportForm(forms.ModelForm):
    class Meta:
        model = DumpingReport
        fields = ['photo', 'waste_type', 'district', 'description', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
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