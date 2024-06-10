from django.contrib import admin
from django.contrib.admin import TabularInline

from breaks.models import replacements, dicts, breaks


###############################
# INLINES
###############################
class ReplacementEmployeeInline(TabularInline):
    model = replacements.ReplacementEmployee
    fields = (
        'employee', 'status',
    )


###############################
# MODELS
###############################
@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration',
    )
    inlines = (
        ReplacementEmployeeInline,
    )


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active',
    )


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active',
    )


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'replacement', 'break_start', 'break_end',
    )
