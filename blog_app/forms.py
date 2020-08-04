from django import forms
from .models import Post, Subscription

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
