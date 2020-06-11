from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Point)