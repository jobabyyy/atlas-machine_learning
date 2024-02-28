-- trigger that decreases quantity of an item after new order added
DROP TRIGGER IF EXSITS after_order_insert;

CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE items.name = NEW.item_name;
END;