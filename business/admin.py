
from django.contrib import admin
from .models import ServicesProductsList, RegistrationStatusList, DevelopmentStageList, IndustrySectorList, BusinessRecord, OutcomeRecord

admin.site.register(ServicesProductsList)
admin.site.register(RegistrationStatusList)
admin.site.register(DevelopmentStageList)
admin.site.register(IndustrySectorList)
admin.site.register(BusinessRecord)
admin.site.register(OutcomeRecord)
