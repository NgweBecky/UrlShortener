from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import Url
from .models import UrlData
import random
import string


def index(request):
    return HttpResponse("hello world")

def urlShort(request):
    if request.method == "POST":
        form = Url(request.POST)
        if form.is_valid():
            ud = UrlData()
            ud.slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
            ud.url = form.cleaned_data['url']
            #new_url = UrlData(url=url, slug=slug)
            #new_url = new_url.save()
            #request.user.add(new_url)
            ud.save()
            return HttpResponseRedirect('/')
    else:
        form = Url()
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
        }
    return render(request, 'index.html', context)
    
def urlRedirect(request, slugs):
    data = UrlData.objects.get(slug = slugs)
    return redirect(data.url)
