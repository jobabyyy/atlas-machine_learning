-- computes and stores the avg score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;
    IF EXISTS (SELECT 1 FROM user_average_scores WHERE user_id = user_id) THEN
        UPDATE user_average_scores
        SET average_score = avg_score
        WHERE user_id = user_id;
    ELSE
        INSERT INTO user_average_scores (user_id, average_score)
        VALUES (user_id, avg_score);
    END IF;
END$$

DELIMITER ;
