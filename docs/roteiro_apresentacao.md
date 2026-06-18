# Roteiro de apresentação

## 1. Como abrir o projeto

1. Abrir a pasta do projeto no editor.
2. Mostrar rapidamente a estrutura:
   - `main.py`
   - `models/`
   - `services/`
   - `ui/`
   - `utils/`
   - `data/perguntas.json`
   - `docs/`

## 2. Como rodar

No terminal, executar:

```bash
python main.py
```

## 3. Como demonstrar o quiz

1. Informar o nome do jogador.
2. Mostrar que o sistema lista 4 tópicos.
3. Escolher um tópico pelo número.
4. Responder uma pergunta corretamente.
5. Mostrar que o sistema informa o acerto e exibe a alternativa correta.
6. Responder uma pergunta incorretamente.
7. Mostrar que o sistema informa o erro, exibe a alternativa correta e apresenta a explicação.
8. Digitar uma entrada inválida, como `E`, para mostrar a validação.
9. Finalizar as 5 perguntas.
10. Mostrar o resultado final com acertos, erros, percentual e feedback geral.
11. Testar a opção de jogar novamente com `S`.
12. Encerrar com `N`.

## 4. Onde apontar Programação Orientada a Objetos

Apontar a pasta `models/`.

- `Pergunta`: representa cada pergunta.
- `Jogador`: representa o participante.
- `RespostaDoJogador`: registra cada resposta.
- `Quiz`: controla o estado da partida.
- `Resultado`: representa o resumo final.
- `BancoDePerguntas`: carrega e organiza as perguntas.

Explicação curta: a Programação Orientada a Objetos foi usada para modelar as entidades principais do quiz.

## 5. Onde apontar Programação Funcional

Apontar o arquivo `utils/funcoes_funcionais.py`.

- `filtrar_perguntas_por_topico`: usa `filter` e `lambda`.
- `calcular_acertos`: usa `map` e `sum`.
- `calcular_percentual`: função pura.
- `gerar_feedback_geral`: função pura.

Explicação curta: a Programação Funcional foi usada para filtros e cálculos sem depender de estado externo.

## 6. Frase final de defesa

O projeto foi mantido simples para demonstrar claramente os dois paradigmas: a Programação Orientada a Objetos organiza as entidades do quiz, enquanto a Programação Funcional resolve filtros e cálculos de forma direta e reutilizável.
