from django.contrib import admin

from brand.models import Portfolio, Port, BrandShapka, Poslugi


# admin.site.register(Portfolio)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(BrandShapka)
class BrandShapka(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Poslugi)
class Poslugi(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}