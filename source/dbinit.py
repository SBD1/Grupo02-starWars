# Load dotenv
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
from db.database import connect

def initDB():

  try: 
    connection = psycopg2.connect(host=os.getenv("DB_HOST"),
                                    user=os.getenv("DB_USER"),
                                    password=os.getenv("DB_PASS"),
                                    port=os.getenv("DB_PORT"))

    connection.autocommit = True

    cursor = connection.cursor()

    sql = '''CREATE database starwars'''

    cursor.execute(sql)
    print("Database created successfully........")

    connection.close()

    [cursorDatabase, connDatabase] = connect()

    script = ''' 
        -- TRANSACTION TABLES 
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
          impacto INTEGER NOT NULL,
          caracteristica VARCHAR(30) NOT NULL
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

        CREATE TABLE IF NOT EXISTS instancia_item_localizacao (
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
          oponente SERIAL,

          CONSTRAINT jogador_combate_fk FOREIGN KEY (jogador) REFERENCES jogador (id) ON DELETE SET NULL,
          CONSTRAINT Oponente_combate_fk FOREIGN KEY (oponente) REFERENCES oponente (id) ON DELETE SET NULL
        );

        COMMIT;

        BEGIN;
        -- Campos astronomicos

        INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Tatooine', 'Territórios da Orla Exterior', 'Arkanis', 'Respirável');
        INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Coruscant', 'Mundos do núcleo', 'Corusca', 'Respirável');
        INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Dagobah', 'Territórios da Orla Exterior', 'Sluis', 'Respirável');
        INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Hoth', 'Territórios da Orla Exterior', 'Anoat', 'Respirável');
        INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Endor', 'Territórios da Orla Exterior', 'Moddell', 'Respirável');
        INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Naboo', 'Orla Média', 'Chommell', 'Respirável');

        -- Regiões

        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (2,'Naboo','Neutro', 'Padmé Amidala', 'Republica',1);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (2,'Floresta Coruscant','Neutro', 'Padmé Amidala', 'Republica',2);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (2,'Lianorm swamp','Chuvoso', 'Padmé Amidala', 'Republica',5);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (2,'Planicie Naboo','Neutro', 'Padmé Amidala', 'Republica',3);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (2,'Lake Paonga','Chuvoso', 'Rugor Nass', 'Republica',8);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (2,'Paonga island','Neutro', 'Padmé Amidala', 'Republica',3);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (2,'Colinas verdejantes','Montanhoso', 'Padmé Amidala', 'Republica',5);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Mos Espa', 'Desértico', 'Hutts', 'Cartel Hutt', 1);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Bestine', 'Desértico', 'Hutts', 'Cartel Hutt', 2);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Mos Eisley', 'Desértico', 'Hutts', 'Cartel Hutt', 1);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Mar das Dunas', 'Desértico', 'Incursores Tusken', 'Tribo do povo da areia', 5);
        INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Cânion do Mendigo', 'Desértico', 'Sem governante', 'Eremitas', 7);

        -- Habilidade

        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Tiro simples com blaster', 'Tiro simples com uma pistola blaster causando impacto a distância no adversários. Utilizado uma vez por turno.', 5, 10, 'Possuir uma pistola blaster', 'Inteligencia');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Golpe de sabre de luz', 'Aplica um golpe corpo a corpo no adversário com o sabre de luz. Utilizado uma vez por turno.', 1, 10, 'Possuir um sabre de luz', 'Forca Fisica');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Sequência de golpes de sabre de luz', 'Aplica uma sequência de golpes corpo a corpo no adversário com o sabre de luz. Utilizado uma vez por turno.', 15, 20, 'Possuir um sabre de luz', 'Agilidade');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Levitar objetos', 'Desloca qualquer objeto no mapa. Pode ser utilizado durante uma batalha para esquivar de golpes à distância. Utilizado uma vez por turno.', 15, 0, 'Ter a ordem Jedi, Gray Jedi ou Sith', 'Inteligencia');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Velocidade da força', 'Utiliza-se da força para se deslocar rapidamento. Pode ser utilizado em batalha para se esquivar de golpes ou aplicar um impacto no adversário mais facilmente. Utilizado uma vez por turno.', 25, 10, 'Ter a ordem Jedi, Gray Jedi ou Sith', 'Agilidade');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Abrir portas com droid', 'Utiliza-se de um droid para abrir uma porta.', 5, 0, 'Possuir um droid com o modelos astromech', 'Neutro');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Tradução universal', 'Utiliza-se de um droid para se comunicar em outras linguas.', 5, 0, 'Possuir um droid com o modelos Protocolo', 'Neutro');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Corte simples', 'Utiliza-se de objeto afiado para cortar o adversario', 1, 5, 'Possuir objeto afiado', 'Forca Fisica');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Tiros multiplos', 'Tiro multiplo com uma rifle causando impacto a distância no adversários. Utilizado uma vez por turno', 10, 30, 'Possuir blaster de repetição', 'Inteligencia');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Choque Booma', 'Choque causado por uma granada Booma', 3, 10, 'Possuir granada Booma', 'Inteligencia');
        INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito, caracteristica) VALUES ('Soco', 'Combate corpo a corpo', 3, 2, 'Sem pre-requisito', 'Forca Fisica');


        -- Habilidade com arma

        INSERT INTO habilidade_arma (habilidade, tipo, municao) VALUES (1, 'Blaster Simples ', 30);
        INSERT INTO habilidade_arma (habilidade, tipo, municao) VALUES (2, 'Sabre de Luz Simbles', 1);
        INSERT INTO habilidade_arma (habilidade, tipo, municao) VALUES (3, 'Sabre de Luz Simbles', 1);


        -- Poderes da força

        INSERT INTO habilidade_forca (habilidade, classificacao, aspecto) VALUES (4, 'Simples', 'Controle');
        INSERT INTO habilidade_forca (habilidade, classificacao, aspecto) VALUES (5, 'Simples', 'Alteração');


        -- Habilidade droid

        INSERT INTO habilidade_droid (habilidade, aspecto) VALUES (6, 'Mobilidade');
        INSERT INTO habilidade_droid (habilidade, aspecto) VALUES (7, 'Comunicacao');


        -- Itens

        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Lança rustica', 'Lança simples feita com galho de arvaore e pedra lancada, contruida pela tribo dos Ewoks', 'Arma', 1);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Garra de Veermok','Garra afiada da mão de um Veemok abatido,  pode ser utilizado para cofecção de armas', 'Peça', 2);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Carne de Shaak', 'Pedaço de carne fresca de um Shaak abatido, util para alimentação', 'Alimento', 1);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Presa de Tusk cat', 'Presa da mandibula superior de um Tusl cat adulto, pode ser utilizado para cofecção de armas', 'Peça', 2);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Carne de Tusk cat', 'Pedaço de carne fresca de um Tusk Cat abatido, util para alimentação', 'Alimento', 1);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Pele de Tusk cat', 'Pele para proteção de um Tusk cat', 'Vestimenta', 1);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Pistola Blaster simples', 'Pistola Blaster simples, arma com disporos unicos com manuseio apenas uma mão', 'Arma', 2);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Rifle de repetição Blaster', 'Rifle de repetição Blaster, arma de repetição com manuseio de duas mãos', 'Arma', 5);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Escamas de Colo Claw Fish', 'Escamas resistentes', 'Vestimenta', 1);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Booma', 'Granada de energia ', 'Arma', 2);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Sangue de Dianoga', 'Sangue azul com alto teor venenoso', 'Peça', 8);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Sabre de Luz', 'Sabre de luz, arma tradicional de usuários da força', 'Arma',1);
        INSERT INTO item(nome, descricao, tipo, nivel) VALUES ('Pele de Wampa', 'Pele para proteção de um TWampa', 'Vestimenta', 2);


        -- Itens utilizaveis

        INSERT INTO item_utilizavel(habilidade, item) VALUES (8, 1);
        INSERT INTO item_utilizavel(habilidade, item) VALUES (1, 7);
        INSERT INTO item_utilizavel(habilidade, item) VALUES (9, 8);
        INSERT INTO item_utilizavel(habilidade, item) VALUES (10, 10);
        INSERT INTO item_utilizavel(habilidade, item) VALUES (2, 12);


        -- Itens consumiveis

        INSERT INTO item_consumivel(item, carga) VALUES (2, 1);
        INSERT INTO item_consumivel(item, carga) VALUES (3, 4);
        INSERT INTO item_consumivel(item, carga) VALUES (4, 1);
        INSERT INTO item_consumivel(item, carga) VALUES (5, 2);
        INSERT INTO item_consumivel(item, carga) VALUES (6, 1);
        INSERT INTO item_consumivel(item, carga) VALUES (9, 1);
        INSERT INTO item_consumivel(item, carga) VALUES (11, 2);
        INSERT INTO item_consumivel(item, carga) VALUES (13, 1);


        -- Jogador

        INSERT INTO jogador(nome, raca, midichlorians, vida, nivel, ordem, rank, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Grogo', 'senciente', 1000, 100, 10, 'Jedi', 'Padawan', 5, 5, 5, 5, 15);


        -- Oponente
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Ewok','Ewok', 30, 100, 0.20, 3, 2, 3, 2, -20, 'Ataque com lança', 3, 'Forca Fisica');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Veermok','Veermok', 50, 100, 0.30, 3, 4, 5, 3, 10, 'Mordida agressiva', 5, 'Forca Fisica');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Shaak','Shaak', 20, 100, 0.10, 1, 2, 4, 1, 0, 'Contra-Ataque ágil', 2, 'Agilidade');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Tusk cat','Tusk cat', 500, 100, 0.30, 4, 5, 7, 4, 10, 'Ataque Forte da Garra', 5, 'Agilidade');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Droid de batalha B1','Droid separatista', 50, 100, 0.20, 2, 3, 3, 4, 20, 'Tiro com Rifle de blaster', 3, 'Forca Fisica');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Super Droid','Droid separatista', 100, 100, 0.40, 5, 5, 4, 6, 20, 'Tiro com lançador de pulso duplo', 5, 'Forca Fisica');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Colo Claw Fish','Cordaxian Sea', 2500, 100, 0.50, 7, 10, 10, 8, 10, 'Presa venenosa', 8, 'Agilidade');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Gungan','Gungan', 50, 100, 0.20, 2, 4, 3, 3, -20, 'Bastão atordoante', 2, 'Inteligencia');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Dianoga','Dianoga', 5000, 100, 0.90, 9, 10, 10, 9, 10, 'Tentáculos pegajosos', 7, 'Inteligencia');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Wampa','Wampa', 1000, 100, 0.40, 6, 7, 5, 6, 10, 'Esmagamento com a garra', 3, 'Forca Fisica');
        INSERT INTO oponente(nome, raca, midichlorians, vida, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca, ataque, impacto, caracteristica) VALUES ('Putch Ingball','Espantalho de treinamento', 0, 100, 0, 1, 1, 1, 0, 0, 'Permanece parado', 0, 'Inteligencia');

        -- Nave

        INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('AT-AT', 'AT-AT', 'Transporte Blindado para Todo Terreno', 1, 'Blaster medio R-90C');
        INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('YT-1300', 'Millennium Falcon', 'Cargueiro', 1050, 'Duas turreas quad laser');
        INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('MC85', 'Raddus', 'Nave de batalha', 400, 'Canhão laser antipessoal');
        INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('AC-3640', 'A Arca', 'Cargueiro', 150, 'Não possui');
        INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('CR-400', 'Cruzador leve Hutt', 'Cruzador leve', 560, 'Lançadores de mísseis de concussão');

        -- Roteiro

        INSERT INTO roteiro(titulo, campo, historia, abertura) VALUES ('Episódio I - Parte I - Surgimento dos clones', 2 , 'Um jovem padawan inicia sua trajetória treinando para se tornar Jedi e ajudar o seu povo na guerra. Sua trajetória terá muitos desafios que colocará em dúvida a sua integridade moral. Qual caminho ele seguirá?', 'Uma inquietação toma conta do Senado Galáctico. Milhares de sistemas solares declararam suas intenções em deixar a República. Esse movimento separatista, sob a liderança do misterioso Conde Dookan, tem criado dificuldades para o limitado número de Cavaleiros Jedi manter a paz e a ordem na galáxia. Senadora Amidala, a antiga rainha de Naboo, está retornando ao Senado Galáctico para a votação da proposta crítica de criação de um Exército da República, para auxiliar os sobrecarregados Jedi...');

        -- Droid

        INSERT INTO droid (nro_serie, habilidade, nome, modelo) VALUES ('D1', 1, 'R2D2', 'Astromech');
        INSERT INTO droid (nro_serie, habilidade, nome, modelo) VALUES ('D2', 2, 'C3PO', 'Protocolo');

        -- Localização

        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-9,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-9,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-9,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-9,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-9,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-9,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-9,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-9,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-9,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-8,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-8,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-8,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-8,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-8,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-8,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-8,6);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-8,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-7,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-7,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-7,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-7,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-7,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-7,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-6,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-6,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-6,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-6,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-6,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-6,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-6,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-5,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-5,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-5,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-5,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-5,5);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-5,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-4,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-3,7);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,-1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,-1,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,-1,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,-1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,-1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,-1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,-1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,-1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,-1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,-1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,-1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,0,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,0,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,0,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,0,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,1,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,1,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,1,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,1,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,1,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,1,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,2,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,2,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,2,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,3,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,3,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,3,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,3,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,3,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,3,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,3,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,3,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,3,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,3,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,4,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,4,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,4,4);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,4,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,4,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,4,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,4,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,4,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,4,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,4,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,4,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,4,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,4,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,4,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,4,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,4,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,4,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,4,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,4,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,4,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,4,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,4,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,5,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,5,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,5,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,5,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,5,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,5,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,5,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,5,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,5,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,5,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,5,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,5,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,5,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,5,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,5,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,5,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,5,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,6,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,6,2);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,6,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-8,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-7,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-6,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-5,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-4,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-3,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-2,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (-1,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (0,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (1,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (2,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (3,7,1);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (4,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (5,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (6,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (7,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (8,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (9,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (10,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (11,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (12,7,3);
        INSERT INTO localizacao(longitude, latitude, regiao) VALUES (13,7,3);

        -- Oponente
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (9,7,39);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (9,7,42);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (9,7,19);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (10,8,10);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (10,8,66);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (10,8,77);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (10,8,85);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (10,8,51);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (10,8,56);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (10,8,31);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (4,4,350);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (4,4,308);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (5,4,329);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (5,4,373);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (6,4,198);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (6,4,242);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,193);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,216);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,238);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,262);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,346);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,367);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,352);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,348);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,370);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,284);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,280);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,302);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,170);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,175);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,173);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,213);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,218);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,217);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,325);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (3,3,305);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,278);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,273);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,297);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,319);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,322);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,93);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,49);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,24);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,2);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,26);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,300);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,301);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,250);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,210);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,230);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,253);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,256);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,71);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,69);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (1,1,89);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,1);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,23);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,25);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,45);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,46);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,47);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,48);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,279);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,294);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,295);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,275);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,258);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,342);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,168);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (2,2,91);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,113);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,136);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,141);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,159);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,164);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,186);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,229);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,269);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,244);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (7,5,205);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (8,6,117);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (8,6,133);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (8,6,179);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (8,6,201);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (8,6,221);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (13,10,101);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (13,10,123);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (13,10,127);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (13,10,132);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (13,10,148);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (11,9,6);
        INSERT INTO instancia_oponente(item, oponente, localizacao) VALUES (12,11,353);



        -- Instância nave

        INSERT INTO instancia_de_nave(nro_serie, jogador, localizacao) VALUES ('AT-AT', 1, 184);
        INSERT INTO instancia_de_nave(nro_serie, jogador, localizacao) VALUES ('AT-AT', 1, 160);
        INSERT INTO instancia_de_nave(nro_serie, jogador, localizacao) VALUES ('AT-AT', 1, 180);

        -- NPC
        INSERT INTO npc (item, nome, raca, descricao, dialogo, localizacao) VALUES (12, 'Obi-Wan Kenobi', 'Humano', 'Conhecido também como Ben Kenobi durante seu exílio, foi um Humano Mestre Jedi que serviu à República Galáctica.', 'Bem-vindo à Coruscant! Aqui você iniciará sua jornada no universo star wars e com o tempo aprenderás a confiar em teus instintos, então serás invencível! Como todo aprendiz, você conhecerá a força com o tempo. Aqui você deve fazer aquilo que você acha que tem fazer. Diante das suas atitudes, você saberá qual lado está! Aqui está um Sabre de Luz, para que você consiga se aventurar por esse mundo e atacar ou se defender de inimigos. Que a força esteja com você!', 353);


        -- Objetivo

        INSERT INTO objetivo(roteiro, ordem, midichlorians, pontos_forca, classificacao, descricao) VALUES ('Episódio I - Parte I - Surgimento dos clones', 'Jedi', 200, 1, True, 'Fale com o NPC e siga suas orientações');
        INSERT INTO objetivo(roteiro, ordem, midichlorians, pontos_forca, classificacao, descricao) VALUES ('Episódio I - Parte I - Surgimento dos clones', 'Jedi', 250, 10, True, 'Treine na sala de treinamento jedi');

        -- Instância de itens
        INSERT INTO instancia_item_localizacao(item, localizacao) VALUES (1, 5), (2, 91), (3, 23), (4, 202), (5, 162), (6, 254), (7, 190), (8, 126), (9, 197), (10, 286);


        COMMIT;

        -- TRANSACTION PROCEDURES
        BEGIN;
        -- Retorna a quantidade de itens de um jogador
        CREATE OR REPLACE FUNCTION contar_items(idJogador INTEGER)
        RETURNS INTEGER AS $qtd_itens$
        BEGIN
          RETURN (SELECT count(*) AS qtd_itens FROM instancia_item_jogador WHERE jogador = new.jogador);
        END;
        $qtd_itens$ 
        LANGUAGE plpgsql;

        -- Retorna o droid do jogador
        CREATE OR REPLACE FUNCTION get_droid(jogador INTEGER)
          RETURNS INTEGER AS $droid$
        BEGIN
          SELECT id, nro_serie 
          FROM instancia_de_droid 
          WHERE jogador=jogador;
        END;
        $droid$ LANGUAGE plpgsql;

        -- Verifica se existe um jogador com o mesmo nome
        CREATE OR REPLACE FUNCTION verifica_nome_jogador() 
        RETURNS trigger AS $insert_jogador$
        BEGIN
            PERFORM * 
            FROM jogador 
            WHERE nome = new.nome;
            IF FOUND 
            THEN RAISE EXCEPTION 'Esse nome já foi escolhido por outro jogador';
            END IF;
            RETURN NEW;
        END;
        $insert_jogador$ LANGUAGE plpgsql;

        -- Verifica se o inventário está cheio
        CREATE OR REPLACE FUNCTION inventario()
        RETURNS trigger AS $verificar_inventario$
        DECLARE
          qtd_itens INTEGER :=  (SELECT count(jogador) AS qtd_itens FROM instancia_item_jogador WHERE jogador = new.jogador);
        BEGIN                                                     
                IF qtd_itens  >= 10 
                THEN RAISE EXCEPTION 'Inventário está cheio';
                END IF;  
                RETURN NEW;     
        END;
        $verificar_inventario$ 
        LANGUAGE plpgsql;

        COMMIT;

        -- TRANSACTION TRIGGER
        BEGIN;
        -- Jogador
        CREATE TRIGGER insert_jogador
        BEFORE INSERT ON jogador
        FOR EACH ROW EXECUTE PROCEDURE verifica_nome_jogador();

        -- Item
        CREATE TRIGGER verificar_inventario
        BEFORE INSERT ON instancia_item_jogador
        FOR EACH ROW EXECUTE PROCEDURE inventario();

        COMMIT;
      '''

    cursorDatabase.execute(script)
    connDatabase.commit()

    connDatabase.close()

  except:
    print('Banco configurado...')

