from django.shortcuts import render

def home(request): 
    return render(request, 'index.html', {})

def about(request):
    context = {'first_name': 'Gurpreet', 'last_name': 'Dosanjh'}
    return render(request, 'about.html', context)