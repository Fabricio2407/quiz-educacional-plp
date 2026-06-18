import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from models.banco_de_perguntas import BancoDePerguntas
from models.resposta_do_jogador import RespostaDoJogador
from utils.funcoes_funcionais import (
    calcular_acertos,
    calcular_percentual,
    gerar_feedback_geral,
)
from utils.validadores import validar_alternativa


CAMINHO_PERGUNTAS = ROOT / "data" / "perguntas.json"


def carregar_banco() -> BancoDePerguntas:
    banco = BancoDePerguntas(CAMINHO_PERGUNTAS)
    banco.carregar()
    return banco


def carregar_dados_json() -> list[dict]:
    with CAMINHO_PERGUNTAS.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def test_carregar_perguntas_do_json() -> None:
    banco = carregar_banco()
    assert banco.perguntas


def test_total_de_perguntas() -> None:
    banco = carregar_banco()
    assert len(banco.perguntas) == 20


def test_total_de_topicos() -> None:
    banco = carregar_banco()
    assert len(banco.listar_topicos()) == 4


def test_cada_topico_tem_cinco_perguntas() -> None:
    banco = carregar_banco()

    for topico in banco.listar_topicos():
        assert len(banco.buscar_por_topico(topico)) == 5


def test_filtrar_perguntas_por_topico() -> None:
    banco = carregar_banco()
    perguntas = banco.buscar_por_topico("Programação Funcional")

    assert len(perguntas) == 5
    assert all(pergunta.categoria == "Programação Funcional" for pergunta in perguntas)


def test_validar_resposta_correta() -> None:
    banco = carregar_banco()
    pergunta = banco.perguntas[0]

    assert pergunta.verificar_resposta(pergunta.resposta_correta)


def test_validar_resposta_incorreta() -> None:
    banco = carregar_banco()
    pergunta = banco.perguntas[0]
    alternativa_errada = next(
        alternativa
        for alternativa in pergunta.alternativas
        if alternativa != pergunta.resposta_correta
    )

    assert not pergunta.verificar_resposta(alternativa_errada)


def test_calcular_acertos() -> None:
    respostas = [
        RespostaDoJogador(1, "Topico", "A", "A", True),
        RespostaDoJogador(2, "Topico", "B", "C", False),
        RespostaDoJogador(3, "Topico", "D", "D", True),
    ]

    assert calcular_acertos(respostas) == 2


def test_calcular_percentual() -> None:
    assert calcular_percentual(4, 5) == 80.0
    assert calcular_percentual(0, 0) == 0.0


def test_gerar_feedback_geral() -> None:
    assert gerar_feedback_geral(80) == "Excelente desempenho!"
    assert gerar_feedback_geral(60) == "Bom desempenho!"
    assert gerar_feedback_geral(40) == "Revise o conteúdo e tente novamente."


def test_validar_entrada_alternativa() -> None:
    assert validar_alternativa("A")
    assert validar_alternativa("b")
    assert not validar_alternativa("E")
    assert not validar_alternativa("")


def test_nao_existe_campo_dificuldade() -> None:
    dados = carregar_dados_json()

    assert all("dificuldade" not in pergunta for pergunta in dados)


def executar_testes() -> None:
    testes = [
        test_carregar_perguntas_do_json,
        test_total_de_perguntas,
        test_total_de_topicos,
        test_cada_topico_tem_cinco_perguntas,
        test_filtrar_perguntas_por_topico,
        test_validar_resposta_correta,
        test_validar_resposta_incorreta,
        test_calcular_acertos,
        test_calcular_percentual,
        test_gerar_feedback_geral,
        test_validar_entrada_alternativa,
        test_nao_existe_campo_dificuldade,
    ]

    for teste in testes:
        teste()

    print("Todos os testes passaram.")


if __name__ == "__main__":
    executar_testes()
