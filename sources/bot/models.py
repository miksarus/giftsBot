from enum import unique
from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="ID пользователя в соц сети",
        unique=True,
    )
    name = models.TextField(verbose_name="Имя пользователя", default='Unknown')

    def __str__(self):
        return f"{self.name} (@{self.external_id})"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    profile = models.ForeignKey(
        to='bot.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(verbose_name='Текст', )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f"Сообщение от {self.profile}: {self.text}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщеня'
