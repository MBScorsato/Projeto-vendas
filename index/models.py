from django.db import models


class bootstrap_navbar(models.Model):
    nome_navbar = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_navbar

    class Meta:
        verbose_name = "Nome site"

    class Meta:
        verbose_name_plural = "Nome site"


class NavBar_Links(models.Model):
    link_referente_cadastro = models.CharField(max_length=50)
    link_referente_produto = models.CharField(max_length=50)
    link_referente_receita = models.CharField(max_length=50)
    link_referente_cliente = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Defenir nomes dos links"

    class Meta:
        verbose_name_plural = "Defenir nomes dos links"


class Apresentaca_Site(models.Model):
    titulo = models.CharField(max_length=50)
    arq = models.FileField(upload_to="img")
    descricao = models.TextField()

    class Meta:
        verbose_name = "Imagem principal do Site (Logotipo da Empresa)"

    class Meta:
        verbose_name_plural = "Imagem principal do Site (Logotipo da Empresa)"
