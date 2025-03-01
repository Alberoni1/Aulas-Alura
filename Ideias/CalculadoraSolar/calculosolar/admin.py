from django.contrib import admin
from calculosolar.models import CalculoSolarPF,CalculoIrradianciaSolar,CalculoSolarPJ,CalculoPotenciaGeracaoPF,CalculoPotenciaGeracaoPJ

@admin.register(CalculoIrradianciaSolar)
class CalculoIrradianciaAdmin(admin.ModelAdmin):
    list_display = ('estado','cidade','bairro', 'media_irradiancia')
    readonly_fields = ('media_irradiancia',)
    fieldsets = (
            ('Bairro', {
                'fields': ('estado','cidade','bairro',)
            }),
            ('Consumo Mensal (kWh)', {
                'fields': (
                    ('irradi_jan', 'irradi_fev', 'irradi_mar'),
                    ('irradi_abr', 'irradi_mai', 'irradi_jun'),
                    ('irradi_jul', 'irradi_ago', 'irradi_set'),
                    ('irradi_out', 'irradi_nov', 'irradi_dez')
                )
            }),
            ('Resultados', {
                'fields': ('media_irradiancia',),
                'classes': ('collapse',)
            }),
        )
    
    def media_irradiancia(self, obj):
            return f"{obj.media_irradiancia:.2f} kWh/m^(2).dia"
    media_irradiancia.short_description = 'Média Mensal'

@admin.register(CalculoSolarPF)
class CalculoSolarPFAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'media_consumo')
    readonly_fields = ('media_consumo',)
    fieldsets = (
            ('Cliente', {
                'fields': ('cliente',)
            }),
            ('Consumo Mensal (kWh)', {
                'fields': (
                    ('cons_jan', 'cons_fev', 'cons_mar'),
                    ('cons_abr', 'cons_mai', 'cons_jun'),
                    ('cons_jul', 'cons_ago', 'cons_set'),
                    ('cons_out', 'cons_nov', 'cons_dez')
                )
            }),
            ('Resultados', {
                'fields': ('media_consumo',),
                'classes': ('collapse',)
            }),
        )
    
    def media_consumo(self, obj):
            return f"{obj.media_consumo:.2f} kWh/mês"
    media_consumo.short_description = 'Média Mensal'

@admin.register(CalculoPotenciaGeracaoPF)
class CalculoPotGeracaoPFAdmin(admin.ModelAdmin):
    list_display = ('cliente','calculogeracao')
    readonly_fields = ('calculogeracao',)
    
    fieldsets = (
            ('Cliente', {
                'fields': ('cliente',)
            }),
            ('Potencia de Geração Necessaria (kWp)', {
                'fields': (
                    ('consumo','irradi','rendimento')
                )
            }),
            ('Resultados', {
                'fields': ('calculogeracao',),
                'classes': ('collapse',)
            }),
        )

    def calculogeracao(self, obj):
            return f"{obj.calculogeracao:.2f} kWp"
    calculogeracao.short_description = 'Potencia de Geração Necessária'
 
@admin.register(CalculoSolarPJ)
class CalculoSolarPJAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'media_consumo')
    readonly_fields = ('media_consumo',)
    fieldsets = (
            ('Cliente', {
                'fields': ('cliente',)
            }),
            ('Consumo Mensal (kWh)', {
                'fields': (
                    ('cons_jan', 'cons_fev', 'cons_mar'),
                    ('cons_abr', 'cons_mai', 'cons_jun'),
                    ('cons_jul', 'cons_ago', 'cons_set'),
                    ('cons_out', 'cons_nov', 'cons_dez')
                )
            }),
            ('Resultados', {
                'fields': ('media_consumo',),
                'classes': ('collapse',)
            }),
        )
    
    def media_consumo(self, obj):
            return f"{obj.media_consumo:.2f} kWh/mês"
    media_consumo.short_description = 'Média Mensal'

@admin.register(CalculoPotenciaGeracaoPJ)
class CalculoPotGeracaoPJAdmin(admin.ModelAdmin):
    list_display = ('cliente','calculogeracao')
    readonly_fields = ('calculogeracao',)
    
    fieldsets = (
            ('Cliente', {
                'fields': ('cliente',)
            }),
            ('Potencia de Geração Necessaria (kWp)', {
                'fields': (
                    ('consumo','irradi','rendimento')
                )
            }),
            ('Resultados', {
                'fields': ('calculogeracao',),
                'classes': ('collapse',)
            }),
        )

    def calculogeracao(self, obj):
            return f"{obj.calculogeracao:.2f} kWp"
    calculogeracao.short_description = 'Potencia de Geração Necessária'
   