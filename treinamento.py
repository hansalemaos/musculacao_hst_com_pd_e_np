import numpy as np
import pandas as pd
from PrettyColorPrinter import add_printer

add_printer(True)


def criar_exercicio(
    exercicio_max_10_vezes,
    passo_peso,
    nome_do_exercicio,
    comecar_com,
    terminar_com,
    semanas=6,
    dias_por_semana=5,
):
    peso_comeco = exercicio_max_10_vezes * comecar_com
    peso_fim = exercicio_max_10_vezes * terminar_com
    a = np.linspace(peso_comeco, peso_fim, num=semanas * dias_por_semana)
    df = pd.DataFrame(a)
    df = df[0].divmod(passo_peso)[0] * passo_peso
    df = df.to_frame().T
    df.columns = df.columns + 1
    df.index = [nome_do_exercicio]
    return df


semanas = 6
dias_por_semana = 5
todos_os_fichas = []
todos_os_os_exercicios = {
    "supino": dict(
        exercicio_max_10_vezes=100,
        passo_peso=2.5,
        comecar_com=0.6,
        terminar_com=1.1,
    ),
    "agachamento": dict(
        exercicio_max_10_vezes=200,
        passo_peso=5,
        comecar_com=0.6,
        terminar_com=1.1,
    ),
    "levantamento morto": dict(
        exercicio_max_10_vezes=300,
        passo_peso=10,
        comecar_com=0.6,
        terminar_com=1.1,
    ),
}

for exercicio, dados in todos_os_os_exercicios.items():
    todos_os_fichas.append(
        criar_exercicio(
            semanas=semanas,
            dias_por_semana=dias_por_semana,
            nome_do_exercicio=exercicio,
            **dados,
        )
    )
print(todos_os_fichas)
df = pd.concat(todos_os_fichas).T
