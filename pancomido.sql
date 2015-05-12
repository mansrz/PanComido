-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 12-05-2015 a las 02:20:45
-- Versión del servidor: 5.5.43-0ubuntu0.14.04.1
-- Versión de PHP: 5.5.9-1ubuntu4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `pancomido`
--
CREATE DATABASE IF NOT EXISTS `pancomido` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `pancomido`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Elaborado`
--

DROP TABLE IF EXISTS `Elaborado`;
CREATE TABLE IF NOT EXISTS `Elaborado` (
  `Elaborado_id` int(11) NOT NULL,
  `Elaborado_nombre` varchar(100) NOT NULL,
  `Elaborado_precio` float NOT NULL,
  `Elaborado_expiracion` int(11) NOT NULL,
  PRIMARY KEY (`Elaborado_id`),
  UNIQUE KEY `Elaborado_nombre` (`Elaborado_nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ElaboradoElemento`
--

DROP TABLE IF EXISTS `ElaboradoElemento`;
CREATE TABLE IF NOT EXISTS `ElaboradoElemento` (
  `Elemento_id` int(11) NOT NULL,
  `Elaborado_id` int(11) NOT NULL,
  `ElaboradoElemento_cantidad` decimal(10,0) NOT NULL,
  `ElaboradoElemento_secuencial` int(11) NOT NULL,
  PRIMARY KEY (`Elemento_id`,`Elaborado_id`,`ElaboradoElemento_secuencial`),
  KEY `Elaborado_id` (`Elaborado_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Elemento`
--

DROP TABLE IF EXISTS `Elemento`;
CREATE TABLE IF NOT EXISTS `Elemento` (
  `Elemento_nombre` varchar(50) NOT NULL,
  `Elemento_precio` decimal(10,0) NOT NULL,
  `Elemento_tipo` int(11) NOT NULL,
  `Elemento_expiracion` int(11) NOT NULL,
  `Elemento_id` int(11) NOT NULL,
  PRIMARY KEY (`Elemento_id`),
  UNIQUE KEY `nombre` (`Elemento_nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Movimiento`
--

DROP TABLE IF EXISTS `Movimiento`;
CREATE TABLE IF NOT EXISTS `Movimiento` (
  `Movimiento_id` int(11) NOT NULL,
  `Movimiento_tipo` int(11) NOT NULL,
  `Movimiento_egreso` decimal(10,0) NOT NULL DEFAULT '0',
  `Movimiento_ingreso` decimal(10,0) NOT NULL DEFAULT '0',
  `Movimiento_elaborado` int(11) NOT NULL DEFAULT '0',
  `Movimiento_elemento` int(11) NOT NULL DEFAULT '0',
  `Movimiento_fecha` date NOT NULL,
  PRIMARY KEY (`Movimiento_id`,`Movimiento_elaborado`,`Movimiento_elemento`,`Movimiento_fecha`),
  KEY `Movimiento_elaborado` (`Movimiento_elaborado`),
  KEY `Movimiento_elemento` (`Movimiento_elemento`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
CREATE TABLE IF NOT EXISTS `Usuario` (
  `usuario_nick` varchar(16) NOT NULL,
  `usuario_pwd` varchar(32) NOT NULL,
  `create_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Usuario`
--

INSERT INTO `Usuario` (`usuario_nick`, `usuario_pwd`, `create_time`) VALUES
('admin', '123', '2015-05-09 23:36:04');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ElaboradoElemento`
--
ALTER TABLE `ElaboradoElemento`
  ADD CONSTRAINT `ElaboradoElemento_ibfk_1` FOREIGN KEY (`Elaborado_id`) REFERENCES `Elaborado` (`Elaborado_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `ElaboradoElemento_ibfk_2` FOREIGN KEY (`Elemento_id`) REFERENCES `Elemento` (`Elemento_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `Movimiento`
--
ALTER TABLE `Movimiento`
  ADD CONSTRAINT `Movimiento_ibfk_1` FOREIGN KEY (`Movimiento_elaborado`) REFERENCES `Elaborado` (`Elaborado_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `Movimiento_ibfk_2` FOREIGN KEY (`Movimiento_elemento`) REFERENCES `ElaboradoElemento` (`Elemento_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
