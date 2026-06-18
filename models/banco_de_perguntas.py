import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from models.pergunta import Pergunta


@dataclass
class BancoDePerguntas:
    """Parte de Programacao Orientada a Objetos: carrega as perguntas fixas."""

    caminho_arquivo: Path | str
    perguntas: list[Pergunta] = field(default_factory=list)

    def carregar(self) -> list[Pergunta]:
        caminho = Path(self.caminho_arquivo)

        with caminho.open("r", encoding="utf-8") as arquivo:
            dados: list[dict[str, Any]] = json.load(arquivo)

        self.perguntas = [self._criar_pergunta(item) for item in dados]
        return self.perguntas

    def listar_topicos(self) -> list[str]:
        topicos: list[str] = []

        for pergunta in self.perguntas:
            if pergunta.categoria not in topicos:
                topicos.append(pergunta.categoria)

        return topicos

    def buscar_por_topico(self, topico: str) -> list[Pergunta]:
        topico_normalizado = topico.strip().casefold()

        return [
            pergunta
            for pergunta in self.perguntas
            if pergunta.categoria.casefold() == topico_normalizado
        ]

    def _criar_pergunta(self, dados: dict[str, Any]) -> Pergunta:
        return Pergunta(
            id=dados["id"],
            categoria=dados["categoria"],
            enunciado=dados["enunciado"],
            alternativas=dados["alternativas"],
            resposta_correta=dados["resposta_correta"],
            explicacoes_erros=dados["explicacoes_erros"],
        )
