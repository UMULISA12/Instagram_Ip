from django import forms
from .models import Image,Profile,Comment


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user','likes','upload_date','profile']



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','comment_date','image',]