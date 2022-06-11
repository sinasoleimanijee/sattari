from django.forms import ModelForm, DateInput, TimeInput, Form
from django import forms
from django.shortcuts import get_object_or_404
from resources.models import Resource
from django.utils import timezone
from courses.models import Course
from users.models import User


class CreateResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = ('resource_name', 'resource_file', 'course')


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        user_object = User.objects.filter(username=user.username)
        new_user_object = get_object_or_404(user_object)
        self.fields['course'].queryset = self.fields['course'].queryset.filter(teacher=new_user_object.id)
        self.fields['resource_name'] = forms.CharField(widget=forms.TextInput(
            attrs={
                'dir': 'rtl',
                'placeholder': 'نام منبع',
            }
        ))
        self.fields['resource_name'].label = "نام منبع"
        self.fields['resource_file'].label = "فایل منبع"
        self.fields['course'].label = "درس"
