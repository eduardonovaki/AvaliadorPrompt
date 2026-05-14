from src.prompt_builder import (
    montar_prompt,
    adicionar_exemplos,
    adicionar_cot
)


def zero_shot(tarefa, input_texto):
    return montar_prompt(
        tarefa["instrucao"],
        "",
        input_texto,
        tarefa["formato_output"]
    )


def few_shot(tarefa, input_texto):
    prompt = montar_prompt(
        tarefa["instrucao"],
        "",
        input_texto,
        tarefa["formato_output"]
    )

    return adicionar_exemplos(
        prompt,
        tarefa["exemplos_fewshot"]
    )


def chain_of_thought(tarefa, input_texto):
    prompt = montar_prompt(
        tarefa["instrucao"],
        "",
        input_texto,
        tarefa["formato_output"]
    )

    return adicionar_cot(
        prompt,
        tarefa["passos_cot"]
    )


def role_prompting(tarefa, input_texto):
    system = tarefa["persona"]

    user = montar_prompt(
        tarefa["instrucao"],
        "",
        input_texto,
        tarefa["formato_output"]
    )

    return system, user