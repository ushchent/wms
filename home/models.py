from django.db import models

class Produkt(models.Model):

    title = models.CharField(max_length=30)
    lead = models.CharField(max_length=100, default="Краткое описание продукта")
    description = models.TextField()
    # Проблема в том, что app_name нужно самому запомнить и правильно внести в БД
    app_name = models.CharField(max_length=30, default="Ссылка на страницу приложения")

    def __str__(self):
        return self.title
