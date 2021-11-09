from django.contrib import admin

from apps.company_info.models import Company, CompanyName, Language, Tag


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """Language Admin Definition"""


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag Admin Definition"""

    list_display = ("id", "name", "language")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Company Admin Definition"""

    list_display = ("id", "names")

    def names(self, obj):
        return ",".join([k.name for k in obj.company_name.all()])


@admin.register(CompanyName)
class CompanyNameAdmin(admin.ModelAdmin):
    """CompanyName Admin Definition"""
