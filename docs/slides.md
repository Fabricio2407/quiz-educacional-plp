# Roteiro de slides

## 1. Capa

- Quiz Educacional PLP
- Disciplina: Paradigmas de Linguagens de Programação
- Projeto em Python no terminal
- Nome dos integrantes

## 2. Objetivo do projeto

- Criar um quiz educacional simples.
- Demonstrar Programação Orientada a Objetos.
- Demonstrar Programação Funcional.
- Manter o sistema direto e fácil de executar.

## 3. Funcionalidades principais

- Usuário informa o nome.
- Sistema lista 4 tópicos.
- Usuário escolhe um tópico.
- Sistema apresenta 5 perguntas.
- Usuário responde com A, B, C ou D.
- Sistema mostra feedback imediato.
- Resultado final mostra acertos, erros, percentual e feedback geral.

## 4. Modelagem OO

- `Pergunta`: dados e validação da resposta.
- `RespostaDoJogador`: resposta escolhida pelo usuário.
- `Jogador`: nome e lista de respostas.
- `Quiz`: estado da partida.
- `Resultado`: resumo final.
- `BancoDePerguntas`: carregamento das perguntas.

## 5. Programação Funcional

- Arquivo: `utils/funcoes_funcionais.py`.
- Uso de `filter` e `lambda` para filtrar perguntas.
- Uso de `map` e `sum` para contar acertos.
- Funções puras para percentual e feedback.

## 6. Fluxo do sistema

- `main.py` monta as dependências.
- `QuizService` coordena a partida.
- `MenuTerminal` faz entrada e saída no terminal.
- `BancoDePerguntas` carrega o JSON.
- `Quiz` registra respostas.
- `Resultado` resume o desempenho.

## 7. Comparação dos paradigmas

- OO organiza entidades e responsabilidades.
- Programação Funcional facilita filtros e cálculos.
- Os dois paradigmas foram usados juntos.
- OO ficou mais forte na modelagem.
- Funcional ficou mais forte nas operações sobre dados.

## 8. Demonstração

- Rodar `python main.py`.
- Informar nome.
- Escolher um tópico.
- Responder uma pergunta correta.
- Responder uma pergunta errada.
- Mostrar explicação do erro.
- Mostrar resultado final.
- Testar jogar novamente ou sair.

## 9. Conclusão

- O quiz funciona no terminal.
- O projeto usa OO e Programação Funcional.
- O escopo foi mantido simples.
- Não há frontend, banco real, ranking, dificuldade ou embaralhamento.
