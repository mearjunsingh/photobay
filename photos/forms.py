from .models import Photo, Category
from django import forms

class UploadForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Photo Title',
            }
        ))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', widget=forms.Select(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            }
        ))
    image = forms.ImageField(label='Photo File', widget=forms.FileInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            }
        ))
    description = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Image Description',
            'cols' : '0',
            'rows' : '3',
            }
        ))
    photo_camera = forms.CharField(label='Camera', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Camera/Phone Model',
            }
        ))
    photo_location = forms.CharField(label='Location', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Location (City)',
            }
        ))
    tags = forms.CharField(label='Tags', help_text='Use as many tags you want separeted by comma. It will help your photo to better indexing.', widget=forms.Textarea(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Separeted by comma',
            'cols' : '0',
            'rows' : '3',
            }
        ))

    class Meta:
        model = Photo
        fields = ['title', 'category', 'image', 'description', 'photo_camera', 'photo_location','tags']
    
    def clean_photo_camera(self):
        data = self.cleaned_data.get('photo_camera')
        data = data.strip()
        if data == None or data == ' ' or data == '':
            raise forms.ValidationError('This field is required.')
        return data

    def clean_photo_location(self):
        data = self.cleaned_data.get('photo_location')
        data = data.strip()
        if data == None or data == ' ' or data == '':
            raise forms.ValidationError('This field is required.')
        return data


class EditForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Photo Title',
            }
        ))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category', widget=forms.Select(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            }
        ))
    description = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Image Description',
            'cols' : '0',
            'rows' : '3',
            }
        ))
    photo_camera = forms.CharField(label='Camera', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Camera/Phone Model',
            }
        ))
    photo_location = forms.CharField(label='Location', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Location (City)',
            }
        ))
    tags = forms.CharField(label='Tags', help_text='Use as many tags you want separeted by comma. It will help your photo to better indexing.', widget=forms.Textarea(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Separeted by comma',
            'cols' : '0',
            'rows' : '3',
            }
        ))

    class Meta:
        model = Photo
        fields = ['title', 'category', 'description', 'photo_camera', 'photo_location','tags']
    
    def clean_photo_camera(self):
        data = self.cleaned_data.get('photo_camera')
        data = data.strip()
        if data == None or data == ' ' or data == '':
            raise forms.ValidationError('This field is required.')
        return data

    def clean_photo_location(self):
        data = self.cleaned_data.get('photo_location')
        data = data.strip()
        if data == None or data == ' ' or data == '':
            raise forms.ValidationError('This field is required.')
        return data