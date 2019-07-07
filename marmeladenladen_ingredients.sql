-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 07, 2019 at 05:47 PM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.1.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `marmelade`
--

-- --------------------------------------------------------

--
-- Table structure for table `marmeladenladen_ingredients`
--

CREATE TABLE `marmeladenladen_ingredients` (
  `id` int(11) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `marmeladenladen_ingredients`
--

INSERT INTO `marmeladenladen_ingredients` (`id`, `Name`, `Type`) VALUES
(1, 'Bananas', 'Fruit'),
(2, 'Blueberries', 'Fruit'),
(3, 'Strawberries', 'Fruit'),
(4, 'Raspberries', 'Fruit'),
(5, 'Apples', 'Fruit'),
(6, 'Cherries', 'Fruit'),
(7, 'Peaches', 'Fruit'),
(8, 'Nectarines', 'Fruit'),
(9, 'Oranges', 'Fruit'),
(10, 'Lemons', 'Fruit'),
(11, 'Grapefruit', 'Fruit'),
(12, 'Limes', 'Fruit'),
(13, 'Mangos', 'Fruit'),
(14, 'Blackberries', 'Fruit'),
(15, 'Johannes berries', 'Fruit'),
(16, 'Pears', 'Fruit'),
(17, 'Apricots', 'Fruit'),
(18, 'Plums', 'Fruit'),
(19, 'Dates', 'Fruit'),
(20, 'Papayas', 'Fruit'),
(21, 'Figs', 'Fruit'),
(22, 'Red currents', 'Fruit'),
(23, 'Cranberries', 'Fruit'),
(24, 'Gooseberries', 'Fruit'),
(25, 'Grapes', 'Fruit'),
(26, 'Kiwis', 'Fruit'),
(27, 'Passionfruit', 'Fruit'),
(28, 'Rhubarb', 'Fruit'),
(35, 'Mint', 'Spice'),
(36, 'Pepper', 'Spice'),
(37, 'Aniseed', 'Spice'),
(38, 'Basil', 'Spice'),
(39, 'Ginger', 'Spice'),
(40, 'Honey', 'Spice'),
(41, 'Lemon Zest', 'Spice'),
(42, 'Agave nectar', 'Spice'),
(43, 'Cinnamon', 'Spice'),
(44, 'Cloves', 'Spice'),
(45, 'Garlic', 'Spice'),
(46, 'Cocoa', 'Spice'),
(47, 'Coconut Flakes', 'Spice'),
(48, 'Chili Flakes', 'Spice'),
(49, 'Rosemary', 'Spice'),
(50, 'Vanilla', 'Spice');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `marmeladenladen_ingredients`
--
ALTER TABLE `marmeladenladen_ingredients`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `marmeladenladen_ingredients`
--
ALTER TABLE `marmeladenladen_ingredients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
