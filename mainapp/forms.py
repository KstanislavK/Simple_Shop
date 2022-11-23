from django import forms

from .models import FeedbackList


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackList
        fields = ('name', 'email', 'message')
        widgets = {'message': forms.Textarea(attrs={'rows': 3})}
