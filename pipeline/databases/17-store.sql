-- trigger that decreases quanitity of an item after new order added
DROP trigger IF EXSITS after_order_insert;
CREATE trigger after_order_insert AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quanitity = quanitity - NEW.number
    WHERE items.name = NEW.item_name;