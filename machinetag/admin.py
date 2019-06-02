from django.contrib import admin

from machinetag.models import MachineTag


class MachineTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(MachineTag, MachineTagAdmin)
