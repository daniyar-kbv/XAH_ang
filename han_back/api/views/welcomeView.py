from django.shortcuts import render, redirect
from ..models import Article


def welcome(request):
    context = {
        "articles": Article.objects.all()
    }
    return render(request, "api/welcome_page.html", context)