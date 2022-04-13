/*
 Navicat Premium Data Transfer

 Source Server         : 172.17.0.2
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : 172.17.0.2:3306
 Source Schema         : webapp

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 13/04/2022 13:54:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bnf_emp
-- ----------------------------
DROP TABLE IF EXISTS `bnf_emp`;
CREATE TABLE `bnf_emp` (
  `id` int NOT NULL,
  `experiences` int NOT NULL,
  `insuarance` int NOT NULL,
  `last_salary` decimal(10,2) NOT NULL,
  `current_salary` decimal(10,2) NOT NULL,
  `PA_Toeic` int DEFAULT NULL,
  `PA_Perform` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_benefit` varchar(255) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of bnf_emp
-- ----------------------------
BEGIN;
INSERT INTO `bnf_emp` (`id`, `experiences`, `insuarance`, `last_salary`, `current_salary`, `PA_Toeic`, `PA_Perform`, `id_benefit`) VALUES (94, 5, 4, 9000.00, 10000.00, 3000, 'Excellent', '');
INSERT INTO `bnf_emp` (`id`, `experiences`, `insuarance`, `last_salary`, `current_salary`, `PA_Toeic`, `PA_Perform`, `id_benefit`) VALUES (100, 11, 21, 10000.00, 4.00, 5, 'Bad', '');
COMMIT;

-- ----------------------------
-- Table structure for rest_emp
-- ----------------------------
DROP TABLE IF EXISTS `rest_emp`;
CREATE TABLE `rest_emp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `address` text,
  `password` varchar(45) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of rest_emp
-- ----------------------------
BEGIN;
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (94, 'Nhat Thanh', 'banxaxvi@gmail.com', '0982640106', 'Nguyen Van Troi', '123456', 'blob:http://localhost:3000/cf658153-1716-4ff6-b508-48a653bec657', 'SME');
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (100, 'Nhat Thanh', 'banxaxvi@gmail.com', '0982640106', 'Nguyen Van Troi 17', '123456', 'blob:http://localhost:3000/cf658153-1716-4ff6-b508-48a653bec657', 'DIRECTOR');
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (105, 'Nhat', 'banxaxvi@gmail.com', '0982640106', 'Nguyen Van TrAM', '123456', 'blob:http://localhost:3000/cf658153-1716-4ff6-b508-48a653bec657', 'TESTER');
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (106, 'Nh2', 'banxavi@gmail.com', '0982640106', 'Phú Yên', '123456', 'blob:http://localhost:3000/1808edad-46eb-4bbc-a51d-b6cc35a14452', 'TEAMLEAD');
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (108, 'axa', 'cax@gmail.com', '123', '1233', '123456', 'blob:http://localhost:3000/484c6484-88e9-4dcb-8f27-2c7cc95ab77c', 'SME');
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (109, 'axz', 'bvax@gas2', '12', '123', '123456', 'blob:http://localhost:3000/a79823e5-6292-4639-bd03-846acb5415e1', 'PM');
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (110, 'Nhat BAN', 'banxavi@gmail.com1', '0982640106', 'Phú Yên1', '123456', '', 'DIRECTOR');
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (111, '123', 'banxav2@gmail.com', '213', '123', '123456', 'blob:http://localhost:3000/191aec8f-f1ec-4238-98c7-53351d43f7ec', 'PM');
INSERT INTO `rest_emp` (`id`, `name`, `email`, `phone`, `address`, `password`, `image`, `position`) VALUES (112, '121', 'axa@gmail.com', '213312', '12312', '123456', 'blob:http://localhost:3000/215df486-addb-41d2-8f97-6506ce71455f', 'PM');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
