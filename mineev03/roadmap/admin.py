from django.contrib import admin
# Register your models here.
from .models import Topik, ResourceLern, ResourceStudy, KeyWord, RoadMapStudy

admin.site.register(Topik)
admin.site.register(ResourceLern)
admin.site.register(ResourceStudy)
admin.site.register(KeyWord)
admin.site.register(RoadMapStudy)
