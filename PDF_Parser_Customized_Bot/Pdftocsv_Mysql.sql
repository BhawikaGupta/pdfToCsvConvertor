-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: pdftocsv
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `balancesheet`
--

DROP TABLE IF EXISTS `balancesheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `balancesheet` (
  `index` bigint(20) DEFAULT NULL,
  `Particulars` text,
  `year2015` double DEFAULT NULL,
  `year2016` text,
  KEY `ix_balancesheet_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `balancesheet`
--

LOCK TABLES `balancesheet` WRITE;
/*!40000 ALTER TABLE `balancesheet` DISABLE KEYS */;
INSERT INTO `balancesheet` VALUES (0,'To Opening Stock',105400,'95830.00'),(1,'By Sale',234294,'274200'),(2,'To Purchase',151007,'168940.00'),(3,'By Job Work Income',550000,'636478'),(4,'To Gross Profit',623717,'759868.00'),(5,'By Closing Stock',95830,'113960'),(8,'To  Accounting Charges',15000,'20000.00'),(9,'By Gross Profit B/D',623717,'759868'),(10,'To Business Promotion Exp.',7640,'8610.00'),(11,'By Discount',32905,'45460'),(12,'To Depreciation',8452.5,'7277.78'),(14,'To Electricity Exp.',23410,'25630.00'),(16,'To Freight',10350,'16480.00'),(18,'To Bonus',6340,'8640.00'),(20,'To Internet Fex Charges',6310,'7660.00'),(22,'To Misc. Exp',14470,'23790.00'),(24,'To Printing & Stationary',2670,'3280.00'),(26,'To Rent',104400,'124500.00'),(28,'To Repair & Maintenance Exp.',12988,'24970.00'),(30,'To Salary',404000,'473888.00'),(32,'To Staff welfare Exp.',17490,'19340.00'),(34,'To Short & Excess',62,'52.22'),(36,'To Telephone Exp',8680,'10460.00'),(38,'To Conveyance Exp.',10670,'14280.00'),(40,'To Net Profit for the Year',3689.5,'16470.00'),(44,'Total Rs.',656622,'805328.00');
/*!40000 ALTER TABLE `balancesheet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-01 17:11:53
