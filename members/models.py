from django.db import models


class SkillModel(models.Model):
    """ Skill Model Definition """

    skill_name = models.CharField(max_length=40)

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name_plural = "SKILLS"


class MemberModel(models.Model):
    """ Member Model Definition """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    )

    name = models.CharField(max_length=30)
    birth = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    avatar = models.ImageField()
    mobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True)
    skills = models.ManyToManyField("SkillModel", blank=True)

    def __str__(self):
        return self.name

    def view_mobile(self):

        current_value = self.mobile
        max_len = len(current_value)

        first_mobile = current_value[0:3]
        second_mobile = current_value[3:7]
        third_mobile = current_value[7:max_len]

        return f"{first_mobile}-{second_mobile}-{third_mobile}"

    view_mobile.short_description = "MOBILE"

    def count_skills(self):
        return f"{self.skills.all().count()}개"

    count_skills.short_description = "SKILLS"

    class Meta:
        verbose_name_plural = "MEMBERS"
