from django.db import models


class GuestResponse(models.Model):
    ATTENDANCE_CHOICES = [
        ('yes', 'Ha, albatta kelaman'),
        ('no', 'Afsuski, kelolmayman'),
    ]

    name = models.CharField(max_length=200, verbose_name="Ism Familiya")
    guests_count = models.IntegerField(verbose_name="Mehmonlar soni")
    attendance = models.CharField(
        max_length=3,
        choices=ATTENDANCE_CHOICES,
        verbose_name="Ishtirok"
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    message = models.TextField(blank=True, verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")

    class Meta:
        verbose_name = "Mehmon javobi"
        verbose_name_plural = "Mehmon javoblari"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.get_attendance_display()}"


class WeddingSong(models.Model):
    title = models.CharField(max_length=200, verbose_name="Qo'shiq nomi")
    artist = models.CharField(max_length=200, verbose_name="Ijrochi")
    audio_file = models.FileField(upload_to='songs/', verbose_name="Audio fayl")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "To'y qo'shig'i"
        verbose_name_plural = "To'y qo'shiqlari"

    def __str__(self):
        return f"{self.title} - {self.artist}"
