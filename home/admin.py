
from django.contrib import admin
from .models import Gender, UserRecord, PhoneRecord, WhatsappNumRec, EmailRecord, Skill

admin.site.register(Gender)
admin.site.register(UserRecord)
admin.site.register(PhoneRecord)
admin.site.register(WhatsappNumRec)
admin.site.register(EmailRecord)
admin.site.register(Skill)

