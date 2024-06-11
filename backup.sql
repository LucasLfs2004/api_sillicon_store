mysqldump: [Warning] Using a password on the command line interface can be insecure.
-- MySQL dump 10.13  Distrib 8.0.33, for Linux (aarch64)
--
-- Host: localhost    Database: SILLICON_STORE
-- ------------------------------------------------------
-- Server version	8.0.33

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
mysqldump: Error: 'Access denied; you need (at least one of) the PROCESS privilege(s) for this operation' when trying to dump tablespaces

--
-- Table structure for table `banner`
--

DROP TABLE IF EXISTS `banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banner` (
  `id` int NOT NULL,
  `img_banner_web` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `link` varchar(255) DEFAULT NULL,
  `active` bit(1) NOT NULL DEFAULT b'1',
  `img_banner_mobile` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banner`
--

LOCK TABLES `banner` WRITE;
/*!40000 ALTER TABLE `banner` DISABLE KEYS */;
INSERT INTO `banner` VALUES (89054760,'1712942706.639152carouselRtxWeb.png','/brand/320535756',_binary '','1712942706.639925CarouselRtx.png'),(375410623,'1714180547.7806232xbox-banner-web.png','/brand/570676007',_binary '','1714180547.782022xbox-banner-mobile.png'),(849095396,'1714180495.78243ps5-banner-web.png','/brand/222272032',_binary '','1714180509.7624378ps5-banner-mobile.png');
/*!40000 ALTER TABLE `banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `brand_logo` varchar(255) DEFAULT NULL,
  `brand_logo_black` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (222272032,'Playstation','1714086534.447819playstationLogoWhite.svg','1714086534.449085playstationLogoBlacke.svg'),(270057385,'Apple','1701967705.244529appleLogo.svg','1701967705.24575appleLogoBlack.svg'),(320535756,'Nvidia','1711118261.105237nvidiaLogoWhite.svg','1711118261.106121nvidiaLogoBlack.svg'),(418385379,'Logitech','1705363665.608329logitechLogo.svg','1705363665.6089962logitechLogoBlack.svg'),(478247585,'AMD','1701969648.097261amdLogo.svg','1701968609.433053amdLogoBlack.svg'),(570676007,'Xbox','1705363680.967099xboxLogo.svg','1705363680.967749xboxLogoBlack.svg'),(583708911,'Gigabytee','1702053523.413929gigabyteLogo.svg','1702053597.327959gigabyteLogoBlack.svg'),(712377020,'Samsung','1712435909.4934149samsungLogoWhite.svg','1712435909.494536samsungLogoBlack.svg'),(859051422,'Asus','1705363642.068414asusLogo.svg','1705363642.069669asusLogoBlack.svg'),(876444037,'Zotac','1712845079.1939662zotacLogo.svg','1712845079.1957362zotacLogoBlack.svg'),(937577720,'Acer','1718125025.541983acer-white.svg','1718125025.543534acer-black.svg');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `delete_products_before_delete_in_brand` BEFORE DELETE ON `brand` FOR EACH ROW BEGIN 
	-- Atualiza o valor_total na tabela cart_user
	DELETE FROM `PRODUCT` WHERE product.brand_id = OLD.id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `cart_items`
--

DROP TABLE IF EXISTS `cart_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_items` (
  `id` varchar(255) NOT NULL,
  `id_person` varchar(255) DEFAULT NULL,
  `id_product` varchar(255) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_person` (`id_person`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `cart_items_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id`),
  CONSTRAINT `cart_items_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_items`
--

LOCK TABLES `cart_items` WRITE;
/*!40000 ALTER TABLE `cart_items` DISABLE KEYS */;
INSERT INTO `cart_items` VALUES ('1419969116','7f652081-2d3a-4e27-b81e-b988a34a5ae7','1197754295',1),('1779982008','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','1433408084',1),('2354188167','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','1738295407',1);
/*!40000 ALTER TABLE `cart_items` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `update_cart_user_after_insert` AFTER INSERT ON `cart_items` FOR EACH ROW BEGIN 
	-- Atualiza o valor_total na tabela cart_user
	UPDATE cart_user cu
	SET
	    cu.discount = (
	        select IFNULL(discount, 0)
	        from discount_list
	        WHERE
	            discount_list.code = cu.voucher
	    ),
	    cu.product_total_value = IFNULL((
	        SELECT SUM(
	                COALESCE(value_product.price_now, value_product.common_price) * cart_items.amount
	            )
	        FROM value_product
	            INNER JOIN cart_items ON value_product.id_product = cart_items.id_product
	        WHERE
	            cart_items.id_person = cu.id_person
	    ), 0),
	    cu.portions = IFNULL((
	        SELECT MIN(value_product.portions)
	        FROM value_product
	            INNER JOIN cart_items ON value_product.id_product = cart_items.id_product
	        WHERE
	            cart_items.id_person = cu.id_person
	    ),0),
	    cu.discount_value = IFNULL(
	        CASE
	            WHEN cu.discount < 1 THEN (
	                cu.product_total_value * cu.discount
	            )
	            ELSE (
	                cu.product_total_value - cu.discount
	            )
	        END, 0
	    ),
	    cu.cart_total_value = IFNULL(
	        cu.product_total_value - IFNULL(cu.discount_value, 0) + IFNULL(cu.ship_value, 0)
	    , 0)
	WHERE
	    cu.id_person = NEW.id_person;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `update_cart_user_after_update` AFTER UPDATE ON `cart_items` FOR EACH ROW BEGIN 
	-- Atualiza o valor_total na tabela cart_user
	UPDATE cart_user cu
	SET
	    cu.discount = (
	        select IFNULL(discount, 0)
	        from discount_list
	        WHERE
	            discount_list.code = cu.voucher
	    ),
	    cu.product_total_value = IFNULL((
	        SELECT SUM(
	                COALESCE(value_product.price_now, value_product.common_price) * cart_items.amount
	            )
	        FROM value_product
	            INNER JOIN cart_items ON value_product.id_product = cart_items.id_product
	        WHERE
	            cart_items.id_person = cu.id_person
	    ), 0),
	    cu.portions = IFNULL((
	        SELECT MIN(value_product.portions)
	        FROM value_product
	            INNER JOIN cart_items ON value_product.id_product = cart_items.id_product
	        WHERE
	            cart_items.id_person = cu.id_person
	    ), 0),
	    cu.discount_value = IFNULL(
	        CASE
	            WHEN cu.discount < 1 THEN (
	                cu.product_total_value * cu.discount
	            )
	            ELSE (
	                cu.product_total_value - cu.discount
	            )
	        END, 0
	    ),
	    cu.cart_total_value = IFNULL(
	        cu.product_total_value - IFNULL(cu.discount_value, 0) + IFNULL(cu.ship_value, 0)
	    ,0)
	WHERE
	    cu.id_person = OLD.id_person;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `update_cart_user_after_delete` AFTER DELETE ON `cart_items` FOR EACH ROW BEGIN 
	-- Atualiza o valor_total na tabela cart_user
	UPDATE cart_user cu
	SET
	    cu.discount = (
	        select IFNULL(discount, 0)
	        from discount_list
	        WHERE
	            discount_list.code = cu.voucher
	    ),
	    cu.product_total_value = IFNULL((
	        SELECT SUM(
	                COALESCE(value_product.price_now, value_product.common_price) * cart_items.amount
	            )
	        FROM value_product
	            INNER JOIN cart_items ON value_product.id_product = cart_items.id_product
	        WHERE
	            cart_items.id_person = cu.id_person
	    ), 0),
	    cu.portions = IFNULL((
	        SELECT MIN(value_product.portions)
	        FROM value_product
	            INNER JOIN cart_items ON value_product.id_product = cart_items.id_product
	        WHERE
	            cart_items.id_person = cu.id_person
	    ), 0),
	    cu.discount_value = IFNULL(
	        CASE
	            WHEN cu.discount < 1 THEN (
	                cu.product_total_value * cu.discount
	            )
	            ELSE (
	                cu.product_total_value - cu.discount
	            )
	        END, 0
	    ),
	    cu.cart_total_value = IFNULL(
	        cu.product_total_value - IFNULL(cu.discount_value, 0) + IFNULL(cu.ship_value, 0)
	    ,0)
	WHERE
	    cu.id_person = OLD.id_person;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `cart_user`
--

DROP TABLE IF EXISTS `cart_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_user` (
  `id_person` varchar(255) NOT NULL,
  `discount` double DEFAULT '0',
  `discount_value` double DEFAULT '0',
  `product_total_value` double NOT NULL DEFAULT '0',
  `voucher` varchar(255) DEFAULT NULL,
  `portions` int DEFAULT '0',
  `ship_value` double DEFAULT '0',
  `cart_total_value` double NOT NULL DEFAULT '0',
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ship_cep` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `ship_street` varchar(100) DEFAULT NULL,
  `ship_deadline` int DEFAULT NULL,
  `ship_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_person`),
  KEY `voucher` (`voucher`),
  CONSTRAINT `cart_user_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id`),
  CONSTRAINT `cart_user_ibfk_2` FOREIGN KEY (`voucher`) REFERENCES `discount_list` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_user`
--

LOCK TABLES `cart_user` WRITE;
/*!40000 ALTER TABLE `cart_user` DISABLE KEYS */;
INSERT INTO `cart_user` VALUES ('7f652081-2d3a-4e27-b81e-b988a34a5ae7',NULL,0,5999,NULL,10,0,5999,'2024-05-21 20:17:13','04843-030','Rua Nicolau Paganini - Parque Brasil',3,NULL),('88c9a90d-4eb0-4908-a128-bb33f0085e2a',0,0,0,NULL,0,0,0,'2024-02-05 14:23:06',NULL,NULL,NULL,NULL),('b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',NULL,0,21699.98,NULL,12,0,21699.98,'2024-06-11 14:45:28','04843-060','Rua Vicente do Rego Monteiro - Parque Brasil',3,NULL);
/*!40000 ALTER TABLE `cart_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `path_img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (144885085,'Smartphone',NULL),(206162907,'Smartwatch',NULL),(253562178,'Processador',NULL),(455143761,'Desktop',NULL),(479191233,'Tablet',NULL),(480423886,'Placa de Vídeo',NULL),(773985694,'Videogame',NULL),(795519762,'Notebook',NULL),(1066042836,'Periféricos',NULL);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `delete_products_before_delete_in_category` BEFORE DELETE ON `category` FOR EACH ROW BEGIN 
	-- Atualiza o valor_total na tabela cart_user
	DELETE FROM `PRODUCT` WHERE product.category_id = OLD.id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id_comment` varchar(255) NOT NULL,
  `id_product` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `comment_text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `title_text` varchar(255) NOT NULL,
  `rating_value` double NOT NULL,
  `id_order_item` varchar(255) NOT NULL,
  PRIMARY KEY (`id_comment`),
  KEY `id_product` (`id_product`),
  KEY `id_order_item` (`id_order_item`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `PRODUCT` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`id_order_item`) REFERENCES `order_item` (`id_order_item`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES ('1297754295','1197754295','Excelente produto, atendeu todas as minhas expectativas','2024-02-19 14:46:54','Amei!',4.5,'b7e6d8c1-bda9-4cb3-a954-9e38f4d25efm'),('1397754295','1197754295','O produto é de qualidade Apple, fnciona muito bem, a câmera é incrível e consigo tirar ótimas fotos com ele, a bateria poderia durar um pouco mais, mas acho que é por causa do tamanho do celular ','2024-02-23 11:38:46','Celular Excelente',5,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25ubg'),('2bf8b4e3-bf4d-45b7-9d66-95dc0c0fda67','1738295407','','2024-06-11 13:58:58','Ótimo',4.5,'3934303884'),('4014fd08-1659-472c-a28f-fb1aad488caa','1197754295','','2024-06-11 14:17:53','Adorei esse celular',5,'1284248364'),('55cb232b-5aa6-4fc1-bfdd-5b80c097485b','1197754295','Amei o celular, melhor celular que poderia ter comprado, amo as fotos e o sistema operacional.','2024-06-11 13:39:24','Excelente!',5,'1189945183'),('5faa0965-1829-412b-a9c2-11c19dff3f1e','1433408084','Uma das melhores placas pelo preço que custa','2024-06-11 14:21:48','Ótimo custo benefício',4.5,'1665410681'),('70ccfc96-bf87-4c19-9e0d-df70bcadd398','184972226','Controle mais lindo que já tive, e ótimo em ergonomia\n','2024-06-11 14:23:03','Controle perfeito!',5,'368222797'),('ad98574d-73d1-48a5-8ece-0514f9db33c9','1301611670','Processador muito potente, consigo editar meus vídeos sem dificuldade nenhuma, amei!','2024-06-11 13:58:38','Melhor notebook que já tive',5,'2966531467'),('f0b1abe7-59fd-48ab-a6d5-5776d917bfe3','3592125269','Tinha um Series S e comprei esse, console maravilhoso, gosto demais do design e do poder que oferece nos jogos.','2024-06-11 14:22:40','Xbox é Xbox',5,'1158804371');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `AFTER_INSERT_COMMENT` AFTER INSERT ON `comment` FOR EACH ROW BEGIN 
	-- ATUALIZAR A TABELA RATING PARA REFLETIR O NOVO COMENTÁRIO
	-- Atualizar a tabela rating para refletir o novo comentário
	UPDATE rating
	SET
	    amount = amount + 1,
		rating = ROUND((rating * (amount - 1) + NEW.rating_value)/amount, 1)
	WHERE
	    id_product = NEW.id_product;
	-- Certificar-se de atualizar apenas para o produto específico
	-- Se não houver uma entrada de rating para o produto, criar uma nova
	IF ROW_COUNT() = 0 THEN
	INSERT INTO
	    rating (id_product, amount, rating)
	VALUES (
	        NEW.id_product, 1, NEW.rating_value
	    );
END
	IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `after_delete_comment` AFTER DELETE ON `comment` FOR EACH ROW BEGIN
    DECLARE current_amount INT;
    DECLARE current_rating DECIMAL(5, 2);
    SELECT amount, rating
    INTO current_amount, current_rating
    FROM rating
    WHERE id_product = OLD.id_product;
    SET current_amount = current_amount - 1;
    IF current_amount > 0 THEN
        SET current_rating = (current_rating * (current_amount + 1) - OLD.rating_value) / current_amount;
    ELSE
        
        SET current_rating = 0;
    END IF;
    UPDATE rating
    SET amount = current_amount,
        rating = current_rating
    WHERE id_product = OLD.id_product;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `description_product`
--

DROP TABLE IF EXISTS `description_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `description_product` (
  `id_description` varchar(255) NOT NULL,
  `description_html` text,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `id_product` varchar(255) NOT NULL,
  PRIMARY KEY (`id_description`),
  UNIQUE KEY `id_product` (`id_product`),
  CONSTRAINT `description_product_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `PRODUCT` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `description_product`
--

LOCK TABLES `description_product` WRITE;
/*!40000 ALTER TABLE `description_product` DISABLE KEYS */;
INSERT INTO `description_product` VALUES ('1074196961','<h2>ROG Strix GeForce RTX 4090 24GB GDDR6X White OC Edition com DLSS 3 e desempenho térmico no topo das paradas</h2><p>&nbsp;</p><h3>Principais Recursos</h3><p>&nbsp;</p><p><strong>Multiprocessadores NVIDIA Ada Lovelace Streaming:</strong>&nbsp;até 2x desempenho e eficiência de energia.</p><p>&nbsp;</p><p><strong>Núcleos tensores de 4ª geração:</strong>&nbsp;desempenho de até 4x com DLSS 3 versus renderização de força bruta.</p><p>&nbsp;</p><p><strong>Núcleos RT de 3ª geração:</strong>&nbsp;desempenho de rastreamento de raio até 2X.</p><p>&nbsp;</p><p><strong>Modo OC:</strong>&nbsp;2640 MHz (modo OC) / 2610 MHz (modo padrão).</p><p>&nbsp;</p><p>Ventiladores de&nbsp;<strong>tecnologia axial ampliados para 23%</strong>&nbsp;mais fluxo de ar.</p><p>&nbsp;</p><p>Nova câmara de vapor patenteada com dissipador de calor fresado para temperaturas de GPU mais baixas.</p><p>&nbsp;</p><p><strong>Design de 3,5 slots:</strong>&nbsp;enorme conjunto de aletas otimizado para fluxo de ar dos três ventiladores Axial-tech.</p><p>&nbsp;</p><p>A&nbsp;<strong>cobertura, a estrutura e a placa traseira fundidas</strong>&nbsp;adicionam rigidez e são ventiladas para maximizar ainda mais o fluxo de ar e a dissipação de calor.</p><p>&nbsp;</p><p>Controle de energia digital com estágios de energia de alta corrente e&nbsp;<strong>capacitores de 15K</strong>&nbsp;para alimentar o desempenho máximo.</p><p>&nbsp;</p><p><strong>Fabricação automatizada de precisão:</strong>&nbsp;Auto-Extreme para maior confiabilidade.</p><p>&nbsp;</p><p>O software GPU Tweak III: oferece ajustes de desempenho intuitivos, controles térmicos e monitoramento do sistema.</p><p>&nbsp;</p><h3>COM A INCRÍVEL SOMA DE SUAS PARTES</h3><p>&nbsp;</p><p>A ROG Strix GeForce RTX 4080 traz um novo significado para acompanhar o fluxo. Por dentro e por fora, cada elemento da placa dá à monstruosa margem de manobra da GPU para respirar livremente e alcançar o máximo desempenho. O reinado desencadeado da arquitetura NVIDIA ADA Lovelace está aqui.</p><p>&nbsp;</p><h3>Atualizações de tecnologia axial - Uma Volta Nova</h3><p>&nbsp;</p><p>Maior e melhor. Os ventiladores Axial-tech giram em rolamentos de esferas duplas e foram dimensionados para impulsionar 23% mais ar através do cartão, preparando o cenário para temperaturas mais baixas, menos ruído e maior desempenho.</p><p>&nbsp;</p><h3>Rotação reversa e tecnologia 0dB - Relaxamento orquestrado</h3><p>&nbsp;</p><p>Os dois ventiladores laterais giram no sentido anti-horário para minimizar a turbulência e maximizar a dispersão do ar pelo dissipador de calor. Todos os três ventiladores param quando as temperaturas da GPU estão abaixo de 50 graus Celsius, permitindo que você jogue jogos menos exigentes ou execute tarefas leves em relativo silêncio.</p><p>&nbsp;</p><p>Os ventiladores ligam novamente quando as temperaturas estão acima de 55 C, referenciando uma curva de velocidade que equilibra desempenho e acústica para trabalho ou lazer.</p>','2024-06-11 17:25:29','2022549509'),('1227785245','<h2>Processador AMD Ryzen 3 3200G</h2><p>&nbsp;</p><h2>O Poder de Jogar Totalmente Desbloqueado</h2><p>A capacidade de resposta e desempenho que você esperaria de um PC muito mais caro.</p><p>&nbsp;</p><p>A&nbsp;<strong>arquitetura Zen 2</strong>&nbsp;do núcleo de<strong>&nbsp;alto desempenho</strong>&nbsp;da AMD permite que os Processadores de 2ª geração Ryzen ofereçam o mais alto desempenho para uma ou múltiplas linhas de execução e de qualquer Processador de desktop convencional.</p>','2024-06-11 17:33:38','1474542769'),('1379956576','<h2>Mac Studio - CPU de 24 núcleos</h2><p>&nbsp;</p><h2>Design</h2><p>O chip da Apple permitiu a criação de um desktop&nbsp;<strong>poderoso</strong>&nbsp;como nenhum outro. Com seu design compacto, o Mac Studio cabe embaixo da maioria dos monitores e transforma qualquer ambiente de trabalho em um estúdio.</p><p>&nbsp;</p><h2>Conectividade</h2><p>O Mac Studio vem com um conjunto versátil de&nbsp;<strong>12 portas</strong>&nbsp;compatíveis com leitor de cartão SDXC, uma saída HDMI aprimorada,&nbsp;<strong>Wi-Fi 6E</strong>&nbsp;Consultar avisos legais e&nbsp;<strong>Bluetooth 5.3.</strong></p><p>&nbsp;</p><h2>Otimizados para os chips da Apple</h2><p>Poderoso,&nbsp;<strong>intuitivo e confiável</strong>, o macOS foi desenvolvido para acompanhar as possibilidades do chip da Apple. E, com milhares de apps otimizados para aproveitar ao máximo o M2 Max e o M2 Ultra, você pode trabalhar, criar e se divertir como nunca.</p><p>&nbsp;</p><h3>Compre agora no KaBuM!</h3><h2><br></h2><h2>INFORMAÇÕES TÉCNICAS</h2><p><br></p><p><strong>Características:</strong></p><p>- Marca: Mac Studio</p><p>- Modelo: MQH63BZ/A</p><p>&nbsp;</p><p><strong>Especificações:</strong></p><p>&nbsp;</p><p><strong>Geral:</strong></p><p>- Chip M2 Ultra para desempenho fenomenal&nbsp;</p><p>- CPU de 24 núcleos com desempenho até 3,3x mais veloz que o iMac de 27 polegadas, para expandir as possibilidades dos fluxos de trabalho mais exigentes*&nbsp;</p><p>- GPU de até 76 núcleos com desempenho até 6,1x mais veloz que o iMac de 27 polegadas, para os fluxos de trabalho profissionais com gráficos pesados**&nbsp;</p><p>- Neural Engine de 32 núcleos para tarefas de aprendizado de máquina avançado&nbsp;</p><p>- Memória unificada de até 192GB para usar vários apps profissionais ao mesmo tempo&nbsp;</p><p>- Até 8TB de armazenamento SSD ultrarrápido para abrir apps e arquivos num instante***&nbsp;</p><p>- Conexão sem fio Wi-Fi 6 E rápida****&nbsp;</p><p>- Seis portas Thunderbolt 4, duas portas USB-A, porta HDMI, Ethernet de 10Gb, slot para cartão SDXC e entrada para fones de ouvido&nbsp;</p><p>- Suporte para até oito monitores&nbsp;</p><p>- Design compacto em prateado com laterais de 19,7cm e altura de 9,5cm&nbsp;</p><p>- macOS Ventura, que traz novas maneiras de trabalhar, compartilhar e colaborar e funciona perfeitamente com o iPhone e o iPad*****&nbsp;</p><p>&nbsp;</p><p><strong>Áudio:</strong></p><p>- Alto-falante integrado&nbsp;</p><p>- Entrada para fones de ouvido de 3,5 mm e compatibilidade avançada com fones de ouvido de alta impedância&nbsp;</p><p>- Porta HDMI compatível com saída de áudio multicanal&nbsp;&nbsp;</p><p>- Portas&nbsp;&nbsp;&nbsp;</p><p>- Quatro portas Thunderbolt 4 com suporte para:&nbsp;</p><p>- Thunderbolt 4 (até 40 Gb/s)&nbsp;</p><p>- DisplayPort&nbsp;</p><p>- USB 4 (até 40 Gb/s)&nbsp;</p><p>- USB 3.1 Gen 2 (até 10 Gb/s)&nbsp;</p><p>- Duas portas USB‑A (até 5 Gb/s)&nbsp;</p><p>- Porta HDMI&nbsp;</p><p>- Ethernet de 10 Gb&nbsp;</p><p>- Entrada para fones de ouvido de 3,5 mm&nbsp;</p><p>- Na frente (M2 Ultra):&nbsp;&nbsp;</p><p>- Duas portas Thunderbolt 4 (até 40 Gb/s)&nbsp;</p><p>- Slot para cartão SDXC (UHS‑II)&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p><strong>Rede:&nbsp;&nbsp;&nbsp;</strong></p><p>- Wi-Fi 6E (802.11ax)&nbsp;</p><p>- Bluetooth 5.3&nbsp;</p><p>- Ethernet&nbsp;</p><p>- Ethernet de 10 Gb (Ethernet Nbase-T compatível com Ethernet de 1 Gb, 2,5 Gb, 5 Gb e 10 Gb usando um conector RJ‑45)&nbsp;</p><p>&nbsp;</p><p><strong>Requisitos elétricos e operacionais:&nbsp;&nbsp;</strong></p><p>- Voltagem: 100–240 VCA&nbsp;</p><p>- Frequência: 50–60 Hz, monofase&nbsp;</p><p>- Potência contínua máxima: 370W&nbsp;</p><p>- Temperatura operacional: 10 ºC a 35 ºC&nbsp;</p><p>- Temperatura de armazenamento:-40 ºC a 47 ºC&nbsp;</p><p>- Umidade relativa: 5% a 95%, sem condensação&nbsp;</p><p>- Altitude operacional: testado até 5.000m&nbsp;</p><p>&nbsp;</p><p><strong>Softwares:&nbsp;&nbsp;&nbsp;</strong></p><p>- MacOS&nbsp;&nbsp;&nbsp;</p><p>&nbsp;</p><p><strong>Apps incluídos:&nbsp;&nbsp;</strong></p><p>- App Store&nbsp;</p><p>- Atalhos&nbsp;</p><p>- Bolsa&nbsp;</p><p>- Buscar&nbsp;</p><p>- Calendário&nbsp;</p><p>- Casa&nbsp;</p><p>- Contatos&nbsp;</p><p>- FaceTime&nbsp;</p><p>- Fotos&nbsp;</p><p>- Freeform&nbsp;</p><p>- GarageBand&nbsp;</p><p>- Gravador&nbsp;</p><p>- iMovie&nbsp;</p><p>- Keynote&nbsp;</p><p>- Lembretes&nbsp;</p><p>- Livros&nbsp;</p><p>- Mail&nbsp;</p><p>- Mapas&nbsp;</p><p>- Mensagens&nbsp;</p><p>- Música&nbsp;</p><p>- Notas&nbsp;</p><p>- Numbers&nbsp;</p><p>- Pages&nbsp;</p><p>- Photo Booth&nbsp;</p><p>- Podcasts&nbsp;</p><p>- Pré-Visualização&nbsp;</p><p>- QuickTime Player&nbsp;</p><p>- Safari&nbsp;</p><p>- Siri&nbsp;</p><p>- Time Machine&nbsp;</p><p>- TV&nbsp;</p><p>&nbsp;</p><p><strong>Conteúdo da Embalagem:</strong></p><p>- Mac Studio&nbsp;</p><p>- Cabo de alimentação&nbsp;</p><p><br></p><h3>Garantia:</h3><p>12 meses de garantia</p><h3>Peso:</h3><p>6280 gramas (bruto com embalagem)</p>','2024-06-11 15:03:02','1974991426'),('1400021259','<h2 class=\"ql-align-justify\">Notebook Gamer ASUS Tuf Intel Core i7 12700H</h2><p class=\"ql-align-justify\">&nbsp;</p><p class=\"ql-align-justify\">Conheça a nova linha de notebooks gamer TUF Gaming, da ASUS, feita para aqueles que buscam performance em jogos competitivos e querem vencer todos os desafios do dia a dia. Preparado para qualquer campo de batalha, o novo ASUS TUF Gaming F15 supera os limites, seja jogando, fazendo livestreams ou em qualquer outra atividade. Graças ao poderoso&nbsp;<strong>processador Intel Core i7-12700H</strong>&nbsp;com&nbsp;<strong>14 núcleos</strong>, até as tarefas mais complicadas ficam simples.&nbsp;</p><p class=\"ql-align-justify\">Para que a sua gameplay seja excelente, este notebook vem equipado com a<strong>&nbsp;placa de vídeo NVIDIA GeForce RTX 3050</strong>, que habilita todas as tecnologias baseadas em Inteligência Artificial desenvolvidos pela NVIDIA, como<strong>&nbsp;Ray Tracing</strong>,&nbsp;<strong>DLSS</strong>&nbsp;e muitas outras. Trabalhando com uma potência gráfica (TGP) de&nbsp;<strong>95 W</strong>, você terá muito&nbsp;<strong>mais FPS</strong>&nbsp;que seus oponentes.</p><p><br></p>','2024-06-11 17:12:13','2378042936'),('1538452261','<h2>Crie mais rápido:</h2><p>O ASUS Vivobook 16X é o notebook perfeito para quem precisa de&nbsp;<strong>desempenho de alto nível</strong>. Com o processador Intel Core Série H da 12ª geração e a placa de vídeo NVIDIA GeForce RTX 2050, você pode criar, editar e jogar com facilidade.</p><p>O armazenamento SSD de&nbsp;<strong>512 GB</strong>, a memória&nbsp;<strong>DDR4</strong>&nbsp;de&nbsp;<strong>até 16 GB</strong>&nbsp;e o&nbsp;<strong>Wi-Fi 6E5</strong>&nbsp;ultrarrápido garantem que você tenha espaço, velocidade e conectividade para fazer tudo o que precisa. Com o ASUS Vivobook 16X, você pode transformar suas ideias em realidade.</p><p>&nbsp;</p><h2>Tenha um processador poderoso:</h2><p>O processador Intel Core i5-12450H de 12ª geração oferece desempenho de alto nível para usuários que precisam lidar com projetos exigentes. Com<strong>&nbsp;8 núcleos e 12 threads</strong>, ele pode lidar com vários aplicativos e tarefas simultaneamente sem problemas.</p><p>O&nbsp;<strong>Modo Performance</strong>&nbsp;oferece um aumento de velocidade adicional para tarefas que precisam de um desempenho máximo. Ele aumenta a potência da CPU para um pico de&nbsp;<strong>50 W</strong>, o que pode ser útil para jogos, edição de vídeo e outros aplicativos que exigem muita potência.</p><p>&nbsp;</p><h2>Seu companheiro criativo:</h2><p>O notebook perfeito para quem quer começar a carreira criativa ou se aventurar no mundo dos games. Com a placa de vídeo&nbsp;<strong>NVIDIA GeForce RTX 2050</strong>, você pode criar, editar e jogar com facilidade.</p><p>&nbsp;</p><h2>Uma tela incrível:</h2><p>O ASUS Vivobook 16X traz uma experiência impressionante cheia de detalhes, graças à sua tela&nbsp;<strong>NanoEdge de 16 polegadas</strong>&nbsp;WUXGA de nível IPS e até&nbsp;<strong>120 Hz1</strong>, com proporção&nbsp;<strong>16:10</strong>&nbsp;capaz de oferecer mais espaço de visualização.</p>','2024-06-11 17:15:48','2650605247'),('1594725867','<h2>Mac Studio - CPU de 24 núcleos</h2><p>&nbsp;</p><h2>Design</h2><p>O chip da Apple permitiu a criação de um desktop&nbsp;<strong>poderoso</strong>&nbsp;como nenhum outro. Com seu design compacto, o Mac Studio cabe embaixo da maioria dos monitores e transforma qualquer ambiente de trabalho em um estúdio.</p><p>&nbsp;</p><h2>Conectividade</h2><p>O Mac Studio vem com um conjunto versátil de&nbsp;<strong>12 portas</strong>&nbsp;compatíveis com leitor de cartão SDXC, uma saída HDMI aprimorada,&nbsp;<strong>Wi-Fi 6E</strong>&nbsp;Consultar avisos legais e&nbsp;<strong>Bluetooth 5.3.</strong></p><p>&nbsp;</p><h2>Otimizados para os chips da Apple</h2><p>Poderoso,&nbsp;<strong>intuitivo e confiável</strong>, o macOS foi desenvolvido para acompanhar as possibilidades do chip da Apple. E, com milhares de apps otimizados para aproveitar ao máximo o M2 Max e o M2 Ultra, você pode trabalhar, criar e se divertir como nunca.</p><p>&nbsp;</p><h3>Compre agora no KaBuM!</h3><h2><br></h2><h2>INFORMAÇÕES TÉCNICAS</h2><p><br></p><p><strong>Características:</strong></p><p>- Marca: Mac Studio</p><p>- Modelo: MQH63BZ/A</p><p>&nbsp;</p><p><strong>Especificações:</strong></p><p>&nbsp;</p><p><strong>Geral:</strong></p><p>- Chip M2 Ultra para desempenho fenomenal&nbsp;</p><p>- CPU de 24 núcleos com desempenho até 3,3x mais veloz que o iMac de 27 polegadas, para expandir as possibilidades dos fluxos de trabalho mais exigentes*&nbsp;</p><p>- GPU de até 76 núcleos com desempenho até 6,1x mais veloz que o iMac de 27 polegadas, para os fluxos de trabalho profissionais com gráficos pesados**&nbsp;</p><p>- Neural Engine de 32 núcleos para tarefas de aprendizado de máquina avançado&nbsp;</p><p>- Memória unificada de até 192GB para usar vários apps profissionais ao mesmo tempo&nbsp;</p><p>- Até 8TB de armazenamento SSD ultrarrápido para abrir apps e arquivos num instante***&nbsp;</p><p>- Conexão sem fio Wi-Fi 6 E rápida****&nbsp;</p><p>- Seis portas Thunderbolt 4, duas portas USB-A, porta HDMI, Ethernet de 10Gb, slot para cartão SDXC e entrada para fones de ouvido&nbsp;</p><p>- Suporte para até oito monitores&nbsp;</p><p>- Design compacto em prateado com laterais de 19,7cm e altura de 9,5cm&nbsp;</p><p>- macOS Ventura, que traz novas maneiras de trabalhar, compartilhar e colaborar e funciona perfeitamente com o iPhone e o iPad*****&nbsp;</p><p>&nbsp;</p><p><strong>Áudio:</strong></p><p>- Alto-falante integrado&nbsp;</p><p>- Entrada para fones de ouvido de 3,5 mm e compatibilidade avançada com fones de ouvido de alta impedância&nbsp;</p><p>- Porta HDMI compatível com saída de áudio multicanal&nbsp;&nbsp;</p><p>- Portas&nbsp;&nbsp;&nbsp;</p><p>- Quatro portas Thunderbolt 4 com suporte para:&nbsp;</p><p>- Thunderbolt 4 (até 40 Gb/s)&nbsp;</p><p>- DisplayPort&nbsp;</p><p>- USB 4 (até 40 Gb/s)&nbsp;</p><p>- USB 3.1 Gen 2 (até 10 Gb/s)&nbsp;</p><p>- Duas portas USB‑A (até 5 Gb/s)&nbsp;</p><p>- Porta HDMI&nbsp;</p><p>- Ethernet de 10 Gb&nbsp;</p><p>- Entrada para fones de ouvido de 3,5 mm&nbsp;</p><p>- Na frente (M2 Ultra):&nbsp;&nbsp;</p><p>- Duas portas Thunderbolt 4 (até 40 Gb/s)&nbsp;</p><p>- Slot para cartão SDXC (UHS‑II)&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p><strong>Rede:&nbsp;&nbsp;&nbsp;</strong></p><p>- Wi-Fi 6E (802.11ax)&nbsp;</p><p>- Bluetooth 5.3&nbsp;</p><p>- Ethernet&nbsp;</p><p>- Ethernet de 10 Gb (Ethernet Nbase-T compatível com Ethernet de 1 Gb, 2,5 Gb, 5 Gb e 10 Gb usando um conector RJ‑45)&nbsp;</p><p>&nbsp;</p><p><strong>Requisitos elétricos e operacionais:&nbsp;&nbsp;</strong></p><p>- Voltagem: 100–240 VCA&nbsp;</p><p>- Frequência: 50–60 Hz, monofase&nbsp;</p><p>- Potência contínua máxima: 370W&nbsp;</p><p>- Temperatura operacional: 10 ºC a 35 ºC&nbsp;</p><p>- Temperatura de armazenamento:-40 ºC a 47 ºC&nbsp;</p><p>- Umidade relativa: 5% a 95%, sem condensação&nbsp;</p><p>- Altitude operacional: testado até 5.000m&nbsp;</p><p>&nbsp;</p><p><strong>Softwares:&nbsp;&nbsp;&nbsp;</strong></p><p>- MacOS&nbsp;&nbsp;&nbsp;</p><p>&nbsp;</p><p><strong>Apps incluídos:&nbsp;&nbsp;</strong></p><p>- App Store&nbsp;</p><p>- Atalhos&nbsp;</p><p>- Bolsa&nbsp;</p><p>- Buscar&nbsp;</p><p>- Calendário&nbsp;</p><p>- Casa&nbsp;</p><p>- Contatos&nbsp;</p><p>- FaceTime&nbsp;</p><p>- Fotos&nbsp;</p><p>- Freeform&nbsp;</p><p>- GarageBand&nbsp;</p><p>- Gravador&nbsp;</p><p>- iMovie&nbsp;</p><p>- Keynote&nbsp;</p><p>- Lembretes&nbsp;</p><p>- Livros&nbsp;</p><p>- Mail&nbsp;</p><p>- Mapas&nbsp;</p><p>- Mensagens&nbsp;</p><p>- Música&nbsp;</p><p>- Notas&nbsp;</p><p>- Numbers&nbsp;</p><p>- Pages&nbsp;</p><p>- Photo Booth&nbsp;</p><p>- Podcasts&nbsp;</p><p>- Pré-Visualização&nbsp;</p><p>- QuickTime Player&nbsp;</p><p>- Safari&nbsp;</p><p>- Siri&nbsp;</p><p>- Time Machine&nbsp;</p><p>- TV&nbsp;</p><p>&nbsp;</p><p><strong>Conteúdo da Embalagem:</strong></p><p>- Mac Studio&nbsp;</p><p>- Cabo de alimentação&nbsp;</p><p><br></p><h3>Garantia:</h3><p>12 meses de garantia</p><h3>Peso:</h3><p>6280 gramas (bruto com embalagem)</p>','2024-06-11 15:04:21','1994704223'),('1769516489','<h2>Teclado Sem Fio Logitech MX Keys S</h2><p>&nbsp;</p><p>Experimente um novo nível de desempenho com o MX Keys S. O MX Keys S é um teclado de<strong>&nbsp;alto desempenho</strong>, projetado para&nbsp;<strong>digitação confortável</strong>, rápida e fluida.</p><p>Agora seu teclado conta com&nbsp;<strong>iluminação</strong>&nbsp;ainda mais inteligente, as teclas de luz de fundo acendem quando suas mãos se aproximam do teclado e automaticamente se iluminam ou se apagam para se adequar ao seu ambiente. Com o&nbsp;<strong>software Logi Option+</strong>&nbsp;você pode configurar a duração e intensidade das luzes do seu MX Keys S.</p><p>Uma tecla, é tudo o que você precisa para automatizar suas tarefas repetitivas com o Smart Action, função disponível no software Logi Option+, idealizada para facilitar sua vida e aumentar sua produtividade.</p><p>&nbsp;</p><h2>Design Discreto e o Ângulo Ideal</h2><p>Para uma posição mais natural do pulso proporcionam precisão sem esforço e mais horas de conforto na digitação. O MX Keys S traz carregamento rápido via USB-C que permite uma autonomia de bateria de até 10 dias com uma carga completa e até 5 meses com a luz de fundo desativada*. Você pode carregá-lo enquanto trabalha, sem problemas.</p><p>&nbsp;</p><h2>Ampla Conectividade</h2><p>Alterne facilmente entre&nbsp;<strong>até 3 dispositivos</strong>&nbsp;com apenas um botão. Além disso, o MX Keys S traz dupla conectividade:&nbsp;<strong>Bluetooth</strong>&nbsp;e&nbsp;<strong>Receptor USB</strong>&nbsp;Logi Bolt (incluso), escolha a maneira de conexão que mais combina com seu estilo e comece o trabalho.</p>','2024-06-11 16:43:13','2178406116'),('1849844609','<h2>Notebook Acer Nitro V15</h2><p>&nbsp;</p><h2>Ação do Começo ao Fim</h2><p>O Nitro V15 conta com a placa de vídeo<strong>&nbsp;NVIDIA GeForce RTX 3050</strong>&nbsp;com&nbsp;<strong>6 GB</strong>&nbsp;de memória dedicada&nbsp;<strong>GDDR6</strong>&nbsp;com eficiência total (TGP) de&nbsp;<strong>até 80W</strong>&nbsp;que oferece o melhor desempenho para você aproveitar ao máximo suas horas de jogatina.</p><p>&nbsp;</p><h2>Processador Que Faz Os Adversários Tremerem</h2><p>Nada pode te parar com o&nbsp;<strong>Intel Core i5-13420H de 13ª geração</strong>&nbsp;deste notebook. Juntamente com&nbsp;<strong>8 GB de memória RAM</strong>, expansível&nbsp;<strong>até 32 GB</strong>, o processador te leva aos níveis mais avançados de games e criação de conteúdo.</p><p>&nbsp;</p><h2>Veloz e Furioso</h2><p>O nitro V15 entrega&nbsp;<strong>imagens vívidas e fluídas</strong>, que permitem uma jogabilidade mais rápida. Tudo isso, devido a sua tela de alta resolução e taxa de atualização.</p>','2024-06-11 16:52:54','1549139476'),('1867794863','<h2>Teclado Mecânico Gamer Sem Fio Logitech G715</h2><p>&nbsp;</p><h2>Mais personalidade:</h2><p>O design branco do G715; o apoio de mãos em formato de nuvem; o layout compacto do teclado mecânico TKL e a altura ajustável são a combinação perfeita para os seus melhores jogos</p><p>&nbsp;</p><h2>Play On:</h2><p>Jogue sem preocupações com a bateria recarregável de longa duração para até 25 horas de jogo (com iluminação completa), a tecnologia LIGHTSPEED sem fio e conectividade Bluetooth.</p><p>&nbsp;</p><h2>Poder do LIGHTSPEED:</h2><p>Jogue suas melhores batalhas com a tecnologia LIGHTSPEED sem fio; economize uma porta USB e dupla sincronização com este teclado mecânico Logitech G sem fio e o seu mouse gamer G705.</p><p>&nbsp;</p><h2>Iluminação personalizável:</h2><p>O RGB LIGHTSYNC da Logitech G possui animações pré-carregadas Play Mood, a iluminação criada para a Aurora Collection; personalize a iluminação do seu teclado gamer RGB no Logitech G HUB.</p><p>&nbsp;</p><h2>Tecnologia de nível de jogo:</h2><p>Faça grandes partidas com o G715 com switches GX, reprodução sem fio ou com fio e controles de mídia completos ao seu alcance</p><p>&nbsp;</p><h2>Da Aurora Collection:</h2><p>Ainda melhor juntos - Teclado Sem Fio Logitech G715, Teclado Logitech G713, Headset Logitech G735 e&nbsp;Mouse Logitech G705. Vendidos separadamente.</p>','2024-06-11 16:41:08','2520567394'),('1944877552','<h2>MacBook Air de 15.3 polegadas&nbsp;</h2><p>&nbsp;</p><p>O MacBook Air de 15 polegadas é incrivelmente fino, mas tem uma tela Liquid Retina espetacular. Com a potência do chip M2 e até 18 horas de bateria*, ele proporciona desempenho impressionante em um design ultraportátil.&nbsp;</p><h2>Um notebook leve e potente para fazer de tudo em qualquer lugar!</h2><p>&nbsp;</p><p>O chip M2 acelera tudo o que você faz, como editar um vídeo para a aula, colaborar em um plano de negócios ou assistir a um streaming sem falhas durante compras online. Outra coisa boa é que você não precisa se prender à tomada ou a lugar nenhum: a bateria é para o dia todo.</p><p>&nbsp;</p><p>A tela Liquid Retina no MacBook Air é um espetáculo. Ela tem suporte para um bilhão de cores e até o dobro da resolução de um notebook PC similar. As fotos e vídeos ganham alto contraste e mais detalhes. E os textos, nitidez elevada para facilitar a leitura.</p><p>&nbsp;</p><h2>Câmera de alta definição</h2><p>&nbsp;</p><p>Brilhe nas chamadas de vídeo com a câmera FaceTime HD de 1080p. Tanto faz se é num bate-papo em família ou colaborando com gente do mundo todo.</p><p>&nbsp;</p><p><strong>Sistema de som envolvente:</strong>&nbsp;Os alto?falantes do MacBook Air são compatíveis com Áudio Espacial e Dolby Atmos para criar uma experiência sonora tridimensional em músicas e filmes.</p><p>&nbsp;</p><p>Aproveite o desempenho impressionante do MacBook Air!</p>','2024-06-11 17:02:32','122532913'),('2155741376','<h2>Pronto para vencer:</h2><p>O novo mouse PRO X SUPERLIGHT 2 é a evolução de um ícone agora&nbsp;<strong>mais rápido</strong>&nbsp;e&nbsp;<strong>mais preciso</strong>. Pesando apenas&nbsp;<strong>60g</strong>&nbsp;e projetado em parceria com os principais jogadores profissionais do mundo. Conta com a inovadora tecnologia&nbsp;<strong>LIGHTFORCE</strong>&nbsp;de switches híbridos ópticos-mecânicos, que combinam velocidade e precisão. Ele tem também o novo sensor&nbsp;<strong>HERO 2</strong>, para que você tenha a experiência máxima em jogos com&nbsp;<strong>32.000 DPI</strong>&nbsp;e mais de&nbsp;<strong>500 IPS</strong>. Com o PRO X SUPERLIGHT 2 você tem conexão sem fio via receptor&nbsp;<strong>LIGHTSPEED</strong>&nbsp;e autonomia de bateria de&nbsp;<strong>até 95 horas</strong>*. O PRO X SUPERLIGHT 2 é um mouse PRO desenvolvido para quebrar qualquer barreira entre você e a vitória.</p><p>&nbsp;</p><p>* A autonomia de bateria varia de acordo com as condições de uso.</p>','2024-06-11 16:33:18','3567247046'),('2337721854','<p>O zenfone 9 ultracompacto, ultraelegante e ultrarrápido cabe perfeitamente na sua mão, tem um excelente desempenho com o processador premium snapdragon® 8+ gen 1 e uma bateria de 4.300mah de longa duração. O sistema de câmera dupla inclui um estabilizador de imagens de 6 eixos para fotos e vídeos superstáveis. Grandes possibilidades estão esperando por você, conheça o zenfone 9!</p><p><br></p><h1>Informações Técnicas</h1><p><br></p><p><strong>bandas:</strong>&nbsp;5g non-standalone (nsa): n1, n2, n3, n5, n7, n8, n12, n20, n28, n38, n77, n78 5g standalone (sa): n77, n78</p><p><strong>sistema operacional:</strong>&nbsp;android 12</p><p><strong>bluetooth:</strong>&nbsp;bluetooth 5,2</p><p><strong>fingerprint:</strong>&nbsp;sim</p><p><strong>resolução da tela:</strong>&nbsp;1080 x. 2400</p><p><strong>garantia:</strong>&nbsp;12 meses</p><p><strong>cartão de memória:</strong>&nbsp;não</p><p><strong>peso do produto:</strong>&nbsp;0,169 kg</p><p><strong>rádio:</strong>&nbsp;não</p><p><strong>áudio:</strong>&nbsp;audio jack: 3.5mmdual mic</p><p><strong>memória ram:</strong>&nbsp;8 gb</p><p><strong>saídas:</strong>&nbsp;1x usb 2.0 tytpe-c otg com quick charge e. Power delivery 3.01x 3,5mm earphones</p><p><strong>dimensões:</strong>&nbsp;14,65 cm x. 6,81 cm x. 0,91 ~. 0,91 cm</p><p><strong>sim:</strong>&nbsp;dual sim</p><p><strong>bateria:</strong>&nbsp;1 cells / 4300 mah</p><p><strong>câmera frontal:</strong>&nbsp;12mp af</p><p><strong>wi-fi:</strong>&nbsp;wi-fi 6e (802.11ax)+bluetooth 5.2 (dual band) 2x2</p><p><strong>tecnologia:</strong>&nbsp;5g 5g nr fr1 (dl/up): 4.3gbps/0.9 4300 mbps</p><p><strong>tipo do sim card 2:</strong>&nbsp;nano sim</p><p><strong>conteúdo da embalagem:</strong>&nbsp;telefonecarregadorcabo de dadosmanual do usuariocartão garantiapino ejetor</p><p><strong>sensor de giroscópio:</strong>&nbsp;sim</p><p><strong>tipo do sim card 1:</strong>&nbsp;nano sim</p><p><strong>adaptador de energia:</strong>&nbsp;30,00 w.</p><p><strong>sensor de proximidade:</strong>&nbsp;sim</p><p><strong>armazenamento:</strong>&nbsp;256 gb ufs3.1</p><p><strong>processador:</strong>&nbsp;qualcomm snapdragon 8+ gen1 3,2 ghz, 6 mb cache</p><p><strong>cor:</strong>&nbsp;azul</p><p><strong>tela:</strong>&nbsp;5,92´´ amoled 120hz</p><p><strong>câmera principal:</strong>&nbsp;dupla: 50mp com ois +12mp wide</p><p><strong>nfc:</strong>&nbsp;sim</p><p><strong>gps:</strong>&nbsp;gps (l1+l5) glonass glonass (g1) bds (b1) galileo (e1+e5a) qzss (l1+l5)</p><p><strong>código de homologação anatel:</strong>&nbsp;11153-22-03109</p><p><strong>operadora:</strong>&nbsp;desbloqueado</p><p><strong>memória interna:</strong>&nbsp;256 gb</p><p><strong>compatible phone models:</strong>&nbsp;usb-c</p><p>&nbsp;</p><p><strong>Garantia do Fornecedor</strong></p><p>12 Meses De Garantia ( 12 Meses )</p><p><br></p><h3>Peso:</h3><p>1000 gramas (bruto com embalagem)</p>','2024-06-11 17:18:15','3170794124'),('2454333572','<h2>Processador AMD Ryzen 7 7800X3D, 5.0GHz Max Turbo</h2><p>&nbsp;</p><p>O melhor&nbsp;<strong>processador para jogos</strong>, com&nbsp;<strong>tecnologia AMD 3D V-Cache</strong>&nbsp;para ainda mais desempenho em jogos.</p><p>O processador de&nbsp;<strong>8</strong>&nbsp;<strong>núcleos</strong>&nbsp;que pode fazer tudo com desempenho incrível da AMD para os jogadores e criadores mais exigentes. Além disso, aproveite os benefícios da&nbsp;<strong>tecnologia AMD 3D V-Cache</strong>&nbsp;<strong>de última geração</strong>&nbsp;para<strong>&nbsp;baixa latência</strong>&nbsp;e ainda mais desempenho de jogo.</p>','2024-06-11 17:34:16','2628540100'),('2489069053','<h2>Mouse Gamer Sem Fio Logitech G502 X Plu</h2><p>&nbsp;</p><p>Ícone reinventado: A partir do legado do G502, o G502 X PLUS foi reinventado e redesenhado com as mais recentes inovações em tecnologia de gaming.</p><p>&nbsp;</p><h2>Switches LIGHTFORCE:</h2><p>Nova tecnologia de switches híbridos óptico-mecânicos para mais velocidade e confiabilidade, resposta imediata e horas de desempenho.</p><p>&nbsp;</p><h2>RGB LIGHTSYNC:</h2><p><strong>Iluminação personalizável e inteligente</strong>, adaptando-se ao seu jogo com efeitos de liga/desliga e&nbsp;<strong>otimização de bateria por meio de aproximação das mãos.</strong></p><p>&nbsp;</p><h2>LIGHTSPEED sem fio:</h2><p>Possui&nbsp;<strong>conectividade profissional e atualizada</strong>&nbsp;alcançando uma&nbsp;<strong>taxa de resposta até 68% mais rápida</strong>&nbsp;do que a geração anterior.</p><p>&nbsp;</p><h2>Sensor Gamer Hero 25K:</h2><p>Incrivelmente preciso até o sub-mícron para exatidão de alta precisão com zero suavização, filtragem ou aceleração. Garante&nbsp;<strong>alto desempenho</strong>&nbsp;<strong>nos jogos.</strong></p><p>&nbsp;</p><h2>Botão de DPI ajustável redesenhado:</h2><p>O G502 X PLUS possui um&nbsp;<strong>botão de DPI ajustável removível</strong>&nbsp;para você personalizar como quiser.</p><p>&nbsp;</p><h2>Roda de Scroll hiper-rápida:</h2><p>Alterne entre os modos catraca ou giro livre ou incline para a esquerda ou para a direita para obter&nbsp;<strong>dois botões personalizáveis ??adicionais.</strong></p><p>&nbsp;</p><h2>Compatível com POWERPLAY:</h2><p>Jogue sem preocupação, faça um duo com nosso mousepad para&nbsp;<strong>carregamento sem fio</strong>&nbsp;exclusivo (vendido separadamente) e seu mouse gamer sem fio G502 X LIGHTSPEED e permaneça com bateria, seja jogando ou em repouso.</p>','2024-06-11 16:37:25','2384805177'),('2759748104','<h2>Mac Studio - CPU de 24 núcleos</h2><p>&nbsp;</p><h2>Design</h2><p>O chip da Apple permitiu a criação de um desktop&nbsp;<strong>poderoso</strong>&nbsp;como nenhum outro. Com seu design compacto, o Mac Studio cabe embaixo da maioria dos monitores e transforma qualquer ambiente de trabalho em um estúdio.</p><p>&nbsp;</p><h2>Conectividade</h2><p>O Mac Studio vem com um conjunto versátil de&nbsp;<strong>12 portas</strong>&nbsp;compatíveis com leitor de cartão SDXC, uma saída HDMI aprimorada,&nbsp;<strong>Wi-Fi 6E</strong>&nbsp;Consultar avisos legais e&nbsp;<strong>Bluetooth 5.3.</strong></p><p>&nbsp;</p><h2>Otimizados para os chips da Apple</h2><p>Poderoso,&nbsp;<strong>intuitivo e confiável</strong>, o macOS foi desenvolvido para acompanhar as possibilidades do chip da Apple. E, com milhares de apps otimizados para aproveitar ao máximo o M2 Max e o M2 Ultra, você pode trabalhar, criar e se divertir como nunca.</p><p>&nbsp;</p><h3>Compre agora no KaBuM!</h3><h2><br></h2><h2>INFORMAÇÕES TÉCNICAS</h2><p><br></p><p><strong>Características:</strong></p><p>- Marca: Mac Studio</p><p>- Modelo: MQH63BZ/A</p><p>&nbsp;</p><p><strong>Especificações:</strong></p><p>&nbsp;</p><p><strong>Geral:</strong></p><p>- Chip M2 Ultra para desempenho fenomenal&nbsp;</p><p>- CPU de 24 núcleos com desempenho até 3,3x mais veloz que o iMac de 27 polegadas, para expandir as possibilidades dos fluxos de trabalho mais exigentes*&nbsp;</p><p>- GPU de até 76 núcleos com desempenho até 6,1x mais veloz que o iMac de 27 polegadas, para os fluxos de trabalho profissionais com gráficos pesados**&nbsp;</p><p>- Neural Engine de 32 núcleos para tarefas de aprendizado de máquina avançado&nbsp;</p><p>- Memória unificada de até 192GB para usar vários apps profissionais ao mesmo tempo&nbsp;</p><p>- Até 8TB de armazenamento SSD ultrarrápido para abrir apps e arquivos num instante***&nbsp;</p><p>- Conexão sem fio Wi-Fi 6 E rápida****&nbsp;</p><p>- Seis portas Thunderbolt 4, duas portas USB-A, porta HDMI, Ethernet de 10Gb, slot para cartão SDXC e entrada para fones de ouvido&nbsp;</p><p>- Suporte para até oito monitores&nbsp;</p><p>- Design compacto em prateado com laterais de 19,7cm e altura de 9,5cm&nbsp;</p><p>- macOS Ventura, que traz novas maneiras de trabalhar, compartilhar e colaborar e funciona perfeitamente com o iPhone e o iPad*****&nbsp;</p><p>&nbsp;</p><p><strong>Áudio:</strong></p><p>- Alto-falante integrado&nbsp;</p><p>- Entrada para fones de ouvido de 3,5 mm e compatibilidade avançada com fones de ouvido de alta impedância&nbsp;</p><p>- Porta HDMI compatível com saída de áudio multicanal&nbsp;&nbsp;</p><p>- Portas&nbsp;&nbsp;&nbsp;</p><p>- Quatro portas Thunderbolt 4 com suporte para:&nbsp;</p><p>- Thunderbolt 4 (até 40 Gb/s)&nbsp;</p><p>- DisplayPort&nbsp;</p><p>- USB 4 (até 40 Gb/s)&nbsp;</p><p>- USB 3.1 Gen 2 (até 10 Gb/s)&nbsp;</p><p>- Duas portas USB‑A (até 5 Gb/s)&nbsp;</p><p>- Porta HDMI&nbsp;</p><p>- Ethernet de 10 Gb&nbsp;</p><p>- Entrada para fones de ouvido de 3,5 mm&nbsp;</p><p>- Na frente (M2 Ultra):&nbsp;&nbsp;</p><p>- Duas portas Thunderbolt 4 (até 40 Gb/s)&nbsp;</p><p>- Slot para cartão SDXC (UHS‑II)&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p><strong>Rede:&nbsp;&nbsp;&nbsp;</strong></p><p>- Wi-Fi 6E (802.11ax)&nbsp;</p><p>- Bluetooth 5.3&nbsp;</p><p>- Ethernet&nbsp;</p><p>- Ethernet de 10 Gb (Ethernet Nbase-T compatível com Ethernet de 1 Gb, 2,5 Gb, 5 Gb e 10 Gb usando um conector RJ‑45)&nbsp;</p><p>&nbsp;</p><p><strong>Requisitos elétricos e operacionais:&nbsp;&nbsp;</strong></p><p>- Voltagem: 100–240 VCA&nbsp;</p><p>- Frequência: 50–60 Hz, monofase&nbsp;</p><p>- Potência contínua máxima: 370W&nbsp;</p><p>- Temperatura operacional: 10 ºC a 35 ºC&nbsp;</p><p>- Temperatura de armazenamento:-40 ºC a 47 ºC&nbsp;</p><p>- Umidade relativa: 5% a 95%, sem condensação&nbsp;</p><p>- Altitude operacional: testado até 5.000m&nbsp;</p><p>&nbsp;</p><p><strong>Softwares:&nbsp;&nbsp;&nbsp;</strong></p><p>- MacOS&nbsp;&nbsp;&nbsp;</p><p>&nbsp;</p><p><strong>Apps incluídos:&nbsp;&nbsp;</strong></p><p>- App Store&nbsp;</p><p>- Atalhos&nbsp;</p><p>- Bolsa&nbsp;</p><p>- Buscar&nbsp;</p><p>- Calendário&nbsp;</p><p>- Casa&nbsp;</p><p>- Contatos&nbsp;</p><p>- FaceTime&nbsp;</p><p>- Fotos&nbsp;</p><p>- Freeform&nbsp;</p><p>- GarageBand&nbsp;</p><p>- Gravador&nbsp;</p><p>- iMovie&nbsp;</p><p>- Keynote&nbsp;</p><p>- Lembretes&nbsp;</p><p>- Livros&nbsp;</p><p>- Mail&nbsp;</p><p>- Mapas&nbsp;</p><p>- Mensagens&nbsp;</p><p>- Música&nbsp;</p><p>- Notas&nbsp;</p><p>- Numbers&nbsp;</p><p>- Pages&nbsp;</p><p>- Photo Booth&nbsp;</p><p>- Podcasts&nbsp;</p><p>- Pré-Visualização&nbsp;</p><p>- QuickTime Player&nbsp;</p><p>- Safari&nbsp;</p><p>- Siri&nbsp;</p><p>- Time Machine&nbsp;</p><p>- TV&nbsp;</p><p>&nbsp;</p><p><strong>Conteúdo da Embalagem:</strong></p><p>- Mac Studio&nbsp;</p><p>- Cabo de alimentação&nbsp;</p><p><br></p><h3>Garantia:</h3><p>12 meses de garantia</p><h3>Peso:</h3><p>6280 gramas (bruto com embalagem)</p>','2024-06-11 15:03:52','236442349'),('2762532830','<h1>RTX 4090</h1><p><br></p><p><br></p><ul><li>16.384 núcleos NVIDIA CUDA</li><li>Suporta 4K 120Hz HDR, 8K 60Hz HDR e taxa de atualização variável conforme especificado em HDMI 2.1a</li><li>Novos multiprocessadores de streaming: desempenho de até 2x e eficiência energética</li><li>Núcleos tensores de quarta geração: desempenho de até 2x IA</li><li>Núcleos RT de terceira geração: desempenho de até 2x ray tracing. Desempenho Acelerado por AI: NVIDIA DLSS 3. Resposta vencedora de jogos: plataforma de baixa latência</li><li>NVIDIA Reflex.Construído para transmissão ao vivo: NVIDIA Encoder.8K HDR Gaming</li></ul>','2024-06-11 16:12:31','2663578255'),('2829637471','<h2>Placa de vídeo RTX 4060 ASUS Dual O8G</h2><p>&nbsp;</p><h2>NVIDIADLSS3</h2><p>DLSS é um avanço revolucionário em&nbsp;<strong>gráficos de IA que multiplicam o desempenh</strong>o. Equipado com os novos Tensor Cores de quarta geração e o Optical Flow Accelerator nas GPUs GeForce RTX Série 40, o&nbsp;<strong>DLSS 3 usa IA</strong>&nbsp;para criar quadros adicionais e melhorar a qualidade da imagem.</p><p>&nbsp;</p><h2>Ajuste de GPU III</h2><p>O utilitário ASUS&nbsp;<strong>GPU Tweak III</strong>&nbsp;leva o ajuste da placa gráfica para o próximo nível. Ele permite ajustar parâmetros críticos, incluindo clocks do núcleo da GPU, frequência de memória e configurações de voltagem, com a opção de monitorar tudo em tempo real por meio de uma exibição na tela personalizável. O controle avançado do ventilador também está incluído, juntamente com muitos outros recursos para ajudá-lo a aproveitar ao máximo sua placa gráfica.</p><p>&nbsp;</p><h2>Design de ventilador de tecnologia Axial</h2><p><strong>Dois ventiladores Axial-tech</strong>&nbsp;testados e comprovados apresentam um cubo menor que facilita lâminas mais longas e um anel de barreira para aumentar a pressão do ar descendente.</p>','2024-06-11 17:21:11','3220644470'),('2968949771','<h2>Processador AMD Ryzen 5 5600X</h2><p>&nbsp;</p><p>Jogue com os melhores<strong>&nbsp;6 núcleos incríveis</strong>&nbsp;para quem quer apenas jogar. Imbatível no jogo&nbsp;<strong>Obtenha o desempenho de jogos de alta velocidade</strong>&nbsp;do melhor processador de desktop do mundo. AMD Ryzen para criadores Codifique mais rápido.</p><p>&nbsp;</p><h2>Renderize mais Rápido. Repita mais Rápido</h2><p>Crie mais e mais rápido com os processadores AMD Ryzen.&nbsp;<strong>Desempenho de próximo nível</strong>&nbsp;para arquitetos, engenheiros e profissionais criativos Imagine o que você pode fazer com o processador mais avançado do mundo.</p><p><strong>Não possui&nbsp;video integrado</strong></p>','2024-06-11 17:33:00','4080007038'),('3185490883','<h2>Placa de Vídeo ASUS NVIDIA TUF Gaming GeForce RTX4090 Edition, 24 GB GDDR6X, DLSS, Ray Tracing</h2><p>&nbsp;</p><h2>Armado para Fluxo</h2><p>A&nbsp;<strong>arquitetura NVIDIA Ada Lovelace</strong>&nbsp;elevada por&nbsp;<strong>resfriamento aprimorado</strong>&nbsp;e<strong>&nbsp;fornecimento de energia</strong>, e apoiada por um arsenal de reforços robustos para cobrir seus seis. Bloqueie, carregue e domine com a TUF Gaming GeForce RTX 4090.</p><p>&nbsp;</p><h2>Resfriamento</h2><p>Uma cobertura fundida e uma&nbsp;<strong>placa traseira de alumínio</strong>&nbsp;otimizado para trabalho de fluxo de ar em conjunto com&nbsp;<strong>ventiladores Axial-tech</strong>&nbsp;redesenhados que mudam&nbsp;<strong>23% mais ar</strong>, mantendo os&nbsp;<strong>níveis de ruído baixos e GPU temperaturas sob controle rígido</strong>.</p><p>&nbsp;</p><h2>Durabilidade</h2><p>Capacitores de longa duração,&nbsp;<strong>rolamentos de esferas duplas</strong>&nbsp;e um processo de fabricação automatizado garante&nbsp;<strong>longa confiabilidade</strong>&nbsp;de prazo para sua compilação de jogos.</p><p>&nbsp;</p><h2>Estética</h2><p>Uma pitada de<strong>&nbsp;iluminação Aura RGB</strong>&nbsp;brilha através do&nbsp;<strong>Logo TUF</strong>, adicionando uma camada de personalização através de uma&nbsp;<strong>gama de decoração e funcional efeitos</strong>.</p><p>&nbsp;</p><h2>Software</h2><p>Hardware e software se unem para permitir que você personalizar totalmente sua experiência e obter o máximo fora de sua placa gráfica. GPU Tweak III permite&nbsp;<strong>ajustes de hardware e monitoramento</strong>, e O&nbsp;<strong>QuantumCloud</strong>&nbsp;utiliza sua computação GPU sobressalente poder de gerar renda passiva.</p>','2024-06-11 17:23:24','3730391284'),('3229565050','<h1>Console Sony Playstation 5</h1><p>&nbsp;</p><p><br></p><h3>Jogar no PS5 Não Tem Limites</h3><p>Desfrute do carregamento do seu PS5, extremamente rápido com o SSD de altíssima velocidade, uma imersão mais profunda com suporte a feedback tátil, gatilhos adaptáveis e áudio 3D, além de uma geração inédita de jogos incríveis para PlayStation.</p><p><br></p><h3>Veloz como um raio, SSD ultrarrápido</h3><p>Domine o poder de uma CPU e GPU personalizadas e o SSD com E/S integradas que redefinem as regras do que o console PlayStation pode fazer.</p><p>Maximize suas sessões de jogo com tempo de carregamento praticamente instantâneo para jogos do PS5 instalados.</p><p><br></p><h3>Jogos impressionantes para PS5</h3><p>Maravilhe-se com os gráficos incríveis e experimente os recursos do novo PS5. \"Ray Tracing\" (Rastreamento de raios) Mergulhe em mundos com um nível inédito de realismo enquanto os raios de luz são simulados individualmente, criando sombras e reflexos realistas em jogos compatíveis com Playstation 5. Jogos para TVs 4K Curta seus jogos favoritos do PS5 na sua incrível TV 4K. Até 120 fps com saída em 120 Hz Desfrute da fluidez e taxa de quadros de até 120 fps em jogos compatíveis, com suporte a saída de 120 Hz em telas 4K.</p><p>&nbsp;</p><h3>Tecnologia HDR</h3><p>Com uma TV HDR, os jogos compatíveis do PS5 exibem uma variedade de cores inacreditavelmente vibrantes e realistas. Saída em 8K Os consoles PS5 oferecem suporte à saída 8K, para que você possa jogar na sua tela com resolução de 4320p.</p><p><br></p><h3>Tempest 3D AudioTech</h3><p>Mergulhe em palcos sonoros que farão você acreditar que os sons estão vindo de todas as direções. Seja com seus fones de ouvido ou os alto-falantes de sua TV, seu ambiente ganhará vida com o Tempest 3D AudioTech em jogos compatíveis.</p><p><br></p><h3>Resposta tátil</h3><p>Experimente a resposta tátil com o controle sem fio DualSense em jogos selecionados do PS5 e sinta o impacto de suas ações no jogo através da resposta sensorial dinâmica.</p><p><br></p><h3>Gatilhos adaptáveis</h3><p>Assuma o controle com os imersivos gatilhos adaptáveis, agora com níveis dinâmicos de resistência que simulam o impacto físico das atividades em jogos selecionados do PS5.</p>','2024-03-22 16:46:18','1874139195'),('344410717','<h2>Processador AMD Ryzen 7 5700X3D</h2><p>&nbsp;</p><h2>Arquitetura Zen 3 Refinada</h2><p>Desfrute de velocidades supersônicas com<strong>&nbsp;8 núcleos</strong>&nbsp;e<strong>&nbsp;16 threads</strong>&nbsp;de processamento, prontos para enfrentar os títulos mais desafiadores. Frequência base de&nbsp;<strong>3,0GHz</strong>&nbsp;e boost dinâmico de até&nbsp;<strong>4,1GHz</strong>&nbsp;para eliminar qualquer engasgo.</p><p>&nbsp;</p><h2>Eficiência Energética sem Abdicar da Potência</h2><p>Jogue por horas sem se preocupar. O<strong>&nbsp;TDP de</strong>&nbsp;<strong>105W</strong>&nbsp;garante&nbsp;<strong>alto desempenho</strong>&nbsp;sem consumo excessivo de energia.</p>','2024-06-11 17:30:40','941978367'),('3449452302','<h1>iPhone 15 Pro Max</h1><p><br></p><ul><li><strong>FORJADO EM TITÂNIO</strong> — O iPhone 15 Pro Max tem design robusto e leve em titânio aeroespacial. Na parte de trás, vidro matte texturizado e, na frente, Ceramic Shield mais resistente que qualquer vidro de smartphone. Ele também é durão contra respingos, água e poeira</li><li><strong>TELA AVANÇADA</strong> — A tela Super Retina XDR de 6,7 pol. com ProMotion aumenta as taxas de atualização para 120 Hz quando você precisa de gráficos mais impressionantes. A Dynamic Island mostra alertas e Atividades ao Vivo. Além disso, com a tela Sempre Ativa, você nem precisa tocar na Tela Bloqueada para ficar de olho em tudo.</li><li><strong>CHIP A17 PRO REVOLUCIONÁRIO</strong> — Com GPU de categoria Pro, os games para celular ficam mais imersivos, com ambientes detalhados e personagens muito realistas. O chip A17 Pro é incrivelmente eficiente e ajuda a garantir bateria para o dia todo</li><li><strong>SISTEMA DE CÂMERA PRO PODEROSO</strong> — Aumente suas possibilidades de enquadramento com sete lentes Pro. Fotografe em altíssima resolução e tenha mais cores e detalhes com a câmera grande-angular de 48 MP. Os closes vão ficar mais nítidos a uma distância ainda maior com a câmera teleobjetiva de 5x no iPhone 15 Pro Max.</li><li><strong>BOTÃO DE AÇÃO CONFIGURÁVEL</strong> — O botão de Ação deixa seu recurso favorito sempre à mão. Basta definir qual ação você quer usar, como modo Silencioso, Câmera, Gravador, Atalhos, entre outras. Depois, mantenha o botão pressionado para iniciar.</li><li><strong>CONECTIVIDADE PRO</strong> — Com a nova porta USB‑C, você recarrega seu iPhone 15 Pro com o mesmo cabo que usa para recarregar o Mac ou o iPad. Com USB 3, a velocidade de transferência de dados dá um salto enorme. E você transfere arquivos até duas vezes mais rápido</li><li><strong>RECURSO ESSENCIAL DE SEGURANÇA</strong> — Com a Detecção de Acidente, o iPhone é capaz de identificar se você sofreu um acidente grave de carro e ligar para a emergência se você não puder</li><li><strong>PROJETADO PARA FAZER A DIFERENÇA</strong> — O iPhone protege sua privacidade e deixa você no controle dos seus dados. Ele é feito com mais materiais reciclados para minimizar o impacto ambiental. E vem com recursos integrados para ser cada vez mais acessível a todas as pessoas.</li></ul>','2024-03-21 17:43:21','1197754295'),('3481989436','<h2>Mouse Gamer Sem Fio Logitech G PRO Wireless&nbsp;</h2><p><br></p><p><br></p><p>Projetado em colaboração direta de muitos jogadores profissionais de e-sports, o mouse gamer PRO Wireless foi desenvolvido de acordo com os exigentes padrões de alguns dos maiores profissionais de e-sports do mundo. O PRO Wireless gaming mouse foi concebido para oferecer um desempenho de ponta e inclui as mais recentes e avançadas tecnologias disponíveis. Com a tecnologia sem fio LIGHTSPEED, o PRO Wireless supera as limitações de latência, conectividade e energia para oferecer uma conexão de taxa de transmissão de 1 ms, sólida e super-rápida. O PRO Wireless gaming mouse também está equipado com a versão mais recente do sensor HERO 25K, nosso sensor óptico de última geração que é o sensor para jogos de melhor desempenho e eficiência do mercado com sensibilidade ajustável. Play to win.</p><h2><br></h2><h2>Sensor óptico para jogos mais preciso</h2><p><br></p><p>Como os profissionais do eSports buscam velocidade e precisão cada vez maiores, o mesmo acontece com a Logitech G. Com a invenção do HERO 25K, o sensor de jogos de última geração, o mundo agora tem um novo líder. Para o PRO Wireless, o HERO 25K foi otimizado para rastrear movimentos insanos a velocidades superiores a 400 IPS sem falhas. O HERO 25K oferece desempenho máximo em qualquer sensibilidade com suavização, aceleração ou filtragem zero de 100 a 25,600 DPI. O HERO 25K também consome 10x menos energia que os antecessores, como o sensor PMW3366, permitindo uma bateria mais leve e mais durável. Profissionais exigem o que há de melhor, e o HERO 25K atende a essa exigência.</p>','2024-06-11 16:35:22','4152333900'),('3557217015','<h2>Notebook Acer Nitro V15</h2><p>&nbsp;</p><h2>Ação do Começo ao Fim</h2><p>O Nitro V15 conta com a placa de vídeo<strong>&nbsp;NVIDIA GeForce RTX 3050</strong>&nbsp;com&nbsp;<strong>6 GB</strong>&nbsp;de memória dedicada&nbsp;<strong>GDDR6</strong>&nbsp;com eficiência total (TGP) de&nbsp;<strong>até 80W</strong>&nbsp;que oferece o melhor desempenho para você aproveitar ao máximo suas horas de jogatina.</p><p>&nbsp;</p><h2>Processador Que Faz Os Adversários Tremerem</h2><p>Nada pode te parar com o&nbsp;<strong>Intel Core i5-13420H de 13ª geração</strong>&nbsp;deste notebook. Juntamente com&nbsp;<strong>8 GB de memória RAM</strong>, expansível&nbsp;<strong>até 32 GB</strong>, o processador te leva aos níveis mais avançados de games e criação de conteúdo.</p><p>&nbsp;</p><h2>Veloz e Furioso</h2><p>O nitro V15 entrega&nbsp;<strong>imagens vívidas e fluídas</strong>, que permitem uma jogabilidade mais rápida. Tudo isso, devido a sua tela de alta resolução e taxa de atualização.</p>','2024-06-11 16:56:42','3110931476'),('3883195237','<h2>Processador AMD Ryzen 7 5700X</h2><p>&nbsp;</p><p>Quando você tem a&nbsp;<strong>arquitetura de processador&nbsp;de desktop&nbsp;mais avançada do mundo</strong>&nbsp;<strong>para jogadores e criadores</strong>&nbsp;<strong>de conteúdo</strong>, as possibilidades são infinitas. Esteja você jogando os jogos mais recentes, projetando o próximo prédio ou processando dados, você precisa de um&nbsp;<strong>processador poderoso</strong>&nbsp;que possa lidar com tudo - e muito mais. Sem dúvida, os processadores AMD Ryzen série 5000 definem o padrão para jogadores e artistas.</p><p>&nbsp;</p><h2>Experiência definitiva de jogos para PC</h2><p>Os processadores AMD Ryzen e as placas de vídeo AMD Radeon com Windows possibilitam a experiência definitiva de jogos por meio de gráficos superiores, desempenho incrível, recursos de segurança otimizados e suporte para os recursos mais recentes.</p><p>&nbsp;</p><h2>Eficiência incrível</h2><p>De maneira impressionante, os&nbsp;<strong>ganhos de desempenho</strong>&nbsp;da&nbsp;<strong>arquitetura “Zen 3”</strong>&nbsp;podem ser fornecidos sem aumento no consumo de energia ou TDP. A combinação de uma arquitetura de última geração com o processo de<strong>&nbsp;7 nm</strong>&nbsp;líder do setor dá ao AMD Ryzen série 5000 uma melhoria de + 24% de geração em eficiência energética e uma impressionante vantagem de 2,8X sobre as arquiteturas concorrentes.</p><p>&nbsp;</p><h2>Dentro do jogo</h2><p>Com a avançada arquitetura “Zen 3” dos processadores AMD Ryzen Série 5000 G, você tem o&nbsp;<strong>desempenho de computação que os jogos imersivos exigem</strong>. A<strong>&nbsp;tecnologia de 7 nm</strong>&nbsp;é um&nbsp;<strong>design com alta performance</strong>&nbsp;e&nbsp;<strong>alta eficiência</strong>&nbsp;extraordinários, além das possibilidades&nbsp;<strong>poderosas de thread único</strong>&nbsp;<strong>ou múltiplo</strong>. Assim, você tem frames rápidos para uma melhor experiência nos jogos.</p><p><br></p><p>*Não possui&nbsp;video integrado</p>','2024-06-11 17:31:45','1165821908'),('3921050805','<h2>Mac Studio - CPU de 24 núcleos</h2><p>&nbsp;</p><h2>Design</h2><p>O chip da Apple permitiu a criação de um desktop&nbsp;<strong>poderoso</strong>&nbsp;como nenhum outro. Com seu design compacto, o Mac Studio cabe embaixo da maioria dos monitores e transforma qualquer ambiente de trabalho em um estúdio.</p><p>&nbsp;</p><h2>Conectividade</h2><p>O Mac Studio vem com um conjunto versátil de&nbsp;<strong>12 portas</strong>&nbsp;compatíveis com leitor de cartão SDXC, uma saída HDMI aprimorada,&nbsp;<strong>Wi-Fi 6E</strong>&nbsp;Consultar avisos legais e&nbsp;<strong>Bluetooth 5.3.</strong></p><p>&nbsp;</p><h2>Otimizados para os chips da Apple</h2><p>Poderoso,&nbsp;<strong>intuitivo e confiável</strong>, o macOS foi desenvolvido para acompanhar as possibilidades do chip da Apple. E, com milhares de apps otimizados para aproveitar ao máximo o M2 Max e o M2 Ultra, você pode trabalhar, criar e se divertir como nunca.</p><p>&nbsp;</p><h3>Compre agora no KaBuM!</h3><h2><br></h2><h2>INFORMAÇÕES TÉCNICAS</h2><p><br></p><p><strong>Características:</strong></p><p>- Marca: Mac Studio</p><p>- Modelo: MQH63BZ/A</p><p>&nbsp;</p><p><strong>Especificações:</strong></p><p>&nbsp;</p><p><strong>Geral:</strong></p><p>- Chip M1 Ultra para desempenho fenomenal&nbsp;</p><p>- CPU de 24 núcleos com desempenho até 3,3x mais veloz que o iMac de 27 polegadas, para expandir as possibilidades dos fluxos de trabalho mais exigentes*&nbsp;</p><p>- GPU de até 76 núcleos com desempenho até 6,1x mais veloz que o iMac de 27 polegadas, para os fluxos de trabalho profissionais com gráficos pesados**&nbsp;</p><p>- Neural Engine de 32 núcleos para tarefas de aprendizado de máquina avançado&nbsp;</p><p>- Memória unificada de até 192GB para usar vários apps profissionais ao mesmo tempo&nbsp;</p><p>- Até 8TB de armazenamento SSD ultrarrápido para abrir apps e arquivos num instante***&nbsp;</p><p>- Conexão sem fio Wi-Fi 6 E rápida****&nbsp;</p><p>- Seis portas Thunderbolt 4, duas portas USB-A, porta HDMI, Ethernet de 10Gb, slot para cartão SDXC e entrada para fones de ouvido&nbsp;</p><p>- Suporte para até oito monitores&nbsp;</p><p>- Design compacto em prateado com laterais de 19,7cm e altura de 9,5cm&nbsp;</p><p>- macOS Ventura, que traz novas maneiras de trabalhar, compartilhar e colaborar e funciona perfeitamente com o iPhone e o iPad*****&nbsp;</p><p>&nbsp;</p><p><strong>Áudio:</strong></p><p>- Alto-falante integrado&nbsp;</p><p>- Entrada para fones de ouvido de 3,5 mm e compatibilidade avançada com fones de ouvido de alta impedância&nbsp;</p><p>- Porta HDMI compatível com saída de áudio multicanal&nbsp;&nbsp;</p><p>- Portas&nbsp;&nbsp;&nbsp;</p><p>- Quatro portas Thunderbolt 4 com suporte para:&nbsp;</p><p>- Thunderbolt 4 (até 40 Gb/s)&nbsp;</p><p>- DisplayPort&nbsp;</p><p>- USB 4 (até 40 Gb/s)&nbsp;</p><p>- USB 3.1 Gen 2 (até 10 Gb/s)&nbsp;</p><p>- Duas portas USB‑A (até 5 Gb/s)&nbsp;</p><p>- Porta HDMI&nbsp;</p><p>- Ethernet de 10 Gb&nbsp;</p><p>- Entrada para fones de ouvido de 3,5 mm&nbsp;</p><p>- Na frente (M1 Ultra):&nbsp;&nbsp;</p><p>- Duas portas Thunderbolt 4 (até 40 Gb/s)&nbsp;</p><p>- Slot para cartão SDXC (UHS‑II)&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p><strong>Rede:&nbsp;&nbsp;&nbsp;</strong></p><p>- Wi-Fi 6E (802.11ax)&nbsp;</p><p>- Bluetooth 5.3&nbsp;</p><p>- Ethernet&nbsp;</p><p>- Ethernet de 10 Gb (Ethernet Nbase-T compatível com Ethernet de 1 Gb, 2,5 Gb, 5 Gb e 10 Gb usando um conector RJ‑45)&nbsp;</p><p>&nbsp;</p><p><strong>Requisitos elétricos e operacionais:&nbsp;&nbsp;</strong></p><p>- Voltagem: 100–240 VCA&nbsp;</p><p>- Frequência: 50–60 Hz, monofase&nbsp;</p><p>- Potência contínua máxima: 370W&nbsp;</p><p>- Temperatura operacional: 10 ºC a 35 ºC&nbsp;</p><p>- Temperatura de armazenamento:-40 ºC a 47 ºC&nbsp;</p><p>- Umidade relativa: 5% a 95%, sem condensação&nbsp;</p><p>- Altitude operacional: testado até 5.000m&nbsp;</p><p>&nbsp;</p><p><strong>Softwares:&nbsp;&nbsp;&nbsp;</strong></p><p>- MacOS&nbsp;&nbsp;&nbsp;</p><p>&nbsp;</p><p><strong>Apps incluídos:&nbsp;&nbsp;</strong></p><p>- App Store&nbsp;</p><p>- Atalhos&nbsp;</p><p>- Bolsa&nbsp;</p><p>- Buscar&nbsp;</p><p>- Calendário&nbsp;</p><p>- Casa&nbsp;</p><p>- Contatos&nbsp;</p><p>- FaceTime&nbsp;</p><p>- Fotos&nbsp;</p><p>- Freeform&nbsp;</p><p>- GarageBand&nbsp;</p><p>- Gravador&nbsp;</p><p>- iMovie&nbsp;</p><p>- Keynote&nbsp;</p><p>- Lembretes&nbsp;</p><p>- Livros&nbsp;</p><p>- Mail&nbsp;</p><p>- Mapas&nbsp;</p><p>- Mensagens&nbsp;</p><p>- Música&nbsp;</p><p>- Notas&nbsp;</p><p>- Numbers&nbsp;</p><p>- Pages&nbsp;</p><p>- Photo Booth&nbsp;</p><p>- Podcasts&nbsp;</p><p>- Pré-Visualização&nbsp;</p><p>- QuickTime Player&nbsp;</p><p>- Safari&nbsp;</p><p>- Siri&nbsp;</p><p>- Time Machine&nbsp;</p><p>- TV&nbsp;</p><p>&nbsp;</p><p><strong>Conteúdo da Embalagem:</strong></p><p>- Mac Studio&nbsp;</p><p>- Cabo de alimentação&nbsp;</p><p><br></p><h3>Garantia:</h3><p>12 meses de garantia</p><h3>Peso:</h3><p>6280 gramas (bruto com embalagem)</p>','2024-06-11 15:05:21','835329450'),('4028264064','<h2>Notebook Gamer ASUS ROG STRIX G16 Intel Core i9-13980HX</h2><p>&nbsp;</p><p>O novo ROG Strix G16 traz a&nbsp;<strong>13a geração</strong>&nbsp;<strong>de processadores Intel&nbsp;Core&nbsp;i9-13980HX</strong>, que garante o desempenho supremo que você precisa para elevar sua gameplay e carregar seu time em quaisquer desafios, graças aos seus&nbsp;<strong>8 núcleos de performance</strong>&nbsp;e&nbsp;<strong>16 núcleos de eficiência</strong>.</p><p>Este poderoso notebook gamer conta com a novíssima&nbsp;<strong>placa NVIDIA&nbsp;GeForce RTX&nbsp;4060</strong>, que fornece mais poder de processamento gráfico combinado com uma surpreendente e inovadora tecnologia de inteligência artificial. E com modernos recursos como o novo&nbsp;<strong>DLSS 3</strong>, que&nbsp;<strong>aumenta o FPS dos jogos</strong>, o ROG Strix G16 é capaz de trazer uma experiência ainda mais imersiva e realista.</p><h2><br></h2><h2>Tecnologia MUX Switch + NVIDIA&nbsp;Advanced Optimus</h2><p>&nbsp;</p><p>Para aumentar ainda mais o desempenho gráfico do&nbsp;<strong>ROG Strix G16</strong>, ele conta com a tecnologia&nbsp;<strong>MUX Switch</strong>&nbsp;aliada ao sistema&nbsp;<strong>Advanced Optimus da NVIDIA</strong>. O MUX Switch permite que o fluxo gráfico saia diretamente do processador para a GPU, garantindo o&nbsp;<strong>melhor desempenho gráfico</strong>&nbsp;do sistema. Já o Advanced Optimus ativa o MUX Switch sem reiniciar o sistema, facilitando o uso desta tecnologia.&nbsp;</p><p>Altas taxas de atualização são críticas em jogos competitivos, pois com movimentos mais rápidos e suaves, permitem uma maior precisão durante a partida. Pensando nisso, o ROG Strix G16 foi projetado com&nbsp;<strong>tela IPS capaz de atingir uma taxa de atualização de 165 Hz.</strong>&nbsp;Sua r<strong>esolução Full HD +</strong>&nbsp;de proporção 16:10 possui cobertura de cores de 100% do espaço sRGB, gerando uma qualidade de imagem excepcional e reprodução muito mais fluida e rápida; tudo com o mais alto padrão para manter seus oponentes sempre na mira.&nbsp;</p><p>&nbsp;</p><h2>Metal Líquido aplicado no processador - Redução de até 15 °C</h2><p>Com componentes tão poderosos, o sistema de refrigeração é extremamente importante para que você possa atingir o melhor desempenho do sistema. Para entregar a refrigeração ideal, o novo ROG Strix G16 utiliza&nbsp;<strong>Metal Líquido - Conductonaut Extreme, da Thermal Grizzly, aplicado diretamente no processador</strong>. Este material é 17x mais condutivo termicamente e&nbsp;<strong>reduz em até 15 °C a temperatura da CPU</strong>. Além disso, este notebook conta com um sistema inteligente de refrigeração, o ROG Intelligent Cooling. Ele inclui&nbsp;<strong>a tecnologia Tri-Fan, com</strong>&nbsp;<strong>3 exaustores que ampliam o fluxo de ar</strong>. As saídas de ar também foram aumentadas permitindo a rápida dissipação de calor, enquanto as aletas de cobre de 0,1 mm, por fim,&nbsp;apresentam alta eficiência térmica e reduzem drasticamente a resistência do ar.</p>','2024-06-11 17:10:43','3821092638'),('4177996387','<h2>Processador AMD Ryzen 9 5900X</h2><p>&nbsp;</p><p><strong>O melhor processador de jogos do mundo</strong>, com&nbsp;<strong>12 núcleos</strong>&nbsp;para alimentar jogos, streaming e muito mais. Imbatível no jogo Obtenha o&nbsp;<strong>desempenho de jogos de alta velocidade</strong>&nbsp;do melhor processador de desktop do mundo.</p><p>&nbsp;</p><p>&nbsp;</p><h2>AMD Ryzen para criadores</h2><p><strong>Codifique mais rápido. Renderize mais rápido. Repita mais rápido</strong>. Crie mais e mais rápido com os processadores AMD Ryzen.</p><p>&nbsp;</p><h2>AMD \"Zen 3\" Core Architecture</h2><p>Os núcleos mais rápidos do mundo para jogadores de PC&nbsp;<strong>Tecnologia AMD StoreMI</strong>&nbsp;É um jeito rápido e fácil de expandir e acelerar o armazenamento nos PCs com um processador AMD Ryzen.</p><p>&nbsp;</p><h2>Utilitário AMD Ryzen Master</h2><p>O&nbsp;<strong>utilitário de overclocking simples</strong>&nbsp;e&nbsp;<strong>potente</strong>&nbsp;para os processadores AMD Ryzen.</p><p>&nbsp;</p><h2>AMD Ryzen VR-Ready Premium</h2><p>Para usuários que querem&nbsp;<strong>uma experiência de realidade virtual premium</strong>, a AMD oferece os processadores de alto desempenho Ryzen&nbsp;<strong>VR-Ready Premium</strong>.</p><p><br></p><p>*Não possui&nbsp;video integrado</p><p>&nbsp;</p>','2024-06-11 17:32:27','2564146670'),('4217437514','<h2 class=\"ql-align-justify\">Notebook Gamer ASUS Tuf Intel Core i7 12700H</h2><p class=\"ql-align-justify\">&nbsp;</p><p class=\"ql-align-justify\">Conheça a nova linha de notebooks gamer TUF Gaming, da ASUS, feita para aqueles que buscam performance em jogos competitivos e querem vencer todos os desafios do dia a dia. Preparado para qualquer campo de batalha, o novo ASUS TUF Gaming F15 supera os limites, seja jogando, fazendo livestreams ou em qualquer outra atividade. Graças ao poderoso&nbsp;<strong>processador Intel Core i7-12700H</strong>&nbsp;com&nbsp;<strong>14 núcleos</strong>, até as tarefas mais complicadas ficam simples.&nbsp;</p><p class=\"ql-align-justify\">Para que a sua gameplay seja excelente, este notebook vem equipado com a<strong>&nbsp;placa de vídeo NVIDIA GeForce RTX 3050</strong>, que habilita todas as tecnologias baseadas em Inteligência Artificial desenvolvidos pela NVIDIA, como<strong>&nbsp;Ray Tracing</strong>,&nbsp;<strong>DLSS</strong>&nbsp;e muitas outras. Trabalhando com uma potência gráfica (TGP) de&nbsp;<strong>95 W</strong>, você terá muito&nbsp;<strong>mais FPS</strong>&nbsp;que seus oponentes.</p><p><br></p>','2024-06-11 17:13:21','3518494235'),('786559378','<h2 class=\"ql-align-center\">A PRÓXIMA DIMENSÃO</h2><p class=\"ql-align-center\">Um avanço em design e projeto, o G915 inclui LIGHTSPEED profissional sem fio, LIGHTSYNC RGB avançado e novos switches mecânicos de perfil baixo de alto desempenho. Meticulosamente produzido a partir de materiais superiores, o G915 possui um design sofisticado de beleza, força e desempenho incomparáveis. Conheça o G915 LIGHTSPEED e jogue na próxima dimensão.</p><p><br></p><h2>TECLADO SEM FIO PARA JOGOS LIGHTSPEED</h2><p>O G915 inclui a tecnologia LIGHTSPEED sem fio de nível profissional que atinge um desempenho super-rápido de 1 ms. É a mesma tecnologia sem fio em que os profissionais de eSports de todo o mundo confiam para competições. O G915 se mantém completamente funcional quando conectado via USB, para que você possa jogar e carregar simultaneamente.</p><p><br></p><h2>INCRIVELMENTE FINO</h2><p>O G915 é um feito de engenharia e design. Meticulosamente fabricado a partir de materiais superiores, o G915 é extraordinariamente refinado, incrivelmente fino e fabricado sem perda de desempenho ou recursos. Durável, confortável e pronto para sessões de jogo intensas, o G915 é verdadeiramente a próxima geração de teclados mecânicos para jogos.</p><p><br></p><h2 class=\"ql-align-center\">MATERIAIS SUPERIORES</h2><p class=\"ql-align-center\">A estrutura em liga de alumínio 5052 une-se a uma base reforçada com aço, resultando em um teclado leve, de design ultrafino e ao mesmo tempo forte e durável. Este teclado repleto de recursos foi meticulosamente projetado e desenvolvido para combinar desempenho descompromissado com uma estética suave.</p><p class=\"ql-align-center\"><br></p><h2>FUNÇÃO FORMATIVA</h2><p class=\"ql-align-center\">Cada detalhe foi executado cuidadosamente e otimizado para a melhor experiência. A roda de volume fabricada em alumínio foi precisamente tensionada para sensação e toque superiores. Os botões de controle de perfil e mídia de toque suave fornecem feedback tátil que propicia controle fácil e intuitivo.</p><p class=\"ql-align-center\"><br></p><h2>FORTE E DURÁVEL</h2><p class=\"ql-align-center\">As superfícies de metal escovado e as teclas com revestimento oleofóbico são projetadas para minimizar as impressões digitais. A base reforçada com aço dá ao G915 a força necessária para perseverar mesmo sob as condições de uso mais estressantes.&nbsp;</p><p class=\"ql-align-center\"><br></p><h2 class=\"ql-align-center\">BAIXO PERFIL MECÂNICO AVANÇADO</h2><p class=\"ql-align-center\">O G915 é nosso primeiro teclado a apresentar os switches mecânicos GL de perfil baixo e alto desempenho, que fornecem a velocidade, precisão e desempenho dos switches tradicionais com a metade da altura. Nossos switches GL são rigorosamente testados para alcançar requisitos estritos de resistência, responsividade e precisão. Disponível em três tipos de switches:</p><p class=\"ql-align-center\"><br></p><p class=\"ql-align-center\"><strong>GL Clicky</strong>:clique audível e sensação tátil</p><p class=\"ql-align-center\"><strong>GL Tactile</strong>: um toque suave com uma leve sensação tátil</p><p class=\"ql-align-center\"><strong>GL Linear</strong>: um toque de teclas completamente suave</p><p class=\"ql-align-center\"><br></p><p><br></p>','2024-06-11 16:48:01','1175111691'),('791677648','<h1><span style=\"color: rgb(1, 15, 32);\">Controle Starfield Edition Series</span></h1>','2024-03-20 16:01:00','184972226');
/*!40000 ALTER TABLE `description_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount_list`
--

DROP TABLE IF EXISTS `discount_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount_list` (
  `code` varchar(255) NOT NULL,
  `discount` double NOT NULL,
  `expire_at` timestamp NOT NULL,
  `min_value` double NOT NULL DEFAULT '0',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount_list`
--

LOCK TABLES `discount_list` WRITE;
/*!40000 ALTER TABLE `discount_list` DISABLE KEYS */;
INSERT INTO `discount_list` VALUES ('NADAMAL',0.05,'2025-01-01 00:00:01',50),('SILLICON100',100,'2025-01-01 00:00:01',999.99),('SILLICON200',200,'2027-07-22 00:24:01',1699.99);
/*!40000 ALTER TABLE `discount_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image`
--

DROP TABLE IF EXISTS `image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `image` (
  `id` varchar(255) NOT NULL,
  `id_product` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL,
  `index_image` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `image_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
INSERT INTO `image` VALUES ('0319fc5c-f19a-4461-8ae6-eef8a427f4f8','122532913','1718125352.527435macbook-air-15-chip-m2-3.jpeg',2),('03a781fa-b51c-44f3-a8fa-6f42ef0f78ac','2650605247','1718126148.937305asus-vivobook-16x-3.jpeg',2),('042ab917-7ee9-4452-814a-f704ce876f8b','1301611670','1707435524.912864macbook-pro-m3-pro-1.jpeg',0),('05c28574-3883-4337-9512-78eb433acee4','3220644470','1718126471.012435rtx-4060-asus-3.jpeg',2),('076c7d10-f099-4bef-8bba-7e987d6c9dee','1973491187','1708128547.840339iphone-14-plus-3.jpeg',3),('0791ae87-8c0a-4c54-bbea-f5437f3a2554','2663578255','1712944147.617687rtx4090-2.jpg',1),('08964e2d-7d9e-49e3-a098-77ffea8320e5','2520567394','1718124068.752202g-715-4.jpeg',3),('09adf512-7d2b-472b-b02c-4779fd0d7a66','1994704223','1718118261.471827mac-studio-m1-max-4.jpeg',3),('0b038e47-ef32-4b6f-bc21-f4db4d52c750','1175111691','1718124481.180646g915-2.jpeg',1),('0e9d85b6-f104-49e2-bb51-a5ac80a5bd76','1433408084','1712944660.2149124090asus-5.jpeg',4),('0f317405-ae5e-4086-8d02-91d3e7cdde69','3518494235','1718126001.588211asus-tuf-4.jpeg',3),('0f58c062-51c3-4b62-8b30-b67262c532a9','236442349','1718118232.297673mac-studio-m1-max-4.jpeg',3),('1417834f-bef9-4da6-adba-d361fcef0d49','3592125269','1705529758.8960488xbox-series-x-2.jpeg',2),('15451003-de77-4533-a533-fd707198e23b','1197754295','1702917824.8963342iphone15pro_5.jpeg',4),('190da25a-6e87-4898-a7a0-1e721fdc3e38','1994704223','1718118261.473341mac-studio-m1-max-5.jpeg',4),('1b272214-c12c-4f9e-ad4d-5183075ef84b','3567247046','1718123598.210887logi-g-pro-5.jpeg',4),('1b33e986-c22e-40fc-b971-774e7ef25495','2520567394','1718124068.741257g-715-2.jpeg',1),('1cc09289-004b-43a3-8074-ebbb6bbe55b1','1197754295','1702917824.8984802iphone15pro_6.jpeg',5),('1e68c829-5617-45c2-8fca-57b303a0de99','236442349','1718118232.301333mac-studio-m1-max-7.jpeg',6),('1e762532-a4ca-4f70-8536-27e37942062e','1549139476','1718124774.4764469acer-nitro-4.jpeg',3),('1e7f0585-93f2-4a4b-95ed-dc716f2a8d82','835329450','1718118321.786326mac-studio-m1-max-4.jpeg',3),('213eedcd-5cde-407e-a255-e6ca656aed34','1433408084','1712944660.2234954090asus-9.jpeg',8),('217922a1-3086-41e6-9387-d148cc877cf3','835329450','1718118321.793097mac-studio-m1-max-6.jpeg',5),('22c503c7-89e1-47f7-9816-830187912ded','2022549509','1718126729.755967rtx-4090-rog-strix-4.jpeg',3),('26fc9023-f33c-4caa-a255-e6268cb2c63f','1175111691','1718124481.183854g915-4.jpeg',3),('283b9126-8443-4913-a482-9e09557cdb95','3567247046','1718123598.213359logi-g-pro-7.jpeg',6),('2ad27779-6848-436c-8876-5add6910761a','3110931476','1718125002.688681acer-nitro-3.jpeg',2),('2ae4c80e-199e-4b9b-8f0a-ffcfb503141b','1738295407','1708129366.016474iPad-pro-12pol-2.jpeg',2),('2b49191f-aea1-431c-970b-f85c48556c74','1197754295','1702917824.89391iphone15pro_4.jpeg',3),('2b863b5c-12d5-4b24-ba97-27e77e859549','1433408084','1712944660.2193794090asus-7.jpeg',6),('2d36a5aa-16d8-4044-b05a-d1c52017b700','2378042936','1718125933.1398559asus-tuf-1.jpeg',0),('3213898b-02d1-4f59-8cdf-c7c5162b1791','1973491187','1708128547.837899iphone-14-plus-2.jpeg',2),('3535fc72-2ac0-4e85-b8e6-24d9f19ca58d','3220644470','1718126471.0149398rtx-4060-asus-4.jpeg',3),('365e40f7-4807-44e5-90dc-6953ef1511c5','3170794124','1718126295.246469Asus-Zenfone-2.jpeg',1),('37a975ee-b207-4040-aa13-300c3742b7e8','2178406116','1718124193.055447mx-4.jpeg',3),('3bf63bbd-7a78-4d6b-a7fd-4218779fd33b','3518494235','1718126001.585331asus-tuf-3.jpeg',2),('3d8a208d-d1d1-4d61-9e09-53c0d7f900e4','2650605247','1718126148.935571asus-vivobook-16x-2.jpeg',1),('3df8678e-ecad-4327-bdf1-ac73129314c9','2378042936','1718125933.147134asus-tuf-4.jpeg',3),('413f0296-2af5-4705-ab58-44312a18129b','1549139476','1718124774.475361acer-nitro-3.jpeg',2),('416524dc-0263-4479-bd19-b1552afa590e','1549139476','1718124774.4710588acer-nitro-1.jpeg',0),('41a90df5-ae90-4afb-9f38-b7d8eab79e4a','1175111691','1718124481.1854231g915-5.jpeg',4),('42dd75c0-0a30-41fa-a6ab-8fb93d00252f','3170794124','1718126295.247287Asus-Zenfone-3.jpeg',2),('4360f0c2-88f9-4be9-b85a-4e7085c5eb56','2378042936','1718125933.145293asus-tuf-3.jpeg',2),('43735006-a4df-45ec-b251-310dae3770eb','1549139476','1718124774.473807acer-nitro-2.jpeg',1),('43b8f866-6834-40c2-ac65-f01691fa8f7d','3730391284','1718126604.4061959rtx-4090-asus-5.jpeg',4),('47c52dd0-ca60-4aec-bd49-13c40e978f32','1549139476','1718124774.478794acer-nitro-6.jpeg',5),('484b3f80-68f6-4972-919c-4838f85c6ed2','1874139195','1711124440.943258ps5_5.jpeg',4),('49136683-063d-484c-ab77-688cac584712','1994704223','1718118261.468092mac-studio-m1-max-2.jpeg',2),('49f27758-ef9d-490b-8a3e-1df25749fa0e','2663578255','1712944147.61964rtx4090-3.jpg',2),('4b2177fa-9a55-488f-a884-eb2e0ac5f2c9','184972226','1710805217.003028controle-starfield-4.jpg',3),('4d113a78-aced-4f5f-b950-3eea8813edcd','1433408084','1712944660.2072734090asus-1.jpeg',0),('4ebd5a87-e325-462c-a220-c6f33bf2e230','2022549509','1718126729.75441rtx-4090-rog-strix-3.jpeg',2),('4fa1562c-5675-4941-b456-de875108fd97','3592125269','1705529758.893436xbox-series-x-1.jpeg',1),('4fb80d41-5903-45ee-8d45-8ee611a7f316','1974991426','1718118182.748031mac-studio-m1-max-2.jpeg',4),('54b80afd-4769-4c49-92be-05d26549ee9f','1433408084','1712944660.2253344090asus-10.jpeg',9),('556cc939-21ff-4aed-a490-f877b75c4ac1','3821092638','1718125843.7454238rog-srix-g16-3.jpeg',2),('56dd91a8-227f-4029-a054-eb523093ce0d','3730391284','1718126604.404854rtx-4090-asus-4.jpeg',3),('5795e18a-d336-4e80-8bc2-95be69808e80','3220644470','1718126471.0096068rtx-4060-asus-2.jpeg',1),('5b9d5301-aeb9-4b1a-9e3f-c92a1a296eaf','2520567394','1718124068.7487092g-715-3.jpeg',2),('5c2ce26f-a20d-4e8b-8e33-4e076783f690','1874139195','1711124440.938012ps5_3.jpeg',2),('5d9e03d7-a209-4256-9036-70324f7e4c4c','1874139195','1711124440.932311ps5_1.jpeg',1),('5df86764-7f80-4982-a2a1-f0d867237bcc','1175111691','1718124481.182376g915-3.jpeg',2),('5e615e61-dc0a-4ac8-a738-8992646ff87d','1974991426','1718118182.753112mac-studio-m1-max-7.jpeg',3),('5ef13a12-ca98-4c41-a66f-91b785d22f0a','1974991426','1718118182.751104mac-studio-m1-max-5.jpeg',0),('5ffeb346-275c-4ff6-b670-fc66387ba364','3110931476','1718125002.685777acer-nitro-2.jpeg',1),('61ef2666-bb85-4a81-a404-341eddf1efa1','3170794124','1718126295.2454631Asus-Zenfone-1.jpeg',0),('6208d1e4-f135-4a56-bff6-ef625a1e26ba','941978367','1718127040.853421ryzen-7-5700x3d-2.jpeg',1),('620dbf87-89d6-46f8-bfa3-26816d15670f','835329450','1718118321.78985mac-studio-m1-max-5.jpeg',4),('621969d9-39f5-4dc3-85db-59dfb43fccad','236442349','1718118232.2994719mac-studio-m1-max-5.jpeg',4),('684d64c3-b09e-4064-b0bd-ba9e32d4c1ef','1973491187','1708128547.8347719iphone-14-plus-1.jpeg',1),('69d0906f-66ca-46e1-bd9c-3644869da45a','1974991426','1718118182.75004mac-studio-m1-max-4.jpeg',6),('6b2853c4-e741-4290-bb77-031627384af5','3730391284','1718126604.4029691rtx-4090-asus-3.jpeg',2),('6c9d10a3-571a-4a33-80a9-be5ab9a689f3','3170794124','1718126295.247881Asus-Zenfone-4.jpeg',3),('6d1f19e6-d691-4871-956e-30b7d14aacda','3110931476','1718125002.6909811acer-nitro-4.jpeg',3),('6e60090e-08ad-4fe1-b2bd-9e359f308f06','835329450','1718118321.781954mac-studio-m1-max-2.jpeg',1),('711804c9-b31a-44f2-84a4-af10407e49af','3170794124','1718126295.24887Asus-Zenfone-5.jpeg',4),('747ab822-236a-4b86-8f95-955075020951','3821092638','1718125843.746637rog-srix-g16-4.jpeg',3),('75277bcd-02ad-4f16-93f4-4bdd6acfd2e7','3821092638','1718125843.749413rog-srix-g16-6.jpeg',5),('7554c6a2-1f6d-4cf9-8f45-5492bdf555aa','1165821908','1718128750.984558ryzen-7-5700x-1.jpeg',0),('776a21b6-6c5b-4a7f-bb2f-4df459d47b2d','835329450','1718118321.794471mac-studio-m1-max-7.jpeg',6),('7780001b-d9b7-4d8a-be62-72a0c1271b65','2022549509','1718126729.758977rtx-4090-rog-strix-7.jpeg',6),('78c50c93-74a5-4320-9121-3b1f202b9e0d','3821092638','1718125843.747871rog-srix-g16-5.jpeg',4),('7e143ff5-38d8-4a87-a04a-1aae80928b52','1738295407','1708129366.0176818iPad-pro-12pol-3.jpeg',3),('7e7d6535-5dbb-453a-a179-8ef4b2bfbdef','2650605247','1718126148.938637asus-vivobook-16x-5.jpeg',3),('7e8c1fd1-5f20-40d4-9705-78d5b4322df8','2022549509','1718126729.757903rtx-4090-rog-strix-6.jpeg',5),('7eaf376d-2aaa-4b0a-a133-ae5e3e24d7fe','2378042936','1718125933.1432378asus-tuf-2.jpeg',1),('8229913c-e049-44dc-82ae-a109b10b9dd1','3567247046','1718123598.2037601logi-g-pro-1.jpeg',0),('84ca602b-19fe-47ed-af0b-6e9133f6838d','1874139195','1711124440.940184ps5_4.jpeg',3),('8737638f-db55-47a7-ac5a-b2d840d9ca1b','2178406116','1718124193.052576mx-3.jpeg',2),('87b52e85-f009-43d9-a2af-66f4ab676fc9','2384805177','1718123845.586781g502-3.jpeg',2),('8878a609-d235-45fc-83f7-9a1d87b7990c','1994704223','1718118261.474903mac-studio-m1-max-6.jpeg',5),('89e626a4-74ca-4001-b1a2-08208dade137','1197754295','1702917824.881082iphone15pro_2.jpeg',1),('8a56cfac-117c-4a8f-9964-e728059e5866','1874139195','1711124440.935627ps5_2.jpeg',0),('8b5ddc9d-492f-4d32-bae6-0c305ceb8ea1','835329450','1718118321.7840471mac-studio-m1-max-3.jpeg',2),('8db0dbad-faac-470b-837f-cd65d5c3dfe9','3730391284','1718126604.39455rtx-4090-asus-1.jpeg',0),('9106c65a-6399-425f-a7fb-27784838a677','184972226','1710805216.999567controle-starfield-2.jpg',0),('969ad04f-7803-4626-b7c4-1075e123395f','3821092638','1718125843.739996rog-srix-g16-1.jpeg',0),('9762761e-582d-4981-8699-c8e5b645ae0f','2384805177','1718123845.5851252g502-2.jpeg',1),('9845b60b-b689-403e-a549-dd4e10dab5a3','2384805177','1718123845.581516g502-1.jpeg',0),('9a96b684-afcd-49d0-8110-922dd5fc906c','1549139476','1718124774.4775639acer-nitro-5.jpeg',4),('9a96b684-afcd-49d0-8110-922dd5fc90TG','1165821908','1718128750.984558ryzen-7-5700x-1.jpeg',0),('a173803d-adf1-474c-b497-9c8546f42f3f','1474542769','1718128750.984558ryzen-7-5700x-1.jpeg',NULL),('a558761b-d3ee-42b0-b379-0ad3b2ae6a6e','3220644470','1718126471.00486rtx-4060-asus-1.jpeg',0),('a6c2663f-2821-4325-9107-e76fc8eebb0b','1994704223','1718118261.470485mac-studio-m1-max-3.jpeg',1),('a83470fb-57e8-4c66-80de-4280b6abf45a','2520567394','1718124068.733839g-715-1.jpeg',0),('a8cc244b-76d5-4e46-98b9-1b954468ff28','236442349','1718118232.29618mac-studio-m1-max-3.jpeg',2),('a9328d59-e490-411a-9b28-a165a082b597','1974991426','1718118182.751831mac-studio-m1-max-6.jpeg',5),('aafd361a-4d27-498d-b707-399ec75048e1','184972226','1710805217.0040588controle-starfield-3.jpg',2),('accbd20d-36da-47d7-9b97-16a562dad30f','2178406116','1718124193.047029mx-1.jpeg',0),('ae7e1fe9-e6ff-4653-b39e-36705f60f8b7','2663578255','1712944147.6258628rtx4090-5.jpg',4),('b21e09e8-fe9e-4c17-b444-2c3370def137','3518494235','1718126001.576886asus-tuf-1.jpeg',0),('b28a33d5-b627-4c36-8b34-aee8ebe01f1f','2022549509','1718126729.752701rtx-4090-rog-strix-2.jpeg',1),('b4eb8a78-6d50-48e0-9df4-f4c6578284d8','3592125269','1705529758.8977149xbox-series-x-3.jpeg',3),('b5581854-34ff-4c41-b57d-2c896f790620','941978367','1718127040.849685ryzen-7-5700x3d-1.jpeg',0),('b6129dd4-87bd-4ca9-b456-fdfc2a9dc6d8','122532913','1718125352.519844macbook-air-15-chip-m2-1.jpeg',0),('b6df3c88-e6b5-4975-b5e8-a0819a6ba38a','1301611670','1707435524.9167528macbook-pro-m3-pro-2.jpeg',2),('b91ffc0e-c495-40b2-b2f6-4a44f35b49a3','2022549509','1718126729.749158rtx-4090-rog-strix-1.jpeg',0),('be1d393c-843a-448b-8dd3-9f415de2dc05','1197754295','1702917824.9114602iphone15pro_7.jpeg',6),('bf30faf0-5e17-422b-b108-1971137b0ce1','2663578255','1712944147.624196rtx4090-4.jpg',3),('bf8c6aa4-195d-4e5f-96c0-033a1e2c8b3e','1738295407','1708129366.018751iPad-pro-12pol-4.jpeg',4),('c19bf332-8de1-4b24-ad38-1a3beac71896','1994704223','1718118261.476477mac-studio-m1-max-7.jpeg',6),('c26c8349-cd73-470b-9b83-9a8012f01455','3730391284','1718126604.4075189rtx-4090-asus-6.jpeg',5),('c296d396-546f-43ff-b1b2-fbdbebcdad3c','1175111691','1718124481.1785789g915-1.jpeg',0),('c472dbeb-249c-461b-8e5e-9d7746ff8372','1433408084','1712944660.21687914090asus-6.jpeg',5),('c54075f8-921b-4e88-aa2b-38ffb83c1465','1433408084','1712944660.2095534090asus-2.jpeg',1),('c5cfd3e7-afc5-4435-8294-cb4cccfdacdb','3110931476','1718125002.682809acer-nitro-1.jpeg',0),('c9d5072f-2a60-4bf3-9878-6424dd4fcbe3','3518494235','1718126001.5824509asus-tuf-2.jpeg',1),('cab3e99b-bb01-4723-b09a-d871bd20d88d','122532913','1718125352.525284macbook-air-15-chip-m2-2.jpeg',1),('cbb50829-0492-4b38-95a7-3b20e90bbd62','3730391284','1718126604.396202rtx-4090-asus-2.jpeg',1),('cbcb84f3-58cb-4ed9-a8de-86773327144b','4152333900','1718123722.788718g-pro-2.jpeg',1),('cc089fba-d3ac-4459-94c8-5adbb46e930d','4152333900','1718123722.793982g-pro-4.jpeg',3),('cc4e11a9-0333-46e1-b738-6848e9757544','2178406116','1718124193.05074mx-2.jpeg',1),('ccc8abb3-2799-4961-94f7-822906a44bc4','1433408084','1712944660.21140984090asus-3.jpeg',2),('ccd11113-ea13-4b86-944c-8c9d9d8f2001','3567247046','1718123598.206272logi-g-pro-2.jpeg',1),('cde31048-93f1-4249-b39d-7868f0239aa5','4152333900','1718123722.78559g-pro-1.jpeg',0),('d18991d3-3762-4245-b440-32312328f667','236442349','1718118232.294652mac-studio-m1-max-2.jpeg',1),('d2968cbc-5cbb-42c8-a0ac-5f59879ff07c','236442349','1718118232.300373mac-studio-m1-max-6.jpeg',5),('d3536aae-922e-4a0a-ae50-6871ed2c01d7','4152333900','1718123722.789856g-pro-3.jpeg',2),('d6d0d429-729a-4b02-83f6-423407a123f4','1738295407','1708129366.014598iPad-pro-12pol-1.jpeg',1),('d7175b67-6fa8-446f-a5e6-83905002a060','2520567394','1718124068.754207g-715-5.jpeg',4),('d738218c-5231-4ab9-9ae4-921f7335789c','184972226','1710805217.001955controle-starfield-1.jpg',1),('dbb478d4-fc86-4e4e-8fb3-676c04682940','1994704223','1718118261.463524mac-studio-m1-max-1.jpeg',0),('dc36b10d-f86a-44e3-abbf-ae45d2243e04','1301611670','1707435524.921124macbook-pro-m3-pro-4.jpeg',3),('dd245d6d-e2bd-41a1-8b5d-041c7e6a236f','4080007038','1718127180.8482618ryzen-7-5700x-1.jpeg',0),('dda7f636-e331-438c-b1f6-8c0cdf73e9eb','1738295407','1708129366.0196888iPad-pro-12pol-5.jpeg',5),('ddb3e838-8e8e-4590-8f9e-a0d24ce6ddfa','2384805177','1718123845.588104g502-4.jpeg',3),('ddb66893-9386-4264-a786-84b28edae720','2022549509','1718126729.757004rtx-4090-rog-strix-5.jpeg',4),('dfe6ac37-12f4-4202-8524-1bb629a48d23','3567247046','1718123598.209784logi-g-pro-4.jpeg',3),('dfef0f44-764a-4221-9449-eb9f7febd29b','1197754295','1702917824.864584iphone15pro_1.jpeg',0),('e26afdc9-6757-41fe-91ce-c7016d02ca26','3821092638','1718125843.742976rog-srix-g16-2.jpeg',1),('e2a5c14b-e755-4cc9-8553-160086c99497','1433408084','1712944660.2213844090asus-8.jpeg',7),('e3b72ad1-53ae-48fa-853e-e6aa89b769b6','3567247046','1718123598.212288logi-g-pro-6.jpeg',5),('e3fd0c06-875d-4c3b-8e1d-2d971f3b016a','122532913','1718125352.5288582macbook-air-15-chip-m2-4.jpeg',3),('e76c4d1d-9cfb-4cc2-a752-cf4e6f6f8b04','3110931476','1718125002.693294acer-nitro-5.jpeg',4),('ea5e8790-aa96-4f59-b912-136ed61178cb','1974991426','1718118182.749006mac-studio-m1-max-3.jpeg',2),('ead59272-dc29-4369-82a3-02a0badc6e3d','236442349','1718118232.293239mac-studio-m1-max-1.jpeg',0),('ecc16cee-ae14-4823-a102-75645a0470a2','1433408084','1712944660.2136864090asus-4.jpeg',3),('efc1428a-79c2-45fd-a24a-74c87a082cce','3110931476','1718125002.6961632acer-nitro-6.jpeg',5),('f0197e44-592f-4494-bbb1-16c12ab6c51c','2650605247','1718126148.933401asus-vivobook-16x-1.jpeg',0),('f0508655-f924-4510-91a0-ac1d4dbcfaae','1197754295','1702917824.8915389iphone15pro_3.jpeg',2),('f129a265-fffb-4446-8d10-44415fc487ed','1973491187','1708128547.842051iphone-14-plus-4.jpeg',4),('f2249e60-d751-41cf-883b-a00bc09eccf3','2663578255','1712944147.615015rtx4090-1.jpg',0),('f238bf9a-c65a-4279-9eb1-f963130aa3a9','1301611670','1707435524.9191308macbook-pro-m3-pro-3.jpeg',1),('f46b2fc9-e829-4829-abde-5c317667c1fc','1974991426','1718118182.745753mac-studio-m1-max-1.jpeg',1),('f8b8d038-1cd8-497a-b378-af22a49d5822','3567247046','1718123598.208158logi-g-pro-3.jpeg',2),('fd3ace67-14f0-4612-a564-21e4c2ceee78','3730391284','1718126604.409rtx-4090-asus-7.jpeg',6),('fee8d37c-aa01-4fa3-8c1c-b011714f1ad6','2384805177','1718123845.589411g502-5.jpeg',4),('ff442298-dad5-424f-a066-d2d8197ce518','835329450','1718118321.778721mac-studio-m1-max-1.jpeg',0);
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_item`
--

DROP TABLE IF EXISTS `order_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_item` (
  `id_order_item` varchar(255) NOT NULL,
  `id_order` varchar(255) NOT NULL,
  `id_product` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id_order_item`),
  KEY `id_order` (`id_order`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `order_item_ibfk_1` FOREIGN KEY (`id_order`) REFERENCES `purchase_order` (`id_order`),
  CONSTRAINT `order_item_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_item`
--

LOCK TABLES `order_item` WRITE;
/*!40000 ALTER TABLE `order_item` DISABLE KEYS */;
INSERT INTO `order_item` VALUES ('1158804371','860940801','3592125269',1,4881.69),('1189945183','3333839500','1197754295',1,6891.69),('1284248364','1170107652','1197754295',2,6301.35),('1665410681','3191211293','1433408084',1,14077.84),('1740183223','1196224188','1301611670',1,12899.99),('2966531467','3333839500','1301611670',1,14534.61),('297903572','1720350909','1973491187',1,4599.99),('3610244804','2566930357','1738295407',1,10492.13),('368222797','3536153431','184972226',1,913.53),('3721178038','3778022946','2663578255',1,16192.31),('3934303884','3333839500','1738295407',1,11808.98),('4063589153','2751911738','1874139195',1,3099.99),('b7e6d8c1-bda9-4cb3-a954-9e38f4d25efm','b7e6d8c1-bda9-4cb3-a954-9e38f4d25efg','1197754295',1,5999),('b7e6d8c1-bda9-4cb3-a954-9e39f4d25ubg','b7e6d8c1-bda9-4cb3-a954-9e39f4d25efg','1197754295',1,6626.63);
/*!40000 ALTER TABLE `order_item` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `update_stock_of_product_after_order` AFTER INSERT ON `order_item` FOR EACH ROW BEGIN 
    DECLARE current_stock INT;
    
    -- Armazena o valor atual do estoque na variável temporária
    SELECT stock INTO current_stock FROM PRODUCT WHERE id = NEW.id_product;
    
    -- Atualiza o estoque do produto
    UPDATE PRODUCT 
    SET stock = current_stock - NEW.quantity 
    WHERE id = NEW.id_product;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `cpf` varchar(15) NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `birthday` date NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `password` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `principal_ship_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES ('7f652081-2d3a-4e27-b81e-b988a34a5ae7','Sillicon Store','000.000.000-00','admin@silliconstore.com.br','2004-06-19','(11) 97968-4799','$2b$12$OAU4QnW1SfVhKGlKilvV0eF9guLyTekgZRdG.42EVU2vR0g.JrNKa','2023-12-17 20:12:37','2024-05-21 20:19:02','3422588601'),('88c9a90d-4eb0-4908-a128-bb33f0085e2a','Miriam Ferreira José Silva','320.916.198-41','miriam_ssp@hotmail.com','1985-07-27','(11) 96029-7355','$2b$12$rYEaxd63fy4QjB6hmjurtO0ZLylORabNgKlZQH3ZAYhx/f2izhiwa','2023-12-18 13:07:30','2023-12-18 13:07:30',NULL),('b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','Lucas Ferreira Silva','520.945.658-74','lucas.lfs2004@gmail.com','2004-06-19','(11) 97968-4799','$2b$12$jK45qkLKW7tITpij378.I.LBE1pEf97bbXlHX465j5uh.4UTNPLnK','2023-12-17 20:01:05','2024-05-23 14:55:38','3304848291');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `create_cart_user` AFTER INSERT ON `person` FOR EACH ROW BEGIN 
	-- Cria a tabela cart_user
	INSERT INTO cart_user (id_person) VALUES (NEW.id);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `portion`
--

DROP TABLE IF EXISTS `portion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `portion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cart_user` varchar(255) DEFAULT NULL,
  `often` int NOT NULL,
  `value_credit` decimal(10,2) DEFAULT NULL,
  `value_portion` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_cart_user` (`id_cart_user`),
  CONSTRAINT `portion_ibfk_1` FOREIGN KEY (`id_cart_user`) REFERENCES `cart_user` (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=11297 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portion`
--

LOCK TABLES `portion` WRITE;
/*!40000 ALTER TABLE `portion` DISABLE KEYS */;
INSERT INTO `portion` VALUES (10885,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',1,22046.98,22046.98),(10886,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',2,22715.04,11357.52),(10887,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',3,23061.67,7687.22),(10888,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',4,23417.02,5854.26),(10889,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',5,23781.35,4756.27),(10890,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',6,24154.92,4025.82),(10891,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',7,24538.00,3505.43),(10892,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',8,24930.86,3116.36),(10893,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',9,25333.79,2814.87),(10894,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',10,25747.09,2574.71),(10895,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',11,26171.05,2379.19),(10896,'b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b',12,26605.98,2217.16),(11287,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',1,6238.96,6238.96),(11288,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',2,6364.36,3182.18),(11289,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',3,6428.01,2142.67),(11290,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',4,6492.29,1623.07),(11291,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',5,6557.21,1311.44),(11292,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',6,6622.78,1103.80),(11293,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',7,6689.01,955.57),(11294,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',8,6755.90,844.49),(11295,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',9,6823.46,758.16),(11296,'7f652081-2d3a-4e27-b81e-b988a34a5ae7',10,6891.69,689.17);
/*!40000 ALTER TABLE `portion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PRODUCT`
--

DROP TABLE IF EXISTS `PRODUCT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PRODUCT` (
  `id` varchar(255) NOT NULL,
  `seller_id` varchar(255) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `brand_id` int NOT NULL,
  `category_id` int NOT NULL,
  `stock` int NOT NULL,
  `warranty` int NOT NULL,
  `active` tinyint(1) NOT NULL,
  `featured` tinyint(1) NOT NULL,
  `model` varchar(150) DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `brand_id` (`brand_id`),
  KEY `category_id` (`category_id`),
  KEY `seller_id` (`seller_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`id`),
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `seller_id` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PRODUCT`
--

LOCK TABLES `PRODUCT` WRITE;
/*!40000 ALTER TABLE `PRODUCT` DISABLE KEYS */;
INSERT INTO `PRODUCT` VALUES ('1165821908','7f652081-2f45-4e27-b81e-b988a34a5fin','Processador AMD Ryzen 7 5700X, 3.4GHz (4.6GHz Max Turbo), Cache 36MB, AM4, Sem Vídeo',478247585,253562178,100,12,1,1,'undefined','2024-06-11 17:31:45','2024-06-11 17:31:45'),('1175111691','7f652081-2f45-4e27-b81e-b988a34a5fin','Teclado Logitech G915 Carbon TKL Wireless/Bluetooth Mecânico US Switch Gl Tatile',418385379,1066042836,24,12,1,1,'undefined','2024-06-11 16:48:01','2024-06-11 16:48:01'),('1197754295','7f652081-2f45-4e27-b81e-b988a34a5fin','iPhone 15 Pro Apple (512GB) Titânio Natural, Tela de 6,1\", 5G e Câmera de 48MP',270057385,144885085,49,24,1,1,'115288','2024-06-11 14:17:37','2023-12-18 16:43:44'),('122532913','7f652081-2f45-4e27-b81e-b988a34a5fin','MacBook Air Apple 15\", M2, CPU 8 Núcleos, GPU 10 Núcleos, 8GB RAM, SSD 256GB, Cinza Espacial',270057385,795519762,25,12,1,1,'undefined','2024-06-11 17:02:32','2024-06-11 17:02:32'),('1301611670','7f652081-2f45-4e27-b81e-b988a34a5fin','Notebook MacBook Pro Apple, Tela Retina 14\", Chip M3 Pro, 18GB RAM, Prateado',270057385,795519762,26,12,1,1,'MRX63BZ/A','2024-06-04 21:45:28','2024-02-08 23:38:44'),('1433408084','7f652081-2f45-4e27-b81e-b988a34a5fin','Placa de Vídeo RTX 4090 Asus NVIDIA ROG Strix, 24 GB GDDR6X, ARGB, DLSS, Ray Tracing',859051422,480423886,10,12,1,1,'undefined','2024-06-04 14:57:25','2024-04-12 17:57:40'),('1474542769','7f652081-2f45-4e27-b81e-b988a34a5fin','Processador AMD Ryzen 3 3200G, 3.6GHz (4GHz Max Turbo), Cache 4MB, Quad Core, 4 Threads, AM4',478247585,253562178,100,12,1,1,'undefined','2024-06-11 17:33:38','2024-06-11 17:33:38'),('1549139476','7f652081-2f45-4e27-b81e-b988a34a5fin','Notebook Gamer Acer Nitro V15 Intel Core i5-13420H, 8GB RAM, GeForce RTX 3050, SSD 512GB, 15.6\" FHD IPS 144Hz, Windows 11, Preto',937577720,795519762,36,12,1,1,'undefined','2024-06-11 16:58:54','2024-06-11 16:52:54'),('1738295407','7f652081-2f45-4e27-b81e-b988a34a5fin','Apple iPad Pro 12.9\" 6ª Geração, Wi-Fi, 128GB, Cinza Espacial',270057385,479191233,46,12,1,1,'MNXP3BZ/A','2024-06-11 17:26:48','2024-02-17 00:22:45'),('184972226','7f652081-2f45-4e27-b81e-b988a34a5fin','Controle Starfield Edition Series X/S, One, PC',570676007,773985694,3,3,1,1,'undefined','2024-06-04 14:58:45','2024-03-18 23:40:16'),('1874139195','7f652081-2f45-4e27-b81e-b988a34a5fin','Console Playstation 5 Sony, SSD 825GB, Controle sem fio DualSense, Com Mídia Física, Branco',222272032,773985694,23,12,1,1,'undefined','2024-06-04 14:59:03','2024-03-22 16:20:40'),('1973491187','7f652081-2f45-4e27-b81e-b988a34a5fin','Iphone 14 Plus Apple, 256GB, Câmera Dupla 12MP + Selfie 12MP, Tela de 6.7\", Azul - MQ583BR/A',270057385,144885085,49,12,1,1,'MQ583BR/A','2024-06-04 15:01:10','2024-02-17 00:09:07'),('1974991426','7f652081-2f45-4e27-b81e-b988a34a5fin',' Mac Studio Apple, 64GB RAM, CPU 24 Núcleos, GPU 60 núcleos, Neural Engine 32 núcleos, SSD 1TB - Prata',270057385,455143761,12,12,1,1,'undefined','2024-06-11 15:03:02','2024-06-11 15:03:02'),('1994704223','7f652081-2f45-4e27-b81e-b988a34a5fin',' Mac Studio Apple, 64GB RAM, CPU 24 Núcleos, GPU 60 núcleos, Neural Engine 32 núcleos, SSD 2TB - Prata',270057385,455143761,12,12,1,1,'undefined','2024-06-11 15:04:21','2024-06-11 15:04:21'),('2022549509','7f652081-2f45-4e27-b81e-b988a34a5fin','Placa de Vídeo RTX 4090 ROG Strix Edition Asus NVIDIA GeForce, 24 GB GDDR6X, ARGB, DLSS, Ray Tracing, Branco',859051422,480423886,26,24,1,1,'undefined','2024-06-11 17:25:29','2024-06-11 17:25:29'),('2178406116','7f652081-2f45-4e27-b81e-b988a34a5fin','Teclado Sem Fio Logitech MX Keys S, Com Iluminação Inteligente, Bluetooth ou USB, Logi Bolt e Bateria Recarregável, Grafite',418385379,1066042836,24,12,1,1,'undefined','2024-06-11 16:43:13','2024-06-11 16:43:13'),('236442349','7f652081-2f45-4e27-b81e-b988a34a5fin',' Mac Studio Apple, 32GB RAM, CPU 24 Núcleos, GPU 60 núcleos, Neural Engine 32 núcleos, SSD 1TB - Prata',270057385,455143761,12,12,1,1,'undefined','2024-06-11 15:03:52','2024-06-11 15:03:52'),('2378042936','7f652081-2f45-4e27-b81e-b988a34a5fin','Notebook Gamer ASUS TUF Gaming F15, Intel Core i7-12700H, 8GB RAM, GeForce RTX 3050, SSD 512GB, 15.6, Full HD 144Hz, KeepOS, Cinza',859051422,795519762,40,12,1,1,'undefined','2024-06-11 17:12:13','2024-06-11 17:12:13'),('2384805177','7f652081-2f45-4e27-b81e-b988a34a5fin','Mouse Gamer Sem Fio Logitech G502 X Plus, RGB, 25600 DPI, 13 Botões, Switch, Preto',418385379,1066042836,15,12,1,1,'undefined','2024-06-11 16:37:25','2024-06-11 16:37:25'),('2520567394','7f652081-2f45-4e27-b81e-b988a34a5fin','Teclado Mecânico Gamer Sem Fio Logitech G715 LIGHTSPEED Switch GX Brown Tactile, RGB, Layout ABNT, Apoio em Formato de Nuvem',418385379,1066042836,70,12,1,1,'undefined','2024-06-11 16:41:08','2024-06-11 16:41:08'),('2564146670','7f652081-2f45-4e27-b81e-b988a34a5fin','Processador AMD Ryzen 9 5900X, 3.7GHz (4.8GHz Max Turbo), Cache 70MB, 12 Núcleos, 24 Threads, AM4',478247585,253562178,100,12,1,1,'undefined','2024-06-11 17:35:06','2024-06-11 17:32:27'),('2628540100','7f652081-2f45-4e27-b81e-b988a34a5fin','Processador AMD Ryzen 7 7800X3D, 5.0GHz Max Turbo, Cache 104MB, AM5, 8 Núcleos, Vídeo Integrado',478247585,253562178,100,12,1,1,'undefined','2024-06-11 17:34:16','2024-06-11 17:34:16'),('2650605247','7f652081-2f45-4e27-b81e-b988a34a5fin','Notebook Gamer ASUS Vivobook 16X Intel Core I5-12450H, 8GB, SSD 512GB, Tela 16, RTX 2050, Win 11, Preto',859051422,795519762,40,12,1,1,'undefined','2024-06-11 17:15:48','2024-06-11 17:15:48'),('2663578255','7f652081-2f45-4e27-b81e-b988a34a5fin','Placa de Vídeo NVIDIA GeForce RTX 4090 Founders Edition',320535756,480423886,5,12,1,1,'RTX-4090','2024-06-11 16:14:59','2024-04-12 17:49:07'),('3110931476','7f652081-2f45-4e27-b81e-b988a34a5fin','Notebook Gamer Acer Nitro V15 Intel Core i5-13420H, 8GB RAM, GeForce RTX 3050, SSD 512GB, 15.6\" FHD IPS 144Hz, Windows 11, Preto',583708911,795519762,36,12,1,1,'undefined','2024-06-11 16:56:42','2024-06-11 16:56:42'),('3170794124','7f652081-2f45-4e27-b81e-b988a34a5fin','Smartphone Asus Zenfone 9, 5G, 256GB, 8GB RAM, Câmera Dupla 50MP, Com Ois + 12MP Wide, Tela 5.92, Azul',859051422,144885085,8,12,1,1,'undefined','2024-06-11 17:18:15','2024-06-11 17:18:15'),('3220644470','7f652081-2f45-4e27-b81e-b988a34a5fin','Placa de vídeo RTX 4060 ASUS Dual O8G EVO NVIDIA GeForce, 8GB GDDR6, G-SYNC, Ray Tracing',859051422,480423886,80,24,1,1,'undefined','2024-06-11 17:21:10','2024-06-11 17:21:10'),('3518494235','7f652081-2f45-4e27-b81e-b988a34a5fin','Notebook Gamer ASUS TUF Gaming F15, Intel Core i7-12700H, 8GB RAM, GeForce RTX 3050, SSD 512GB, 15.6, Full HD 144Hz, KeepOS, Cinza',859051422,795519762,40,12,1,1,'undefined','2024-06-11 17:13:21','2024-06-11 17:13:21'),('3567247046','7f652081-2f45-4e27-b81e-b988a34a5fin','Mouse Gamer Sem Fio Logitech G Pro X Superlight 2 com Lightspeed, 32000 DPI, Sensor Hero 2, com Bateria Recarregável, Preto',418385379,1066042836,18,12,1,1,'undefined','2024-06-11 16:33:18','2024-06-11 16:33:18'),('3592125269','7f652081-2f45-4e27-b81e-b988a34a5fin',' Console Xbox Series X + Forza Horizon 5, Edição Premium, Microsoft - RRT-00057',570676007,773985694,41,12,1,1,NULL,'2024-06-04 14:58:28','2024-01-17 22:15:58'),('3730391284','7f652081-2f45-4e27-b81e-b988a34a5fin','Placa de Vídeo RTX 4090 Asus NVIDIA TUF Gaming GeForce Edition, 24GB GDDR6X, DLSS, Ray Tracing',859051422,480423886,26,24,1,1,'undefined','2024-06-11 17:23:24','2024-06-11 17:23:24'),('3821092638','7f652081-2f45-4e27-b81e-b988a34a5fin','Notebook Gamer Asus Rog Strix G16 Intel Core i9-13980HX, 16GB RAM, Nvidia GeForce RTX 4060 8GB, SSD 512GB, 16\'\' Full HD 165Hz, IPS 100% sRGB, Win 11, Cinza',859051422,795519762,40,12,1,1,'undefined','2024-06-11 17:10:43','2024-06-11 17:10:43'),('4080007038','7f652081-2f45-4e27-b81e-b988a34a5fin',' Processador AMD Ryzen 5 5600X, 3.7GHz (4.6GHz Max Turbo), Cache 35MB, 6 Núcleos, 12 Threads, AM4',478247585,253562178,100,12,1,1,'undefined','2024-06-11 17:33:00','2024-06-11 17:33:00'),('4152333900','7f652081-2f45-4e27-b81e-b988a34a5fin','Mouse Gamer Sem Fio Logitech G PRO Wireless LIGHTSPEED, RGB LIGHTSYNC, Ambidestro, 6 Botões Programáveis, HERO 25K',418385379,1066042836,15,12,1,1,'undefined','2024-06-11 16:35:22','2024-06-11 16:35:22'),('835329450','7f652081-2f45-4e27-b81e-b988a34a5fin',' Mac Studio Apple, 64GB RAM, Chip M1 Ultra, SSD 4TB - Prata',270057385,455143761,8,12,1,1,'undefined','2024-06-11 15:05:21','2024-06-11 15:05:21'),('941978367','7f652081-2f45-4e27-b81e-b988a34a5fin','Processador AMD Ryzen 7 5700X3D, 3.6 GHz, (4.1GHz Max Turbo), Cachê 4MB, 8 Núcleos, 16 Threads, AM4',478247585,253562178,100,12,1,1,'undefined','2024-06-11 17:30:40','2024-06-11 17:30:40');
/*!40000 ALTER TABLE `PRODUCT` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `BEFORE_DELETE_PRODUCT` BEFORE DELETE ON `product` FOR EACH ROW BEGIN 
	-- EXCLUIR REGISTROS DE RATING RELACIONADOS
	-- EXCLUIR REGISTROS DE RATING RELACIONADOS
	DELETE FROM rating WHERE id_product = OLD.id;
	-- Excluir registros de comentários
	DELETE FROM comment WHERE id_product = OLD.id;
	-- Excluir registros de image relacionados
	DELETE FROM image WHERE id_product = OLD.id;

	-- Excluir registros de cart_items relacionados
	DELETE FROM cart_items WHERE id_product = OLD.id;

	-- Excluir registros de value_product relacionados
	DELETE FROM value_product WHERE id_product = OLD.id;
	DELETE FROM description_product where id_product = OLD.id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `purchase_order`
--

DROP TABLE IF EXISTS `purchase_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_order` (
  `id_order` varchar(255) NOT NULL,
  `id_customer` varchar(255) NOT NULL,
  `order_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status_order` enum('pending','processing','completed','canceled') NOT NULL,
  `total_value` double NOT NULL,
  `payment_method` enum('pix','credit-card','boleto') NOT NULL,
  `portions_value` double DEFAULT '0',
  `often` int DEFAULT '0',
  `delivery_street` varchar(255) NOT NULL,
  `delivery_city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `delivery_state` varchar(50) NOT NULL,
  `delivery_cep` varchar(10) NOT NULL,
  `delivery_number` int NOT NULL,
  `delivery_complement` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `discount_value` double DEFAULT '0',
  `ship_value` double DEFAULT '0',
  `delivery_receiver` varchar(255) NOT NULL,
  PRIMARY KEY (`id_order`),
  KEY `id_customer` (`id_customer`),
  CONSTRAINT `purchase_order_ibfk_1` FOREIGN KEY (`id_customer`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_order`
--

LOCK TABLES `purchase_order` WRITE;
/*!40000 ALTER TABLE `purchase_order` DISABLE KEYS */;
INSERT INTO `purchase_order` VALUES ('1170107652','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-11 14:17:37','completed',12477.92,'credit-card',12477.92,1,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Amanda Ferreira José Silva'),('1196224188','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 14:56:20','completed',12899.99,'pix',0,0,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('1720350909','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 15:01:10','completed',4599.99,'boleto',0,0,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('2566930357','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 14:58:08','completed',10492.13,'credit-card',1748.69,6,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('2751911738','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 14:59:03','completed',3099.99,'boleto',0,0,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('3191211293','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 14:57:25','completed',14077.84,'credit-card',1173.15,12,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('3333839500','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 21:45:28','completed',31573.52,'credit-card',3157.35,10,'Rua Coronel Juliano','São Paulo','SP','04782-100',34,'Escritório',1379.95,0,'Miriam Ferreira José Silva'),('3536153431','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 14:58:45','completed',904.49,'credit-card',904.49,1,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('3778022946','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 14:59:18','completed',16031.99,'credit-card',16031.99,1,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('860940801','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-06-04 14:58:28','completed',4881.69,'credit-card',697.38,7,'Rua Vicente do Rego Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('b7e6d8c1-bda9-4cb3-a954-9e38f4d25efg','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-05-28 16:15:28','completed',5999,'pix',NULL,NULL,'Rua Vicente do Rêgo Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva'),('b7e6d8c1-bda9-4cb3-a954-9e39f4d25efg','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','2024-05-25 00:00:00','completed',6626.63,'credit-card',662.66,10,'Rua Vicente do Rêgo Monteiro','São Paulo','SP','04843-060',137,'Casa',0,0,'Lucas Ferreira Silva');
/*!40000 ALTER TABLE `purchase_order` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_unicode_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`%`*/ /*!50003 TRIGGER `clear_cart_after_insert_in_purchase_order` AFTER INSERT ON `purchase_order` FOR EACH ROW BEGIN 
	-- Atualiza o valor_total na tabela cart_user
	DELETE FROM `cart_items` WHERE cart_items.id_person = NEW.id_customer;

    UPDATE cart_user SET discount = 0, discount_value = 0, voucher = NULL, portions = 0, ship_value = 0, cart_total_value = 0, ship_cep = NULL, ship_street = NULL, ship_deadline = NULL, ship_id = NULL WHERE id_person = NEW.id_customer;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `rating`
--

DROP TABLE IF EXISTS `rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rating` (
  `id` varchar(255) NOT NULL,
  `id_product` varchar(255) NOT NULL,
  `amount` int NOT NULL,
  `rating` double NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `rating_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rating`
--

LOCK TABLES `rating` WRITE;
/*!40000 ALTER TABLE `rating` DISABLE KEYS */;
INSERT INTO `rating` VALUES ('1165821908','1165821908',0,0,'2024-06-11 17:31:45'),('1175111691','1175111691',0,0,'2024-06-11 16:48:01'),('1197754295','1197754295',4,4.88,'2023-12-18 16:43:44'),('122532913','122532913',0,0,'2024-06-11 17:02:32'),('1301611670','1301611670',1,5,'2024-02-08 23:38:44'),('1433408084','1433408084',1,4.5,'2024-04-12 17:57:40'),('1474542769','1474542769',0,0,'2024-06-11 17:33:38'),('1549139476','1549139476',0,0,'2024-06-11 16:52:54'),('1738295407','1738295407',1,4.5,'2024-02-17 00:22:46'),('184972226','184972226',1,5,'2024-03-18 23:40:17'),('1874139195','1874139195',0,0,'2024-03-22 16:20:40'),('1973491187','1973491187',0,0,'2024-02-17 00:09:07'),('1974991426','1974991426',0,0,'2024-06-11 15:03:02'),('1994704223','1994704223',0,0,'2024-06-11 15:04:21'),('2022549509','2022549509',0,0,'2024-06-11 17:25:29'),('2178406116','2178406116',0,0,'2024-06-11 16:43:13'),('236442349','236442349',0,0,'2024-06-11 15:03:52'),('2378042936','2378042936',0,0,'2024-06-11 17:12:13'),('2384805177','2384805177',0,0,'2024-06-11 16:37:25'),('2520567394','2520567394',0,0,'2024-06-11 16:41:08'),('2564146670','2564146670',0,0,'2024-06-11 17:32:27'),('2628540100','2628540100',0,0,'2024-06-11 17:34:16'),('2650605247','2650605247',0,0,'2024-06-11 17:15:48'),('2663578255','2663578255',0,0,'2024-04-12 17:49:07'),('3110931476','3110931476',0,0,'2024-06-11 16:56:42'),('3170794124','3170794124',0,0,'2024-06-11 17:18:15'),('3220644470','3220644470',0,0,'2024-06-11 17:21:11'),('3518494235','3518494235',0,0,'2024-06-11 17:13:21'),('3567247046','3567247046',0,0,'2024-06-11 16:33:18'),('3592125269','3592125269',1,5,'2024-01-17 22:15:58'),('3730391284','3730391284',0,0,'2024-06-11 17:23:24'),('3821092638','3821092638',0,0,'2024-06-11 17:10:43'),('4080007038','4080007038',0,0,'2024-06-11 17:33:00'),('4152333900','4152333900',0,0,'2024-06-11 16:35:22'),('835329450','835329450',0,0,'2024-06-11 15:05:21'),('941978367','941978367',0,0,'2024-06-11 17:30:40');
/*!40000 ALTER TABLE `rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller`
--

DROP TABLE IF EXISTS `seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seller` (
  `id` varchar(255) NOT NULL,
  `id_person` varchar(255) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `seller` tinyint(1) NOT NULL,
  `store_name` varchar(255) NOT NULL DEFAULT 'Sillicon Store',
  PRIMARY KEY (`id`),
  KEY `id_person` (`id_person`),
  CONSTRAINT `seller_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller`
--

LOCK TABLES `seller` WRITE;
/*!40000 ALTER TABLE `seller` DISABLE KEYS */;
INSERT INTO `seller` VALUES ('7f652081-2f45-4e27-b81e-b988a34a5fin','7f652081-2d3a-4e27-b81e-b988a34a5ae7',1,1,'Sillicon Store');
/*!40000 ALTER TABLE `seller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ship_info`
--

DROP TABLE IF EXISTS `ship_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ship_info` (
  `id` varchar(255) NOT NULL,
  `id_person` varchar(255) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `district` varchar(50) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `receiver` varchar(100) NOT NULL,
  `street` varchar(255) NOT NULL,
  `cep` varchar(9) NOT NULL,
  `complement` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `number` int NOT NULL,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_id_person` (`id_person`),
  CONSTRAINT `fk_id_person` FOREIGN KEY (`id_person`) REFERENCES `person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ship_info`
--

LOCK TABLES `ship_info` WRITE;
/*!40000 ALTER TABLE `ship_info` DISABLE KEYS */;
INSERT INTO `ship_info` VALUES ('1008862567','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa - Lucas','(11) 979684799','Parque Brasil','São Paulo','SP','LUKETA','Rua Vicente do Rego Monteiro','04843060','Casa',137,'2024-05-21 19:25:17'),('1034091200','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa','(11) 97968-4799','Parque Brasil','São Paulo','SP','Lucas Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:22:03'),('1143478168','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','sfafadfadf','Rua Vicente do Rego Monteiro','04843-060','Casa',1,'2024-05-21 19:46:40'),('1296208071','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','Luketa','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:31:28'),('132875342','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','snifniasnfn','Rua Vicente do Rego Monteiro','04843-060','Casa',1,'2024-05-21 19:44:59'),('1375959665','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','Luketaaaaaaa','Rua Vicente do Rego Monteiro','04843-060','Casa',3,'2024-05-21 20:19:11'),('1454164537','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','Escritório - Mãe','(11) 96029-7355','Capela do Socorro','São Paulo','SP','Miriam Ferreira José Silva','Rua Coronel Juliano','04782-100','Escritório',34,'2024-05-23 14:37:49'),('1600443684','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 979684799','Parque Brasil','São Paulo','SP','fafagadg','Rua Vicente do Rego Monteiro','04843060','Casa',1,'2024-05-21 20:05:19'),('1993019035','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa Joh','(11) 932808999','Parque América','São Paulo','SP','Joelma Souza pereira','Rua Nazaré Prado','04822-230','Casa',86,'2024-05-02 20:37:18'),('1994578586','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa - Miriam Ferreira Silva','(11) 96029-7355','Parque Brasil','São Paulo','SP','Miriam Ferreira José Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-03-08 01:49:14'),('2162066413','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','sfafadfadf','Rua Vicente do Rego Monteiro','04843-060','Casa',1,'2024-05-21 19:46:10'),('2212791701','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','LUKETA','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:31:34'),('2427873343','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:28:26'),('2465275346','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','snifniasnfn','Rua Vicente do Rego Monteiro','04843-060','Casa',1,'2024-05-21 19:44:43'),('2498303779','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa - TITA','(11) 979684799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-02 20:37:18'),('2704260458','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa - Lucas','(11) 979684799','Parque Brasil','São Paulo','SP','LUKETA','Rua Vicente do Rego Monteiro','04843060','Casa',137,'2024-05-21 19:25:23'),('2705090734','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','Luketa','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:30:19'),('2721072783','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Escritório','(11) 97968-4799','Itaim Bibi','São Paulo','SP','Lucas Ferreira Silva','Rua Iguatemi','01451-010','Conjunto 192',192,'2024-03-08 00:04:39'),('2726177617','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','nindinindfin','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:31:57'),('2831930019','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 979684799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843060','Casa',1,'2024-05-21 20:04:14'),('291507482','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:28:34'),('3185475352','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','Lucas Ferreira Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',1,'2024-05-21 19:41:04'),('320031814','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:28:58'),('3304848291','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','Casa - TITA','(11) 97968-4799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-23 14:55:38'),('3319936275','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa - Lucas','(11) 979684799','Parque Brasil','São Paulo','SP','LUKETA','Rua Vicente do Rego Monteiro','04843060','Casa',137,'2024-05-21 19:25:09'),('3325776328','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','Lucas Ferreira Silva','Rua Vicente do Rego Monteiro','04843-060','Conjunto 192',137,'2024-05-21 18:55:45'),('3422588601','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','LUKETA','Rua Vicente do Rego Monteiro','04843-060','Casa',3,'2024-05-21 20:19:02'),('3479093020','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','Lucas Ferreira Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:23:32'),('3512828124','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa - TITA','(11) 979684799','Parque América','São Paulo','SP','Lucas Ferreira Silva','Rua Nazaré Prado','04822230','Conjunto 192',36,'2024-05-21 18:58:13'),('3559828748','7f652081-2d3a-4e27-b81e-b988a34a5ae7','asas','(11) 97968-4799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',1,'2024-05-21 19:17:54'),('3684565205','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','Lucas Ferreira','Rua Vicente do Rego Monteiro','04843-060','Casa',6,'2024-05-23 14:55:16'),('3742389233','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','Luketa','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:29:50'),('3773156111','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:28:30'),('3788061362','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 979684799','Parque Brasil','São Paulo','SP','innindiaifnifefaggae','Rua Vicente do Rego Monteiro','04843060','Casa',1,'2024-05-21 20:05:40'),('381383487','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','nuun','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:33:31'),('3824655004','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','Luketa','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:29:04'),('3941560287','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','alooooo','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:31:50'),('4040125423','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Itaim Bibi','São Paulo','SP','Lucas Ferreira Silva','Rua Iguatemi','01451-010','Casa',137,'2024-05-21 19:23:52'),('4054300763','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','sfafadfadf','Rua Vicente do Rego Monteiro','04843-060','Casa',1,'2024-05-21 19:47:33'),('4273159423','b7e6d8c1-bda9-4cb3-a954-9e39f4d25e5b','Copagaz','(11) 96029-7364','Veleiros','São Paulo','SP','Douglas Pereira da Silva','Avenida Berna','04774-020','Copagaz',137,'2024-05-23 14:55:03'),('432763917','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','nindinindfin','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:33:25'),('497824042','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Lucas Ferreira Silva','(11) 97968-4799','Parque Brasil','São Paulo','SP','Luketa','Rua Vicente do Rego Monteiro','04843-060','Casa',3,'2024-05-21 20:19:06'),('517656228','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa - TITA','(11) 979684799','Parque Brasil','São Paulo','SP','Amanda Ferreira José Silva','Rua Vicente do Rego Monteiro','04843060','Casa',137,'2024-05-21 19:24:55'),('7d352081-2d3a-4e27-b81e-b988a34a5ae7','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Casa','(11) 97968-4799','Parque Brasil','São Paulo','SP','Lucas Ferreira Silva','Rua Vicente do Rêgo Monteiro','04843-060','Casa',137,'2024-02-07 23:33:44'),('7e352581-2d3a-4e27-b81e-b988a34a5ae7','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Escritório','(11) 97968-4799','Interlagos','São Paulo','SP','Miriam Ferreira José Silva','Rua Coronel Julia','04782-100','Escritório',34,'2024-02-07 23:33:44'),('873217050','7f652081-2d3a-4e27-b81e-b988a34a5ae7','Apple iPad Pro 12.9\" 6ª','(11) 97968-4799','Parque Brasil','São Paulo','SP','nindinindfin','Rua Vicente do Rego Monteiro','04843-060','Casa',137,'2024-05-21 19:33:17');
/*!40000 ALTER TABLE `ship_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ship_value`
--

DROP TABLE IF EXISTS `ship_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ship_value` (
  `region` varchar(50) NOT NULL,
  `value` double NOT NULL,
  `deadline` int NOT NULL,
  PRIMARY KEY (`region`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ship_value`
--

LOCK TABLES `ship_value` WRITE;
/*!40000 ALTER TABLE `ship_value` DISABLE KEYS */;
INSERT INTO `ship_value` VALUES ('CENTRO-OESTE',8.99,7),('NORDESTE',9.99,10),('NORTE',24.99,15),('SUDESTE',0,3),('SUL',3.99,5);
/*!40000 ALTER TABLE `ship_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `value_product`
--

DROP TABLE IF EXISTS `value_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `value_product` (
  `id` varchar(255) NOT NULL,
  `id_product` varchar(255) NOT NULL,
  `price_now` double DEFAULT NULL,
  `common_price` double NOT NULL,
  `portions` int NOT NULL,
  `fees_monthly` double DEFAULT '0',
  `fees_credit` double DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id_product` (`id_product`),
  CONSTRAINT `value_product_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `value_product`
--

LOCK TABLES `value_product` WRITE;
/*!40000 ALTER TABLE `value_product` DISABLE KEYS */;
INSERT INTO `value_product` VALUES ('05599262-0d46-41b5-a1aa-c701948fb900','2384805177',NULL,799.99,12,1,0.4),('09286d72-2229-48e4-9846-fc192c2b2e71','3518494235',NULL,5349.99,12,1,1),('20bfdcb3-12d4-493f-a9e7-f0eb780ba861','2378042936',NULL,5349.99,12,1,1),('25627058-b081-48dc-8e0a-8ca825382cb5','1474542769',NULL,449.99,12,1,1),('297ece56-7cef-4540-aa3e-6a8c041e6ef1','835329450',29999.89,32799.89,12,1,0.5),('2be8e636-cdce-49a0-98cd-f1cda458e7ec','236442349',27299.89,29999.89,12,1,0.5),('3856d1dc-3207-481c-a86e-03ec51f6ed3a','184972226',899.99,999.99,10,1,0.5),('407657cd-917b-48e4-93a4-c5926e8f080c','4080007038',NULL,1149.99,12,1,1),('41a02b97-97f6-43ff-b796-0b0d1132fe08','1165821908',NULL,1499.99,12,1,1),('434665ea-18b7-4b7c-8649-8e9bfa4e1af2','2520567394',NULL,739.99,12,1,0.4),('443f236b-0000-420a-8380-daa3c61d96a0','2178406116',NULL,589.49,12,1,0.4),('4ee24495-40aa-4356-ba04-3bc0aaae7f6f','1175111691',NULL,999.99,10,1,0.4),('51a3fa02-9f26-4756-beeb-294cae9cab29','3730391284',NULL,10599.99,12,1,1),('58d0e7e8-e6a2-4f08-96f4-2dac715620b7','1738295407',NULL,8699.99,12,3,1),('598a6523-b500-4532-a272-aaa30ce35e36','3170794124',NULL,4999.99,12,1,1),('63ee8912-06d5-41ee-a585-84dc21e0d6da','1994704223',NULL,38799.89,12,1,0.5),('6ff30ddf-df1e-4476-a0b0-b0c944baca92','941978367',NULL,2899.99,12,1,1),('74735cf7-9345-4c5d-b12d-7da39e5fcaad','4152333900',NULL,489.99,10,1,0.3),('7afe4c85-8bf7-4b13-a6f8-80407406b319','2663578255',NULL,15999.99,12,1,0.2),('88d8a34a-c218-4683-817a-ff97d19303f6','3592125269',NULL,4299.99,12,1.4,3),('92182631-e0a2-41d7-bd83-a5726447d40a','3567247046',NULL,659.99,10,1,0.3),('a7a602a0-cdf1-4d77-b167-1922e33efdc5','1973491187',NULL,4599.99,12,2,0.5),('a90ab0bd-04f1-401a-ab30-d17d915e5a8d','122532913',NULL,10899.99,8,0.65,0.3),('aab52de2-65a0-4baa-ac56-5e703ec85de3','3821092638',NULL,11799.99,12,1,1),('b3100125-91c1-409f-83f4-c8a2e0fe7890','3110931476',NULL,3999.99,12,1,0.2),('b6285d64-fcfb-45d5-a4f3-a30777e99041','1433408084',NULL,12999.99,12,0.5,2),('b7bae492-d4ea-42af-9e3f-cfcfd1b07bd6','2650605247',NULL,3949.99,12,1,1),('c24d83f2-8d9c-41fd-b25c-f16b9580cb1b','1549139476',NULL,3999.99,12,1,0.2),('ca16d817-e839-40b1-ad82-e680142682d9','1197754295',5999,8999.99,10,1,4),('d2cebf39-233b-403c-b4d3-f2cb44a94544','1974991426',NULL,34499.89,12,1,0.5),('d5c0de75-9b78-4dde-93ad-ed5bf823dc7b','1874139195',3099.99,3159.99,12,1,0.8),('e05aeffd-0b4b-4d06-b50d-74267289dceb','2022549509',NULL,11899.99,12,1,1),('e30e24e9-833e-4d14-8309-9ba8db44f22f','3220644470',NULL,2139.99,12,1,1),('e4efe252-e774-444d-9a59-818ea51bdeaf','1301611670',12899.99,14999.99,12,1,2),('f03e453c-afe2-48f5-8eba-9798add0afa7','2628540100',NULL,2449.99,12,1,1),('fd5ca498-a5e5-4ac7-b5cd-263d5c77d08a','2564146670',NULL,1749.99,12,1,1);
/*!40000 ALTER TABLE `value_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-11 20:33:00
