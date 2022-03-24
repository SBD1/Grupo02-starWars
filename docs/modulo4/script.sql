CREATE TABLE campo_astronomico(
 id SERIAL PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 setor VARCHAR(100) NOT NULL,
 regiaoAstronomica VARCHAR(100) NOT NULL,
 atmosfera VARCHAR(100) NOT NULL,

 CONSTRAINT campo_un UNIQUE(nome),
 CONSTRAINT campo_atmosfera_ck CHECK(atmosfera IN ('Respirável','Não Respirável'))
);

CREATE TABLE regiao(
 id SERIAL PRIMARY KEY,
 nome_corpo_astronomico VARCHAR(100) NOT NULL
 nome VARCHAR(100) NOT NULL,
 clima VARCHAR(140) NOT NULL,
 governante VARCHAR(140) NOT NULL,
 dominio VARCHAR(140) NOT NULL,
 nivel SMALLINT NOT NULL,

 CONSTRAINT campo_un UNIQUE(nome),
 CONSTRAINT regiao_corpo_fk FOREIGN KEY (nome_corpo_astronomico) REFERENCES campo_astronomico (nome) ON DELETE CASCADE

);

CREATE TABLE habilidade(
 id SERIAL PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 descricao VARCHAR(100) NOT NULL,
 nivel SMALLINT NOT NULL,
 impacto INTEGER NOT NULL,
 preRequisito VARCHAR(100) NOT NULL,

 CONSTRAINT habilidade_nome_un UNIQUE(nome),
 CONSTRAINT habilidade_nivel_ck CHECK( (nivel >= 1) AND (nivel <= 100)),
 CONSTRAINT habilidade_impacto_ck CHECK( impacto >= 0 )
);

CREATE TABLE habilidade_arma(
  id SERIAL PRIMARY KEY,
  habilidade SERIAL,
  tipo VARCHAR(100) NOT NULL,
  municao SMALLINT NOT NULL,

  CONSTRAINT habilidade_arma_municao_ck CHECK( (municao >= 0) AND (municao <= 100)),
  CONSTRAINT habilidade_habArma_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE
);

CREATE TABLE habilidade_droid(
  id SERIAL PRIMARY KEY,
  habilidade SERIAL,
  aspecto VARCHAR(100) NOT NULL,

  CONSTRAINT habilidade_habDroid_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE
);

CREATE TABLE habilidade_forca(
  id SERIAL PRIMARY KEY,
  habilidade SERIAL,
  classificacao VARCHAR(100) NOT NULL,
  aspecto VARCHAR(100) NOT NULL,

  CONSTRAINT habilidade_habForca_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE
);

CREATE TABLE jogador (
   id	 	         SERIAL PRIMARY KEY,
   nome		      VARCHAR(30) NOT NULL UNIQUE,
   raca 	       	VARCHAR(60) NOT NULL,
   midichlorians  SMALLINT NOT NULL, 
   vida		      INTEGER NOT NULL,
   nivel	       	INTEGER NOT NULL,
   ordem	       	INTEGER NOT NULL,
   rank		      VARCHAR(30) NOT NULL,
   inteligencia	INTEGER NOT NULL,
   forca_fisica	INTEGER NOT NULL,
   agilidade	   INTEGER NOT NULL,
   resistencia	   INTEGER NOT NULL,
   espectro_forca INTEGER NOT NULL
);

CREATE TABLE oponente (
   id		          SERIAL PRIMARY KEY,
   nome		       VARCHAR(30) NOT NULL UNIQUE,
   raca 	          VARCHAR(60) NOT NULL,
   vida		       INTEGER NOT NULL,
   midichlorians   SMALLINT NOT NULL, 
   probabilidade   REAL NOT NULL,
   inteligencia	 INTEGER NOT NULL,
   forca_fisica	 INTEGER NOT NULL,
   agilidade	    INTEGER NOT NULL,
   resistencia	    INTEGER NOT NULL,
   espectro_forca  INTEGER NOT NULL
);

CREATE TABLE nave(
 NroSerie SERIAL PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 descricao VARCHAR(140) NOT NULL,
 velocidade_maxima INTEGER NOT NULL,
 arma VARCHAR(100) NOT NULL,

 CONSTRAINT campo_un UNIQUE(nome),
);


INSERT INTO jogador(nome, raca, midichlorians, vida, nivel, ordem, rank, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Ciclóvis o ciclope', 'algum', 5, 100, 100, 100, 'algum', 100, 100, 100, 100, 100);

INSERT INTO oponente(nome, raca, vida, midichlorians, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Ciclope o Ciclóvis', 'algum', 100, 100, 0.25, 100, 100, 100, 100, 100);
