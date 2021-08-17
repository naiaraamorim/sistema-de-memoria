import datetime
from datetime import datetime

from processo import Processo
from memoria import Memoria

# tamanho =  recebe do usuario
# prioridade = recebe do usuario

p1 = Processo(1, 3, 0, criado_em=datetime.now())
p2 = Processo(2, 3, 0, criado_em=datetime.now())
p3 = Processo(3, 5, 0, criado_em=datetime.now())
p4 = Processo(4, 5, 0, criado_em=datetime.now())
p5 = Processo(5, 5, 1, criado_em=datetime.now())

memoria1 = Memoria()

i = 0
while i < memoria1.tamanho:
    memoria1.paginas[f"pag{i}"] = ""
    i += 1


def func_escalona_proc(m, p):
    cont1 = 1
    while cont1 <= 20:
        if m[f"pag{i}"] == "":
            cont2 = 1
            while cont2 <= p.tamanho:
                m[f"pag{i}"] = f"{p.nome}"
                cont2 += 1
            cont1 += 1


func_escalona_proc(memoria1.paginas, p1)
