# quiz/views.py
from django.shortcuts import render
from .models import Quiz, Question

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})
# quiz/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quiz, Question, Choice

def quiz_detail_view(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def quiz_submit_view(request, quiz_id):
    if request.method == 'POST':
        selected_choice_ids = request.POST.getlist('choices')
        # Process the selected choices here
        return HttpResponse("Quiz submitted successfully!")
    else:
        return HttpResponse("Invalid request method")
