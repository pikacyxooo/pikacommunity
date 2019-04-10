from ckeditor.widgets import CKEditorWidget
from django import forms


class BlogPulishForm(forms.Form):
    blog_content = forms.CharField(widget=CKEditorWidget())