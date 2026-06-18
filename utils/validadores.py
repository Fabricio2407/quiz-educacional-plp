# Validadores simples usados pela interface de terminal.


def validar_alternativa(resposta: str) -> bool:
    return resposta.strip().upper() in {"A", "B", "C", "D"}


def validar_topico(escolha: str, topicos: list[str]) -> bool:
    if not escolha.strip().isdigit():
        return False

    numero = int(escolha)
    return 1 <= numero <= len(topicos)


def validar_jogar_novamente(resposta: str) -> bool:
    return resposta.strip().upper() in {"S", "N"}
