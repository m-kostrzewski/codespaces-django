from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Gamers Spot",
        },
    )


def profile(request):
    return render(request, 'profile.html')

def talk(request):
    return render(request, 'talk.html')