import json

from src.tasks import tarefas
from src.techniques import (
    zero_shot,
    few_shot,
    chain_of_thought,
    role_prompting
)
from src.llm_client import LLMClient
from src.evaluator import contar_tokens, medir_acuracia
from src.report import gerar_tabela, grafico_acuracia


client = LLMClient()
resultados = []

# lê os inputs do JSON
with open("data/inputs.json", "r", encoding="utf-8") as arquivo:
    inputs = json.load(arquivo)

# pega a primeira tarefa
tarefa = tarefas[0]

# pega os dados dessa tarefa
dados_tarefa = inputs["classificacao_sentimento"]

# percorre os 5 inputs
for dado in dados_tarefa:
    entrada = dado["input"]
    esperado = dado["esperado"]

    # técnicas normais
    tecnicas = {
        "zero_shot": zero_shot(tarefa, entrada),
        "few_shot": few_shot(tarefa, entrada),
        "chain_of_thought": chain_of_thought(tarefa, entrada)
    }

    for nome, prompt in tecnicas.items():
        resposta = client.chat(prompt)["resposta"]

        resultados.append({
            "tecnica": nome,
            "entrada": entrada,
            "resposta": resposta,
            "esperado": esperado,
            "acuracia": int(medir_acuracia(resposta, esperado)),
            "tokens": contar_tokens(prompt)
        })

    # role prompting separado
    system, user = role_prompting(tarefa, entrada)

    resposta_role = client.chat(user, system=system)["resposta"]

    resultados.append({
        "tecnica": "role_prompting",
        "entrada": entrada,
        "resposta": resposta_role,
        "esperado": esperado,
        "acuracia": int(medir_acuracia(resposta_role, esperado)),
        "tokens": contar_tokens(user)
    })


# gera relatório
df = gerar_tabela(resultados)
grafico_acuracia(resultados)

print(df)
print("Finalizado.")