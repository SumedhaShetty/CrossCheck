from django.contrib import admin
from .models import Semester
from .models import Subjects
from .models import Department
from .models import Book,Data
# Register your models here.

admin.site.register(Semester)
admin.site.register(Subjects)
admin.site.register(Department)
admin.site.register(Book)
admin.site.register(Data)