CREATE TABLE `posts_DJPost` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(200) NOT NULL,
    `content` TEXT NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `author` VARCHAR(200) DEFAULT NULL,
    `category` VARCHAR(100) DEFAULT NULL,
    `updated_at` DATETIME DEFAULT NULL,
    `likes_count` INT NOT NULL DEFAULT 0,
    `author_id` INT DEFAULT NULL,
    `is_published` BOOLEAN NOT NULL DEFAULT TRUE,
    `views` INT NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
