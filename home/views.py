from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response

def home_view(request):
  return render_to_response('home/home.html', context_instance=RequestContext(request))
