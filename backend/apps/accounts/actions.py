def deactivate_guards(modeladmin, request, queryset):
    queryset.update(is_active=False)
deactivate_guards.short_description = "Deactivate selected guards"


def mark_as_guard(modeladmin, request, queryset):
    queryset.update(role="GUARD", is_active=True, is_staff=True)
mark_as_guard.short_description = "Mark selected users as guards"