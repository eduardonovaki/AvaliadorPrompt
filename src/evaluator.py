import tiktoken


def contar_tokens(texto):
    encoder = tiktoken.get_encoding("cl100k_base")
    return len(encoder.encode(texto))


def medir_acuracia(resposta, esperado):
    return resposta.strip().upper() == esperado.strip().upper()