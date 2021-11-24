from django.shortcuts import render
from . models import Lead, Post



def asosiy(request):
    data = Post.objects.all()
    return render(request, "index.html", {'posts': data})

def about(request):
    data = Lead.objects.all()
    return render(request, "about.html", {'leads': data})

def news(request):
    data = Post.objects.all()
    return render(request, "news.html", {'posts': data})

def single(request, slug):
    data = Post.objects.get(slug = slug)
    return render(request, 'single.html', {'post': data})

def double(request, slug):
    data = Lead.objects.get(slug = slug)
    return render(request, 'double.html', {'lead': data})



