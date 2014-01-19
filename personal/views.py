from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from personal.models import Personal
from django.contrib.auth.models import User

class StaffForm(ModelForm):
    first_name=forms.CharField(label="Nombre",max_length=30)
    last_name=forms.CharField(label="Apellido(s)",max_length=30)
    email=forms.EmailField(label="Correo",help_text='')
    pwd1=forms.CharField(label="Password",widget=forms.PasswordInput,help_text='Indique solo si desea cambiar su Password actual',required=False)
    pwd2=forms.CharField(label="Repetir Password",widget=forms.PasswordInput,required=False)
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        try:
            self.fields['email'].initial = self.instance.user.email
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['pwd1'].initial = ''
            self.fields['pwd2'].initial = ''
        except User.DoesNotExist:
            pass
        self.fields.keyOrder = [
            'first_name', 'last_name', 'email', 'telefono', 'telefonoMovil', 'direccion', 'nss', 'rfc',
            'foto', 'fechaIngreso', 'especialidades', 'pwd1', 'pwd2'
        ]
    class Meta:
        model = Personal
        exclude = ('user','trabajos','puestos','privilegios')
    def clean_pwd2(self):
        if 'pwd1' in self.cleaned_data:
            pwd_1 = self.cleaned_data['pwd1']
            pwd_2 = self.cleaned_data['pwd2']
            if pwd_1 == pwd_2:
                return pwd_2
        raise forms.ValidationError('Passwords deben ser iguales')
    def save(self, *args, **kwargs):
        usr = self.instance.user
        newpwd = self.cleaned_data['pwd2']
        if newpwd != '':
            usr.set_password(newpwd)
        usr.email = self.cleaned_data['email']
        usr.first_name = self.cleaned_data['first_name']
        usr.last_name = self.cleaned_data['last_name']
        usr.save()
        profile = super(StaffForm, self).save(*args,**kwargs)
        return profile

@login_required(login_url='/login/')
def staff_list(request, template_name='staff/staff_list.html'):
    liststaffs = Personal.objects.all()
    paginator = Paginator(liststaffs,27)
    page = request.GET.get('page')
    try:
        lststaffs=paginator.page(page)
    except PageNotAnInteger:
        lststaffs=paginator.page(1)
    except EmptyPage:
        lststaffs=paginator.page(paginator.num_pages)
    return render(request, template_name, {'staffslist':lststaffs})

@login_required(login_url='/login/')
def staff_profile(request,template_name='staff/staff_form.html'):
    objstaff = get_object_or_404(Personal, user=request.user)
    form = StaffForm(request.POST or None, instance=objstaff)
    if form.is_valid():
        form.save()
        return redirect('/staff/my_profile/')
    return render(request, template_name, {'form':form})
