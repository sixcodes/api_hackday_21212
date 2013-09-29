# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(r):
    return render_to_response('home.html', context_instance=RequestContext(r))

def listarBolao(r):
    return render_to_response('listar-bolao.html', context_instance=RequestContext(r))

def criarBolao(r):
    return render_to_response('form-criar-bolao.html', context_instance=RequestContext(r))

def exibirBolao(r):
    return render_to_response('exibir-bolao.html', context_instance=RequestContext(r))
