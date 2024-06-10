from django.contrib import admin

from breaks.models import replacements
from organisations.models import organisations, groups, dicts


###############################
# INLINES
###############################
class EmployeeInline(admin.TabularInline):
    model = organisations.Employee
    fields = (
        'user', 'position', 'date_joined',
    )


class MemberInline(admin.TabularInline):
    model = groups.Member
    fields = (
        'user', 'date_joined',
    )


class ProfileBreakInline(admin.StackedInline):
    model = replacements.GroupInfo
    fields = (
        'min_active', 'break_start', 'break_end', 'break_max_duration',
    )


###############################
# MODELS
###############################
@admin.register(organisations.Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'director',
    )
    inlines = (EmployeeInline,)
    readonly_fields = (
        'created_at', 'created_by', 'updated_at', 'updated_by',
    )


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    inlines = (
        ProfileBreakInline,
        MemberInline,
    )
    readonly_fields = (
        'created_at', 'created_by', 'updated_at', 'updated_by',
    )


@admin.register(dicts.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active',
    )
