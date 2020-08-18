from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()
# Register your models here.
"""
admin.site.register(Account)
admin.site.register(Job)
admin.site.register(Offer)
admin.site.register(Review)
"""# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import User
from django.contrib import admin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    


class Custom1UserAdmin(UserAdmin):
    model = User
    #add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    #list_display = getFieldsModel(User)

def getFieldsModel(model):
    return [field.name for field in model._meta.fields  if ( not field.many_to_many  and  field.name != "id" and not field.name=="logentry")]
    
class CompanyAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(User)

from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'description',
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
#admin.site.register(User)
admin.site.register(Job)
admin.site.register(Offer)
admin.site.register(Review)
admin.site.register(Order)