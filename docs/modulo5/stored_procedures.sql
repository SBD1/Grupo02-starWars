-- Retorna a quantidade de itens de um jogador
CREATE OR REPLACE FUNCTION count_items(jogador INTEGER)
  RETURNS INTEGER AS $items$
BEGIN
  RETURN (SELECT count(*) FROM instancia_item WHERE jogador=jogador);
END;
$items$ LANGUAGE plpgsql;

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
END;
$insert_jogador$ LANGUAGE plpgsql;

