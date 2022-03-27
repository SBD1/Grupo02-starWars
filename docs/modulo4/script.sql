CREATE DATABASE IF NOT EXISTS starWars;

CREATE TABLE campo_astronomico(
 id SERIAL PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 setor VARCHAR(100) NOT NULL,
 regiaoAstronomica VARCHAR(100) NOT NULL,
 atmosfera VARCHAR(100) NOT NULL,

 CONSTRAINT campo_un UNIQUE(nome),
 CONSTRAINT campo_atmosfera_ck CHECK(atmosfera IN ('Respirável','Não Respirável'))
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
   id SERIAL PRIMARY KEY,
   nome VARCHAR(30) NOT NULL UNIQUE,
   raca VARCHAR(60) NOT NULL,
   midichlorians SMALLINT NOT NULL, 
   vida INTEGER NOT NULL,
   nivel INTEGER NOT NULL,
   ordem INTEGER NOT NULL,
   rank VARCHAR(60) NOT NULL,
   inteligencia INTEGER NOT NULL,
   forca_fisica INTEGER NOT NULL,
   agilidade INTEGER NOT NULL,
   resistencia INTEGER NOT NULL,
   espectro_forca INTEGER NOT NULL
);

CREATE TABLE oponente (
   id SERIAL PRIMARY KEY,
   nome VARCHAR(30) NOT NULL UNIQUE,
   raca VARCHAR(60) NOT NULL,
   vida INTEGER NOT NULL,
   midichlorians SMALLINT NOT NULL, 
   probabilidade REAL NOT NULL,
   inteligencia INTEGER NOT NULL,
   forca_fisica INTEGER NOT NULL,
   agilidade INTEGER NOT NULL,
   resistencia INTEGER NOT NULL,
   espectro_forca INTEGER NOT NULL
);

CREATE TABLE item (
   id SERIAL PRIMARY KEY,
   nome VARCHAR(30) NOT NULL UNIQUE,
   descricao VARCHAR(120) NOT NULL,
   tipo VARCHAR(30) NOT NULL
);

CREATE TABLE item_utilizavel (
   id SERIAL PRIMARY KEY,
   habilidade SERIAL NOT NULL,
   item SERIAL NOT NULL,
   nivel INTEGER NOT NULL,
   
   CONSTRAINT habilidade_habForca_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE,
   CONSTRAINT item_itemUtilizavel_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE CASCADE
);

CREATE TABLE item_consumivel (
   id SERIAL PRIMARY KEY,
   item SERIAL NOT NULL,
   carga	 INTEGER NOT NULL,
   
   CONSTRAINT item_itemUtilizavel_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE CASCADE
);

CREATE TABLE instancia_item (
   id SERIAL PRIMARY KEY,
   item SERIAL NOT NULL,
   
   CONSTRAINT item_itemUtilizavel_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE CASCADE
);

CREATE TABLE droid(
  nro_serie SERIAL PRIMARY KEY,
  habilidade SERIAL,
  nome VARCHAR(100) NOT NULL,
  modelo VARCHAR(30) NOT NULL,

  CONSTRAINT habDroid_droid_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE
);

CREATE TABLE intancia_de_droid(
  id SERIAL PRIMARY KEY,
  nro_serie SERIAL,
  jogador SERIAL,

  CONSTRAINT instDroid_droid_fk FOREIGN KEY (nro_serie) REFERENCES droid (nro_serie) ON DELETE CASCADE,
  CONSTRAINT jogador_droid_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE CASCADE
);

-- TESTAR --

CREATE TABLE intancia_de_oponente(
  id SERIAL PRIMARY KEY,
  instancia_item SERIAL,
  oponente SERIAL,

  CONSTRAINT instItem_instOpon_fk FOREIGN KEY (instancia_item) REFERENCES instancia_item (nro_serie) ON DELETE CASCADE,
  CONSTRAINT oponente_instOpon_fk FOREIGN KEY (oponente) REFERENCES oponente (id) ON DELETE CASCADE
);

CREATE TABLE npc(
  id SERIAL PRIMARY KEY,
  instancia_item SERIAL,
  nome VARCHAR(30) NOT NULL,
  raca VARCHAR(60) NOT NULL,
  descricao VARCHAR(100) NOT NULL,
  dialogo VARCHAR(1000) NOT NULL,

  CONSTRAINT instItem_npc_fk FOREIGN KEY (instancia_item) REFERENCES instancia_item (nro_serie) ON DELETE CASCADE,
  
);


-- Inserção de dados --

INSERT INTO jogador(nome, raca, midichlorians, vida, nivel, ordem, rank, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Ciclóvis o ciclope', 'algum', 5, 100, 100, 100, 'algum', 100, 100, 100, 100, 100);

INSERT INTO oponente(nome, raca, vida, midichlorians, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Ciclope o Ciclóvis', 'algum', 100, 100, 0.25, 100, 100, 100, 100, 100);

INSERT INTO habilidade(nome, descricao, nivel, impacto, preRequisito) VALUES ('Atirar', 'Causa 30 de dano ao oponente', 5, 30, 'Sem pre-requisitos');

INSERT INTO habilidade_arma(habilidade, tipo, municao) VALUES (1, 'Pistola', 50);

INSERT INTO item(nome, descricao, tipo) VALUES ('Pistola Verde', 'Atira 2 vezes por milissegundo', 'Pistola');

INSERT INTO item_utilizavel(habilidade, item, nivel) VALUES (1, 1, 5);

INSERT INTO item_consumivel(item, carga) VALUES (1, 5);

INSERT INTO instancia_item (item) VALUES (1);	

