-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 30, 2021 at 03:14 PM
-- Server version: 5.7.32
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `HungryFoodie`
--
CREATE DATABASE IF NOT EXISTS `HungryFoodie` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `HungryFoodie`;

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `CustomerID` int(100) NOT NULL,
  `CustomerName` varchar(100) NOT NULL,
  `CustomerContact` int(8) NOT NULL,
  `CustomerAddress` varchar(100) NOT NULL,
  `CustPostalCode` int(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FoodList`
--

CREATE TABLE `FoodList` (
  `FoodID` int(100) NOT NULL,
  `RestaurantID` int(100) NOT NULL,
  `FoodName` varchar(100) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `Price` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `FoodOrder`
--

CREATE TABLE `FoodOrder` (
  `FoodOrderID` int(100) NOT NULL,
  `CustomerID` int(100) NOT NULL,
  `RiderID` int(100) NOT NULL,
  `DateTime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `RestaurantID` int(100) NOT NULL,
  `FoodID` int(100) NOT NULL,
  `Price` int(100) NOT NULL,
  `Status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `FoodOrder`
--

INSERT INTO `FoodOrder` (`FoodOrderID`, `CustomerID`, `RiderID`, `DateTime`, `RestaurantID`, `FoodID`, `Price`, `Status`) VALUES
(1, 1, 1, '2021-03-20 11:23:03', 1, 123, 10, 'Pending'),
(2, 2, 2, '2021-03-20 11:23:03', 2, 321, 20, 'Delivered'),
(3, 1, 1, '2021-03-20 12:25:17', 1, 123, 10, 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `Restaurant`
--

CREATE TABLE `Restaurant` (
  `RestaurantID` int(100) NOT NULL,
  `RestaurantName` varchar(100) NOT NULL,
  `RestaurantContact` int(8) NOT NULL,
  `RestaurantAddress` varchar(100) NOT NULL,
  `PostalCode` int(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Rider`
--

CREATE TABLE `Rider` (
  `RiderID` int(100) NOT NULL,
  `RiderName` varchar(100) NOT NULL,
  `VehicleNo` varchar(100) NOT NULL,
  `RiderContact` int(8) NOT NULL,
  `PostalCode` int(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`CustomerID`);

--
-- Indexes for table `FoodList`
--
ALTER TABLE `FoodList`
  ADD PRIMARY KEY (`FoodID`);

--
-- Indexes for table `FoodOrder`
--
ALTER TABLE `FoodOrder`
  ADD PRIMARY KEY (`FoodOrderID`);

--
-- Indexes for table `Restaurant`
--
ALTER TABLE `Restaurant`
  ADD PRIMARY KEY (`RestaurantID`);

--
-- Indexes for table `Rider`
--
ALTER TABLE `Rider`
  ADD PRIMARY KEY (`RiderID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Customer`
--
ALTER TABLE `Customer`
  MODIFY `CustomerID` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FoodList`
--
ALTER TABLE `FoodList`
  MODIFY `FoodID` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `FoodOrder`
--
ALTER TABLE `FoodOrder`
  MODIFY `FoodOrderID` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Restaurant`
--
ALTER TABLE `Restaurant`
  MODIFY `RestaurantID` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Rider`
--
ALTER TABLE `Rider`
  MODIFY `RiderID` int(100) NOT NULL AUTO_INCREMENT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
