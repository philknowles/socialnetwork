from django.shortcuts import render


# Create your views here.
def all_exercises(request):
    return render(request, 'fitness/exercises.html')
