#django
from django.contrib import admin
#local
from auths.models import MyUser

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    """
    MyUserAdmin admin.
    """
    readonly_fields = ()