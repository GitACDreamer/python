/*
Navicat MySQL Data Transfer

Source Server         : MYSQL
Source Server Version : 50713
Source Host           : localhost:3306
Source Database       : student

Target Server Type    : MYSQL
Target Server Version : 50713
File Encoding         : 65001

Date: 2017-06-05 14:40:28
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(255) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `number` int(11) NOT NULL DEFAULT '1001' COMMENT '学号',
  `name` varchar(255) NOT NULL COMMENT '姓名',
  `score` int(11) DEFAULT NULL COMMENT '分数',
  `age` int(11) DEFAULT NULL COMMENT '年龄',
  `gender` bit(1) DEFAULT b'1' COMMENT '性别（1=Male,0=Female)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1', '1001', 'Liliang', '88', '23', '');
INSERT INTO `student` VALUES ('2', '1002', 'LiMing', '93', '22', '\0');
INSERT INTO `student` VALUES ('3', '1003', 'Jom', '100', '20', '');
