/*
 Navicat Premium Data Transfer

 Source Server         : 172.16.20.130（虚拟机）
 Source Server Type    : MySQL
 Source Server Version : 50560
 Source Host           : 172.16.20.130:3306
 Source Schema         : movie

 Target Server Type    : MySQL
 Target Server Version : 50560
 File Encoding         : 65001

 Date: 27/05/2019 16:23:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pwd` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `is_super` smallint(6) NULL DEFAULT NULL,
  `role_id` int(11) NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `role_id`(`role_id`) USING BTREE,
  INDEX `ix_admin_addtime`(`addtime`) USING BTREE,
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (3, 'root', 'pbkdf2:sha256:50000$f54gjQtk$387d459a2bfde6b43270fd73fde2e04b9388432b40d1ded8cbdef0e5f7740f75', 0, 1, '2019-05-24 14:52:26');
INSERT INTO `admin` VALUES (4, 'admin', 'pbkdf2:sha256:50000$F3NSLmvu$99671bb78ebdfdd6c01e7e0df507b00a321c24212b9f43d920646c423740c268', 1, 6, '2019-05-27 11:18:54');

-- ----------------------------
-- Table structure for adminlog
-- ----------------------------
DROP TABLE IF EXISTS `adminlog`;
CREATE TABLE `adminlog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) NULL DEFAULT NULL,
  `ip` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `admin_id`(`admin_id`) USING BTREE,
  INDEX `ix_adminlog_addtime`(`addtime`) USING BTREE,
  CONSTRAINT `adminlog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 43 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of adminlog
-- ----------------------------
INSERT INTO `adminlog` VALUES (1, 3, '172.16.16.47', '2019-05-24 16:36:41');
INSERT INTO `adminlog` VALUES (2, 3, '172.16.16.47', '2019-05-24 16:36:51');
INSERT INTO `adminlog` VALUES (3, 3, '172.16.16.47', '2019-05-24 16:37:00');
INSERT INTO `adminlog` VALUES (4, 3, '172.16.16.47', '2019-05-24 16:45:44');
INSERT INTO `adminlog` VALUES (5, 3, '172.16.16.47', '2019-05-27 09:54:21');
INSERT INTO `adminlog` VALUES (6, 3, '172.16.16.47', '2019-05-27 09:57:51');
INSERT INTO `adminlog` VALUES (7, 4, '172.16.16.47', '2019-05-27 14:06:45');
INSERT INTO `adminlog` VALUES (8, 4, '172.16.16.47', '2019-05-27 14:12:47');
INSERT INTO `adminlog` VALUES (9, 3, '172.16.16.47', '2019-05-27 14:13:24');
INSERT INTO `adminlog` VALUES (10, 3, '172.16.16.47', '2019-05-27 14:18:34');
INSERT INTO `adminlog` VALUES (11, 4, '172.16.16.47', '2019-05-27 14:18:53');
INSERT INTO `adminlog` VALUES (16, 3, '172.16.16.47', '2019-05-27 14:32:40');
INSERT INTO `adminlog` VALUES (17, 3, '172.16.16.47', '2019-05-27 14:41:09');
INSERT INTO `adminlog` VALUES (18, 3, '172.16.16.47', '2019-05-27 14:42:07');
INSERT INTO `adminlog` VALUES (19, 3, '172.16.16.47', '2019-05-27 14:48:47');
INSERT INTO `adminlog` VALUES (20, 3, '172.16.16.47', '2019-05-27 14:49:46');
INSERT INTO `adminlog` VALUES (21, 3, '172.16.16.47', '2019-05-27 14:50:23');
INSERT INTO `adminlog` VALUES (22, 3, '172.16.16.47', '2019-05-27 14:52:45');
INSERT INTO `adminlog` VALUES (23, 3, '172.16.16.47', '2019-05-27 14:53:53');
INSERT INTO `adminlog` VALUES (24, 3, '172.16.16.47', '2019-05-27 14:55:15');
INSERT INTO `adminlog` VALUES (25, 3, '172.16.16.47', '2019-05-27 14:59:13');
INSERT INTO `adminlog` VALUES (26, 3, '172.16.16.47', '2019-05-27 15:04:34');
INSERT INTO `adminlog` VALUES (27, 3, '172.16.16.47', '2019-05-27 15:08:22');
INSERT INTO `adminlog` VALUES (28, 3, '172.16.16.47', '2019-05-27 15:09:31');
INSERT INTO `adminlog` VALUES (29, 3, '172.16.16.47', '2019-05-27 15:28:45');
INSERT INTO `adminlog` VALUES (30, 3, '172.16.16.47', '2019-05-27 15:29:08');
INSERT INTO `adminlog` VALUES (31, 3, '172.16.16.47', '2019-05-27 15:31:57');
INSERT INTO `adminlog` VALUES (32, 4, '172.16.16.47', '2019-05-27 15:32:13');
INSERT INTO `adminlog` VALUES (33, 4, '172.16.16.47', '2019-05-27 15:32:42');
INSERT INTO `adminlog` VALUES (34, 3, '172.16.16.47', '2019-05-27 15:35:18');
INSERT INTO `adminlog` VALUES (35, 3, '172.16.16.47', '2019-05-27 15:40:55');
INSERT INTO `adminlog` VALUES (36, 4, '172.16.16.47', '2019-05-27 15:56:40');
INSERT INTO `adminlog` VALUES (37, 4, '172.16.16.47', '2019-05-27 15:57:03');
INSERT INTO `adminlog` VALUES (38, 4, '172.16.16.47', '2019-05-27 15:58:01');
INSERT INTO `adminlog` VALUES (39, 4, '172.16.16.47', '2019-05-27 15:59:47');
INSERT INTO `adminlog` VALUES (40, 3, '172.16.16.47', '2019-05-27 16:02:22');
INSERT INTO `adminlog` VALUES (41, 4, '172.16.16.47', '2019-05-27 16:04:23');
INSERT INTO `adminlog` VALUES (42, 3, '172.16.16.47', '2019-05-27 16:16:21');

-- ----------------------------
-- Table structure for auth
-- ----------------------------
DROP TABLE IF EXISTS `auth`;
CREATE TABLE `auth`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  UNIQUE INDEX `url`(`url`) USING BTREE,
  INDEX `ix_auth_addtime`(`addtime`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 39 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth
-- ----------------------------
INSERT INTO `auth` VALUES (6, '添加标签', '/admin/tag/add/', '2019-05-27 15:10:44');
INSERT INTO `auth` VALUES (7, '标签列表', '/admin/tag/list/<int:page>/', '2019-05-27 15:11:18');
INSERT INTO `auth` VALUES (8, '标签删除', '/admin/tag/del/<int:id>/', '2019-05-27 15:12:24');
INSERT INTO `auth` VALUES (9, '编辑标签', '/admin/tag/edit/<int:id>/', '2019-05-27 15:12:47');
INSERT INTO `auth` VALUES (10, '添加电影', '/admin/movie/add/', '2019-05-27 15:13:14');
INSERT INTO `auth` VALUES (11, '电影列表', '/admin/movie/list/<int:page>', '2019-05-27 15:13:26');
INSERT INTO `auth` VALUES (12, '删除电影', '/admin/movie/del/<int:id>', '2019-05-27 15:13:40');
INSERT INTO `auth` VALUES (13, '编辑电影', '/admin/movie/edit/<int:id>', '2019-05-27 15:13:51');
INSERT INTO `auth` VALUES (14, '上映预告添加', '/admin/preview/add/', '2019-05-27 15:14:04');
INSERT INTO `auth` VALUES (15, '上映预告列表', '/admin/preview/list/<int:page>/', '2019-05-27 15:14:17');
INSERT INTO `auth` VALUES (16, '预告删除', '/admin/preview/del/<int:id>', '2019-05-27 15:14:28');
INSERT INTO `auth` VALUES (17, '上映预告编辑', '/admin/preview/edit/<int:id>', '2019-05-27 15:14:37');
INSERT INTO `auth` VALUES (18, '会员列表', '/admin/user/list/<int:page>/', '2019-05-27 15:14:47');
INSERT INTO `auth` VALUES (19, '查看会员', '/admin/user/view/<int:id>', '2019-05-27 15:14:59');
INSERT INTO `auth` VALUES (20, '会员删除', '/admin/user/del/<int:id>/', '2019-05-27 15:15:12');
INSERT INTO `auth` VALUES (21, '评论列表', '/admin/comment/list/<int:page>/', '2019-05-27 15:15:21');
INSERT INTO `auth` VALUES (22, '评论删除', '/admin/comment/del/<int:id>/', '2019-05-27 15:15:32');
INSERT INTO `auth` VALUES (23, '收藏列表', '/admin/moviecol/list/<int:page>/', '2019-05-27 15:15:43');
INSERT INTO `auth` VALUES (24, '收藏删除', '/admin/moviecol/del/<int:id>/', '2019-05-27 15:15:54');
INSERT INTO `auth` VALUES (25, '操作日志列表', '/admin/oplog/list/<int:page>/', '2019-05-27 15:16:05');
INSERT INTO `auth` VALUES (26, '管理员登录日志列表', '/admin/adminloginlog/list/<int:page>/', '2019-05-27 15:16:18');
INSERT INTO `auth` VALUES (27, '会员登录日志列表', '/admin/userloginlog/list/<int:page>/', '2019-05-27 15:16:29');
INSERT INTO `auth` VALUES (28, '添加权限', '/admin/auth/add/', '2019-05-27 15:16:40');
INSERT INTO `auth` VALUES (29, '编辑权限', '/admin/auth/edit/<int:id>/', '2019-05-27 15:16:51');
INSERT INTO `auth` VALUES (30, '权限列表', '/admin/auth/list/<int:page>/', '2019-05-27 15:17:01');
INSERT INTO `auth` VALUES (31, '权限删除', '/admin/auth/del/<int:id>/', '2019-05-27 15:17:11');
INSERT INTO `auth` VALUES (32, '添加角色', '/admin/role/add/', '2019-05-27 15:17:21');
INSERT INTO `auth` VALUES (33, '角色列表', '/admin/role/list/<int:page>/', '2019-05-27 15:17:31');
INSERT INTO `auth` VALUES (34, '角色删除', '/admin/role/del/<int:id>/', '2019-05-27 15:17:40');
INSERT INTO `auth` VALUES (35, '编辑角色', '/admin/role/edit/<int:id>/', '2019-05-27 15:17:49');
INSERT INTO `auth` VALUES (36, '添加管理员', '/admin/admin/add/', '2019-05-27 15:18:02');
INSERT INTO `auth` VALUES (37, '管理员列表', '/admin/admin/list/<int:page>/', '2019-05-27 15:18:15');
INSERT INTO `auth` VALUES (38, '系统管理', '/admin/', NULL);

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `movie_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `movie_id`(`movie_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_comment_addtime`(`addtime`) USING BTREE,
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES (2, '还可以', 1, 2, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (3, '很精彩', 1, 3, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (4, '场面真精彩', 1, 5, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (5, '值得一看', 1, 8, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (6, '还不错', 1, 9, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (7, '好看', 1, 4, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (8, '还可以', 1, 6, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (9, '很精彩', 1, 10, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (10, '场面真精彩', 1, 11, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (13, '好看', 1, 1, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (14, '还可以', 1, 1, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (15, '很精彩', 1, 3, '2018-10-21 16:16:16');
INSERT INTO `comment` VALUES (17, '值得一看', 1, 12, '2018-10-21 16:16:16');

-- ----------------------------
-- Table structure for movie
-- ----------------------------
DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `info` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `logo` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `star` smallint(6) NULL DEFAULT NULL,
  `playnum` bigint(20) NULL DEFAULT NULL,
  `commentnum` bigint(20) NULL DEFAULT NULL,
  `tag_id` int(11) NULL DEFAULT NULL,
  `area` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `release_time` date NULL DEFAULT NULL,
  `length` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  UNIQUE INDEX `url`(`url`) USING BTREE,
  UNIQUE INDEX `logo`(`logo`) USING BTREE,
  INDEX `tag_id`(`tag_id`) USING BTREE,
  INDEX `ix_movie_addtime`(`addtime`) USING BTREE,
  CONSTRAINT `movie_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of movie
-- ----------------------------
INSERT INTO `movie` VALUES (1, '变形金刚', '2019052311502357d3fe2f49e342a79152a7cda65493fdhtpy.mp4', '撒旦法都是发撒旦法都是', '2019052311502334c5239f30bf458eb9a725357e556f401348814118469.jpg', 5, 0, 0, NULL, '杭州', '2019-05-17', '160', '2019-05-23 11:50:23');
INSERT INTO `movie` VALUES (2, '琅琊榜', '2019052318153920730725a2c2467fac2b019b9e7cc8f4htpy.mp4', '钱钱钱钱钱钱群群群群群群群群', '20190523181539f47b6f0618b14e599ccacbb8bd427c911348814017665.jpg', 5, 0, 0, NULL, '杭州', '2019-05-21', '160', '2019-05-23 18:15:39');
INSERT INTO `movie` VALUES (5, '琅琊榜3', '20190524091130d680677ee88140d5ac9fa374480d5672htpy.mp4', '11111111111111111111111321', '201905240911308595d45d8a4e40c395216ede00ce37f61348814002177.jpg', 5, 0, 0, NULL, '杭州', '2019-05-23', '160', '2019-05-24 09:11:30');
INSERT INTO `movie` VALUES (6, '琅琊榜2', '20190524155504e78ce1b9fe24413cbc26300dff3d2a0chtpy.mp4', '4655555555555', '201905241555040db966c3541542cbae58aefaed71285c2012FD86-E209-4b89-A710-7B6EF6366F02.png', 5, 0, 0, NULL, '杭州', '2019-05-09', '160', '2019-05-24 09:13:43');
INSERT INTO `movie` VALUES (7, '变形金刚2', '201905240915557d0cee99e4944feca2aac952ce9ec3dehtpy.mp4', '65465151', '201905240915555e8c31bd0f0a4ff098b1ddf7b30cec292012FD86-E209-4b89-A710-7B6EF6366F02.png', 3, 0, 0, 4, '杭州', '2019-05-23', '160', '2019-05-24 09:15:55');

-- ----------------------------
-- Table structure for moviecol
-- ----------------------------
DROP TABLE IF EXISTS `moviecol`;
CREATE TABLE `moviecol`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `movie_id`(`movie_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_moviecol_addtime`(`addtime`) USING BTREE,
  CONSTRAINT `moviecol_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `moviecol_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of moviecol
-- ----------------------------
INSERT INTO `moviecol` VALUES (7, 1, 1, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (8, 1, 2, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (9, 1, 3, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (11, 1, 5, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (12, 1, 6, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (13, 1, 1, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (15, 1, 3, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (18, 1, 6, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (19, 1, 7, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (20, 1, 8, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (21, 1, 9, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (22, 1, 10, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (23, 1, 11, '2018-10-21 16:16:16');
INSERT INTO `moviecol` VALUES (24, 1, 12, '2018-10-21 16:16:16');

-- ----------------------------
-- Table structure for oplog
-- ----------------------------
DROP TABLE IF EXISTS `oplog`;
CREATE TABLE `oplog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_id` int(11) NULL DEFAULT NULL,
  `ip` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `reason` varchar(600) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `admin_id`(`admin_id`) USING BTREE,
  INDEX `ix_oplog_addtime`(`addtime`) USING BTREE,
  CONSTRAINT `oplog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of oplog
-- ----------------------------
INSERT INTO `oplog` VALUES (1, 3, '172.16.16.47', '添加标签经典', '2019-05-24 15:43:20');
INSERT INTO `oplog` VALUES (2, 3, '172.16.16.47', '添加标签排行榜', '2019-05-24 15:45:52');
INSERT INTO `oplog` VALUES (3, 3, '172.16.16.47', '添加标签微视频', '2019-05-24 16:03:55');
INSERT INTO `oplog` VALUES (4, 3, '172.16.16.47', '添加标签123', '2019-05-24 16:04:29');
INSERT INTO `oplog` VALUES (5, 3, '172.16.16.47', '添加标签古典', '2019-05-24 17:15:44');

-- ----------------------------
-- Table structure for preview
-- ----------------------------
DROP TABLE IF EXISTS `preview`;
CREATE TABLE `preview`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `logo` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE,
  UNIQUE INDEX `logo`(`logo`) USING BTREE,
  INDEX `ix_preview_addtime`(`addtime`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of preview
-- ----------------------------
INSERT INTO `preview` VALUES (1, '变形金刚', '201905231157499f1b700a260a47e3b3cf65ea2a4b1f561348814017665.jpg', '2019-05-23 11:57:49');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `auths` varchar(600) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `ix_role_addtime`(`addtime`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES (1, '超级管理员', '6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38', '2019-05-23 11:31:31');
INSERT INTO `role` VALUES (6, '普通管理员', '6,7,9,10,11,13,14,15,17,18,19,21,23,25,38', '2019-05-27 16:08:28');

-- ----------------------------
-- Table structure for tag
-- ----------------------------
DROP TABLE IF EXISTS `tag`;
CREATE TABLE `tag`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `ix_tag_addtime`(`addtime`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of tag
-- ----------------------------
INSERT INTO `tag` VALUES (3, '斯蒂芬', '2019-05-23 11:48:10');
INSERT INTO `tag` VALUES (4, '武侠', '2019-05-23 14:45:20');
INSERT INTO `tag` VALUES (5, '动作', '2019-05-23 14:45:28');
INSERT INTO `tag` VALUES (7, '魔幻', '2019-05-23 17:13:31');
INSERT INTO `tag` VALUES (8, '动画', '2019-05-23 17:26:54');
INSERT INTO `tag` VALUES (11, '爱情', '2019-05-23 17:50:20');
INSERT INTO `tag` VALUES (12, '卡通', '2019-05-24 10:12:03');
INSERT INTO `tag` VALUES (14, '经典', '2019-05-24 15:43:20');
INSERT INTO `tag` VALUES (15, '排行榜', '2019-05-24 15:45:52');
INSERT INTO `tag` VALUES (16, '微视频', '2019-05-24 16:03:55');
INSERT INTO `tag` VALUES (18, '古典', '2019-05-24 17:15:44');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `pwd` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `info` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `face` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  `uuid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  UNIQUE INDEX `phone`(`phone`) USING BTREE,
  UNIQUE INDEX `face`(`face`) USING BTREE,
  UNIQUE INDEX `uuid`(`uuid`) USING BTREE,
  INDEX `ix_user_addtime`(`addtime`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '逗起我', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user01.com', '12800128001', '个人简介', '01.jpg', '2018-01-23 13:01:35', 'd4d9772d0cb84f6b911a50670f55f395');
INSERT INTO `user` VALUES (2, '繁体', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user02.com', '12800128002', '个人简介', '02.jpg', '2019-04-01 13:01:45', '1fbd3079f1fb44afa7ddd9d212798d18');
INSERT INTO `user` VALUES (3, '立体', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user03.com', '12800128003', '个人简介', '03.jpg', '2019-01-06 13:01:56', '3f7f53f88d894f2cad96e8af4662322d');
INSERT INTO `user` VALUES (4, '突然变', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user04.com', '12800128004', '个人简介', '04.jpg', '2019-02-23 13:02:02', '256974f28e7a43809da96a716957921d');
INSERT INTO `user` VALUES (5, '刮胡刀', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user05.com', '12800128005', '个人简介', '05.jpg', '2018-03-05 13:02:07', '294a495e56474c1ea13962f602aed98d');
INSERT INTO `user` VALUES (6, '开机号', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user06.com', '12800128006', '个人简介', '06.jpg', '2019-05-07 13:11:29', 'd4b67132023b4f3c903c8e3e2b8e84e6');
INSERT INTO `user` VALUES (7, '萨达', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user07.com', '12800128007', '个人简介', '07.jpg', '2019-05-13 13:11:34', '7a3956518f034920a312877899afae0e');
INSERT INTO `user` VALUES (8, '认为他', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user08.com', '12800128008', '个人简介', '08.jpg', '2019-05-15 13:11:39', '1c5e5f7a4e564cffafd827c96e05bc2d');
INSERT INTO `user` VALUES (9, '话筒', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user09.com', '12800128009', '个人简介', '09.jpg', '2019-05-15 13:11:48', '1dd3276fdc8440ff92a537a00c13d07a');
INSERT INTO `user` VALUES (10, '机柜号', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user10.com', '12800128010', '个人简介', '10.jpg', '2019-05-15 13:11:42', 'b4fb51f547b8490188c5a889e26bbb06');
INSERT INTO `user` VALUES (11, '珀尔', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user11.com', '12800128011', '个人简介', '11.jpg', '2019-04-29 13:14:45', '94150271639b4e04855c365691cf3a47');
INSERT INTO `user` VALUES (12, '条纹', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user12.com', '12800128012', '个人简介', '12.jpg', '2019-03-30 13:14:49', '137b329d6e874e93b74082b2c133fad0');
INSERT INTO `user` VALUES (13, '与虎添翼', 'pbkdf2:sha256:50000$56hTmVhd$fa3c7d54ead0495e344f', 'user@user13.com', '12800128013', '个人简介', '13.jpg', '2019-02-23 13:14:55', 'c116ef9e419c447fa06991237f4ece87');

-- ----------------------------
-- Table structure for userlog
-- ----------------------------
DROP TABLE IF EXISTS `userlog`;
CREATE TABLE `userlog`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  `ip` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `addtime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `ix_userlog_addtime`(`addtime`) USING BTREE,
  CONSTRAINT `userlog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of userlog
-- ----------------------------
INSERT INTO `userlog` VALUES (1, 1, '17.6.34.8', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (2, 3, '136.25.9.168', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (3, 4, '136.25.34.6', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (4, 5, '4.25.9.168', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (5, 6, '136.25.34.9', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (6, 7, '5.25.34.7', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (7, 8, '136.25.3.7', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (8, 9, '3.6.34.168', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (9, 10, '136.25.34.1', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (10, 11, '2.25.34.168', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (11, 12, '3.25.5.6', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (12, 13, '136.25.34.7', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (13, 1, '136.77.34.168', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (14, 2, '136.25.34.211', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (15, 3, '34.55.56.32', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (16, 4, '6.25.55.87', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (17, 5, '45.25.34.7', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (18, 3, '136.25.34.8', '2018-10-21 16:16:16');
INSERT INTO `userlog` VALUES (19, 7, '136.5.34.32', '2018-10-21 16:16:16');

SET FOREIGN_KEY_CHECKS = 1;
