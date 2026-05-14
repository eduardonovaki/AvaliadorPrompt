def montar_prompt(instrucao, contexto, input_dados, formato_output):
    if not all([instrucao, input_dados, formato_output]):
        raise ValueError("Campos obrigatórios faltando.")

    prompt = f"""
Instrução:
{instrucao}

Contexto:
{contexto}

Input:
{input_dados}

Formato de saída:
{formato_output}
"""
    return prompt.strip()


def adicionar_exemplos(prompt, exemplos):
    texto_exemplos = "\n\nExemplos:\n"

    for exemplo in exemplos:
        texto_exemplos += (
            f'Input: {exemplo["input"]}\n'
            f'Output: {exemplo["output"]}\n\n'
        )

    return prompt + texto_exemplos


def adicionar_cot(prompt, passos):
    texto_passos = "\nPense passo a passo:\n"

    for i, passo in enumerate(passos, 1):
        texto_passos += f"{i}. {passo}\n"

    return prompt + texto_passos    