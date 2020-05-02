from django.contrib import admin
from .models import Curator, CustomUser, FinanceCosts, Contract


admin.site.register(Curator)
admin.site.register(FinanceCosts)
admin.site.register(CustomUser)
admin.site.register(Contract)

# Register your models here.
