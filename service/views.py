from django.shortcuts import render, redirect
from service.models import Post, Comment


def index(req):
    return render(req, 'index.html')
