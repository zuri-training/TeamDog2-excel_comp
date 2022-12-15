from django import forms
from upload.models import Document


class DocumentForm(forms.ModelForm):
    # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
    class Meta:
        model = Document
        fields = ('description', 'document',)
