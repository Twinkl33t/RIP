from django.db import models

class regard(models.Model):
    address = models.CharField(max_length=50, verbose_name='Адрес')

    # def __str__(self):
    #     return self.pk
    class Meta:
        verbose_name = 'Регард'
        verbose_name_plural = 'Регарды'

class Report(models.Model):
    regard_id = models.ForeignKey(regard, on_delete=models.CASCADE, verbose_name='ID Магазина')
    quarter = models.IntegerField(default=0, verbose_name='Год')
    profit = models.IntegerField(default=0, verbose_name='Чистая Прибыль (тыс.руб.)')
    expense = models.IntegerField(default=0, verbose_name='Расходы (тыс.руб.)')
    products = models.IntegerField(default=0, verbose_name='Кол-во Проданных Товаров (тыс.ед.)')

    # def __str__(self):
    #     return self.quarter
    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'