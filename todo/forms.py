from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_completed']
        # fields = "__all__" # this will include owner info, not we want
