from django.contrib import admin
from .models import Quiz, Question, Answer

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class AnswerInlineModel(admin.TabularInline):  # Yoki admin.StackedInline
    model = Answer
    fields = ['answer_text', 'is_right']  # Javob maydonlari (agar mavjud bo'lsa)



class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'quiz']
    list_display = ['title', 'quiz', 'created_at']
    inlines =[ AnswerInlineModel]  # To'g'ri import qilingan inline model

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question']


# Admin saytiga model va admin klasslarini ro'yxatdan o'tkazish
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)  # QuestionAdmin ni qo'shish
admin.site.register(Answer , AnswerAdmin)