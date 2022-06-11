from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'user_type')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['first_name'].label = 'نام'
        self.fields['last_name'].label = 'نام خانوادگی'
        self.fields['email'].label = "آدرس ایمیل"
        self.fields['user_type'].label = ":ثبت نام به عنوان "
        self.fields['password1'].label = "رمز عبور "
        self.fields['password2'].label = "تایید رمز عبور "
