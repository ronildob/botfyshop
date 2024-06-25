from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    html_ = """
Cole aqui o conteúdo do Starter template copiado do site do bootstrap
"""
    return HttpResponse(html_)