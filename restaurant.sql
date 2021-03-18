CREATE DATABASE IF NOT EXISTS `esd-restaurant` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `esd-restaurant`;
-- --------------------------------------------------------

--
-- Table structure for table `restaurant`
--

DROP TABLE IF EXISTS `restaurant`;
CREATE TABLE `restaurant` (
  `restaurantID` int(100) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `restaurantName` char(100) NOT NULL,
  `phone` char(8) NOT NULL,
  `address` varchar(100) NOT NULL,
  `postalCode` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  
-- --------------------------------------------------------

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
CREATE TABLE `food` (
  `foodID` int(100) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `restaurantID` int(100) NOT NULL,
  `foodName` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `price` varchar(200) NOT NULL,
  FOREIGN KEY (restaurantID) REFERENCES restaurant(restaurantID)
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
