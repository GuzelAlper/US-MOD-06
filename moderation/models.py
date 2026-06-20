import uuid
from django.db import models
from django.core.validators import RegexValidator

class BlockingReason(models.Model):
    # 1. Primary key alanını UUIDField yapıyoruz (OpenAPI spesifikasyonuna uygun string/uuid formatı için)
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    
    # 2. Oraya 'code' alanını ekliyoruz ve sadece BÜYÜK_HARF ve alt çizgi kabul edecek regex koyuyoruz
    code = models.CharField(
        max_length=100,
        unique=True,
        validators=[RegexValidator(regex=r'^[A-Z_]+$', message="Code must be UPPERCASE_WITH_UNDERSCORES")]
    )
    
    title = models.CharField(max_length=255)
    hard_block = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        # Soft-delete mantığın (Zaten onaylanan kısım)
        self.is_active = False
        self.save()

    def __str__(self):
        return f"{self.code} - {self.title}"