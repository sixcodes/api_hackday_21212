# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(r):
    return render_to_response('base.html', context_instance=RequestContext(r))