from rest_framework import serializers
from .models import Quiz, Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'  # Agar kerakli maydonlar bo'lsa, ularni yozishingiz mumkin

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)  # Bog'langan javoblar
    class Meta:
        model = Question
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)  # Bog'langan savollar
    question_count = serializers.SerializerMethodField()  # Dinamik qiymat

    class Meta:
        model = Quiz
        fields = '__all__'

    def get_question_count(self, obj):
        return obj.question_count
