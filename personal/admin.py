from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from personal.models import Personal
from personal.models import Especialidad
from personal.models import Puesto
from personal.models import Privilegio

# Define an inline admin descriptor for Personal model
# which acts a bit like a singleton
class PersonalInline(admin.StackedInline):
    model = Personal
    can_delete = False
    verbose_name_plural = 'Personales'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (PersonalInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Especialidad)
admin.site.register(Puesto)
admin.site.register(Privilegio)