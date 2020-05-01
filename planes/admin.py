from django.contrib import admin
from .models import (Curator, CustomUser, FinanceCosts,
                     Quart, CuratorQuartCosts, Contract)

from .models import (PurchaseType, ActivityForm, StateASEZ,
                     NumberPZTRU, ContractStatus, Currency,
                     Price, ContractTerm, Counterpart,)



admin.site.register(Curator)
admin.site.register(FinanceCosts)
admin.site.register(CustomUser)
admin.site.register(Quart)
admin.site.register(CuratorQuartCosts)
admin.site.register(Contract)

admin.site.register(PurchaseType)
admin.site.register(ActivityForm)
admin.site.register(StateASEZ)
admin.site.register(NumberPZTRU)
admin.site.register(ContractStatus)
admin.site.register(Currency)
admin.site.register(Price)
admin.site.register(ContractTerm)
admin.site.register(Counterpart)


