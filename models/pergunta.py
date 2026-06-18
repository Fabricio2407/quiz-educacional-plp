from dataclasses import dataclass, field


@dataclass
class Pergunta:
    """Parte de Programacao Orientada a Objetos: representa uma pergunta."""

    id: int
    categoria: str
    enunciado: str
    alternativas: dict[str, str]
    resposta_correta: str
    explicacoes_erros: dict[str, str] = field(default_factory=dict)

    def verificar_resposta(self, resposta_usuario: str) -> bool:
        resposta_normalizada = self._normalizar_alternativa(resposta_usuario)
        resposta_correta_normalizada = self._normalizar_alternativa(self.resposta_correta)
        return resposta_normalizada == resposta_correta_normalizada

    def obter_resposta_correta_formatada(self) -> str:
        alternativa = self._normalizar_alternativa(self.resposta_correta)
        texto = self.alternativas.get(alternativa, "")

        if texto:
            return f"{alternativa}) {texto}"

        return alternativa

    def obter_explicacao_erro(self, resposta_usuario: str) -> str:
        if self.verificar_resposta(resposta_usuario):
            return ""

        resposta_normalizada = self._normalizar_alternativa(resposta_usuario)
        return self.explicacoes_erros.get(
            resposta_normalizada,
            "Nao ha explicacao cadastrada para esta alternativa.",
        )

    def _normalizar_alternativa(self, alternativa: str) -> str:
        return alternativa.strip().upper()
