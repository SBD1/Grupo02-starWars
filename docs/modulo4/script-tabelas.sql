CREATE DATABASE IF NOT EXISTS starWars;


-- MAPA
CREATE TABLE IF NOT EXISTS campo_astronomico(
 id SERIAL PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 setor VARCHAR(100) NOT NULL,
 regiaoAstronomica VARCHAR(100) NOT NULL,
 atmosfera VARCHAR(100) NOT NULL,

 CONSTRAINT campo_un UNIQUE(nome),
 CONSTRAINT campo_atmosfera_ck CHECK(atmosfera IN ('Respirável','Não Respirável'))
);

CREATE TABLE IF NOT EXISTS regiao(
 id SERIAL PRIMARY KEY,
 campo_astronomico SERIAL NOT NULL,
 nome VARCHAR(100) NOT NULL UNIQUE,
 clima VARCHAR(140) NOT NULL,
 governante VARCHAR(140) NOT NULL,
 dominio VARCHAR(140) NOT NULL,
 nivel SMALLINT NOT NULL,

 CONSTRAINT regiao_nivel_ck CHECK( nivel >= 1),
 CONSTRAINT regiao_campo_fk FOREIGN KEY (campo_astronomico) REFERENCES campo_astronomico (id) ON DELETE CASCADE
);


-- NAVE
CREATE TABLE IF NOT EXISTS nave(
 nro_serie SERIAL PRIMARY KEY,
 nome VARCHAR(100) NOT NULL UNIQUE,
 descricao VARCHAR(140) NOT NULL,
 velocidade_maxima INTEGER NOT NULL,
 arma VARCHAR(100) NOT NULL
);


-- HABILIDADE
CREATE TABLE IF NOT EXISTS habilidade(
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

CREATE TABLE IF NOT EXISTS habilidade_arma(
  id SERIAL PRIMARY KEY,
  habilidade SERIAL,
  tipo VARCHAR(100) NOT NULL,
  municao SMALLINT NOT NULL,

  CONSTRAINT habilidade_arma_municao_ck CHECK( (municao >= 0) AND (municao <= 100)),
  CONSTRAINT habilidade_habArma_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS habilidade_droid(
  id SERIAL PRIMARY KEY,
  habilidade SERIAL,
  aspecto VARCHAR(100) NOT NULL,

  CONSTRAINT habilidade_habDroid_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS habilidade_forca(
  id SERIAL PRIMARY KEY,
  habilidade SERIAL,
  classificacao VARCHAR(100) NOT NULL,
  aspecto VARCHAR(100) NOT NULL,

  CONSTRAINT habilidade_habForca_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE
);

--ITEM
CREATE TABLE IF NOT EXISTS item (
   id	 SERIAL PRIMARY KEY,
   nome VARCHAR(30) NOT NULL UNIQUE,
   descricao VARCHAR(120) NOT NULL,
   tipo VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS item_utilizavel (
   id SERIAL PRIMARY KEY,
   habilidade SERIAL NOT NULL,
   item SERIAL NOT NULL,
   nivel INTEGER NOT NULL,
   
   CONSTRAINT habilidade_habForca_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE,
   CONSTRAINT item_itemUtilizavel_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS item_consumivel (
   id SERIAL PRIMARY KEY,
   item SERIAL NOT NULL,
   carga	 INTEGER NOT NULL,
   
   CONSTRAINT item_itemUtilizavel_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS instancia_item (
   id SERIAL PRIMARY KEY,
   item SERIAL NOT NULL,
   
   CONSTRAINT item_itemUtilizavel_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE CASCADE
);

-- PERSONAGEM
CREATE TABLE IF NOT EXISTS jogador (
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

CREATE TABLE IF NOT EXISTS oponente (
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


CREATE TABLE IF NOT EXISTS npc(
  id SERIAL PRIMARY KEY,
  instancia_item SERIAL,
  nome VARCHAR(30) NOT NULL,
  raca VARCHAR(60) NOT NULL,
  descricao VARCHAR(100) NOT NULL,
  dialogo VARCHAR(1000) NOT NULL,

  CONSTRAINT instItem_npc_fk FOREIGN KEY (instancia_item) REFERENCES instancia_item (id) ON DELETE CASCADE
  
);


-- DROID
CREATE TABLE IF NOT EXISTS droid(
  nro_serie SERIAL PRIMARY KEY,
  habilidade SERIAL,
  nome VARCHAR(100) NOT NULL,
  modelo VARCHAR(30) NOT NULL,

  CONSTRAINT habDroid_droid_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE CASCADE
  
);

CREATE TABLE IF NOT EXISTS intancia_de_droid(
  id SERIAL PRIMARY KEY,
  nro_serie SERIAL,
  jogador SERIAL,

  CONSTRAINT instDroid_droid_fk FOREIGN KEY (nro_serie) REFERENCES droid (nro_serie) ON DELETE CASCADE,
  CONSTRAINT jogador_droid_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE CASCADE
);




-- TESTAR
CREATE TABLE intancia_de_oponente(
  id SERIAL PRIMARY KEY,
  instancia_item SERIAL,
  oponente SERIAL,

  CONSTRAINT instItem_instOpon_fk FOREIGN KEY (instancia_item) REFERENCES instancia_item (id) ON DELETE CASCADE,
  CONSTRAINT oponente_instOpon_fk FOREIGN KEY (oponente) REFERENCES oponente (id) ON DELETE CASCADE
);


-- FASES
CREATE TABLE roteiro (
   titulo		    VARCHAR(60) PRIMARY KEY,
   historia 	    VARCHAR(500) NOT NULL,
   abertura		    VARCHAR(500) NOT NULL
);


CREATE TABLE objetivo (
   id             SERIAL PRIMARY KEY,
   roteiro        VARCHAR NOT NULL,
   ordem 	      VARCHAR(60) NOT NULL,
   midichlorians VARCHAR(1000) NOT NULL,
   pontos_forca   SMALLINT NOT NULL,
   classificacao  BOOLEAN NOT NULL,

   CONSTRAINT roteiro_fk FOREIGN KEY (roteiro) REFERENCES roteiro (titulo) ON DELETE CASCADE
);
