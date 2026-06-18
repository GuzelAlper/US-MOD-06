from django.contrib import admin
from .models import BlockingReason

@admin.register(BlockingReason)
class BlockingReasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'hard_block', 'is_active')
    list_filter = ('is_active', 'hard_block')
    search_fields = ('title',)

    # Admin panelindeki toplu silme aksiyonunu soft-delete'e çevirir
    def delete_queryset(self, request, queryset):
        queryset.update(is_active=False)