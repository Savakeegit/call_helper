from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User, models.CASCADE, related_name='profile', verbose_name='Пользователь', primary_key=True,
    )
    telegram_id = models.CharField(
        'Telegram ID', max_length=30, null=True, blank=True, unique=True,
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'{self.user} ({self.pk})'

    @receiver(post_save, sender=User)
    def post_save_user(self, instance, created, **kwargs):
        if created:
            if not hasattr(instance, 'telegram_id',):
                Profile.objects.create(
                    user=instance,
                )
