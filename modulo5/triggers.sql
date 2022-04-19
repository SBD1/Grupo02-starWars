-- Jogador
CREATE TRIGGER insert_jogador
BEFORE INSERT ON jogador
FOR EACH ROW EXECUTE PROCEDURE verifica_nome_jogador();
