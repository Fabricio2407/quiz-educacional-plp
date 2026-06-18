from dataclasses import dataclass

from models.jogador import Jogador
from models.pergunta import Pergunta
from models.resposta_do_jogador import RespostaDoJogador
from models.resultado import Resultado


@dataclass
class Quiz:
    """Parte de Programacao Orientada a Objetos: controla o estado do quiz."""

    jogador: Jogador
    topico: str
    perguntas: list[Pergunta]
    indice_atual: int = 0

    def tem_proxima_pergunta(self) -> bool:
        return self.indice_atual < len(self.perguntas)

    def obter_pergunta_atual(self) -> Pergunta | None:
        if not self.tem_proxima_pergunta():
            return None

        return self.perguntas[self.indice_atual]

    def avancar(self) -> None:
        if self.tem_proxima_pergunta():
            self.indice_atual += 1

    def registrar_resposta(self, alternativa_escolhida: str) -> RespostaDoJogador:
        pergunta = self.obter_pergunta_atual()

        if pergunta is None:
            raise IndexError("Nao ha pergunta atual para responder.")

        correta = pergunta.verificar_resposta(alternativa_escolhida)
        explicacao_erro = ""

        if not correta:
            explicacao_erro = pergunta.obter_explicacao_erro(alternativa_escolhida)

        resposta = RespostaDoJogador(
            pergunta_id=pergunta.id,
            categoria=pergunta.categoria,
            alternativa_escolhida=alternativa_escolhida.strip().upper(),
            resposta_correta=pergunta.resposta_correta.strip().upper(),
            correta=correta,
            explicacao_erro=explicacao_erro,
        )

        self.jogador.registrar_resposta(resposta)
        return resposta

    def finalizar(self) -> Resultado:
        return Resultado.criar_a_partir_respostas(
            jogador_nome=self.jogador.nome,
            respostas=self.jogador.respostas,
        )
