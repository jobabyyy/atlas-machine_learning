-- function SafeDiv created to divide the 1 and 2 number or return 0
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS INT(10,2)
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$

DELIMITER ;