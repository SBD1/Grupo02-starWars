-- Campos astronomicos

INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Tatooine', 'Territórios da Orla Exterior', 'Arkanis', 'Respirável');
INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Coruscant', 'Mundos do núcleo', 'Corusca', 'Respirável');
INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Dagobah', 'Territórios da Orla Exterior', 'Sluis', 'Respirável');
INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Hoth', 'Territórios da Orla Exterior', 'Anoat', 'Respirável');
INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Endor', 'Territórios da Orla Exterior', 'Moddell', 'Respirável');
INSERT INTO campo_astronomico (nome, setor, regiaoAstronomica, atmosfera) VALUES ('Naboo', 'Orla Média', 'Chommell', 'Respirável');

-- Regiões

INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Mos Espa', 'Desértico', 'Hutts', 'Cartel Hutt', 1);
INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Bestine', 'Desértico', 'Hutts', 'Cartel Hutt', 2);
INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Mos Eisley', 'Desértico', 'Hutts', 'Cartel Hutt', 1);
INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Mar das Dunas', 'Desértico', 'Incursores Tusken', 'Tribo do povo da areia', 5);
INSERT INTO regiao (campo_astronomico, nome, clima, governante, dominio, nivel) VALUES (1, 'Cânion do Mendigo', 'Desértico', 'Sem governante', 'Eremitas', 7);


-- Items

INSERT INTO item(nome, descricao, tipo) VALUES ('Pistola Blaster', 'Pistola Blaster simples, arma com disporos unicos com manuseio apenas uma mão', 'Arma');
INSERT INTO item(nome, descricao, tipo) VALUES ('Rifle de repetição Blaster', 'Rifle de repetição Blaster, arma de repetição com manuseio de duas mãos', 'Arma');
INSERT INTO item(nome, descricao, tipo) VALUES ('Sabre de Luz', 'Sabre de luz, arma tradicional de usuários da força', 'Arma');
INSERT INTO item(nome, descricao, tipo) VALUES ('Poção pequena', 'Poção basica, cura 20 de vida do personagem', 'Poção');


-- Habilidade

INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito) VALUES ('Tiro simples com blaster', 'Tiro simples com uma pistola blaster causando impacto a distância no adversários. Utilizado uma vez por turno.', 5, 10, 'Possuir uma pistola blaster');
INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito) VALUES ('Golpe de sabre de luz', 'Aplica um golpe corpo a corpo no adversário com o sabre de luz. Utilizado uma vez por turno.', 2, 20, 'Possuir um sabre de luz');
INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito) VALUES ('Sequência de golpes de sabre de luz', 'Aplica uma sequência de golpes corpo a corpo no adversário com o sabre de luz. Utilizado uma vez por turno.', 15, 40, 'Possuir um sabre de luz');
INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito) VALUES ('Levitar objetos', 'Desloca qualquer objeto no mapa. Pode ser utilizado durante uma batalha para esquivar de golpes à distância. Utilizado uma vez por turno.', 15, 0, 'Ter a ordem Jedi, Gray Jedi ou Sith');
INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito) VALUES ('Velocidade da força', 'Utiliza-se da força para se deslocar rapidamento. Pode ser utilizado em batalha para se esquivar de golpes ou aplicar um impacto no adversário mais facilmente. Utilizado uma vez por turno.', 25, 10, 'Ter a ordem Jedi, Gray Jedi ou Sith');
INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito) VALUES ('Abrir portas com droid', 'Utiliza-se de um droid para abrir uma porta.', 5, 0, 'Possuir um droid com o modelos astromech');
INSERT INTO habilidade (nome, descricao, nivel, impacto, preRequisito) VALUES ('Tradução universal', 'Utiliza-se de um droid para se comunicar em outras linguas.', 5, 0, 'Possuir um droid com o modelos Protocolo');


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


-- Itens utilizaveis

INSERT INTO item_utilizavel(habilidade, item, nivel) VALUES (1, 1, 5);


-- Itens consumiveis

INSERT INTO item_consumivel(item, carga) VALUES (4, 10);


-- Jogador

INSERT INTO jogador(nome, raca, midichlorians, vida, nivel, ordem, rank, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Grogo', 'senciente', 1000, 100, 10, 100, 'Padawan', 5, 5, 5, 5, 15);


-- Oponente

INSERT INTO oponente(nome, raca, vida, midichlorians, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Nômade Tusken', 'tusken', 20, 0, 0.25, 02, 10, 5, 0, 0);

-- Nave

INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('YT-1300', 'Millennium Falcon', 'Cargueiro', 1050, 'Duas turreas quad laser');
INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('MC85', 'Raddus', 'Nave de batalha', 400, 'Canhão laser antipessoal');
INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('AC-3640', 'A Arca', 'Cargueiro', 150, 'Não possui');
INSERT INTO nave(nro_serie, nome, descricao, velocidade_maxima, arma) VALUES ('CR-400', 'Cruzador leve Hutt', 'Cruzador leve', 560, 'Lançadores de mísseis de concussão');

-- Roteiro

INSERT INTO roteiro(titulo, campo, historia, abertura) VALUES ('Episódio I - Parte I - Surgimento dos clones', 2 , 'Um jovem padawan inicia sua trajetória treinando para se tornar Jedi e ajudar o seu povo na guerra. Sua trajetória terá muitos desafios que colocará em dúvida a sua integridade moral. Qual caminho ele seguirá?', 'Uma inquietação toma conta do Senado Galáctico. Milhares de sistemas solares declararam suas intenções em deixar a República. Esse movimento separatista, sob a liderança do misterioso Conde Dookan, tem criado dificuldades para o limitado número de Cavaleiros Jedi manter a paz e a ordem na galáxia. Senadora Amidala, a antiga rainha de Naboo, está retornando ao Senado Galáctico para a votação da proposta crítica de criação de um Exército da República, para auxiliar os sobrecarregados Jedi...');

-- Droid

INSERT INTO droid (nro_serie, habilidade, nome, modelo) VALUES ('D1', 1, 'R2D2', 'Astromech');
INSERT INTO droid (nro_serie, habilidade, nome, modelo) VALUES ('D2', 2, 'C3PO', 'Protocolo');

-- Instâncias

INSERT INTO instancia_item(item) VALUES (1);
INSERT INTO instancia_oponente(instancia_item, oponente) VALUES (1,1);
INSERT INTO instancia_de_nave(nro_serie, jogador) VALUES ('YT-1300', 1);

-- NPC

INSERT INTO npc (instancia_item, nome, raca, descricao, dialogo) VALUES (1, 'Qui-Gon Jinn', 'Humano', 'HumanMestre Jedi do templo', 'Que a força esteja com você' );

-- Localização

INSERT INTO localizacao(latitude, longitude, regiao, instancia_item, instancia_oponente, instancia_de_nave) VALUES (0,0,1,1,1,1);

-- Objetivo

INSERT INTO objetivo(roteiro, ordem, midichlorians, pontos_forca, classificacao, descricao) VALUES ('Episódio I - Parte I - Surgimento dos clones', 'Jedi', 200, 1, True, 'Fale com o NPC e siga suas orientações');
INSERT INTO objetivo(roteiro, ordem, midichlorians, pontos_forca, classificacao, descricao) VALUES ('Episódio I - Parte I - Surgimento dos clones', 'Jedi', 250, 10, True, 'Treine na sala de treinamento jedi');