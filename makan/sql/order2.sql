CREATE DATABASE IF NOT EXISTS `esd-order` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `esd-order`;
-- --------------------------------------------------------
--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `orderID` int(100) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `customerName` char(100) NOT NULL,
  `restaurantName` char(100) NOT NULL,
  `riderID` int(100) NOT NULL,
  `status` char(20) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `order`
--

INSERT INTO `order` 
VALUES 
	(1, 'Benjamin', 'Kopitiam', 1, 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55'),
	(2, 'Kenneth', 'McDonalds', 2, 'NEW', '2020-06-12 02:14:55', '2020-06-12 02:14:55');


-- --------------------------------------------------------

--
-- Table structure for table `order_item`
--

DROP TABLE IF EXISTS `order_item`;
CREATE TABLE IF NOT EXISTS `order_item` (
  `itemID` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `orderID` int(11) NOT NULL,
  `foodName` char(13) NOT NULL,
  `quantity` int(11) NOT NULL
  
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `order_item`
--

INSERT INTO `order_item`
VALUES
	(1, 1, 'Chicken Rice', 1),
	(2, 1, 'Meepok', 1),
    (3, 2, 'Mala', 1),
	(4, 2, 'Happy Meal', 1);

--
-- Constraints for table `order_item`
--
ALTER TABLE `order_item`
  ADD CONSTRAINT `FK_orderID` FOREIGN KEY (`orderID`) REFERENCES `order` (`orderID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;