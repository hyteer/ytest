from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Person, Group, MyUser
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
	fields = ('name','email', 'age')
	list_display = ('name','email', 'age')


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'myuser'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )


admin.site.register(Person, PersonAdmin)
admin.site.register(Group)



# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

