sudo -u postgres psql # Para acessar o banco
\l # listar os bancos de dados;
\c starWars; # Entrar no data base;

CREATE TABLE campo_astromico(
 ID NUMERIC(10) NOT NULL,
 Nome VARCHAR(100) NOT NULL,
 Setor VARCHAR(100) NOT NULL,
 RegiaoAstronomica VARCHAR(100) NOT NULL,
 Atmosfera VARCHAR(100) NOT NULL,

 CONSTRAINT campo_pk PRIMARY KEY(ID),
 CONSTRAINT campo_un UNIQUE(Nome),
 CONSTRAINT campo_atmosfera_ck CHECK(Atmosfera IN ('Respirável','Não Respirável'))
);
