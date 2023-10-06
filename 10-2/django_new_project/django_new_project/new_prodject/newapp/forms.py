from django.forms import ModelForm, CharField, TextInput
from .models import Authors ,  Quotes

class AuthorsForm(ModelForm):

    fullname = CharField()
    born_date = CharField()
    born_location = CharField()
    description = CharField()
    
    class Meta:
        model = Authors
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuotesForm(ModelForm):
    tags = CharField()
    author = CharField()
    quotes = CharField()

    class Meta:
        model = Quotes
        filds = ['tags', 'author', 'quotes']
        exclude = ['author','tags']


