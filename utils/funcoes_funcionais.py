from typing import Any, Sequence


# Programacao Funcional: uso de filter com lambda para selecionar perguntas.
def filtrar_perguntas_por_topico(perguntas: Sequence[Any], topico: str) -> list[Any]:
    topico_normalizado = topico.strip().casefold()

    return list(
        filter(
            lambda pergunta: pergunta.categoria.casefold() == topico_normalizado,
            perguntas,
        )
    )


# Programacao Funcional: uso de map com sum para contar respostas corretas.
def calcular_acertos(respostas: Sequence[Any]) -> int:
    return sum(map(lambda resposta: 1 if resposta.foi_correta() else 0, respostas))


# Programacao Funcional: funcao pura, sem alterar estado externo.
def calcular_percentual(acertos: int, total: int) -> float:
    if total == 0:
        return 0.0

    return acertos / total * 100


# Programacao Funcional: funcao pura, resultado depende apenas da entrada.
def gerar_feedback_geral(percentual: float) -> str:
    if percentual >= 80:
        return "Excelente desempenho!"

    if percentual >= 60:
        return "Bom desempenho!"

    return "Revise o conteúdo e tente novamente."
