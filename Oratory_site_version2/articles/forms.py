from django import forms
from froala_editor.widgets import FroalaEditor
from . import models
from djrichtextfield.widgets import RichTextWidget

class CreateArticle(forms.ModelForm):
    
    body = forms.CharField(widget=RichTextWidget())
    class Meta:
        model=models.Article
        fields={"title","slug", "thumb"}
        