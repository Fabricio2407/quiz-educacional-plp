# Quiz Educacional PLP

Projeto academico da disciplina de Paradigmas de Linguagens de Programacao (PLP).

O objetivo do projeto e construir um quiz educacional simples, executado no terminal com Python. Nesta fase, o repositorio contem apenas a estrutura inicial do sistema, sem implementacao das regras do quiz.

## Escopo previsto

- Aplicacao em Python executada pelo terminal.
- 4 topicos de perguntas.
- 5 perguntas por topico.
- 20 perguntas no total.
- Perguntas fixas armazenadas em `data/perguntas.json`.
- Sem frontend, banco de dados real, login, API, ranking, dificuldade ou embaralhamento.

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicacao.
- `models/`: classes de dominio.
- `services/`: orquestracao do fluxo do quiz.
- `ui/`: entrada e saida no terminal.
- `utils/`: validadores e funcoes auxiliares/funcionais.
- `data/`: arquivo com as perguntas fixas.
- `docs/`: materiais de relatorio, roteiro e slides.

## Dependencias

No momento, o projeto usa apenas a biblioteca padrao do Python.
