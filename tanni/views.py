from django.shortcuts import render

# Create your views here.
def index(request):
    params = {
        'user': 'testuser',
    }
    return render(request, 'tanni/index.html', params)