from django.db import models

class Dron(models.Model):
    name = models.CharField(max_length=100,verbose_name='title')
    image = models.ImageField(upload_to='images/',verbose_name='image')
    price = models.IntegerField(verbose_name='price')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Dron'
        verbose_name_plural = 'Drons'



class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    phone = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Номер телефона"
    )
    subject = models.CharField(max_length=100, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата отправки"
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject}"