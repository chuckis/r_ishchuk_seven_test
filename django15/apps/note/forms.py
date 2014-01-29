from django import forms
from django15.apps.note.models import Note
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class NoteForm(forms.ModelForm):
    body = forms.CharField(max_length=1000, validators=[MinLengthValidator(10)], 
    error_messages={'min_length': _('Ensure message has at least %(limit_value)d characters (it has %(show_value)d).')})
    class Meta:
        model = Note
        fields = ('title', 'body')

