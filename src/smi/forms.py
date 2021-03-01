from django import forms
from .models import Comments
from django.forms import ModelForm, Textarea



class CommentsForm(forms.ModelForm):
    user_name = forms.CharField(label = '',max_length = 2000,required = True,widget = forms.TextInput(attrs = {'class': 'wrap-input100 validate-input input100','placeholder': 'Ваше имя'}))
    user_email = forms.CharField(label = '',max_length = 2000,required = True,widget = forms.TextInput(attrs = {'class': 'wrap-input100 validate-input input100','placeholder': 'E-mail'}))
    user_comment = forms.CharField(label = '',max_length = 12000,required = True,widget = forms.Textarea(attrs = {'class': 'wrap-input100 validate-input input100','placeholder': 'Сообщение'}))

    class Meta:
        model = Comments
        fields = ('user_name', 'user_email','user_comment',)
