from django.shortcuts import render

# Create your views here.


def intro(request):
    return render(request, 'home/intro.html')


def team_introduce(request):
	return render(request, 'home/team_introduce.html')