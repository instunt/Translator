from django import forms
from .models import Text

class textForm(forms.ModelForm):
  class Meta:
    model = Text
    fields = ('id', 'nazovTextu', 'kapitola', 'strana', 'riadok', 'origText', 'otLanguage', 'translatedText', 'ttLanguage')

