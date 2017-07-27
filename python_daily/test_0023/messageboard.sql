/*
Navicat MySQL Data Transfer

Source Server         : MYSQL
Source Server Version : 50713
Source Host           : localhost:3306
Source Database       : messageboard

Target Server Type    : MYSQL
Target Server Version : 50713
File Encoding         : 65001

Date: 2017-07-26 14:40:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` text,
  `timestamp` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_USER` (`user_id`),
  CONSTRAINT `FK_USER` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES ('1', 'One', '2017-07-26 14:38:34', '1');
INSERT INTO `post` VALUES ('2', 'OneDay', '2017-07-27 14:38:53', '1');
INSERT INTO `post` VALUES ('3', 'Two', '2017-07-12 14:39:06', '3');
INSERT INTO `post` VALUES ('4', 'Three', '2017-07-10 14:39:24', '2');
INSERT INTO `post` VALUES ('5', 'Four', '2017-07-28 14:39:37', '4');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '用户表主键',
  `email` varchar(40) DEFAULT NULL,
  `username` varchar(40) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'AC_Dreamer@163.com', 'Leland', null);
INSERT INTO `user` VALUES ('2', 'Cql_liliang@163.com', 'Cql_liliang', null);
INSERT INTO `user` VALUES ('3', '985892962@qq.com', '985892962', null);
INSERT INTO `user` VALUES ('4', 'test@admin.com', 'test', null);
