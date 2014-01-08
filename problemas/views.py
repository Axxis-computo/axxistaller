from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from problemas.models import Problema

class ProblemaForm(ModelForm):
    class Meta:
        model = Problema

def problema_list(request, template_name='problemas/problema_list.html'):
    listproblemas = Problema.objects.all()
    data = {}
    data['problemaslist'] = listproblemas
    return render(request, template_name, data)

def problema_create(request, template_name='problemas/problema_form.html'):
    form = ProblemaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('problema_list')
    return render(request, template_name, {'form':form})

def problema_update(request, pk, template_name='problemas/problema_form.html'):
    objproblema = get_object_or_404(Problema, pk=pk)
    form = ProblemaForm(request.POST or None, instance=objproblema)
    if form.is_valid():
        form.save()
        return redirect('problema_list')
    return render(request, template_name, {'form':form})

def problema_delete(request, pk, template_name='problemas/problema_confirm_delete.html'):
    objproblema = get_object_or_404(Problema, pk=pk)
    if request.method=='POST':
        objproblema.delete()
        return redirect('problema_list')
    return render(request, template_name, {'problema':objproblema})