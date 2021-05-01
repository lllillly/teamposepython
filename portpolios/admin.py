from django.contrib import admin
from . import models


@admin.register(models.PortPolioModel)
class PortPolioAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "url",
    )

    filter_horizontal = ("participants",)
