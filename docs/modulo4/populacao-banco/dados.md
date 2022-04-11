# População - Banco de Dados - Star Wars

## 1. Introdução

Este documento destina-se a apresentar resumidamente de maneira visual os dados para a população do banco de dados.


## 2. Artefato 

### 2.1. Campo astronômico

| ID | Nome | Região | Setor | Atmosfera |
| :-:| :-:  | :-:    | :-:   | :-:       |
| 1  | Tatooine | Territórios da Orla Exterior | Arkanis | Respirável |
| 2  | Coruscant | Mundos do núcleo | Corusca | Respirável |
| 3  | Dagobah | Territórios da Orla Exterior | Sluis | Respirável |
| 4 | Hoth | Territórios da Orla Exterior | Anoat | Respirável |
| 5 | Endor | Territórios da Orla Exterior | Moddell | Respirável |
| 6 | Naboo | Orla Média | Chommell | Respirável |

<a href="https://github.com/SBD1/Grupo02-starWars/blob/main/docs/assets/Canon_galaxy_map.jpg" target="_blank">Clique aqui</a> para ver o mapa da galáxia ampliado.

### 2.2. Região

| ID | Nome | Clima | Governante | Domínio | Nível | Campos Astonomico |
| :-:| :-:  | :-:    | :-:   | :-: | :-: | :-: |
| 1 | Mos Espa | Desértico | Hutts | Cartel Hutt | 1 | Totooine |
| 2 | Bestine | Desértico | Hutts | Cartel Hutt | 2 | Totooine |
| 3 | Mos Eisley | Desértico | Hutts | Cartel Hutt | 1 | Totooine |
| 4 | Mar das Dunas | Desértico | Incursores Tusken | Tribo do povo da areia | 5 | Totooine |
| 5 | Cânion do Mendigo | Desértico | Sem governante | Eremitas | 7 | Totooine |

<a href="https://github.com/SBD1/Grupo02-starWars/blob/main/docs/assets/tatooine.jpg" target="_blank">Clique aqui</a> para ver o mapa de Tatooine ampliado.

## 2.3. Habilidade

| ID | Nome | Descrição | Nível | Impacto | Pré-requisito |
| :-:| :-:  | :-:    | :-:   | :-: | :-: |
| 1 | Tiro simples com blaster | Tiro simples com uma pistola blaster causando impacto a distância no adversários. Utilizado uma vez por turno. | 5 | 10 | Possuir uma pistola blaster |
| 2 | Golpe de sabre de luz | Aplica um golpe corpo a corpo no adversário com o sabre de luz. Utilizado uma vez por turno. | 2 | 20 | Possuir um sabre de luz |
| 3 | Sequência de golpes de sabre de luz | Aplica uma sequência de golpes corpo a corpo no adversário com o sabre de luz. Utilizado uma vez por turno. | 15 | 40 | Possuir um sabre de luz |
| 4 | Levitar objetos | Desloca qualquer objeto no mapa. Pode ser utilizado durante uma batalha para esquivar de golpes à distância. Utilizado uma vez por turno. | 15 | 0 | Ter a ordem Jedi, Gray Jedi ou Sith |
| 5 | Velocidade da força | Utiliza-se da força para se deslocar rapidamento. Pode ser utilizado em batalha para se esquivar de golpes ou aplicar um impacto no adversário mais facilmente. Utilizado uma vez por turno. | 25 | 10 | Ter a ordem Jedi, Gray Jedi ou Sith |
| 6 | Abrir portas com droid | Utiliza-se de um droid para abrir uma porta. | 5 | 0 | Possuir um droid com o modelos astromech |
| 7 | Tradução universal | Utiliza-se de um droid para se comunicar em outras linguas. | 5 | 0 | Possuir um droid com o modelos Protocolo |


#### 2.3.1. Habilidade com arma

| ID | Habilidade | Tipo | Munição |
| :-: | :-: | :-: | :-: |
| 1 | 1 | Blaster Simples | 30 |
| 2 | 2 | Sabre de Luz | 1 |
| 3 | 3 | Sabre de Luz | 1 |


#### 2.3.2 Poderes da Força

| ID | Habilidade | Classificação | Aspecto |
| :-: | :-: | :-: | :-: |
| 1 | 4 | Simples | Contole |
| 2 | 5 | Simples | Alteração |

#### 2.3.3 Habilidade droid

| ID | Habilidade |  Aspecto |
| :-: | :-: | :-: | 
| 1 | 6 | Mobilidade |
| 2 | 7 | Comunicação | 

### 2.5. Itens utilizaveis

| ID | Habilidade | Item | nivel |
| :-: | :-: | :-: | :-: | 
| 1 | 1 | 1 | 5 |

### 2.6. Itens consumiveis

| ID | Item |  Carga |
| :-: | :-: | :-: | 
| 4 | 10 | Mobilidade | 

### 2.8. Jogador

| ID | Nome | Raça | Vida | Nivel | Ordem | Rank | Midichlorians | Inteligencia | Forca_fisica | agilidade | resistencia | espectro_forca |
| :-: | :-: | :-: | :-:  | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | Grogo | senciente | 1000 | 1 | Jedi | Padawan | 0 | 0 | 0 | 0 |0 | 0 |


### 2.9. Oponente

| Nome | Raça | Vida | Midichlorians | Probabilidade | Inteligencia | Forca_fisica | Agilidade | Resistencia | Aspectro_forca |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Nômade Tusken | tusken | 20 | 0 | 0.25 | 02 | 10 | 5 | 0 | 0 | 

### 2.10. Naves

| Nro_Serie | Nome | Descrição | Velocidade máxima | Tipo de arma |
| :-: | :-: | :-: | :-: | :-: |
| YT-1300 | Millennium Falcon | Cargueiro | 1.050 | Duas turreas quad laser |
| MC85 | Raddus | Nave de batalha | 400 | Canhão laser antipessoal |
| AC-3640 | A Arca | Cargueiro | 150 | Não possui |
| CR-400 | Cruzador leve Hutt | Cruzador leve | 560 | Lançadores de mísseis de concussão |

### 2.11. Roteiro

| Título | História | Abertura | 
| :-: | :-: | :-: |
| Episódio I - Parte I - Surgimento dos clones | Um jovem padawan inicia sua trajetória treinando para se tornar Jedi e ajudar o seu povo na guerra. Sua trajetória terá muitos desafios que colocará em dúvida a sua integridade moral. Qual caminho ele seguirá? | Uma inquietação toma conta do Senado Galáctico. Milhares de sistemas solares declararam suas intenções em deixar a República. Esse movimento separatista, sob a liderança do misterioso Conde Dookan, tem criado dificuldades para o limitado número de Cavaleiros Jedi manter a paz e a ordem na galáxia. Senadora Amidala, a antiga rainha de Naboo, está retornando ao Senado Galáctico para a votação da proposta crítica de criação de um Exército da República, para auxiliar os sobrecarregados Jedi... | 

### 2.12. Droid

| NroSerie | Habilidade | Nome | Modelo |
| :-: | :-: | :-: | :-: | 
| D1 | 1 | R2D2 | Astromach |
| D2 | 2 | C3PO | Protocolo |

### 2.13. NPC

| Id | Instancia_item  | Nome | Raça |  Descrição | Dialogo |
| :-: | :-: | :-: | :-: | :-: | :-: | 
| 1 | NULL | Qui-Gon Jinn | Humano | Mestre Jedi do templo | Que a força esteja com você |


### 2.14. Objetivo

| Id | Roteiro  | Ordem | Midichlorians |  PontosForca | Classificacao |
| :-: | :-: | :-: | :-: | :-: | :-: | 
| 1 | 1 | Jedi | 200 | 10 | Primario |

### 2.15. Localização

| Id | latitude | longitude | regiao |  instancia_item | instancia_oponente | instancia_de_nave |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 0 | 0 | 1 | NULL | NULL | NULL |




