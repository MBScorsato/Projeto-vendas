from django.db import models


class bootstrap_navbar(models.Model):
    nome_navbar = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_navbar

    class Meta:
        verbose_name = "Nome site"

    class Meta:
        verbose_name_plural = "Nome site"
