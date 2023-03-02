from django.contrib import admin
# Register your models here.
from .models import Topik, Subject, ResourceStudy, KeyWord, RoadMapStudy

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 0
    list_display = ('current_level', 'name', 'name_en', 'description')
    # exclude = ('study_level',)
    ordering = ('current_level',)
    can_delete = True

# admin.site.register(Topik)
@admin.register(Topik)
class TopikAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_en', 'description')
    sortable_by = ('study_level',)
    fieldsets = (
        ('Название курса', {
            'fields': ('study_level', 'name', 'name_en'),
        }),
        ('Пояснение', {
            'fields': ('description',)
        })
    )
    inlines = [SubjectInline]
    
# admin.site.register(Subject)
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_en', 'topik', 'description')
    # sortable_by = ('study_level',)
    fieldsets = (
        ('Название темы', {
            'fields': ('current_level', 'name', 'name_en'),
        }),
        ('Пояснение', {
            'fields': ('description',)
        }),
        ('ключевые слова', {
            'fields': ('keywords',)
        }),
        ('ресурсы', {
            'fields': ('resource',)
        })
    )
    # inlines = [SubjectInline]
    
admin.site.register(ResourceStudy)
admin.site.register(KeyWord)

class TopikInline(admin.TabularInline):
    model = Topik
    extra = 0
    list_display = ('name', 'name_en', 'description')
    exclude = ('study_level',)
    ordering = ('study_level',)
    can_delete = True

# admin.site.register(RoadMapStudy)
@admin.register(RoadMapStudy)
class RoadMapStudyAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_en', 'description')
    # fields = [('name', 'name_en'), 'description']
    fieldsets = (
        ('Название плана', {
            'fields': ('name', 'name_en'),
        }),
        ('Пояснение', {
            'fields': ('description',)
        })
    )
    inlines = [TopikInline]

