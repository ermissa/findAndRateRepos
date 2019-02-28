from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, JsonResponse


def home(request):
    try:
        if request.method == "GET":
            #return render(request,'index.html')
            form_context = {}
            form_context["tag_form"] = TagModelForm()
            form_context["tag_form"].fields['tags'].widget.attrs = {'id': 'singleFieldTags2'}
            return render(request, 'index.html', form_context)
        elif request.method == "POST":
            tag_form = TagModelForm(request.POST)
            if tag_form.is_valid():
                tag = tag_form.save(commit=False)
                tag.save()
                tag_form.save_m2m()

                #Reinitializing Tag Form
                form_context = {}
                form_context["tag_form"] = TagModelForm()
                form_context["tag_form"].fields['tags'].widget.attrs = {'id': 'singleFieldTags2'}
                return render(request, 'index.html', form_context)
    except KeyError:
        # return HttpResponse(KeyError)
        return KeyError

'''
def search(request):
    try:
        if request.method == "GET":
            #return render(request,'index.html')
            form_context = {}
            form_context["tag_form"] = TagModelForm()
            form_context["tag_form"].fields['tags'].widget.attrs = {'id': 'singleFieldTags2'}
            return render(request, 'index.html', form_context)
        elif request.method == "POST":
            tag_form = TagModelForm(request.POST)
            if tag_form.is_valid():
                tag = tag_form.save(commit=False)
                tag.save()
                tag_form.save_m2m()

                #Reinitializing Tag Form
                form_context = {}
                form_context["tag_form"] = TagModelForm()
                form_context["tag_form"].fields['tags'].widget.attrs = {'id': 'singleFieldTags2'}
                return render(request, 'index.html', form_context)
    except KeyError:
        # return HttpResponse(KeyError)
        return KeyError
'''