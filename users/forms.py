from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from PIL import Image
from .models import BannedUsernames
from .custom_defs import crop_max_square
from django.contrib.auth import get_user_model
User = get_user_model()

#completed
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Username',
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Password',
            }
        ))

#completed
class UserSignupForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter First Name',
            }
        ))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Last Name',
            }
        ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Email',
            }
        ))
    username = forms.CharField(label='Choose Username', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Username',
            }
        ))
    password1 = forms.CharField(label='Choose Password', widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Password',
            }
        ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Password Again',
            }
        ))

    def clean_username(self):
        data = self.cleaned_data['username']
        inv = BannedUsernames.objects.all()
        for vn in inv:
            temp, temp2 = data.lower(), vn.uname.lower()
            if temp == temp2:
                raise forms.ValidationError("You cannot use this username.")
        return data

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2']

#completed
class UserEditForm(UserChangeForm):
    profile_picture = forms.ImageField(label='Profile Picture', help_text='Leaving empty will keep previous photo.', widget=forms.FileInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            }
        ))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter First Name',
            }
        ))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Last Name',
            }
        ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Email',
            }
        ))
    profession = forms.CharField(label='Profession', required=False, widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Profession',
            }
        ))
    address = forms.CharField(label='Address', required=False, widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Address',
            }
        ))
    dob = forms.DateField(label='Date of Birth', required=False, widget=forms.DateInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'type' : 'date',
            }
        ))
    fb_username = forms.CharField(label='Facebook Username', required=False, widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Facebook Username',
            }
        ))
    tw_username = forms.CharField(label='Twitter Username', required=False, widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Twitter Username',
            }
        ))
    in_username = forms.CharField(label='Instagram Username', required=False, widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Instagram Username',
            }
        ))
    password = None

    class Meta:
        model = User
        fields = ['profile_picture','first_name', 'last_name', 'email', 'profession', 'address', 'dob', 'fb_username', 'tw_username', 'in_username']
    
    def save(self):
        photo = super(UserEditForm, self).save()

        image = Image.open(photo.profile_picture)
        cropped_image = crop_max_square(image)
        resized_image = cropped_image.resize((500, 500), Image.ANTIALIAS)
        resized_image.save(photo.profile_picture.path)

        return photo

#completed
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter Old Password',
            }
        ))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Enter New Password',
            }
        ))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Confirm New Password',
            }
        ))