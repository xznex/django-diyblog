from django import forms


class CommentForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea, help_text='Enter comment about blog here.')
