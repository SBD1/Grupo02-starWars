# **Especificação do domínio**

## **1. Introdução**

<p style='text-align: justify;'>Domínio é o tipo de dados que descreve os tipos de valores que podem aparecer em cada coluna do SGBD, especificando os valores que um atributo pode possuir, a definição adequada do domínio é essencial para evitar inconsistência nos dados armazenados.</p>

## **2. Artefato**

### **2.1. Corpo Astronômico** 
| Atributo | Descrição | Tipo de dado e formato |
| :-: | :-- | :-: |
| Nome | Conjunto de todos os possíveis nomes para o corpo astronômico | String - 60 Caracteres |
| Região | Conjunto de todos os possíveis nomes para a região onde o corpo astronômico pertence | String - 60 Caracteres |
| Setor | Conjunto de todos os possíveis nomes do setor do corpo astronômico | String - 60 Caracteres |
| Atmosfera | Descreve se a atmosfera é respirável para humanos ou não | Boolean |


### **2.2. Região**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| ID | Quantidade inteira que ordena a região | Inteiro - Acima de -1 |
| Nome | Conjunto de todos os possíveis nomes para a região | String - 60 Caracteres |
| Clima | Conjunto de todos os climas predominantes da região | String - 60 Caracteres |
| Governante | Conjunto de todos os nomes possíveis dos Gorvenantes da região |String - 60 Caracteres |
| Domínio | Conjunto de todos os nomes possíveis para o grupo dominante da região | String - 60 Caracteres |
| Nível | Número do nível da região | Inteiro entre 1 a 100|


### **2.3. Localização** 

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Latitude | Conjunto de todos os números possíveis do eixo Y | Inteiro |
| Longitude | Conjunto de todos os números possíveis do eixo X | Inteiro |

### **2.4. Personagem**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| ID | Quantidade inteira que ordena o personagem | Inteiro - Acima de -1 |
| Nome | Conjunto de todos os possíveis nomes para o personagem | String - 30 Caracteres |
| Raça | Conjunto de todas as possíveis raças que o personagem pode ser | String - 60 Caracteres |

#### **2.4.1. NPC** 
| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Descrição | Conjunto de todas as descrições dos NPCs | String - 120 Caracteres |
| Diálogo | Conjunto de todos os diálogos possíveis com os NPCs | String - 120 Caracteres |

#### **2.4.2. Oponente** 

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Vida | Quantidade inteira de vida do oponente | Inteiro - Acima de 0 |
| Inteligência | Quantidade inteira de inteligência do oponente | Inteiro - Acima de 0 |
| Força Física | Quantidade inteira de força física do oponente | Inteiro - Acima de 0 |
| Agilidade | Quantidade inteira de agilidade do oponente | Inteiro - Acima de 0 |
| Resitência | Quantidade inteira de resitência do oponente | Inteiro - Acima de 0 |
| Força  | Quantidade inteira de força do oponente | Inteiro - Entre -50 até 50 |
| Midichlorians | Quantidade inteira de experiência que o jogador ganha ao derrotar o oponente | Inteiro - Entre 0 e 1000 |
| Probabilidade | Quantidade em ponto flutuante de obtenção de um item do oponente | Double - 2 Casas decimais |

#### **2.4.3. Jogador** 

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Vida | Quantidade inteira de vida do oponente | Inteiro - Acima de 0 |
| Midichlorians | Quantidade inteira de experiência que o jogador tem | Inteiro - Entre 0 e 100000 |
| Nível | Quantidade inteira do nível do personagem | Inteiro entre 1 a 100 |
| Rank | Conjunto de todos os possíveis nomes para o Rank | String - 30 Caracteres |
| Inteligência | Quantidade inteira de inteligência do oponente | Inteiro - Acima de 0 |
| Força Física | Quantidade inteira de força física do oponente | Inteiro - Acima de 0 |
| Agilidade | Quantidade inteira de agilidade do oponente | Inteiro - Acima de 0 |
| Resitência | Quantidade inteira de resitência do oponente | Inteiro - Acima de 0 |
| Força  | Quantidade inteira de força do oponente | Inteiro - Entre -50 até 50 |

### **2.5. Instância de Oponente**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| ID | Quantidade inteira que ordena o oponente | Inteiro - Acima de -1 |

### **2.6. Itens**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| ID | Quantidade inteira que ordena o oponente | Inteiro - Acima de -1 |
| Nome | Conjunto de todos os possíveis nomes para o item | String - 30 Caracteres |
| Descrição | Conjunto de todas as possíveis descrições do item | String - 120 Caracteres |
| Tipo | Conjunto de todas os possíveis tipos de itens |  String - 30 Caracteres |

#### **2.6.1. Itens Consumíveis** 

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Carga | Quantidade inteira de itens consumíveis | Inteiro - Entre 0 e 10 |

#### **2.6.2. Itens Utilizáveis** 

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Pré-condições | Conjunto de todas as possíveis pré-condições de utilização do item | String - 120 Caracteres |

### **2.7. Instância de item**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| ID | Quantidade inteira que ordena os itens | Inteiro - Acima de -1 |

### **2.8. Habilidade**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| ID | Quantidade inteira que ordena os itens | Inteiro - Acima de -1 |
| Nome | Conjunto de todos os possíveis nomes para a habilidade | String - 30 Caracteres |
| Descrição | Conjunto de todas as possíveis descrições da habilidade | String - 120 Caracteres |
| Nível | Quantidade inteira do nível da habilidade | Inteiro entre 1 a 100 |
| Impacto | Quantidade inteira do impacto da habilidade | Inteiro - Acima de 0 |
| Pré-requisito | Conjunto de todos os possíveis pré-requisitos de utilização da habilidade | String - 120 Caracteres |

#### **2.8.1. Habilidade com arma**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Tipo | Conjunto dos possíveis tipos que a habilidade com a arma pode ser | String - 30 Caracteres |
| Munição | Quantidade inteira de munição da arma | Inteiro - Entre 0 a 100 |

#### **2.8.2. Poderes da Força**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Classificação | Indica se a habilidade é especial ou não | Boolean |
| Aspecto | Conjunto dos possíveis aspectos do poder da força | String - 30 Caracteres |

#### **2.8.3. Habilidade do droid**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Aspecto | Conjunto dos possíveis aspectos do poder do droid | String - 30 Caracteres |

### **2.9. Nave**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Número de série | Conjunto dos possíveis números de série | String - 15 Caracteres |
| Nome | Conjunto de todos os possíveis nomes para a nave | String - 30 Caracteres |
| Descrição | Conjunto de todas as possíveis descrições da nave | String - 120 Caracteres |
| Velocidade Máxima | Conjunto de números inteiros da velocidade máxima medida em Warp | Inteiro entre 0 e 9 |
| Tipo de Arma | Conjunto das possíveis armas que a nave pode ter | String - 30 Caracteres |

### **2.10. Instância de nave** 

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| ID | Quantidade inteira que ordena as naves | Inteiro - Acima de -1 |

### **2.11. Objetivo**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| ID | Quantidade inteira que ordena as naves | Inteiro - Acima de -1 |
| Ordem | Conjunto das possíveis ordens que o objetivo pertence | | String - 30 Caracteres |
| Midichlorians | Quantidade inteira de experiência que o jogador ganha ao cumprir o objetivo | Inteiro - Entre 0 e 1000 |
| Pont. Força | Conjunto de quantidades inteiras de força que o jogador ganha ao cumprir o objetivo | Inteiro - Entre -10 a 10 |
| Classificação | Indica se o objetivo é primário ou não | Boolean |

### **2.12. Roteiro do episódio**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Título | Conjunto de todos os possíveis títulos para o episódio | String - 60 Caracteres |
| História | Conjunto de todas as possíveis histórias do episódio | String - 500 caracteres |
| Abertura | Conjunto de todas as possíveis aberturas do episódio | String - 500 caracteres |

### **2.13. Droid**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Número de série | Conjunto dos possíveis números de série | String - 15 Caracteres |
| Nome | Conjunto de todos os possíveis nomes para o droid | String - 30 Caracteres |
| Modelo | Conjunto de todos os possíveis modelos do droid | String - 30 Caracteres |

### **2.14. Relacionmaneto Cumpre (Jogador-objetivo)**

| Atributo| Descrição| Tipo de dado e formato |
| :-: | :-- | :-: |
| Status | Descreve se o jogador cumpriu ou não o objetivo| Boolean |