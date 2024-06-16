-- MySQL dump 10.13  Distrib 8.4.0, for Win64 (x86_64)
--
-- Host: localhost    Database: shchema
-- ------------------------------------------------------
-- Server version	8.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `KRA_PIN` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'John','Doe','john.doe@example.com','2020-01-15','A1234567B'),(2,'Jane','Smith','jane.smith@example.com','2019-03-22','B2345678C'),(3,'Emily','Jones','emily.jones@example.com','2021-07-01','C3456789D'),(4,'Michael','Brown','michael.brown@example.com','2018-11-11','D4567890E'),(5,'Sarah','Davis','sarah.davis@example.com','2022-05-20','E5678901F'),(6,'David','Wilson','david.wilson@example.com','2017-04-04','F6789012G'),(7,'Laura','Martinez','laura.martinez@example.com','2016-02-18','G7890123H'),(8,'Daniel','Taylor','daniel.taylor@example.com','2023-01-01','H8901234I'),(9,'Olivia','Anderson','olivia.anderson@example.com','2015-09-30','I9012345J'),(10,'Matthew','Thomas','matthew.thomas@example.com','2020-06-25','J0123456K'),(11,'Sophia','Jackson','sophia.jackson@example.com','2019-08-08','K1234567L'),(12,'James','White','james.white@example.com','2021-12-12','L2345678M'),(13,'Emma','Harris','emma.harris@example.com','2018-03-03','M3456789N'),(14,'Liam','Clark','liam.clark@example.com','2022-07-07','N4567890O'),(15,'Isabella','Lewis','isabella.lewis@example.com','2017-01-21','O5678901P'),(16,'Ethan','Robinson','ethan.robinson@example.com','2016-11-15','P6789012Q'),(17,'Ava','Walker','ava.walker@example.com','2023-05-05','Q7890123R'),(18,'Noah','Young','noah.young@example.com','2015-10-10','R8901234S'),(19,'Mia','King','mia.king@example.com','2020-12-12','S9012345T'),(20,'Alexander','Scott','alexander.scott@example.com','2019-02-02','T0123456U');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  `KRA_PIN` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES ('John','Doe','john.doe@example.com','2020-01-15',60000.00,'A1234567B'),('Jane','Smith','jane.smith@example.com','2019-03-22',75000.00,'B2345678C'),('Emily','Jones','emily.jones@example.com','2021-07-01',50000.00,'C3456789D'),('Michael','Brown','michael.brown@example.com','2018-11-11',85000.00,'D4567890E'),('Sarah','Davis','sarah.davis@example.com','2022-05-20',62000.00,'E5678901F'),('David','Wilson','david.wilson@example.com','2017-04-04',72000.00,'F6789012G'),('Laura','Martinez','laura.martinez@example.com','2016-02-18',81000.00,'G7890123H'),('Daniel','Taylor','daniel.taylor@example.com','2023-01-01',67000.00,'H8901234I'),('Olivia','Anderson','olivia.anderson@example.com','2015-09-30',76000.00,'I9012345J'),('Matthew','Thomas','matthew.thomas@example.com','2020-06-25',55000.00,'J0123456K'),('Sophia','Jackson','sophia.jackson@example.com','2019-08-08',70000.00,'K1234567L'),('James','White','james.white@example.com','2021-12-12',58000.00,'L2345678M'),('Emma','Harris','emma.harris@example.com','2018-03-03',53000.00,'M3456789N'),('Liam','Clark','liam.clark@example.com','2022-07-07',64000.00,'N4567890O'),('Isabella','Lewis','isabella.lewis@example.com','2017-01-21',69000.00,'O5678901P'),('Ethan','Robinson','ethan.robinson@example.com','2016-11-15',74000.00,'P6789012Q'),('Ava','Walker','ava.walker@example.com','2023-05-05',61000.00,'Q7890123R'),('Noah','Young','noah.young@example.com','2015-10-10',87000.00,'R8901234S'),('Mia','King','mia.king@example.com','2020-12-12',68000.00,'S9012345T'),('Alexander','Scott','alexander.scott@example.com','2019-02-02',59000.00,'T0123456U');
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'shchema'
--

--
-- Dumping routines for database 'shchema'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-16 17:44:08
