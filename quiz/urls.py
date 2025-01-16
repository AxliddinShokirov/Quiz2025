from django.urls import path
from .views import QuizViewSet, QuestionViewSet, AnswerViewSet

# DRF uchun ViewSet-larni asosan ishlatish uchun router yondashuvisiz alohida marshrutlar
quiz_list = QuizViewSet.as_view({
    'get': 'list',   # GET /quizzes/
    'post': 'create' # POST /quizzes/
})

quiz_detail = QuizViewSet.as_view({
    'get': 'retrieve',   # GET /quizzes/{id}/
    'put': 'update',     # PUT /quizzes/{id}/
    'patch': 'partial_update', # PATCH /quizzes/{id}/
    'delete': 'destroy'  # DELETE /quizzes/{id}/
})

question_list = QuestionViewSet.as_view({
    'get': 'list',   # GET /questions/
    'post': 'create' # POST /questions/
})

question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',   # GET /questions/{id}/
    'put': 'update',     # PUT /questions/{id}/
    'patch': 'partial_update', # PATCH /questions/{id}/
    'delete': 'destroy'  # DELETE /questions/{id}/
})

answer_list = AnswerViewSet.as_view({
    'get': 'list',   # GET /answers/
    'post': 'create' # POST /answers/
})

answer_detail = AnswerViewSet.as_view({
    'get': 'retrieve',   # GET /answers/{id}/
    'put': 'update',     # PUT /answers/{id}/
    'patch': 'partial_update', # PATCH /answers/{id}/
    'delete': 'destroy'  # DELETE /answers/{id}/
})

urlpatterns = [
    # Quiz URLs
    path('quizzes/', quiz_list, name='quiz-list'),
    path('quizzes/<int:pk>/', quiz_detail, name='quiz-detail'),
    
    # Question URLs
    path('questions/', question_list, name='question-list'),
    path('questions/<int:pk>/', question_detail, name='question-detail'),
    
    # Answer URLs
    path('answers/', answer_list, name='answer-list'),
    path('answers/<int:pk>/', answer_detail, name='answer-detail'),
]
