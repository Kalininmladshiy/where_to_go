from django.contrib import admin

from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableTabularInline, SortableAdminMixin


class PlaceimageInline(SortableTabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    fields = ['position', 'picture', 'get_preview']
    extra = 1

    def get_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.picture.url,
            width=(obj.picture.width / 3),
            height=(obj.picture.height / 3),
            )
     )
    


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','description_short',)
    inlines = [PlaceimageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
