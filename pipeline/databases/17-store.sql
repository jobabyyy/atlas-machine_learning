-- trigger that decreases quantity of an item after new order added
DROP trigger IF EXSITS after_order_insert;
CREATE trigger after_order_insert AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE items.name = NEW.item_name;