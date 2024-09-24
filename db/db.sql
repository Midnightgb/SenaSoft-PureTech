CREATE DATABASE ecoconnect;
USE ecoconnect;

-- Crear la tabla USER
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    type ENUM('1', '2', '3', '4') NOT NULL,
    eco_points INT DEFAULT 0
);

-- Crear la tabla MATERIAL
CREATE TABLE material (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    points_per_kg FLOAT NOT NULL
);

-- Crear la tabla RECYCLING_POINT
CREATE TABLE recycling_points (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    current_capacity INT NOT NULL,
    max_capacity INT NOT NULL
);

-- Crear la tabla RECYCLING
CREATE TABLE recycling (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    material_id INT,
    weight FLOAT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    earned_points INT NOT NULL,
    recycling_point_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (material_id) REFERENCES material(id),
    FOREIGN KEY (recycling_point_id) REFERENCES recycling_points(id)
);

-- Crear la tabla REWARD
CREATE TABLE rewards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    cost_points INT NOT NULL
);

-- Crear la tabla REDEEM_HISTORY
CREATE TABLE redeem_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    reward_id INT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (reward_id) REFERENCES rewards(id)
);

-- Crear la tabla ACHIEVEMENT
CREATE TABLE achievements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    required_points INT NOT NULL
);

-- Crear la tabla intermedia USER_ACHIEVEMENT para la relación muchos a muchos
CREATE TABLE user_achievements (
    user_id INT,
    achievement_id INT,
    date_obtained TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, achievement_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (achievement_id) REFERENCES achievements(id)
);

-- Crear la tabla POINT_TRANSACTION
CREATE TABLE point_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    points INT NOT NULL,
    type ENUM('earned', 'redeemed') NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Crear la tabla REPORT
CREATE TABLE reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    data JSON NOT NULL
);

-- Crear índices para mejorar el rendimiento de las consultas frecuentes
CREATE INDEX idx_recycling_user_id ON recycling(user_id);
CREATE INDEX idx_recycling_material_id ON recycling(material_id);
CREATE INDEX idx_recycling_date ON recycling(date);
CREATE INDEX idx_point_transactions_user_id ON point_transactions(user_id);
CREATE INDEX idx_point_transactions_date ON point_transactions(date);
CREATE INDEX idx_redeem_history_user_id ON redeem_history(user_id);
CREATE INDEX idx_redeem_history_reward_id ON redeem_history(reward_id);