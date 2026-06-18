# Quiz Educacional PLP

Projeto acadêmico da disciplina de Paradigmas de Linguagens de Programação (PLP).

## Objetivo

O objetivo do projeto é apresentar um quiz educacional simples, executado no terminal, usando Python para demonstrar conceitos de Programação Orientada a Objetos e Programação Funcional.

O sistema permite que o usuário informe seu nome, escolha um tópico, responda 5 perguntas e veja o resultado final com acertos, erros, percentual e feedback geral.

## Tecnologias usadas

- Python
- Terminal
- JSON para armazenar perguntas fixas
- Biblioteca padrão do Python

## Como rodar

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

Para rodar os testes simples:

```bash
python tests/test_quiz.py
```

## Estrutura de pastas

- `main.py`: ponto de entrada da aplicação.
- `models/`: classes de domínio do quiz.
- `services/`: orquestração do fluxo da partida.
- `ui/`: entrada e saída no terminal.
- `utils/`: validadores e funções funcionais.
- `data/`: perguntas fixas em JSON.
- `tests/`: testes simples do funcionamento principal.
- `docs/`: relatório, roteiro de apresentação e slides.

## Funcionalidades

- Solicitar o nome do jogador.
- Listar 4 tópicos.
- Permitir a escolha de um tópico.
- Apresentar 5 perguntas do tópico escolhido.
- Validar respostas A, B, C ou D.
- Mostrar feedback imediato após cada resposta.
- Mostrar a alternativa correta em todas as respostas.
- Mostrar explicação apenas quando o usuário erra.
- Exibir resultado final com acertos, erros, percentual e feedback geral.
- Permitir jogar novamente ou sair.

## Programação Orientada a Objetos

A Programação Orientada a Objetos aparece principalmente na pasta `models/`.

- `Pergunta`: representa uma pergunta do quiz.
- `RespostaDoJogador`: representa uma resposta dada pelo jogador.
- `Jogador`: armazena o nome e as respostas do participante.
- `Quiz`: controla o estado de uma partida.
- `Resultado`: resume o desempenho final.
- `BancoDePerguntas`: carrega as perguntas fixas e filtra por tópico.

Essas classes organizam os dados e comportamentos principais do domínio do quiz.

## Programação Funcional

A Programação Funcional aparece em `utils/funcoes_funcionais.py`.

O projeto usa:

- `filter` com `lambda` para filtrar perguntas por tópico.
- `map` com `sum` para calcular acertos.
- Funções puras para calcular percentual e gerar feedback geral.

Essas funções não dependem de `input()` ou `print()` e retornam resultado com base apenas nos valores recebidos.

## Fora do escopo

Este projeto não possui:

- Frontend.
- Banco de dados real.
- Login.
- API.
- Ranking.
- Níveis de dificuldade.
- Embaralhamento de perguntas.
- Timer.
- Sons, imagens ou animações.
