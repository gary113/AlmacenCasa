-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 27-04-2020 a las 20:17:23
-- Versión del servidor: 8.0.19-0ubuntu5
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: inventario_casa
--
CREATE DATABASE IF NOT EXISTS inventario_casa DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE inventario_casa;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla Producto
--

DROP TABLE IF EXISTS Producto;
CREATE TABLE Producto (
  id_producto int NOT NULL,
  descripcion_producto varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  cantidad_producto double UNSIGNED NOT NULL,
  unidad_producto varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  lugar_producto varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla Producto
--

INSERT INTO Producto (id_producto, descripcion_producto, cantidad_producto, unidad_producto, lugar_producto) VALUES
(1, 'Ajinomen de gallina', 1, 'Bolsas', 'Cooler'),
(2, 'Spaguetti Tottus', 0, 'Bolsas', 'Cooler'),
(3, 'Pomarola', 3, 'Bolsas', 'Cooler'),
(4, 'Aceite', 2, 'Botellas', 'Cooler'),
(5, 'Sardina en salsa de tomate', 0, 'Latas', 'Cooler'),
(6, 'Fideo canuto grande', 5, 'Bolsas', 'Cooler'),
(7, 'Fideo plumita', 4, 'Bolsas', 'Cooler'),
(8, 'Atún de caballa', 16, 'Latas', 'Cooler'),
(9, 'Atún de jurel', 8, 'Latas', 'Cooler'),
(10, 'Arroz a granel', 9.5, 'Kg', 'Cooler'),
(11, 'Huevo', 28, 'Unidades', 'Refrigeradora'),
(12, 'Limón', 45, 'Unidades', 'Refrigeradora'),
(13, 'Zanahoria', 0, 'Unidades', 'Refrigeradora'),
(14, 'Melocotón', 0, 'Unidades', 'Refrigeradora'),
(15, 'Cebollita china', 0.05, 'Unidades', 'Refrigeradora'),
(16, 'Queso', 0.5, 'Kg', 'Refrigeradora'),
(17, 'Chorizo', 0, 'Unidades', 'Refrigeradora'),
(18, 'Salchicha', 6, 'Unidades', 'Refrigeradora'),
(19, 'Pallar', 0.5, 'Kg', 'Debajo del microondas'),
(20, 'Canchita', 400, 'Gramos', 'Debajo del microondas'),
(21, 'Galleta', 10, 'Paquetes', 'Debajo del microondas'),
(22, 'Gelatina', 280, 'Gramos', 'Debajo del microondas'),
(23, 'Semillas para hacer agua', 280, 'Gramos', 'Debajo del microondas'),
(24, 'Sapolio Lavavajillas', 1.5, 'Unidades', 'Debajo del microondas'),
(25, 'Papel higiénico', 11, 'Rollos', 'Cuarto'),
(26, 'Shampoo', 1, 'Frasco', 'Baño'),
(27, 'Jabón', 4, 'Unidades', 'Baño'),
(28, 'Jabón para ropa', 1, 'Unidades', 'Baño'),
(29, 'Kolinos', 2, 'Unidades', 'Baño'),
(30, 'Azucar rubia', 4, 'Kg', 'Debajo del lavadero de la cocina'),
(31, 'Diente de ajo', 30, 'Unidades', 'Estante de la cocina'),
(32, 'Caja de fósforos', 4, 'Unidades', 'Estante de la cocina'),
(33, 'Papa', 6, 'Unidades', 'Debajo del lavadero de la cocina'),
(34, 'Cebolla', 3, 'Unidades', 'Debajo del lavadero de la cocina'),
(35, 'Poet', 4125, 'ml', 'Debajo del lavadero de la cocina'),
(36, 'Lejia', 5, 'Kg', 'Cocina'),
(37, 'Ace', 2, 'Baldes', 'Cocina'),
(38, 'Tomate', 6, 'Unidades', 'Refrigeradora');

--
-- Disparadores Producto
--
DROP TRIGGER IF EXISTS Producto_delete;
DELIMITER $$
CREATE TRIGGER Producto_delete BEFORE DELETE ON Producto FOR EACH ROW INSERT INTO Producto_historial SELECT 'delete', NULL, NOW(), d.* FROM Producto AS d WHERE d.id_producto = OLD.id_producto
$$
DELIMITER ;
DROP TRIGGER IF EXISTS Producto_insert;
DELIMITER $$
CREATE TRIGGER Producto_insert AFTER INSERT ON Producto FOR EACH ROW INSERT INTO Producto_historial SELECT 'insert', NULL, NOW(), d.* FROM Producto AS d WHERE d.id_producto = NEW.id_producto
$$
DELIMITER ;
DROP TRIGGER IF EXISTS Producto_update;
DELIMITER $$
CREATE TRIGGER Producto_update AFTER UPDATE ON Producto FOR EACH ROW INSERT INTO Producto_historial SELECT 'update', NULL, NOW(), d.* FROM Producto AS d WHERE d.id_producto = NEW.id_producto
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla Producto_historial
--

DROP TABLE IF EXISTS Producto_historial;
CREATE TABLE Producto_historial (
  accion varchar(8) DEFAULT 'insert',
  revision int NOT NULL,
  fecha_hora datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  id_producto int NOT NULL,
  descripcion_producto varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  cantidad_producto double UNSIGNED NOT NULL,
  unidad_producto varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  lugar_producto varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla Producto_historial
--

INSERT INTO Producto_historial (accion, revision, fecha_hora, id_producto, descripcion_producto, cantidad_producto, unidad_producto, lugar_producto) VALUES
('insert', 1, '2020-04-27 19:13:41', 34, 'Cebolla', 3, 'Unidades', 'Debajo del lavadero de la cocina'),
('insert', 1, '2020-04-27 19:13:41', 33, 'Papa', 6, 'Unidades', 'Debajo del lavadero de la cocina'),
('insert', 1, '2020-04-27 19:13:41', 32, 'Caja de fósforos', 4, 'Unidades', 'Estante de la cocina'),
('insert', 1, '2020-04-27 19:13:41', 31, 'Diente de ajo', 30, 'Unidades', 'Estante de la cocina'),
('insert', 1, '2020-04-27 19:13:41', 30, 'Azucar rubia', 4, 'Kg', 'Debajo del lavadero de la cocina'),
('insert', 1, '2020-04-27 19:13:41', 29, 'Kolinos', 2, 'Unidades', 'Baño'),
('insert', 1, '2020-04-27 19:13:41', 28, 'Jabón para ropa', 1, 'Unidades', 'Baño'),
('insert', 1, '2020-04-27 19:13:41', 27, 'Jabón', 4, 'Unidades', 'Baño'),
('insert', 1, '2020-04-27 19:13:41', 26, 'Shampoo', 1, 'Frasco', 'Baño'),
('insert', 1, '2020-04-27 19:13:41', 25, 'Papel higiénico', 11, 'Rollos', 'Cuarto'),
('insert', 1, '2020-04-27 19:13:41', 24, 'Sapolio Lavavajillas', 1.5, 'Unidades', 'Debajo del microondas'),
('insert', 1, '2020-04-27 19:13:41', 23, 'Semillas para hacer agua', 280, 'Gramos', 'Debajo del microondas'),
('insert', 1, '2020-04-27 19:13:41', 22, 'Gelatina', 280, 'Gramos', 'Debajo del microondas'),
('insert', 1, '2020-04-27 19:13:41', 21, 'Galleta', 10, 'Paquetes', 'Debajo del microondas'),
('insert', 1, '2020-04-27 19:13:41', 20, 'Canchita', 400, 'Gramos', 'Debajo del microondas'),
('insert', 1, '2020-04-27 19:13:41', 19, 'Pallar', 0.5, 'Kg', 'Debajo del microondas'),
('insert', 1, '2020-04-27 19:13:41', 18, 'Salchicha', 6, 'Unidades', 'Refrigeradora'),
('insert', 1, '2020-04-27 19:13:41', 17, 'Chorizo', 0, 'Unidades', 'Refrigeradora'),
('insert', 1, '2020-04-27 19:13:41', 16, 'Queso', 0.5, 'Kg', 'Refrigeradora'),
('insert', 1, '2020-04-27 19:13:41', 15, 'Cebollita china', 0.05, 'Unidades', 'Refrigeradora'),
('insert', 1, '2020-04-27 19:13:41', 14, 'Melocotón', 0, 'Unidades', 'Refrigeradora'),
('insert', 1, '2020-04-27 19:13:41', 13, 'Zanahoria', 0, 'Unidades', 'Refrigeradora'),
('insert', 1, '2020-04-27 19:13:41', 12, 'Limón', 45, 'Unidades', 'Refrigeradora'),
('insert', 1, '2020-04-27 19:13:41', 11, 'Huevo', 28, 'Unidades', 'Refrigeradora'),
('insert', 1, '2020-04-27 19:13:41', 10, 'Arroz a granel', 9.5, 'Kg', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 9, 'Atún de jurel', 8, 'Latas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 8, 'Atún de caballa', 16, 'Latas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 7, 'Fideo plumita', 4, 'Bolsas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 6, 'Fideo canuto grande', 5, 'Bolsas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 5, 'Sardina en salsa de tomate', 0, 'Latas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 4, 'Aceite', 2, 'Botellas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 3, 'Pomarola', 3, 'Bolsas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 2, 'Spaguetti Tottus', 0, 'Bolsas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 1, 'Ajinomen de gallina', 1, 'Bolsas', 'Cooler'),
('insert', 1, '2020-04-27 19:13:41', 35, 'Poet', 4125, 'ml', 'Debajo del lavadero de la cocina'),
('insert', 1, '2020-04-27 19:13:41', 36, 'Lejia', 5, 'Kg', 'Cocina'),
('insert', 1, '2020-04-27 19:13:41', 37, 'Ace', 2, 'Baldes', 'Cocina'),
('insert', 1, '2020-04-27 19:13:41', 38, 'Tomate', 6, 'Unidades', 'Refrigeradora');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla Producto
--
ALTER TABLE Producto
  ADD PRIMARY KEY (id_producto);

--
-- Indices de la tabla Producto_historial
--
ALTER TABLE Producto_historial
  ADD PRIMARY KEY (id_producto,revision);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla Producto
--
ALTER TABLE Producto
  MODIFY id_producto int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla Producto_historial
--
ALTER TABLE Producto_historial
  MODIFY revision int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
