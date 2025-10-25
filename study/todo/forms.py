from django import forms
from.models import Todo
from.models import Users

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["task", "coment"]
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'