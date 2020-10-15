SELECT * FROM Animal


INSERT INTO `Animal` VALUES (null, "johndog", "Trim", "Mutt", 1, 2);
INSERT INTO `Animal` VALUES (null, "yanny", "Treatment", "Mutt", 1, 2);
INSERT INTO `Animal` VALUES (null, "korben", "Kennel", "Lab mix", 2, 1);

SELECT 
            a.id,
            a.name,
            a.breed,
            a.status,
            l.name location_name,
            c.name customer_name
        FROM Animal a
        JOIN Location l ON l.id = a.location_id
        JOIN Customer c ON c.id = a.customer_id
        WHERE a.id = 6

