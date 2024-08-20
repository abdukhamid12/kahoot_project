from django.contrib import admin
from .models import *

admin.site.register([Category, Option])


class OptionAdmin(admin.TabularInline):
    model = Option
    extra = 1
    max_num = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionAdmin]