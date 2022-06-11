from django.forms import ModelForm, DateInput, TimeInput, Form, DateTimeInput
from django import forms
from django.shortcuts import get_object_or_404
from assignments.models import SubmitAssignment, Assignment
from django.utils import timezone
from courses.models import Course
from users.models import User

class GradeAssignmentForm(ModelForm):
    
    class Meta:
        model = SubmitAssignment
        fields = ['grade']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].label = "نمره"
class CreateAssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ('assignment_name', 'assignment_description',
                  'due_date', 'course')
        # labels = {
        #     'due_date': 'Due Date (yyyy-mm-dd HH:MM)'
        # }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        user_object = User.objects.filter(username=user.username)
        new_user_object = get_object_or_404(user_object)
        self.fields['course'].queryset = self.fields['course'].queryset.filter(teacher=new_user_object.id)
        self.fields['assignment_name'] = forms.CharField(widget=forms.TextInput(
            attrs={
                'dir': 'rtl',
                'placeholder': 'موضوع تکلیف',
            }
        ))
        self.fields['assignment_description'] = forms.CharField(widget=forms.Textarea(
            attrs={
                'dir': 'rtl',
                'placeholder': 'شرح تکلیف',
            }
        ))

        self.fields['assignment_name'].label = "موضوع تکلیف"
        self.fields['assignment_description'].label = "شرح تکلیف"
        self.fields['course'].label = "درس"

class SubmitAssignmentForm(ModelForm):
    class Meta:
        model = SubmitAssignment
        fields = ('topic', 'description', 'assignment_file', 'assignment_ques', 'author')
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        assignment = kwargs.pop('assignment_id')
        super().__init__(*args, **kwargs)
        self.fields['assignment_ques'].queryset = self.fields['assignment_ques'].queryset.filter(pk=assignment)
        self.fields['author'].queryset = self.fields['author'].queryset.filter(username=user.username)
        self.fields['topic'].label = "موضوع "
        self.fields['description'].label = "توضیحات "
        self.fields['assignment_file'].label = "فایل تکالیف "
        self.fields['assignment_ques'].label = "تکلیف مرتبط "
        self.fields['author'].label = "نویسنده "
