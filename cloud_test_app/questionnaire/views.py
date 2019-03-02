from django.shortcuts import render

def index(request):
    num_answers = FilledQuestionnaire.objects.all().count()
    context = {
        'title': "Basic Questions!",
        'num_answers': num_answers,
    }
    return render(request, 'questionnaire/index.html', context)

def questionnaire(request):
    context = {
        "day_choices": FilledQuestionnaire.day_choices,
        "month_choices": FilledQuestionnaire.month_choices
    }
    return render(request, 'questionnaire/questionnaire.html', context)
