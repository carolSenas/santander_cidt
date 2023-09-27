-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 27-09-2023 a las 16:29:33
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `senasoft`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `establecimientos`
--

CREATE TABLE IF NOT EXISTS `establecimientos` (
  `codigo_establecimiento` bigint NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `responsable` varchar(70) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `direccion` varchar(40) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`codigo_establecimiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE IF NOT EXISTS `servicios` (
  `codigo_servicio` bigint NOT NULL,
  `codigo_establecimiento` bigint NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `descripcion` varchar(200) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `tipo` varchar(25) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`codigo_servicio`),
  FOREIGN KEY (`codigo_establecimiento`) references establecimientos (`codigo_establecimiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE IF NOT EXISTS `usuarios` (
  `documento` bigint NOT NULL,
  `codigo_servicio` bigint NOT NULL,
  `contraseña` varchar(15) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `tipo_documento` bigint NOT NULL,
  `nombre` varchar(20) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `apellidos` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `telefono` bigint NOT NULL,
  `ocupacion` varchar(30) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `correo` varchar(30) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `ciudad` varchar(30) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `direccion` varchar(40) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`documento`),
  FOREIGN KEY (`codigo_servicio`) references servicios (`codigo_servicio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE IF NOT EXISTS `categorias` (
  `codigo_categoria` bigint NOT NULL,
  `codigo_servicio` bigint NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `descripcion` varchar(200) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`codigo_categoria`),
  FOREIGN KEY (`codigo_servicio`) references servicios (`codigo_servicio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_servicios`
--

CREATE TABLE IF NOT EXISTS `detalles_servicios` (
  `codigo_detalle_servicio` bigint NOT NULL,
  `documento` bigint NOT NULL,
  `codigo_servicio` bigint NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`codigo_detalle_servicio`),
  FOREIGN KEY (`documento`) references usuarios (`documento`),
  FOREIGN KEY (`codigo_servicio`) references servicios (`codigo_servicio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `municipios`
--

CREATE TABLE IF NOT EXISTS `municipios` (
  `codigo_municipio` bigint NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `departamento` varchar(20) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`codigo_municipio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------
--
-- Estructura de tabla para la tabla `manzanas`
--

CREATE TABLE IF NOT EXISTS `manzanas` (
  `codigo_manzana` bigint NOT NULL,
  `codigo_municipio` bigint NOT NULL,
  `codigo_servicio` bigint NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `localidad` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `direccion` varchar(40) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`codigo_manzana`),
  FOREIGN KEY (`codigo_municipio`) references municipios (`codigo_municipio`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

drop table manzanas;

ALTER TABLE manzanas
ADD CONSTRAINT fk_codigo_servicio
FOREIGN KEY (`codigo_servicio`)
REFERENCES servicios (`codigo_servicio`);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicio_establecimiento`
--

CREATE TABLE IF NOT EXISTS `servicio_establecimiento` (
  `codigo_servicio_establecimiento` bigint NOT NULL,
  `codigo_servicio` bigint NOT NULL,
  `codigo_establecimiento` bigint NOT NULL,
  PRIMARY KEY (`codigo_servicio_establecimiento`),
  FOREIGN KEY (`codigo_servicio`) references servicios (`codigo_servicio`),
  FOREIGN KEY (`codigo_establecimiento`) references establecimientos (`codigo_establecimiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------


COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
