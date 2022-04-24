BEGIN;

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
 CONSTRAINT regiao_campo_fk FOREIGN KEY (campo_astronomico) REFERENCES campo_astronomico (id) ON DELETE SET NULL
);

-- HABILIDADE
CREATE TABLE IF NOT EXISTS habilidade(
 id SERIAL PRIMARY KEY,
 nome VARCHAR(1000) NOT NULL,
 descricao VARCHAR(1000) NOT NULL,
 nivel SMALLINT NOT NULL,
 caracteristica VARCHAR(30) NOT NULL,
 impacto INTEGER NOT NULL,
 preRequisito VARCHAR(1000) NOT NULL,

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
  CONSTRAINT habilidade_habArma_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS habilidade_droid(
  id SERIAL PRIMARY KEY,
  habilidade SERIAL,
  aspecto VARCHAR(100) NOT NULL,

  CONSTRAINT habilidade_habDroid_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS habilidade_forca(
  id SERIAL PRIMARY KEY,
  habilidade SERIAL,
  classificacao VARCHAR(100) NOT NULL,
  aspecto VARCHAR(100) NOT NULL,

  CONSTRAINT habilidade_habForca_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE SET NULL
);

--ITEM
CREATE TABLE IF NOT EXISTS item (
   id	 SERIAL PRIMARY KEY,
   nome VARCHAR(30) NOT NULL UNIQUE,
   descricao VARCHAR(120) NOT NULL,
   tipo VARCHAR(30) NOT NULL,
   nivel INTEGER NOT NULL
   
);

CREATE TABLE IF NOT EXISTS item_utilizavel (
   id SERIAL PRIMARY KEY,
   habilidade SERIAL NOT NULL,
   item SERIAL NOT NULL,
   
   CONSTRAINT habilidade_habForca_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE SET NULL,
   CONSTRAINT item_itemUtilizavel_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS item_consumivel (
   id SERIAL PRIMARY KEY,
   item SERIAL NOT NULL,
   carga	 INTEGER NOT NULL,
   
   CONSTRAINT item_itemUtilizavel_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE SET NULL
);




-- PERSONAGEM
CREATE TABLE IF NOT EXISTS jogador (
   id SERIAL PRIMARY KEY,
   nome VARCHAR(30) NOT NULL UNIQUE,
   raca VARCHAR(60) NOT NULL,
   midichlorians SMALLINT NOT NULL, 
   vida INTEGER NOT NULL,
   nivel INTEGER NOT NULL,
   ordem VARCHAR(60) NOT NULL,
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
   midichlorians   INTEGER NOT NULL, 
   probabilidade   REAL NOT NULL,
   inteligencia	 INTEGER NOT NULL,
   forca_fisica	 INTEGER NOT NULL,
   agilidade	    INTEGER NOT NULL,
   resistencia	    INTEGER NOT NULL,
   espectro_forca  INTEGER NOT NULL,
   ataque VARCHAR(60),
   impacto INTEGER NOT NULL
);

-- NAVE
CREATE TABLE IF NOT EXISTS nave(
 nro_serie VARCHAR(50) PRIMARY KEY,
 nome VARCHAR(500) NOT NULL UNIQUE,
 descricao VARCHAR(500) NOT NULL,
 velocidade_maxima INTEGER NOT NULL,
 arma VARCHAR(500) NOT NULL
);


CREATE TABLE IF NOT EXISTS possui(
  id SERIAL PRIMARY KEY,
  jogador SERIAL,
  habilidade SERIAL,

  CONSTRAINT jogador_possui_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE SET NULL,
  CONSTRAINT habilidade_possui_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE SET NULL
);

-- DROID
CREATE TABLE IF NOT EXISTS droid(
  nro_serie VARCHAR(10) PRIMARY KEY,
  habilidade SERIAL,
  nome VARCHAR(100) NOT NULL,
  modelo VARCHAR(30) NOT NULL,

  CONSTRAINT habDroid_droid_fk FOREIGN KEY (habilidade) REFERENCES habilidade (id) ON DELETE SET NULL
  
);

-- FASES
CREATE TABLE roteiro (
   titulo		    VARCHAR(60) PRIMARY KEY,
   campo SERIAL,
   historia 	    VARCHAR(500) NOT NULL,
   abertura		    VARCHAR(500) NOT NULL,

   CONSTRAINT campo_roteiro_fk FOREIGN KEY (campo) REFERENCES campo_astronomico (id) ON DELETE SET NULL
);


CREATE TABLE IF NOT EXISTS objetivo (
   id SERIAL PRIMARY KEY,
   roteiro VARCHAR NOT NULL,
   ordem VARCHAR(60) NOT NULL,
   midichlorians SMALLINT NOT NULL, 
   pontos_forca SMALLINT NOT NULL,
   classificacao BOOLEAN NOT NULL,
   descricao VARCHAR(1000) NOT NULL,

   CONSTRAINT roteiro_fk FOREIGN KEY (roteiro) REFERENCES roteiro (titulo) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS cumpre(
  id SERIAL PRIMARY KEY,
  jogador SERIAL,
  objetivo SERIAL,
  status_objetivo VARCHAR(3),

  CONSTRAINT objetivo_cumpre_fk FOREIGN KEY (objetivo) REFERENCES objetivo (id) ON DELETE SET NULL,
  CONSTRAINT cumpre_status_ck CHECK(status_objetivo IN ('Sim','Não')),
  CONSTRAINT jogador_cumpre_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE SET NULL
);


CREATE TABLE IF NOT EXISTS localizacao(
  id SERIAL PRIMARY KEY,
  latitude SMALLINT NOT NULL,
  longitude SMALLINT NOT NULL,
  regiao SERIAL,

  CONSTRAINT regiao_localizacao_fk FOREIGN KEY (regiao) REFERENCES regiao (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS instancia_item_jogador (
   id SERIAL PRIMARY KEY,
   item SERIAL NOT NULL,
   jogador SERIAL,
  
   CONSTRAINT instanciaItem_jogador_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE SET NULL,
   CONSTRAINT instanciaItem_item_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS instancia_item_localização (
   id SERIAL PRIMARY KEY,
   item SERIAL NOT NULL,
   localizacao SERIAL,

   CONSTRAINT localizacao_item_fk FOREIGN KEY (localizacao) REFERENCES localizacao (id) ON DELETE SET NULL,
   CONSTRAINT instanciaItem_item_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS instancia_oponente(
  id SERIAL PRIMARY KEY,
  item SERIAL,
  oponente SERIAL,
  localizacao SERIAL,

  CONSTRAINT localizacao_item_fk FOREIGN KEY (localizacao) REFERENCES localizacao (id) ON DELETE SET NULL,
  CONSTRAINT Item_instOpon_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE SET NULL,
  CONSTRAINT oponente_instOpon_fk FOREIGN KEY (oponente) REFERENCES oponente (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS instancia_de_nave(
  id SERIAL PRIMARY KEY,
  nro_serie VARCHAR,
  jogador SERIAL,
  localizacao SERIAL,

  CONSTRAINT localizacao_item_fk FOREIGN KEY (localizacao) REFERENCES localizacao (id) ON DELETE SET NULL,

  CONSTRAINT instNave_nave_fk FOREIGN KEY (nro_serie) REFERENCES nave (nro_serie) ON DELETE SET NULL,
  CONSTRAINT jogador_nave_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS instancia_de_droid(
  id SERIAL PRIMARY KEY,
  nro_serie VARCHAR,
  jogador SERIAL,

  CONSTRAINT instDroid_droid_fk FOREIGN KEY (nro_serie) REFERENCES droid (nro_serie) ON DELETE SET NULL,
  CONSTRAINT jogador_droid_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS npc(
  id SERIAL PRIMARY KEY,
  item SERIAL,
  nome VARCHAR(30) NOT NULL,
  raca VARCHAR(60) NOT NULL,
  descricao VARCHAR(1000) NOT NULL,
  dialogo VARCHAR(1500) NOT NULL,
  localizacao SERIAL,

  CONSTRAINT localizacao_item_fk FOREIGN KEY (localizacao) REFERENCES localizacao (id) ON DELETE SET NULL,
  CONSTRAINT Item_npc_fk FOREIGN KEY (item) REFERENCES item (id) ON DELETE SET NULL
  
);

CREATE TABLE IF NOT EXISTS interage(
  id SERIAL PRIMARY KEY,
  jogador SERIAL,
  npc SERIAL,

  CONSTRAINT jogador_interage_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE SET NULL,
  CONSTRAINT npc_interage_fk FOREIGN KEY (npc) REFERENCES npc (id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS combate(
  id SERIAL PRIMARY KEY,
  jogador SERIAL,
  instancia_oponente SERIAL,

  CONSTRAINT jogador_combate_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE SET NULL,
  CONSTRAINT instOponente_combate_fk FOREIGN KEY (instancia_oponente) REFERENCES instancia_oponente (id) ON DELETE SET NULL
);

COMMIT;