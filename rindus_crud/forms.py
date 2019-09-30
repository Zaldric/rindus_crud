from django import forms
from rindus_crud.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ("admin_id", )
