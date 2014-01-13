from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from problemas.models import Problema

class ProblemaForm(ModelForm):
    class Meta:
        model = Problema

@login_required(login_url='/login/')
def problema_list(request, template_name='problemas/problema_list.html'):
    problemaslista = Problema.objects.all()
    paginator = Paginator(problemaslista,27)
    page = request.GET.get('page')
    try:
        lstproblemas=paginator.page(page)
    except PageNotAnInteger:
        lstproblemas=paginator.page(1)
    except EmptyPage:
        lstproblemas=paginator.page(paginator.num_pages)
    return render(request, template_name, {'problemaslist':lstproblemas})

@login_required(login_url='/login/')
def problema_create(request, template_name='problemas/problema_form.html'):
    form = ProblemaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('problema_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/login/')
def problema_update(request, pk, template_name='problemas/problema_form.html'):
    objproblema = get_object_or_404(Problema, pk=pk)
    form = ProblemaForm(request.POST or None, instance=objproblema)
    if form.is_valid():
        form.save()
        return redirect('problema_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/login/')
def problema_delete(request):
    if request.method=='POST':
        pk = request.POST['pk']
        objproblema = get_object_or_404(Problema, pk=pk)
        objproblema.delete()
    return redirect('problema_list')