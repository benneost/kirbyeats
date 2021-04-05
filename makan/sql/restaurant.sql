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
  `restaurantContact` char(8) NOT NULL,
  `restaurantAddress` varchar(100) NOT NULL,
  `postalCode` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `restaurant`
--

INSERT INTO `restaurant` 
VALUES 
	(1, 'Kopitiam', '91234567', 'Century Square', 529509),
	(2, 'McDonalds', '91234567', 'Century Square', 529509),
	(3, 'Subway', '91234567', 'Century Square', 529509),
	(4, 'Nam Nam', '91234567', 'Century Square', 529509),
	(5, 'Liho', '91234567', 'Century Square', 529509),
	(6, 'KFC', '91234567', 'Bedok Mall', 467360),
	(7, 'Boost', '91234567', 'Bedok Mall', 467360),
	(8, 'Beef Bro', '91234567', 'Bedok Mall', 467360),
	(9, 'Fun Toast', '91234567', 'Bedok Mall', 467360),
	(10, 'HaidiLao Hotpot', '91234567', 'Eastpoint', 528833),
	(11, 'Kei Kaisendon', '91234567', 'Eastpoint', 528833),
	(12, 'Ichiban Boshi', '91234567', 'Eastpoint', 528833);
  
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
--
-- Dumping data for table `food`
--

INSERT INTO `food` 
VALUES 
	(1, 1, 'Chicken Rice', "Alot alot of chicken", 3),
	(2, 1, 'Meepok', "Alot alot of noodles", 4),
  (3, 1, 'Fried Rice', "Very fried rice", 5),
  (4, 1, 'Mala', "Might burn your tongue off", 10),
  (5, 1, 'Ayam penyet', "fried chicken lor", 4),
  (6, 1, 'Fish soup', "Fried fish", 3.5),
  (7, 2, 'McSpicy Meal', "Very spicy hor", 7),
  (8, 2, 'McNuggets Meal', "Some nuggets of wisdom", 8.2),
  (9, 2, 'Filet O Fish Meal', "Fried fish filet", 6.8),
  (10, 2, 'Happy Meal', "Makes you very happy", 10);

