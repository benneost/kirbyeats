CREATE DATABASE IF NOT EXISTS `esd-customer` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `esd-customer`;
-- --------------------------------------------------------
--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `customerID` int(100) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `customerName` char(100) NOT NULL,
  `phone` char(8) NOT NULL,
  `address` varchar(100) NOT NULL,
  `postalCode` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;