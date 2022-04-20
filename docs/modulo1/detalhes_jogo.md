# **Star Wars: The Shattering of the Force**

## **História do Jogo**

## **Episódio I - Parte I - Surgimento dos clones**

### **Abertura**

<p style='text-align: justify;'>Um jovem padawan inicia sua trajetória treinando para se tornar Jedi e ajudar o seu povo na guerra. Sua trajetória terá muitos desafios que colocará em dúvida a sua integridade moral. Qual caminho ele seguirá?</p>

### **História**

<p style='text-align: justify;'>Uma inquietação toma conta do Senado Galáctico. Milhares de sistemas solares declararam suas intenções em deixar a República. Esse movimento separatista, sob a liderança do misterioso Conde Dookan, tem criado dificuldades para o limitado número de Cavaleiros Jedi manter a paz e a ordem na galáxia. Senadora Amidala, a antiga rainha de Naboo, está retornando ao Senado Galáctico para a votação da proposta crítica de criação de um Exército da República, para auxiliar os sobrecarregados Jedi...</p>

### **Mapa**

![Mapa - Coruscant](../assets/mapaCoruscant.png)

## **Glossário**

### **2. - Jogador**

<p style='text-align: justify;'>É o usuário do jogo, onde pode realizar ações pelo mapa e subir de nível. No início do game, ele pode escolher a ordem (Jedi ou Sith). De acordo com suas ações no game, ele pode mudar de lado da força.</p>

#### **2.1. - Atributos**

- **ID:** Elemento identificador do personagem no banco;
- **Nome:** Nome que o personagem quer utilizar, string de tamanho 20;
- **Vida:** Calculado pelo sistema. Aumentada a cada nível. (Ex: começa com 10 e vai aumentando 1 em 1 a cada nível);
- **Midichlorians:** É a experiência do jogador que evolui a cada ação. Pode aumentar através da realização dos objetivos ou quando se vence um oponente;
- **Nível:** Nível do jogador que aumenta a cada ação (definir teto para cada nível);
- **Rank:** De acordo com a ordem escolhida pode ser: padawans (para os níveis iniciais e depois ele pode escolher a ordem), cavaleiro Jedi e mestre Jedi ou Sith Lord, Darth Lord Sith. Há também a ordem neutra chamada Gray Jedi.
- **Raça:** Pode ser humano, togruta, Twi’lek, Korun, Fallen, Mirialano;
- **Características:** Elas influenciam diretamente no dano que o personagem pode causar no oponente, bem como nas habilidades. A cada nível o jogador pode acrescentar em: Inteligencia, Força Física, Agilidade, Resistência.
- **Força:** A Força Viva é vista como influenciada pelas emoções dos seres vivos. Possui dois aspectos: Luz e Trevas, que têm a ver com as atitudes morais dos seres. A Luz é caracterizada pela compaixão, bondade, altruísmo, humildade. O lado sombrio é caracterizado por ódio, raiva, maldade e ganância. Na filosofia Jedi, a Força é a luz, ou seja: é serena e equilibrada. O lado sombrio abala este equilíbrio com sentimentos negativos.

### **2.2. -  Ordem**

A ordem pode ser escolhida depois do nível 10, onde o padawan deixa de ser padawan e escolhe entre Jedi e Sith. Importante esclarecer que o personagem pode transitar entre Jedi e Sith de acordo com as ações no jogo que implica no aumento da luz ou trevas da força. Se a força tem uma quantidade de luz muito superior que as trevas, então considera-se o jogador como Jedi. Se a força tem uma quantidade de trevas muito maior que a quantidade de luz, então o jogador possui a ordem Sith. Agora, se a quantidade de luz e de trevas forem equilibradas, o jogador é considerado de ordem neutra (Gray Jedi), onde possui habilidades tanto Jedi quanto Sith.

#### **2.3. - Filosofia Jedi:**

> &emsp;&emsp;Não há emoção; há paz. <br>
&emsp;&emsp;Não há ignorância; há conhecimento. <br>
&emsp;&emsp;Não há paixão; há serenidade. <br>
&emsp;&emsp;Não há caos; há harmonia. <br>
&emsp;&emsp;Não há morte; há a Força. <br>

#### **2.4. - Filosofia Gray Jedi:**

> &emsp;&emsp;Deve haver escuridão e luz.<br>
&emsp;&emsp;Farei o que for preciso para manter o equilíbrio, pois o equilíbrio é o que mantém toda a vida.<br>
&emsp;&emsp;Não há bem sem mal, mas não se deve permitir que o mal floresça.<br>
&emsp;&emsp;Há paixão, mas paz; serenidade, mas emoção; caos, mas ordem.<br>
&emsp;&emsp;Eu sou um manejador da chama; campeão do equilíbrio. Eu sou um guardião da vida.<br>
&emsp;&emsp;Eu sou um Jedi Cinzento. <br>

#### **2.5. - Filosofia Sith:**

> &emsp;&emsp;Paz é uma mentira, só existe paixão <br>
&emsp;&emsp;Através da paixão, ganho força.<br>
&emsp;&emsp;Através da força, ganho poder.<br>
&emsp;&emsp;Através do poder, ganho a vitória.<br>
&emsp;&emsp;Através da vitória, minhas correntes se rompem.<br>
&emsp;&emsp;A Força me libertará."<br>

## **3. - Nave**

Especificar quais são os atributos de nave e listar as naves disponíveis;

- **Nome:** Nome da nave;
- **Descrição:** Descrição breve da nave, de ondem vem, de quem pertence ou para que serve;
- **Velocidade máxima:** indica a velocidade máxima que pode alcançar;
- **Tipo de arma:** Indica qual o tipo de arma e se possui arma

## **4. - Habilidades**

Fetiço ou arma que pode ser usada em um combate contra oponentes, desbloquear portas, enganar adversários e etc.

- **ID:** identificação da habilidade;
- **Nome:** Nome da habilidade;
- **Descrição:** Texto de descrição da habilidade;
- **Nível:** Descreve qual nível a habilidade é desbloqueada;
- **Impacto:** Descreve qual o impacto a habilidade pode causar como dano, enganação, fuga e etc;
- **Pré-Requisito:** Indica qual o nível ou ordem necessária para a utilização da habilidade

### **4.1. - Habilidades com Armas**

As habilidades podem incluir armas: Listar as possíveis armas do jogo;

- **Tipo:** indica o tipo de arma: Arco, pistola, espada, metralhadora;
- **Munição:** indica qual o tipo de munição: flecha, balas, NA;

### **4.2. - Poderes da Força**

As habilidades podem ser específicas da força, dependendo do nível e da ordem: listar os possíveis poderes da força;

- **Classificação:** Indica se é uma habilidade especial ou comum;
- **Aspecto:** Indica se é um feitiço que usa a força para controle, habilidade sensitiva, habilidade de alterar posição dos objetos e etc;

## **5. - Roteiro do episódio e Objetivo do jogador**

Cada fase do jogo é definido por um episódio (baseado nos filmes) e em cada episódio o jogador deve cumprir objetivos para ganhar experiência e subir de nível;

### **5.1. - Roteiro**

- **Título:** Título do episódio, que corresponde a fase;
- **Abertura:** Frase de abertura característico dos filmes e games;
- **História:** Armazena um pouco da história do episódio para que o jogador possa consultar durante o jogo;

### **5.2. - Objetivos**

- **Ordem:** Indica qual ordem pertence esse objetivo;
- **Pontos de força:** Indica quanto de Força (luz ou trevas) o jogador ganha ao realizar o objetivo;
- **Midichlorians:** indica quantos pontos de experiência (Midichlorians) o jogador ganha ao realizar o objetivo;
- **Classificação:** indica se o objetivo é primário ou secundário;

## **6. - Itens (Em discussão)**

São os itens que o jogador pode carregar. Os itens podem aumentar as características ou desbloquear uma habilidade especial da força;

- **ID:** identificação da habilidade;
- **Nome:** Descreve o nome do item;
- **Descrição:** Explica o que é o item, como surgiu e quais os bônus que ele concede;
- **Tipo:** Classifica o item como comida, pedras preciosas, traje, anel, capa, chapéu e botas;

## **7. - Personagem**

São personagens predefinidos no jogo onde o jogador pode interagir. Existem os chamados NPCs que são personagens que vão auxiliar o jogador nas decisões, ou seja, há um diálogo e de acordo com as decisões do jogador ele pode ganhar itens, benção, maldição e etc. Exitem também os personagens oponentes, que são personagens no qual o jogador pode combater de alguma maneira usando suas caracterísicas e habilidades.

- **ID:** identificação da habilidade;
- **Nome:** nome do personagem;
- **Expólio:** experiência ou item que pode ser obtido pelo jogador a partir de uma probabilidade;

### **7.1. - NPC**

- **Descrição:** descreve de onde vem, quem é e etc.
- **Diálogo:** Dialogo com as decisões que influenciam na índole do personagem que, consequentemente, interfere na pontuação da força;

### **7.2. - Oponente**

- **Raça:** Descreve a raça do oponente;
- **Vida:** Quantidade de vida para derrotar;
- **Características:** Semelhante as características do jogador;

## **8. - Campo astronômico**

O Campo Astronômico é relativo ao mapa do jogo. É composto por regiões que formam uma localização. Com base na localização, o jogador pode se locomover nas regiões e assim se locomover no campo astronômico;

Os campos astronômicos podem ser: Planeta, Lua ou espaço sideral;

- **Região:** Localização na galáxia (Ex: Territórios da Orla Exterior);
- **Setor:** Em qual setor da região se encontra;
- **Atmosfera:** indica se a atmosfera é respirável ou não;

### **8.1. - Planeta**

- **Sol:** quantidade de sol que o planeta orbita;
- **Lua:** Quantidade de luas que o planeta tem;
- **Período orbital:** duração de uma volta em torno do sol;
- **Período de rotação:** duração do dia (uma volta em torno do seu eixo);

## **9. - Cidade**

Cada campo astronômico tem cidades que o descrevem.

- **Nome:** Nome da cidade;
- **Clima:** Descreve o clima da cidade;
- **Prefeito:** indica o líder político da cidade;

## **10. - Localização**

Trata-se da localização do personagem no campo astronômico (pode ser definida por latitude e longitude?). É importante ressaltar que a localização tem um vínculo com os personagens, ou seja, um oponente ou um NPC vai estar associado a uma localização aleatória dentro do campo astronômico,
