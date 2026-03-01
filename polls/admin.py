from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1


class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
