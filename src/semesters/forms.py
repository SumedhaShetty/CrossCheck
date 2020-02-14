from django import forms

from .models import Data, Book, Subjects, Semester, Department

class PostForm(forms.ModelForm):
    class Meta:
        model = Data
        fields= [
            "title",
            "page_no",
            "content",
            "img",
            "book_link",
#            "draft",
#            "publish",

        ]
#        model = Book
#        fields= [
#            "sem_link",
#       ]
#      model = Subjects 
#     fields= [
#            "sub",
#        ]
#        model = Semester 
#        fields= [
#            "sem",
#        ]
#        model = Department 
#        fields= [
#            "dept",
#        ]
            