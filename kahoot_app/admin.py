from django.contrib import admin
from kahoot_app.models import *
# Register your models here.

admin.site.register([Category, Option])

class OptionAdmin(admin.TabularInline):
    model = Option
    extra = 1
    max_num = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionAdmin]