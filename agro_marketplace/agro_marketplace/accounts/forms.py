from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from agro_marketplace.accounts.models import Profile

UserModel = get_user_model()


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        labels = {
            'username': 'Username',
            'password': 'Password',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'
            field.widget.attrs['placeholder'] = f"Enter {self.Meta.labels.get(field_name, field_name).lower()}"


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username',
                  'email',
                  'password1',
                  'password2'
                  )

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Repeat Password',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correcting the call to super()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'
            field.widget.attrs['placeholder'] = f"Enter {self.Meta.labels.get(field_name, field_name).lower()}"


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_photo',
            'full_name',
            'username_in_marketplace',
            'email',
            'description',
            'country_code',
            'phone',
            'town',
        ]
        labels = {
            'profile_photo': 'Profile Photo',
            'full_name': 'Full Name',
            'username_in_marketplace': 'Name in Marketplace',
            'email': 'Email Address',
            'description': 'Description',
            'country_code': 'Country Code',
            'phone': 'Phone Number',
            'town': 'Town/City',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and (not phone.isdigit() or len(phone) < 10):
            raise forms.ValidationError("Phone number must be at least 10 digits and contain only numbers.")
        return phone

    def __init__(self, *args, **kwargs):
        super(ProfileCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'
            field.widget.attrs['placeholder'] = f"Enter {self.Meta.labels.get(field_name, field_name).lower()}"


class ProfileEditForm(forms.ModelForm):
    newPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        label="New Password",
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        label="Repeat New Password",
    )

    class Meta:
        model = Profile
        fields = ['profile_photo',
                  'full_name',
                  'username_in_marketplace',
                  'email',
                  'country_code',
                  'phone',
                  'town'
                  ]

        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'profile-photo-input'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username_in_marketplace': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'country_code': forms.Select(attrs={'class': 'form-control'}),  # Dropdown widget for country_code
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """
        Custom validation for password fields to ensure they match.
        """
        cleaned_data = super().clean()
        new_password = cleaned_data.get("newPassword")
        confirm_password = cleaned_data.get("confirmPassword")

        if new_password and confirm_password:
            if new_password != confirm_password:
                self.add_error('confirmPassword', "Passwords do not match.")
            if not new_password.strip():
                self.add_error('newPassword', "Password cannot be blank.")

        return cleaned_data
