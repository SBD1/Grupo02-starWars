# **1. Normalização**

&emsp;&emsp;&emsp; A normalização é um processo formal e passo a passo que examina os atributos de uma entidade, com o objetivo de evitar anomalias observadas na inclusão, exclusão e alteração de registros.

&emsp;&emsp;&emsp; A teoria de normalização provê:

&emsp;&emsp;&emsp;&emsp;• uma maneira formal de melhoria de projeto;

&emsp;&emsp;&emsp;&emsp;• desenvolve a intuição de projetos de melhor qualidade.

## **1.1. Formas Normais**
&emsp;&emsp;&emsp;As formas normais são sequenciais, ou seja, se um banco se encontra na terceira forma normal, isso também significa que o mesmo está na segunda e também na primeira. Por isso devemos sempre começar a normalização pela primeira forma normal, para que não hajam problemas mais a frente na nossa normalização.

### **Primeira Forma Normal**
&emsp;&emsp;&emsp; Todos os atributos são monovalorados e atômicos (não há relações aninhadas).

### **Segunda Forma Normal**
&emsp;&emsp;&emsp; Relação está na segunda Forma Normal quando:

&emsp;&emsp;&emsp;&emsp;• Está na primeira Forma Normal,

&emsp;&emsp;&emsp;&emsp;• Atributos comuns não dependem parcialmente de qualquer chave.

### **Terceira Forma Normal**
&emsp;&emsp;&emsp; Uma relação está na terceira Forma Normal quando:
&emsp;&emsp;&emsp;&emsp;• Está na segunda Forma Normal;
&emsp;&emsp;&emsp;&emsp;• Atributos comuns não dependem transitivamente de qualquer superchave.

### **Forma Normal de Boyce-Codd**
&emsp;&emsp;&emsp;É uma versão mais restritiva da terceira Forma Normal, e na maioria dos casos, quando a relação está na terceira Forma Normal, ela satisfaz à Forma Normal de Boyce-Codd.

&emsp;&emsp;&emsp; Uma relação está na Forma Normal de Boyce-Codd quando:
&emsp;&emsp;&emsp;&emsp; • Para toda dependência funcional X -> A, X é uma
chave candidata.
### **Quarta Forma Normal**
&emsp;&emsp;&emsp;A quarta forma normal assegura que não existam entidades com atributos que não fazem parte da chave primária, atributos não chave, e que possem valores múltiplos.

## **1.6. Versão 1**

&emsp;&emsp;&emsp;Normalizações realizadas:
&emsp;&emsp;&emsp;&emsp; •

![Normalização v1](modulo3/../img/normal-v1.svg)

<a href="https://sbd1.github.io/Grupo02-starWars/modulo3/img/normal-v1.svg" target="_blank">Clique aqui</a> para ver o modelo com mais detalhes.

## **1.7. Outras Versões**

<details>
  <summary>Versão 0.1</summary> 

  <img src="https://sbd1.github.io/Grupo02-starWars/modulo3/img/normal-v0.1.svg" alt="Modelo Relacional v0.2">

  <a href="https://sbd1.github.io/Grupo02-starWars/modulo3/img/normal-v0.1.svg" target="_blank">Clique aqui</a> para ver o modelo com mais detalhes.
</details>