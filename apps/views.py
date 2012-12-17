# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from models import *
from PIL import Image, ImageFilter
from forms import FiltForm


def hello(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def view_all(request):
    try:
        all_pics = Pic.objects.all()
    except:
        raise Http404
    return  render_to_response('all.html', {'all_pics':all_pics}, context_instance=RequestContext(request))

def view_picture(request, pic_id):
    pic = get_object_or_404(Pic, pk=pic_id)
    return render_to_response('view_pic.html', {'pic': pic}, context_instance=RequestContext(request))
    
def apply_filter_blur(request, pic_id):
    pic = get_object_or_404(Pic, pk=pic_id)
    im = pic.picture
    img = Image.open(im)
    imag = img.filter(ImageFilter.BLUR)
    #imag.save('/media/images/1.jpg')#пока так
    path = im.url
    path = path.split('/')[3]
    imag.save('media/image/1.jpg')
    #imag.save(pic.picture.url)#выскакивает ошибка No such file or directory: '/media/images/cote_1.jpg'
    return render_to_response('view_filt.html', {'filt':imag}, context_instance=RequestContext(request))
    
def apply_filter_contour(request, pic_id):
    pic = get_object_or_404(Pic, pk=pic_id)
    im = pic.picture
    img = Image.open(im)
    imag = img.filter(ImageFilter.CONTOUR)
    #imag.save('/media/images/1.jpg')#пока так
    path = im.url
    path = path.split('/')[3]
    imag.save('media/image/1.jpg') # imag.save(path)
    #imag.save(pic.picture.url)#выскакивает ошибка No such file or directory: '/media/images/cote_1.jpg'
    return render_to_response('view_filt.html', {'filt':imag}, context_instance=RequestContext(request))
    
def apply_filter_detail(request, pic_id):
    pic = get_object_or_404(Pic, pk=pic_id)
    im = pic.picture
    img = Image.open(im)
    imag = img.filter(ImageFilter.DETAIL)
    #imag.save('/media/images/1.jpg')#пока так
    path = im.url
    path = path.split('/')[3]
    imag.save('media/image/1.jpg') #imag.save(path)
    #imag.save(pic.picture.url)#выскакивает ошибка No such file or directory: '/media/images/cote_1.jpg'
    return render_to_response('view_filt.html', {'filt':imag}, context_instance=RequestContext(request))