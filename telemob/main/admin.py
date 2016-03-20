# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Argument, Campaign, Contact, Politician, HelpText


class ArgumentInline(admin.TabularInline):
    model = Argument


class CampaignAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'date_created'
    )
    inlines = [ArgumentInline]

class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'politician',
        'campaign',
        'contacted_by',
    )

class PoliticianAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'uf',
        'political_party',
    )

class HelpTextAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'campaign',
        'date_created',
    )


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Politician, PoliticianAdmin)
admin.site.register(HelpText, HelpTextAdmin)
