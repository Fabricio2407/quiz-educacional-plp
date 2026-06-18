from dataclasses import dataclass, field

from models.resposta_do_jogador import RespostaDoJogador


@dataclass
class Jogador:
    """Parte de Programacao Orientada a Objetos: representa o participante."""

    nome: str
    respostas: list[RespostaDoJogador] = field(default_factory=list)

    def registrar_resposta(self, resposta: RespostaDoJogador) -> None:
        self.respostas.append(resposta)

    def obter_total_respostas(self) -> int:
        return len(self.respostas)
