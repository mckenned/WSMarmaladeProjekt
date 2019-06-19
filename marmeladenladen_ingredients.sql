-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 28. Mai 2019 um 14:39
-- Server-Version: 10.1.40-MariaDB
-- PHP-Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `marmelade`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `marmeladenladen_ingredients`
--

CREATE TABLE `marmeladenladen_ingredients` (
  `id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `marmeladenladen_ingredients`
--

INSERT INTO `marmeladenladen_ingredients` (`id`, `Name`, `Type`) VALUES
(1, 'Banana', 'Fruit'),
(2, 'Blueberry', 'Fruit'),
(3, 'Strawberry', 'Fruit'),
(4, 'Rasberry', 'Fruit'),
(5, 'Apple', 'Fruit'),
(6, 'Cherry', 'Fruit'),
(7, 'Peach', 'Fruit'),
(8, 'Nectarine', 'Fruit'),
(9, 'Orange', 'Fruit'),
(10, 'Lemon', 'Fruit'),
(11, 'Grapefruit', 'Fruit'),
(12, 'Lime', 'Fruit'),
(13, 'Mango', 'Fruit'),
(14, 'Blackberry', 'Fruit'),
(15, 'Johannes berry', 'Fruit'),
(16, 'Pear', 'Fruit'),
(17, 'Apricot', 'Fruit'),
(18, 'Plum', 'Fruit'),
(19, 'Date', 'Fruit'),
(20, 'Guava', 'Fruit'),
(21, 'Black current', 'Fruit'),
(22, 'Red current', 'Fruit'),
(23, 'Cranberry', 'Fruit'),
(24, 'Goose berry', 'Fruit'),
(25, 'Grape', 'Fruit'),
(26, 'Mint', 'Spice'),
(27, 'Peper', 'Spice'),
(28, 'Salt', 'Spice'),
(29, 'Basil', 'Spice'),
(30, 'Ginger', 'Spice'),
(31, 'Lemon zest', 'Spice'),
(32, 'Lime zest', 'Spice'),
(33, 'Lemon juice', 'Spice'),
(34, 'Lime juice', 'Spice'),
(35, 'Orangezest', 'Spice'),
(36, 'Orange juice', 'Spice'),
(37, 'Cocoa', 'Spice'),
(38, 'Cocoanut flakes', 'Spice'),
(39, 'Chilli flakes', 'Spice'),
(40, 'Nutmeg', 'Spice'),
(41, 'Maplesirup', 'Spice'),
(42, 'Honey', 'Spice'),
(43, 'Cinnamon', 'Spice'),
(44, 'Vanilla', 'Spice'),
(45, 'Aniseed', 'Spice'),
(46, 'Cloves', 'Spice'),
(47, 'Garlic', 'Spice');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `marmeladenladen_ingredients`
--
ALTER TABLE `marmeladenladen_ingredients`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `marmeladenladen_ingredients`
--
ALTER TABLE `marmeladenladen_ingredients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
