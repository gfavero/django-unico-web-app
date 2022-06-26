from django.contrib import admin

# Register your models here.
from .models import (Content_table,Status_table,In_table,
                    Five_w_table, Totem_table, Theme_table, 
                    Principal_table,Conjunto_table, Base_table_new,
                    Sub_base_table)

admin.site.register(Content_table)

admin.site.register(Status_table)

admin.site.register(In_table)

admin.site.register(Five_w_table)

admin.site.register(Totem_table)

admin.site.register(Theme_table)

admin.site.register(Principal_table)

admin.site.register(Conjunto_table)

admin.site.register(Base_table_new)

admin.site.register(Sub_base_table)