/*
 Navicat Premium Data Transfer

 Source Server         : 阿里云6个月
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : rm-2ze9c7bp86pc6m9qd3o.mysql.rds.aliyuncs.com
 Source Database       : huojingyuan

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : utf-8

 Date: 08/23/2019 13:31:23 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) COLLATE utf8_bin DEFAULT NULL,
  `password` varchar(180) COLLATE utf8_bin DEFAULT NULL,
  `name` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `role` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  `xy` varchar(50) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
--  Records of `admin`
-- ----------------------------
BEGIN;
INSERT INTO `admin` VALUES ('1', 'ryp', '123456', '管理员1', 'admin', 'admin'), ('2', 'hjy', '123456', '管理员2', 'admin', 'admin'), ('3', 'zdh', '123456', '自动化', 'user', '智能制造与自动化学院'), ('4', 'gj', '123456', '国教', 'user', '国际教育学院'), ('5', 'wf', '123456', '文法', 'user', '文法学院'), ('6', 'jr', '123456', '金融', 'user', '金融学院'), ('7', 'dk', '123456', '动科', 'user', '动物科技学院'), ('8', 'nd', '123456', '能动', 'user', '能源与动力工程学院'), ('9', 'kj', '123456', '会计', 'user', '会计学院'), ('10', 'ys', '123456', '艺术', 'user', '艺术学院'), ('11', 'gc', '123456', '工程', 'user', '工程管理学院'), ('12', 'zy', '123456', '制药', 'user', '制药工程学院'), ('13', 'dy', '123456', '动医', 'user', '动物医学院'), ('14', 'wgy', '123456', '外国语', 'user', '外国语学院'), ('15', 'gs', '123456', '工商', 'user', '工商管理学院'), ('16', 'sp', '123456', '食品', 'user', '食品与生物工程学院'), ('17', 'bz', '123456', '包装', 'user', '包装与印刷工程学院'), ('18', 'nl', '123456', '农林', 'user', '农林经济管理学院'), ('19', 'wl', '123456', '物流', 'user', '物流与电商学院'), ('20', 'rj', '123456', '软件', 'user', '软件学院'), ('21', 'jm', '123456', '经贸', 'user', '经济贸易学院'), ('22', 'xx', '123456', '信息', 'user', '信息工程学院'), ('23', 'lg', '123456', '旅馆', 'user', '旅游学院');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
