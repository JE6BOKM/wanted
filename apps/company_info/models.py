from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=2)

    class Meta:
        db_table = "languages"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey("Language", on_delete=models.CASCADE, related_name="tags")

    class Meta:
        db_table = "tags"

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50)
    tag = models.ManyToManyField("Tag", related_name="companies")
    language = models.ForeignKey("Language", on_delete=models.CASCADE)

    class Meta:
        db_table = "companies"

    def __str__(self):
        return self.name