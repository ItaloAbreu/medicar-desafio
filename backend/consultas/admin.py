from django.contrib import admin
from consultas.models import Agenda, HorarioAgenda 


class HorarioAgendaInline(admin.StackedInline):
    model = HorarioAgenda
    fields = ('horario',)
    extra = 1
    min_num = 1


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    fields = ('medico', 'dia',)
    inlines = [HorarioAgendaInline]

