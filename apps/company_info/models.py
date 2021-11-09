from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=2)

    class Meta:
        db_table = "languages"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(
        "Language", on_delete=models.CASCADE, related_name="tags"
    )

    class Meta:
        db_table = "tags"

    def __str__(self):
        return str(self.name)


class CompanyName(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(
        "Language",
        on_delete=models.CASCADE,
        related_name="company_name",
    )
    c_id = models.ForeignKey(
        "Company", on_delete=models.CASCADE, related_name="company_name"
    )

    class Meta:
        db_table = "company_names"

    def __str__(self):
        return str(self.name)


class Company(models.Model):
    tags = models.ManyToManyField("Tag", related_name="companies")

    class Meta:
        db_table = "companies"
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return str(self.id)
