from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CommentPost


class Registerfrom(UserCreationForm):
    email = forms.EmailField(required  = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def save(self, commit = True):
        user = super(Registerfrom, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user 


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = '__all__'




