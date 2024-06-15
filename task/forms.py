from django import forms

from .constants import REPEAT_CHOICES
from .models import Task


class CreateTaskForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
                           'placeholder': 'Task Name', 'class': 'd-flex mb-2 col-md-12'}), required=True, label='Task Name')
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={'placeholder': 'dd/mm/yyyy HH:MM', 'class': 'd-flex mb-2 col-md-6'}), required=True, label='Date & Time')
    repeat = forms.ChoiceField(choices=REPEAT_CHOICES, widget=forms.Select(
        attrs={'class': 'd-flex mb-2 col-md-3'}), required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Here can be your description', 'class': 'd-flex mb-2 col-md-12'}), required=True)

    class Meta:
        model = Task
        fields = ['name', 'due_date', 'repeat', 'description',]


class SendEmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'placeholder': 'Email address', 'class': 'd-flex mb-2 col-md-6'}), required=True, label='Email Address')
