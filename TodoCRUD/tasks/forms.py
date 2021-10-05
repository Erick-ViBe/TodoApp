from django import forms
from django.db.models import fields
from .models import Task


class TaskForm(forms.Form):
    description = forms.CharField(max_length=255, required=True, label="Descripcion")

    def clean_description(self):
        description = self.cleaned_data['description']
        description = description.lower()
        if 'matematicas' in description:
            raise forms.ValidationError('No pongas tarea de matematicas, no te compliques la vida bbe!!!')

        return description


class TaskModelForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['description',]
        labels = {
            'description': 'Descripcion',
        }

    def clean_description(self):
        description = self.cleaned_data['description']
        if 'matematicas' in description:
            raise forms.ValidationError('No pongas tarea de matematicas, no te compliques la vida bbe!!!')

        return description


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        #fields = ['description', 'done']
        fields = '__all__'
        labels = {
            'description': 'Descripcion',
            'done': 'Terminada',
        }