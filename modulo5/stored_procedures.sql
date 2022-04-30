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



