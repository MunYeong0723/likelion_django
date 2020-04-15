from django import forms
from .models import Blog

# Blog model을 기반으로 한 form을 만들고 싶고
# 그 중 title과 body를 입력받을 수 있는 공간을 만들고 싶음.
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

class BlogPost_anything(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])

