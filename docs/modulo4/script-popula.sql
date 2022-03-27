INSERT INTO jogador(nome, raca, midichlorians, vida, nivel, ordem, rank, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Ciclóvis o ciclope', 'algum', 5, 100, 100, 100, 'algum', 100, 100, 100, 100, 100);

INSERT INTO oponente(nome, raca, vida, midichlorians, probabilidade, inteligencia, forca_fisica, agilidade, resistencia, espectro_forca) VALUES ('Ciclope o Ciclóvis', 'algum', 100, 100, 0.25, 100, 100, 100, 100, 100);

INSERT INTO habilidade(nome, descricao, nivel, impacto, preRequisito) VALUES ('Atirar', 'Causa 30 de dano ao oponente', 5, 30, 'Sem pre-requisitos');

INSERT INTO habilidade_arma(habilidade, tipo, municao) VALUES (1, 'Pistola', 50);

INSERT INTO item(nome, descricao, tipo) VALUES ('Pistola Verde', 'Atira 2 vezes por milissegundo', 'Pistola');

INSERT INTO item_utilizavel(habilidade, item, nivel) VALUES (1, 1, 5);

INSERT INTO item_consumivel(item, carga) VALUES (1, 5);

INSERT INTO instancia_item (item) VALUES (1);	

