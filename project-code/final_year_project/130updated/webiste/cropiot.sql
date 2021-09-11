/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.5.5-10.4.11-MariaDB : Database - cropiot
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`cropiot` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `cropiot`;

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `userdetails` */

insert  into `userdetails`(`id`,`name`,`email`,`password`) values (1,'azhar','azharkureshi@gmail.com','123'),(2,'sushant','sushant@gmail.com','123'),(3,'yash','yash@gmail.com','123'),(4,'kishan','kishan@gmail.com','123'),(5,'man','man@gmail.com','123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
