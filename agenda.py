from datetime import datetime
from evento import Evento
import re

class Agenda:
    
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        for e in self.eventos:
            if (evento.inicio < e.termino and evento.termino > e.inicio):
                return("Evento tem conflito de horário com um ou mais eventos cadastrados")
            if (evento.nome == e.nome):
                return("Evento tem o mesmo nome de outro evento cadastrado")
        self.eventos.append(evento)
        return f"Evento {evento.nome} adicionado com sucesso"

    def mostrar_agenda(self):
        agenda_list = []
        for evento in self.eventos:
            agenda_list.append(f"{evento.nome}: {evento.inicio.strftime('%Y-%m-%d %H:%M')} a {evento.termino.strftime('%Y-%m-%d %H:%M')}")
        return agenda_list

    def remover_evento(self, nome):
        for evento in self.eventos:
            if evento.nome == nome:
                return "Evento removido com sucesso."
        return "Evento não encontrado."

      

    
    