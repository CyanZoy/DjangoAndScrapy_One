from django.shortcuts import render
from JobSpider.recruit import begin
from django.http import HttpResponse,HttpResponseRedirect
import os


def start_spider(request):
    os.system('python G:/Python-work/Job/JobSpider/recruit/begin.py')
    return render(request, 'Tes.html')