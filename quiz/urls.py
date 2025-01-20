from django.urls import path
from .views import QuizViewSet, QuestionViewSet, AnswerViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger konfiguratsiyasi
schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version='v1',
        description="API documentation for Quiz, Question, and Answer models.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@quizapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Quiz marshrutlari
quiz_list = QuizViewSet.as_view({
    'get': 'list',         # GET /quizzes/
    'post': 'create'       # POST /quizzes/
})
quiz_detail = QuizViewSet.as_view({
    'get': 'retrieve',     # GET /quizzes/{id}/
    'put': 'update',       # PUT /quizzes/{id}/
    'patch': 'partial_update',  # PATCH /quizzes/{id}/
    'delete': 'destroy'    # DELETE /quizzes/{id}/
})

# Question marshrutlari
question_list = QuestionViewSet.as_view({
    'get': 'list',         # GET /questions/
    'post': 'create'       # POST /questions/
})
question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',     # GET /questions/{id}/
    'put': 'update',       # PUT /questions/{id}/
    'patch': 'partial_update',  # PATCH /questions/{id}/
    'delete': 'destroy'    # DELETE /questions/{id}/
})

# Answer marshrutlari
answer_list = AnswerViewSet.as_view({
    'get': 'list',         # GET /answers/
    'post': 'create'       # POST /answers/
})
answer_detail = AnswerViewSet.as_view({
    'get': 'retrieve',     # GET /answers/{id}/
    'put': 'update',       # PUT /answers/{id}/
    'patch': 'partial_update',  # PATCH /answers/{id}/
    'delete': 'destroy'    # DELETE /answers/{id}/
})

# URL patterns
urlpatterns = [
    # Quiz marshrutlari
    path('quizzes/', quiz_list, name='quiz-list'),
    path('quizzes/<int:pk>/', quiz_detail, name='quiz-detail'),

    # Question marshrutlari
    path('questions/', question_list, name='question-list'),
    path('questions/<int:pk>/', question_detail, name='question-detail'),

    # Answer marshrutlari
    path('answers/', answer_list, name='answer-list'),
    path('answers/<int:pk>/', answer_detail, name='answer-detail'),

    # Swagger va ReDoc hujjatlari
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
from django.urls import path
from .views import QuizViewSet, QuestionViewSet, AnswerViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger konfiguratsiyasi
schema_view = get_schema_view(
    openapi.Info(
        title="Quiz API",
        default_version='v1',
        description="API documentation for Quiz, Question, and Answer models.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@quizapp.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Quiz marshrutlari
quiz_list = QuizViewSet.as_view({
    'get': 'list',         # GET /quizzes/
    'post': 'create'       # POST /quizzes/
})
quiz_detail = QuizViewSet.as_view({
    'get': 'retrieve',     # GET /quizzes/{id}/
    'put': 'update',       # PUT /quizzes/{id}/
    'patch': 'partial_update',  # PATCH /quizzes/{id}/
    'delete': 'destroy'    # DELETE /quizzes/{id}/
})

# Question marshrutlari
question_list = QuestionViewSet.as_view({
    'get': 'list',         # GET /questions/
    'post': 'create'       # POST /questions/
})
question_detail = QuestionViewSet.as_view({
    'get': 'retrieve',     # GET /questions/{id}/
    'put': 'update',       # PUT /questions/{id}/
    'patch': 'partial_update',  # PATCH /questions/{id}/
    'delete': 'destroy'    # DELETE /questions/{id}/
})

# Answer marshrutlari
answer_list = AnswerViewSet.as_view({
    'get': 'list',         # GET /answers/
    'post': 'create'       # POST /answers/
})
answer_detail = AnswerViewSet.as_view({
    'get': 'retrieve',     # GET /answers/{id}/
    'put': 'update',       # PUT /answers/{id}/
    'patch': 'partial_update',  # PATCH /answers/{id}/
    'delete': 'destroy'    # DELETE /answers/{id}/
})

# URL patterns
urlpatterns = [
    # Quiz marshrutlari
    path('quizzes/', quiz_list, name='quiz-list'),
    path('quizzes/<int:pk>/', quiz_detail, name='quiz-detail'),

    # Question marshrutlari
    path('questions/', question_list, name='question-list'),
    path('questions/<int:pk>/', question_detail, name='question-detail'),

    # Answer marshrutlari
    path('answers/', answer_list, name='answer-list'),
    path('answers/<int:pk>/', answer_detail, name='answer-detail'),

    # Swagger va ReDoc hujjatlari
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
