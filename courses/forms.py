from .models import Course
from django.forms import ModelForm
from django import forms
class CreateCoursesForm(ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'course_description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_name'] = forms.CharField(widget=forms.TextInput(
            attrs={
                'dir': 'rtl',
                'placeholder': 'نام درس',
            }
        ))
        self.fields['course_description'] = forms.CharField(widget=forms.Textarea(
            attrs={
                'dir': 'rtl',
                'placeholder': 'توضیحات درس',
            }
        ))
        self.fields['course_name'].label = "نام درس "
        self.fields['course_description'].label = "توضیحات درس"