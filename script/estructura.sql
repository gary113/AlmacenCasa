-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 27-04-2020 a las 19:58:57
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
-- Base de datos: `inventario_casa`
--
CREATE DATABASE IF NOT EXISTS `inventario_casa` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `inventario_casa`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Producto`
--

DROP TABLE IF EXISTS `Producto`;
CREATE TABLE `Producto` (
  `id_producto` int NOT NULL,
  `descripcion_producto` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cantidad_producto` double UNSIGNED NOT NULL,
  `unidad_producto` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `lugar_producto` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Disparadores `Producto`
--
DROP TRIGGER IF EXISTS `Producto_delete`;
DELIMITER $$
CREATE TRIGGER `Producto_delete` BEFORE DELETE ON `Producto` FOR EACH ROW INSERT INTO Producto_historial SELECT 'delete', NULL, NOW(), d.* FROM Producto AS d WHERE d.id_producto = OLD.id_producto
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `Producto_insert`;
DELIMITER $$
CREATE TRIGGER `Producto_insert` AFTER INSERT ON `Producto` FOR EACH ROW INSERT INTO Producto_historial SELECT 'insert', NULL, NOW(), d.* FROM Producto AS d WHERE d.id_producto = NEW.id_producto
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `Producto_update`;
DELIMITER $$
CREATE TRIGGER `Producto_update` AFTER UPDATE ON `Producto` FOR EACH ROW INSERT INTO Producto_historial SELECT 'update', NULL, NOW(), d.* FROM Producto AS d WHERE d.id_producto = NEW.id_producto
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Producto_historial`
--

DROP TABLE IF EXISTS `Producto_historial`;
CREATE TABLE `Producto_historial` (
  `accion` varchar(8) DEFAULT 'insert',
  `revision` int NOT NULL,
  `fecha_hora` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_producto` int NOT NULL,
  `descripcion_producto` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cantidad_producto` double UNSIGNED NOT NULL,
  `unidad_producto` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `lugar_producto` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Producto`
--
ALTER TABLE `Producto`
  ADD PRIMARY KEY (`id_producto`);

--
-- Indices de la tabla `Producto_historial`
--
ALTER TABLE `Producto_historial`
  ADD PRIMARY KEY (`id_producto`,`revision`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Producto`
--
ALTER TABLE `Producto`
  MODIFY `id_producto` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Producto_historial`
--
ALTER TABLE `Producto_historial`
  MODIFY `revision` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
