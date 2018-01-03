# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadedfile import InMemoryUploadedFile
import run

#run.run("/root/jianhang.jpg")

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'upload/index.html', context)

@csrf_exempt
def file(request):
    print('ssss1' + request.method)
    if request.method == 'POST':  
        #print('ssss2' + request.POST.File)
        #print(request.POST.File)
        content = "request.POST.get('name1')"
        print(request.POST.items)
        print(request.POST.get('name1'))
        print(request.FILES)
        f = (request.FILES.get('file1'))
        print(request.POST.get('name1'))
        fname = "./files/" + request.POST.get('name1')
        print fname
        with open(fname, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        result = run.run(fname)
        print result
	res = ""
	for key in result:
           res = res + "\n" + result[key][1]
        print res
        return HttpResponse(res)  
    else:  
        content = "request.GET.get('name')"  
        return HttpResponse('GET receive success, name is ' + content)  
