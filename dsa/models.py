from django.db import models

class Dsa(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField()

class Vote(models.Model):
    dsa = models.ForeignKey(Dsa, related_name="votes", on_delete = models.CASCADE)

    evote = models.IntegerField(default=0)
    mvote = models.IntegerField(default=0)
    dvote = models.IntegerField(default=0)
    ivote = models.IntegerField(default=0)

class Tag(models.Model):
    tag = models.CharField(max_length=255)
    dsa = models.ForeignKey(Dsa, related_name="tags", on_delete = models.CASCADE)
