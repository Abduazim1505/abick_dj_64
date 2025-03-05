from django.db import models

class AutoSalon(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.context}"

    class Meta:
        verbose_name = "SALON"
        verbose_name_plural = "SALONS"
        ordering = ['pk']

class Car(models.Model):
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} {self.price} ({self.year})"

    class Meta:
        verbose_name = "CAR"
        verbose_name_plural = "CARS"
        ordering = ['pk']