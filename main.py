from models.banco_de_perguntas import BancoDePerguntas
from services.quiz_service import QuizService
from ui.menu_terminal import MenuTerminal


def main() -> None:
    banco_de_perguntas = BancoDePerguntas("data/perguntas.json")
    banco_de_perguntas.carregar()

    menu = MenuTerminal()
    quiz_service = QuizService(
        banco_de_perguntas=banco_de_perguntas,
        menu=menu,
    )
    quiz_service.executar()


if __name__ == "__main__":
    main()
