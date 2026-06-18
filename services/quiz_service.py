from dataclasses import dataclass

from models.banco_de_perguntas import BancoDePerguntas
from models.jogador import Jogador
from models.quiz import Quiz
from ui.menu_terminal import MenuTerminal


@dataclass
class QuizService:
    """Orquestra o fluxo jogavel sem usar input ou print diretamente."""

    banco_de_perguntas: BancoDePerguntas
    menu: MenuTerminal

    def executar(self) -> None:
        jogar_novamente = True

        while jogar_novamente:
            self.executar_partida()
            jogar_novamente = self.menu.perguntar_jogar_novamente()

    def executar_partida(self) -> None:
        nome = self.menu.solicitar_nome()
        topicos = self.banco_de_perguntas.listar_topicos()

        self.menu.exibir_topicos(topicos)
        topico = self.menu.solicitar_topico(topicos)
        perguntas = self.banco_de_perguntas.buscar_por_topico(topico)

        jogador = Jogador(nome=nome)
        quiz = Quiz(jogador=jogador, topico=topico, perguntas=perguntas)
        total = len(perguntas)

        while quiz.tem_proxima_pergunta():
            pergunta = quiz.obter_pergunta_atual()

            if pergunta is None:
                break

            numero_atual = quiz.indice_atual + 1
            self.menu.exibir_pergunta(pergunta, numero_atual, total)

            alternativa_escolhida = self.menu.solicitar_resposta()
            resposta = quiz.registrar_resposta(alternativa_escolhida)

            self.menu.exibir_feedback_resposta(pergunta, resposta)
            self.menu.aguardar_proxima()
            quiz.avancar()

        resultado = quiz.finalizar()
        self.menu.exibir_resultado(resultado)
