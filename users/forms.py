from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Profile

class UserRegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=Profile.USER_TYPE_CHOICES,
        widget=forms.RadioSelect
    )
    location = forms.CharField(max_length=100)
    contact = forms.CharField(
        max_length=15,
        required=False,
        help_text="Phone number in format: +256XXXXXXXXX"
    )
    accepted_waste_types = forms.MultipleChoiceField(
        choices=Profile.WASTE_TYPE_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 
                 'location', 'contact', 'accepted_waste_types']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = """
        <ul class="text-xs text-gray-500 list-disc pl-5">
            <li>At least 8 characters</li>
            <li>Not too common</li>
            <li>Not entirely numeric</li>
            <li>Shouldn't be similar to username</li>
        </ul>
        """
        
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            validate_password(password1, self.instance)
        except ValidationError as error:
            self.add_error('password1', error)
        return password1

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        
        if user_type in ['collector', 'recycler']:
            if not cleaned_data.get('contact'):
                self.add_error('contact', "Contact information is required for collectors/recyclers")
            
            # Check if at least one waste type is selected
            if not cleaned_data.get('accepted_waste_types'):
                self.add_error('accepted_waste_types', "Please select at least one waste type you collect/produce")
        
        return cleaned_data

class QuickRegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=Profile.USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    location = forms.CharField(max_length=100, required=False)
    contact = forms.CharField(
        max_length=15,
        required=False,
        help_text="Phone number in format: +256XXXXXXXXX"
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type', 'location', 'contact']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = """
        <ul class="text-xs text-gray-500 list-disc pl-5">
            <li>At least 8 characters</li>
            <li>Not too common</li>
            <li>Not entirely numeric , mix of letters(capital and small),numbers and special symbols,</li>
        </ul>
        """

    def save(self, commit=True):
        user = super().save(commit)
        profile, created = Profile.objects.get_or_create(user=user)
        profile.user_type = self.cleaned_data.get('user_type') or 'quick_access'
        profile.location = self.cleaned_data.get('location') or None
        profile.contact = self.cleaned_data.get('contact') or None
        profile.save()
        return user