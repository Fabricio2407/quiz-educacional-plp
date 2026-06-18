# Relatório do Projeto Quiz Educacional PLP

## 1. Introdução

O Quiz Educacional PLP é um projeto acadêmico desenvolvido em Python para a disciplina de Paradigmas de Linguagens de Programação. O sistema funciona no terminal e tem como objetivo demonstrar, de forma simples, o uso de Programação Orientada a Objetos e Programação Funcional em um mesmo projeto.

O quiz possui 4 tópicos, com 5 perguntas por tópico, totalizando 20 perguntas fixas armazenadas em um arquivo JSON. O usuário informa seu nome, escolhe um tópico, responde às perguntas e recebe um resultado final.

## 2. Funcionalidades principais

- Cadastro simples do nome do jogador.
- Listagem de 4 tópicos disponíveis.
- Escolha de um tópico pelo usuário.
- Exibição de 5 perguntas do tópico escolhido.
- Alternativas fixas A, B, C e D.
- Validação de entradas no terminal.
- Feedback imediato após cada resposta.
- Exibição da alternativa correta.
- Explicação específica apenas quando o usuário erra.
- Resultado final com acertos, erros, percentual e feedback geral.
- Opção de jogar novamente ou sair.

## 3. Programação Orientada a Objetos no projeto

A Programação Orientada a Objetos foi usada para representar os principais elementos do domínio do quiz.

As classes principais estão na pasta `models/`:

- `Pergunta`: guarda enunciado, alternativas, resposta correta e explicações de erro.
- `RespostaDoJogador`: registra a alternativa escolhida e se ela está correta.
- `Jogador`: guarda o nome do jogador e suas respostas.
- `Quiz`: controla o estado da partida, pergunta atual e registro de respostas.
- `Resultado`: calcula e apresenta o resumo final.
- `BancoDePerguntas`: carrega as perguntas do arquivo JSON e permite buscar por tópico.

Essa organização ajuda a separar responsabilidades e deixa o código mais fácil de entender e defender.

## 4. Programação Funcional no projeto

A Programação Funcional aparece no arquivo `utils/funcoes_funcionais.py`.

Foram usados recursos como:

- `filter` com `lambda` para selecionar perguntas de um tópico.
- `map` com `sum` para contar respostas corretas.
- Funções puras para calcular percentual e gerar feedback geral.

As funções puras não alteram estado externo e sempre retornam o mesmo resultado quando recebem os mesmos valores.

## 5. Comparação entre os paradigmas

No projeto, a Programação Orientada a Objetos foi mais adequada para modelar entidades com dados e comportamentos, como jogador, pergunta, quiz e resultado.

A Programação Funcional foi mais adequada para operações de transformação, filtragem e cálculo, como filtrar perguntas por tópico, contar acertos e calcular percentual.

Assim, os dois paradigmas foram usados de forma complementar: OO para estruturar o domínio e Programação Funcional para cálculos e operações sem efeitos colaterais.

## 6. Vantagens e limitações

Vantagens da Programação Orientada a Objetos:

- Organização clara das entidades do sistema.
- Facilidade para representar conceitos reais do quiz.
- Separação de responsabilidades em classes.

Limitações da Programação Orientada a Objetos:

- Pode gerar mais arquivos e estruturas mesmo em projetos pequenos.
- Exige cuidado para não misturar regra de negócio com interface.

Vantagens da Programação Funcional:

- Funções simples e reutilizáveis.
- Cálculos mais fáceis de testar.
- Menor dependência de estado externo.

Limitações da Programação Funcional:

- Pode ser menos intuitiva para representar entidades completas.
- Em alguns casos, o uso de `lambda`, `map` e `filter` pode ser menos direto para iniciantes.

## 7. Em quais situações cada paradigma é mais indicado

A Programação Orientada a Objetos é indicada quando o sistema possui entidades bem definidas, com atributos e comportamentos próprios. Neste projeto, ela foi usada para representar pergunta, jogador, quiz e resultado.

A Programação Funcional é indicada para cálculos, validações, filtros e transformações de dados. Neste projeto, ela foi usada para filtrar perguntas, calcular acertos, calcular percentual e gerar feedback geral.

## 8. Conclusão

O projeto atingiu o objetivo de criar um quiz simples em Python no terminal, sem adicionar funcionalidades fora do escopo. A solução mostra a aplicação prática de Programação Orientada a Objetos e Programação Funcional em partes diferentes do mesmo sistema.

A estrutura final ficou simples, organizada e adequada para apresentação acadêmica, com separação entre domínio, serviço, interface de terminal, funções utilitárias, dados e documentação.
