from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from manuales.models import Manual

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ManualForm(ModelForm):
    class Meta:
        model = Manual

def manual_list(request, template_name='manuales/manual_list.html'):
    listmanuales = Manual.objects.all()
    paginator = Paginator(listmanuales,2) #se pagina de 5 en 5
    page = request.GET.get('page')
    try:
        manuales = paginator.page(page)
    except PageNotAnInteger:
        manuales = paginator.page(1)
    except EmptyPage:
        manuales = paginator.page(paginator.num_pages)
    return render(request, template_name, {'manualeslist':manuales})

def manual_create(request, template_name='manuales/manual_form.html'):
    form = ManualForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('manual_list')
    return render(request, template_name, {'form':form})

def manual_update(request, pk, template_name='manuales/manual_form.html'):
    objManual = get_object_or_404(Manual, pk=pk)
    form = ManualForm(request.POST or None, instance=objManual)
    if form.is_valid():
        form.save()
        return redirect('manual_list')
    return render(request, template_name, {'form':form})

def manual_delete(request):
    if request.method=='POST':
        pk = request.POST['pk']
        objManual = get_object_or_404(Manual, pk=pk)    
        objManual.delete()
    return redirect('manual_list')
