from django.db import models


class PortPolioModel(models.Model):

    thumbnail = models.ImageField()
    title = models.CharField(max_length=80)
    sub_title = models.CharField(max_length=100)
    contents = models.TextField()
    url = models.CharField(max_length=100)
    participants = models.ManyToManyField("members.MemberModel", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "PORTPOLIOS"
