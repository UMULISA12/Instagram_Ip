
from .models import Image,Comment,Profile
from django import forms

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['url', 'comments','likes','name','Profile']
        widgets = {}


class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('commented_by','body','for_image')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('profile_pic','bio','user')