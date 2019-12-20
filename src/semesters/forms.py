from django import forms

from .models import Data, Book, Subjects, Semester, Department

class PostForm(forms.ModelForm):
    class Meta:
        model = Data
        fields= [
            "title",
            "page_no",
            "content",
            "book_link",
            
            ]


#    model = Book
#       fields= [
#            "book",
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
            