from django.db import models

class BlockingReason(models.Model):
    title = models.CharField(max_length=255, verbose_name="Engelleme Nedeni")
    hard_block = models.BooleanField(
        default=False, 
        help_text="True ise MOD-05, False ise MOD-04 için kullanılır."
    )
    is_active = models.BooleanField(
        default=True, 
        help_text="Tarihsel referansları bozmamak için silmek yerine False yapılır."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Engelleme Nedeni"
        verbose_name_plural = "Engelleme Nedenleri"

    def __str__(self):
        return f"{self.title} ({'Aktif' if self.is_active else 'Pasif'})"

    def delete(self, *args, **kwargs):
        # Nesne silinmek istendiğinde is_active=False yaparak soft delete uygular
        self.is_active = False
        self.save()