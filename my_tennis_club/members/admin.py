from django.contrib import admin
# da aplicativo members no arquivo models.py importe a classe Member
from .models import Member

# Register your models here.
# isso faz com que a classe Member seja exibida na página admin
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)