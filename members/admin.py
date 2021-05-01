from django.contrib import admin
from . import models


@admin.register(models.SkillModel)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MemberModel)
class MemberAdmin(admin.ModelAdmin):
    """ Member Admin Definition """

    list_display = (
        "name",
        "gender",
        "view_mobile",
        "email",
        "count_skills",
    )

    list_filter = ("gender",)
    filter_horizontal = ("skills",)
