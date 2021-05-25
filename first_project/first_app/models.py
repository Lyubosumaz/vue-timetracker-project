from django.db import models


class Topic(models.Model):
    top_name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)
