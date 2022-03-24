CREATE DATABASE IF NOT EXISTS starWars;

CREATE TABLE campo_astromico(
   id		       	   SERIAL PRIMARY KEY,
   nome		       	VARCHAR(100) NOT NULL UNIQUE,
   setor	       	   VARCHAR(100) NOT NULL,
   regiaoAstronomica	VARCHAR(100) NOT NULL,
   atmosfera		   VARCHAR(100) NOT NULL,

   CONSTRAINT campo_atmosfera_ck CHECK(Atmosfera IN ('Respirável','Não Respirável'))
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

INSERT INTO jogador(nome, raca, midichlorians, vida, nivel, ordem, rank, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Ciclóvis o ciclope', 'algum', 5, 100, 100, 100, 'algum', 100, 100, 100, 100, 100);

INSERT INTO oponente(nome, raca, vida, midichlorians, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Ciclope o Ciclóvis', 'algum', 100, 100, 0.25, 100, 100, 100, 100, 100);

