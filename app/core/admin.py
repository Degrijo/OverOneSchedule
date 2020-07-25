from django.contrib import admin
from django.contrib.auth import get_user_model

from app.core.models import Lesson


admin.site.register(get_user_model())
admin.site.register(Lesson)
