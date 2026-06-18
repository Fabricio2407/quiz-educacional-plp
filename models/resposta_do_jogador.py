from dataclasses import dataclass


@dataclass
class RespostaDoJogador:
    """Parte de Programacao Orientada a Objetos: registra uma resposta dada."""

    pergunta_id: int
    categoria: str
    alternativa_escolhida: str
    resposta_correta: str
    correta: bool
    explicacao_erro: str = ""

    def foi_correta(self) -> bool:
        return self.correta
