""" forms module """
from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    """ Tasks form model """
    class Meta:
        """ Meta class for form model """
        cssStyleForm = 'appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'
        model = Tasks
        fields = ['title', 'description', 'completed']
        widgets = {
            "title": forms.TextInput(attrs={
                'class': cssStyleForm,
                'id': 'input-title',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': cssStyleForm,
                'id': 'textaera-description',
                'rows': '5',
                'required': True
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'leading-tight',
                'id': 'checkbox-completed',
            })
        }
