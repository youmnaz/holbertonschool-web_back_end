--creates a table users
DROP TABLE IF NOT EXISTS `users`;
CREATE TABLE `users` (  
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
);
