from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from clientes.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        exclude = ('trabajos',)

@login_required(login_url='/login/')
def cliente_list(request, template_name='clientes/cliente_list.html'):
    listclientes = Cliente.objects.all()
    paginator = Paginator(listclientes,27)
    page = request.GET.get('page')
    try:
        lstclientes=paginator.page(page)
    except PageNotAnInteger:
        lstclientes=paginator.page(1)
    except EmptyPage:
        lstclientes=paginator.page(paginator.num_pages)
    return render(request, template_name, {'clienteslist':lstclientes})

@login_required(login_url='/login/')
def cliente_create(request, template_name='clientes/cliente_form.html'):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/login/')
def cliente_update(request, pk, template_name='clientes/cliente_form.html'):
    objcliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=objcliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/login/')
def cliente_delete(request):
    if request.method=='POST':
        pk = request.POST['pk']
        objcliente = get_object_or_404(Cliente, pk=pk)
        objcliente.delete()
    return redirect('cliente_list')