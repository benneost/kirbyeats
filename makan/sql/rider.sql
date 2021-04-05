CREATE DATABASE IF NOT EXISTS `esd-rider` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `esd-rider`;
-- --------------------------------------------------------
--
-- Table structure for table `rider`
--

DROP TABLE IF EXISTS `rider`;
CREATE TABLE `rider` (
  `riderID` int(100) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `riderName` char(100) NOT NULL,
  `vehicleNo` varchar(8) NOT NULL,
  `ridercontact` char(8) NOT NULL,
  `postalcode` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;