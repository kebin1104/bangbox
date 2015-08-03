# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def single_photo(request, photo_id):
    return HttpResponse('{0}파일을 보여드립니다'.format(photo_id))

