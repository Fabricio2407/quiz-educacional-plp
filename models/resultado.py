from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from models.resposta_do_jogador import RespostaDoJogador


@dataclass
class Resultado:
    """Parte de Programacao Orientada a Objetos: resume o desempenho final."""

    jogador_nome: str
    total_perguntas: int
    acertos: int
    erros: int
    percentual: float
    feedback_geral: str

    def calcular_erros(self) -> int:
        return self.total_perguntas - self.acertos

    def gerar_resumo(self) -> str:
        return (
            f"Jogador: {self.jogador_nome}\n"
            f"Total de perguntas: {self.total_perguntas}\n"
            f"Acertos: {self.acertos}\n"
            f"Erros: {self.erros}\n"
            f"Percentual: {self.percentual:.1f}%\n"
            f"Feedback: {self.feedback_geral}"
        )

    @classmethod
    def criar_a_partir_respostas(
        cls,
        jogador_nome: str,
        respostas: Sequence[RespostaDoJogador],
    ) -> Resultado:
        total_perguntas = len(respostas)
        acertos = sum(1 for resposta in respostas if resposta.foi_correta())
        erros = total_perguntas - acertos
        percentual = (acertos / total_perguntas * 100) if total_perguntas else 0.0

        return cls(
            jogador_nome=jogador_nome,
            total_perguntas=total_perguntas,
            acertos=acertos,
            erros=erros,
            percentual=percentual,
            feedback_geral=cls._gerar_feedback_geral(percentual),
        )

    @staticmethod
    def _gerar_feedback_geral(percentual: float) -> str:
        if percentual == 100:
            return "Excelente desempenho."

        if percentual >= 70:
            return "Bom desempenho."

        if percentual >= 50:
            return "Desempenho regular."

        return "Continue estudando o conteudo."
