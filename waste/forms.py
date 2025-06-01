from django import forms
from .models import WasteListing

class WasteListingForm(forms.ModelForm):
    class Meta:
        model = WasteListing
        fields = ['waste_type', 'quantity', 'description', 'location', 'image']
        widgets = {
            'waste_type': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={
                'placeholder': 'e.g., 2 heaps, 5 sacks',
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Additional details (e.g., color, condition)',
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'e.g., Kampala',
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity', '').strip()
        if quantity:
            parts = quantity.split()
            if len(parts) < 2 or not parts[0].replace('.', '').isdigit():
                raise forms.ValidationError("Please enter a quantity with a unit (e.g., '2 heaps', '5 sacks').")
        return quantity