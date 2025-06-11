import urllib.parse
from django.shortcuts import render
import random

def random_cat(request):
    phrase = request.POST.get('phrase')
    url_cat = None

    if phrase:
        phrase_url = urllib.parse.quote(phrase)
        url_cat = f"https://cataas.com/cat/says/{phrase_url}?fontSize=25&color=red"
    
    return render(request,'cat/cat.html',{'url_cat':url_cat})
