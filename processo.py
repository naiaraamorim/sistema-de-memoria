from random import randint

class Processo:  # todos os atributos começam como obrigatório
    def __init__(self, nome, tamanho, prioridade, criado_em, temp_exec=randint(5, 20)):
        self.nome = f'Processo {nome}'
        self.tamanho = tamanho
        self.prioridade = prioridade
        self.criado_em = criado_em
        self.temp_exec = temp_exec

    def __repr__(self):
        return f'nome: {self.nome}, tamanho: {self.tamanho}, prioridade: {self.prioridade}, criado_em: {self.criado_em}, temp_exec: {self.temp_exec}'
