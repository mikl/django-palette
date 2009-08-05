from django.contrib import admin
from palette.models import Palette, Colour


class ColourInline(admin.TabularInline):
    model = Colour


class PaletteAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    inlines = [ColourInline]


class ColourAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'palette')


admin.site.register(Palette, PaletteAdmin)
admin.site.register(Colour, ColourAdmin)

