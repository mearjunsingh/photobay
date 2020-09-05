from .models import Photo, Category
from django import forms

class UploadForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Photo Title',
            }
        ))
    slug = forms.SlugField(label='Slug', help_text='Use letters, numbers, underscores or hypens. Example: this-is-my-slug', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Photo Slug',
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
    camera = forms.CharField(label='Camera', help_text='Write your own or choose from dropdown.', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Camera/Phone Model',
            }
        ))
    location = forms.CharField(label='Location', help_text='Locations are relative.', widget=forms.TextInput(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Location (City)',
            }
        ))
    tags = forms.CharField(label='Tags', help_text='Use as many tags you want separeted by comma. It will help your photo to better indexing.', widget=forms.Textarea(
        attrs={
            'class': 'w3-input w3-border w3-margin-bottom',
            'placeholder': 'Separeted by comma',
            }
        ))

    class Meta:
        model = Photo
        fields = ['title', 'slug', 'category', 'image', 'camera', 'location', 'tags']