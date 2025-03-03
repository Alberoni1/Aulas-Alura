from django.contrib import admin
from calculosolarpj.models import QntPaineisPJ,CalculoPotenciaGeracaoPJ,CalculoSolarPJ,GeracaoPrevistaPJ

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
                'fields': ('media_consumo',)
            }),
        )
    
    def media_consumo(self, obj):
            return f"{obj.media_consumo:.2f} kWh/mês"
    media_consumo.short_description = 'Média Mensal'

@admin.register(CalculoPotenciaGeracaoPJ)
class CalculoPotGeracaoPJAdmin(admin.ModelAdmin):
    list_display = ('cliente','calculopainel')
    readonly_fields = ('calculopainel',)
    
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
                'fields': ('calculopainel',)
            }),
        )

    def calculopainel(self, obj):
            return f"{obj.calculopainel:.2f} kWp"
    calculopainel.short_description = 'Potencia de Geração Necessária'

@admin.register(QntPaineisPJ)
class QntPaineisPJAdmin(admin.ModelAdmin):
    list_display = ('cliente','calculopainel')
    readonly_fields = ('calculopainel','potenciasistema')
    
    fieldsets = (
            ('Cliente', {
                'fields': ('cliente',)
            }),
            ('Quantidade de Paineis Necessaria', {
                'fields': (
                    ('potgeracao','potpainel')
                )
            }),
            ('Resultados', {
                'fields': ('calculopainel','potenciasistema')
            }),
        )

    def calculopainel(self, obj):
            return f"{obj.calculopainel} paineis"
    calculopainel.short_description = 'Quantidade Minima de Paineis Necessários'

    def potenciasistema(self,obj):
          return f'{obj.potenciasistema} kWp'
    potenciasistema.short_description = 'Potencia Calculada do Sitsema'
  
@admin.register(GeracaoPrevistaPJ)
class GeracaoPrevistaPJAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'get_irradiacao', 'get_rendimento', 'geracao_formatada')
    readonly_fields = ('geracao_formatada',)

    def geracao_formatada(self, obj):
        # obj.gercaoesperada retorna uma lista de tuplas (mês, valor)
        return "  \n".join([f"{mes}: {valor:.2f}" for mes, valor in obj.gercaoesperada])
    geracao_formatada.short_description = "Geração Esperada (kWh)"


  
    @admin.display(description='Irradiação Média')
    def get_irradiacao(self, obj):
        return f"{obj.irrad.media_irradiancia:.2f} kWh/m²"
    
    @admin.display(description='Rendimento (%)')
    def get_rendimento(self, obj):
        return f"{obj.rend.rendimento}%"