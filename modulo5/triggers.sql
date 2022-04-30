-- Jogador
CREATE TRIGGER insert_jogador
BEFORE INSERT ON jogador
FOR EACH ROW EXECUTE PROCEDURE verifica_nome_jogador();

-- Item
CREATE TRIGGER verificar_inventario
BEFORE INSERT ON instancia_item_jogador
FOR EACH ROW EXECUTE PROCEDURE inventario();
