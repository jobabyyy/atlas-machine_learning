-- trigger that resets atttribute valid_email only when changed
DELIMITER $$
CREATE TRIGGER new_email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = FALSE;
    END IF;
END$$
DELIMITER ;