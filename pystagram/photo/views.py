# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def single_photo(request):
    return HttpResponse('파일을 보여드립니다')

