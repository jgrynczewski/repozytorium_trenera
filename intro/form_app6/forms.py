from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Message

class ContactForm(forms.Form):
    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=[
        ("", '---------'),
        ('question', 'Pytanie'),
        ('other', 'Inne')
    ], label="Kategoria")
    subject = forms.CharField(required=False, label="Tytuł")
    body = forms.CharField(widget=forms.Textarea, label="Treść")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__' # możemy też wskazywać poszczególne pola,
        # lub użyć exclude
        labels = {
            "name":"Imię",
            "email":"Email",
            "category":"Kategoria",
            "subject":"Tytuł",
            "Body": "Treść"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Za pomocą obiektu FormHelper możemy obsługiwać
        # atrybuty formularza w kodzie, np method.

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit', 'Prześlij', css_class="btn btn-primary"
                                                   "")
        )