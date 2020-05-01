from django.contrib import admin
from .models import Curator, CustomUser, FinanceCosts, Quart, CuratorQuartCosts, Contract



admin.site.register(Curator)
admin.site.register(FinanceCosts)
admin.site.register(CustomUser)
admin.site.register(Quart)
admin.site.register(CuratorQuartCosts)
admin.site.register(Contract)


