from django.shortcuts import render

# Create your views here.
def biography(request):
    return render(request, "index.html")