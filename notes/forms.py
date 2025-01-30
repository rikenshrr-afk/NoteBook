from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta():
        model= Note
        fields=['title','content']
        widgest={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter content'})
        }