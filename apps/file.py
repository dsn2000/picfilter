# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from settings import MEDIA_ROOT
from forms import *
from models import *
from django.http import Http404
# Imaginary function to uploaded and view file.

""""
def handle_uploaded_file(f):
    destination = open(MEDIA_ROOT + '/' + f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def upload_file(request):
    
    if request.method == 'POST':
        try:
            handle_uploaded_file(request.FILES['image_file'])
            return render_to_response('yes.html', context_instance=RequestContext(request))
        except:
            return render_to_response('no.html', context_instance=RequestContext(request))
    return render_to_response('file.html', context_instance=RequestContext(request))

"""

def upload_file(request):

    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save()
            print pic.picture.url
            return render_to_response('ajax_response.html', {'pic':pic})
        else:
            response = HttpResponse(form.errors.as_text())
            response.status_code = 406
            return response
    form = PicForm()
    return render_to_response('file.html', {'form':form}, context_instance=RequestContext(request))