from models.pergunta import Pergunta
from models.resposta_do_jogador import RespostaDoJogador
from models.resultado import Resultado
from utils.validadores import (
    validar_alternativa,
    validar_jogar_novamente,
    validar_topico,
)


class MenuTerminal:
    """Interface de terminal: concentra input e print do projeto."""

    def solicitar_nome(self) -> str:
        while True:
            nome = input("Informe seu nome: ").strip()

            if nome:
                return nome

            print("Nome nao pode ficar vazio.")

    def exibir_topicos(self, topicos: list[str]) -> None:
        print("\nTopicos disponiveis:")

        for indice, topico in enumerate(topicos, start=1):
            print(f"{indice}. {topico}")

    def solicitar_topico(self, topicos: list[str]) -> str:
        while True:
            escolha = input("Escolha um topico pelo numero: ").strip()

            if validar_topico(escolha, topicos):
                return topicos[int(escolha) - 1]

            print("Topico invalido. Escolha um numero da lista.")

    def exibir_pergunta(
        self,
        pergunta: Pergunta,
        numero_atual: int,
        total: int,
    ) -> None:
        print(f"\nPergunta {numero_atual} de {total}")
        print(pergunta.enunciado)

        for letra in ("A", "B", "C", "D"):
            print(f"{letra}) {pergunta.alternativas[letra]}")

    def solicitar_resposta(self) -> str:
        while True:
            resposta = input("Resposta (A, B, C ou D): ").strip().upper()

            if validar_alternativa(resposta):
                return resposta

            print("Resposta invalida. Digite A, B, C ou D.")

    def exibir_feedback_resposta(
        self,
        pergunta: Pergunta,
        resposta: RespostaDoJogador,
    ) -> None:
        if resposta.foi_correta():
            print("Voce acertou!")
        else:
            print("Voce errou.")

        print(f"Resposta correta: {pergunta.obter_resposta_correta_formatada()}")

        if not resposta.foi_correta():
            print(f"Explicacao: {resposta.explicacao_erro}")

    def aguardar_proxima(self) -> None:
        input("Pressione Enter para continuar...")

    def exibir_resultado(self, resultado: Resultado) -> None:
        print("\nResultado final")
        print(resultado.gerar_resumo())

    def perguntar_jogar_novamente(self) -> bool:
        while True:
            resposta = input("\nDeseja jogar novamente? (S/N): ").strip().upper()

            if validar_jogar_novamente(resposta):
                return resposta == "S"

            print("Opcao invalida. Digite S para sim ou N para nao.")
