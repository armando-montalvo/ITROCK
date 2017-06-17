CREATE TABLE S_DEPT
(ID		INT(7) PRIMARY KEY AUTO_INCREMENT,
NAME		VARCHAR(25) NOT NULL,
REGION_ID 	INT(7));

CREATE TABLE S_EMP
(ID		INT(7) PRIMARY KEY AUTO_INCREMENT,
LAST_NAME	VARCHAR(25) NOT NULL,
FIRST_NAME	VARCHAR(25),
USERID		VARCHAR(8) NOT NULL,
START_DATE      DATE,
COMMENTS        VARCHAR(100),
MANAGER_ID      INT(7),
TITLE           VARCHAR(25),
DEPT_ID         INT(7),
SALARY          DEC(11,2),
COMMISSION_PCT  DEC(4,2),
CONSTRAINT dept_id_s_emp_fk FOREIGN KEY(DEPT_ID) REFERENCES s_dept(ID));

CREATE TABLE S_CUSTOMER
(ID 		INT(7) PRIMARY KEY AUTO_INCREMENT,
NAME 		VARCHAR(50)  NOT NULL,
PHONE		VARCHAR(25),
ADDRESS		VARCHAR(50),
CITY		VARCHAR(30),
STATE		VARCHAR(20),
COUNTRY	 	VARCHAR(30),
ZIP_CODE 	VARCHAR(75),
CREDIT_RATING	VARCHAR(9),
SALES_REP_ID	INT(7),
REGION_ID	INT(7),
COMMENTS	VARCHAR(200),
CONSTRAINT sales_rep_id_fk FOREIGN KEY(SALES_REP_ID) REFERENCES S_EMP(ID));

CREATE TABLE S_ORD
(ID		INT(7) PRIMARY KEY AUTO_INCREMENT,
CUSTOMER_ID	INT(7) NOT NULL,
DATE_ORDERED    DATE,
DATE_SHIPPED    DATE,
SALES_REP_ID    INT(7),
TOTAL		DEC(11,2),
PAYMENT_TYPE    VARCHAR(6),
ORDER_FILLED	VARCHAR(1),
CONSTRAINT customer_id_fk FOREIGN KEY(customer_id) REFERENCES S_CUSTOMER(ID),
CONSTRAINT s_emp_id_fk FOREIGN KEY(sales_rep_id) REFERENCES S_EMP(id));

CREATE TABLE S_PRODUCT
(ID		INT(7) PRIMARY KEY AUTO_INCREMENT,
NAME		VARCHAR(50) NOT NULL,
SHORT_DESC	VARCHAR(200),
LONGTEXT_ID	INT(7),
IMAGE_ID 	INT(7),
SUGGESTED_WHLSL_PRICE  DEC(11,2),
WHLSL_UNITS	VARCHAR(25));

CREATE TABLE S_ITEM
(ORD_ID			INT(7) NOT NULL,
ITEM_ID			INT(7) NOT NULL,
PRODUCT_ID  		INT(7) NOT NULL,
PRICE			DEC(11,2),
QUANTITY		INT(9),
QUANTITY_SHIPPED	INT(9),
CONSTRAINT s_item_ord_id_fk FOREIGN KEY(ord_id) REFERENCES S_ORD(ID),
CONSTRAINT s_item_product_id_fk FOREIGN KEY(product_id) REFERENCES S_PRODUCT(ID));


create table s_inventory
(product_id    INT(7) not null,
warehouse_id   INT(7) primary key,
amount_in_stock INT(9),
reorder_point   INT(9),
max_in_stock    INT(9),
out_of_stock_explanation VARCHAR(200),
restock_date    date,
constraint product_id_inven_fk foreign key(PRODUCT_ID) references s_product(id));


insert into s_dept values(10,'Finance',1);
insert into s_dept values(31,'Sales',1);
insert into s_dept values(32,'Sales',2);
insert into s_dept values(33,'Sales',3);
insert into s_dept values(34,'Sales',4);
insert into s_dept values(35,'Sales',5);
insert into s_dept values(41,'Operations',1);
insert into s_dept values(42,'Operations',2);
insert into s_dept values(43,'Operations',3);
insert into s_dept values(44,'Operations',4);
insert into s_dept values(45,'Operations',5);
insert into s_dept values(50,'Administration',1);

INSERT INTO S_EMP VALUES(1,'Velasquez','Carmen','cvelasqu','1990-03-03',null,null,'President',50,2500,null);
INSERT INTO S_EMP VALUES(2,'Ngao','LaDoris','lngao','1990-03-08',null,1,'VP,Operations',41,1450,null);
INSERT INTO S_EMP VALUES(3,'Nagayama','Midori','mnagayam','1991-06-17',null,1,'VP,Sales',10,1450,null);
INSERT INTO S_EMP VALUES(4,'Quick-To-See','Mark','mquickto','1990-04-07',null,1,'VP,Finance',10,1450,null);
INSERT INTO S_EMP VALUES(5,'Ropeburn','Audry','aropebur','1990-03-04',null,1,'VP,Administration',50,1550,null);
INSERT INTO S_EMP VALUES(6,'Urguhart','Molly','murguhar','1991-06-18',null,2,'Warehouse Manager',41,1200,null);
INSERT INTO S_EMP VALUES(7,'Menchu','Roberta','rmenchu','1990-05-14',null,2,'Warehouse Manager',42,1250,null);
INSERT INTO S_EMP VALUES(8,'Biri','Ben','bbiri','1990-04-07',null,2,'Warehouse Manager',43,1100,null);
INSERT INTO S_EMP VALUES(9,'Catchpole','Antoinette','acatchpo','1992-02-20',NULL,2,'Warehouse Manager',44,1300,null);
INSERT INTO S_EMP VALUES(10,'Havel','Marta','mhavel','1991-02-27',null,2,'Warehouse Manager',45,1307,null);

INSERT INTO S_CUSTOMER VALUES(201,'Unisports','55-2066101','72 Via','Bahia','Sao Paolo','Brazil',null,'EXCELLENT',10,2,
'El cliente usualmente ordena largas cantidades y tiene un total de ordenes alto. Este es bueno y su nivel de credito es excelente');
INSERT INTO S_CUSTOMER VALUES(202,'Atheletics','81-20101','6741 Takashi Blvd.','Osaka',null,
'Japan',null,'POOR',4,4,'El cliente hace sus pagos en efectivo hasta que se apruebe su nivel de credito');
INSERT INTO S_CUSTOMER VALUES(203,'Delhi Sports','91-10351','11368 Chanakya','New Delhi',null,
'India',null,'GOOD',7,4,'El cliente se especializa en equipo de base ball y es el mas grande distribuidor de la India.');
INSERT INTO S_CUSTOMER VALUES(204,'Womansport','1-206-104-0103281','King Street','Seattle','Washington',
'USA','98101','EXCELLENT',8,1,NULL);
INSERT INTO S_CUSTOMER VALUES(205,'Kam Sporting Goods','852-2257201','15 Henessey Road','Hong Kong', null,
null,null,'EXCELLENT',9,4,NULL);
INSERT INTO S_CUSTOMER VALUES(206,'Sportique','33-2257201','172 Rue de Rivoli','Cannes', null,
'France',null, 'EXCELLENT',1,5,'El cliente se especializa en soccer. Le gusta ordenar accesorios en colores brillantes');

INSERT INTO S_ORD VALUES(100,204,'1992-08-31','1992-09-10',1,601100,'CREDIT','Y');
INSERT INTO S_ORD VALUES(101,205,'1992-08-31','1992-09-15',6,8056.6,'CREDIT','Y');
INSERT INTO S_ORD VALUES(102,206,'1992-09-01','1992-09-08',8,8335,'CREDIT','Y');
INSERT INTO S_ORD VALUES(103,201,'1992-09-02','1992-09-22',9,377,'CASH','Y');
INSERT INTO S_ORD VALUES(104,202,'1992-09-03','1992-09-23',3,32430,'CREDIT','Y');
INSERT INTO S_ORD VALUES(105,203,'1992-09-04','1992-09-18',7,2722.24,'CREDIT','Y');
INSERT INTO S_ORD VALUES(106,206,'1992-09-07','1992-09-15',8,15634,'CREDIT','Y');
INSERT INTO S_ORD VALUES(107,203,'1992-09-07','1992-09-21',5,142171,'CREDIT','Y');
INSERT INTO S_ORD VALUES(108,204,'1992-09-07','1992-09-10',6,149570,'CREDIT','Y');


INSERT INTO S_PRODUCT VALUES(10011,'Boot','Beginners ski boot',518,1001,150,null);
INSERT INTO S_PRODUCT VALUES(10012,'Ace Ski Boot', 'Intermediate ski boot', 519,1002,200,null);
INSERT INTO S_PRODUCT VALUES(10013,'Pro Ski Boot','Advanced ski boot',520,1003,410,null);
INSERT INTO S_PRODUCT VALUES(10021,'Bunny Ski Pole','Beginners ski pole',528,1011,16.25,null);
INSERT INTO S_PRODUCT VALUES(10022,'Ace Ski Pole','Intermediate ski pole',530,1013,40.95,null);
INSERT INTO S_PRODUCT VALUES(10023,'Pro Ski Pole','Advanced ski pole',530,1013,40.95,null);
INSERT INTO S_PRODUCT VALUES(20106,'Junior Soccer Ball','Junior soccer ball',613,null,11,null);
INSERT INTO S_PRODUCT VALUES(20108,'World Cup Soccer Ball','World cup soccer ball', 615,null,28,null);
INSERT INTO S_PRODUCT VALUES(20201,'World Cup Net','World cup net',708,null,123,null);
INSERT INTO S_PRODUCT VALUES(20510,'Black Hawk Knee pads','Knee pads pair',1017,null,9,null);



INSERT INTO S_ITEM VALUES(100,1,10011,135,500,500);
INSERT INTO S_ITEM VALUES(100,2,10013,380,400,400);
INSERT INTO S_ITEM VALUES(100,3,10021,14,500,500);
INSERT INTO S_ITEM VALUES(104,1,20510,9,7,7);
INSERT INTO S_ITEM VALUES(102,1,20108,28,100,100);
INSERT INTO S_ITEM VALUES(102,2,20201,123,45,45);
INSERT INTO S_ITEM VALUES(106,1,20108,28,46,46);
INSERT INTO S_ITEM VALUES(106,2,20201,123,21,21);
INSERT INTO S_ITEM VALUES(107,1,20106,11,50,50);
INSERT INTO S_ITEM VALUES(107,3,20201,115,130,130);
INSERT INTO S_ITEM VALUES(107,2,20108,28,22,22);
INSERT INTO S_ITEM VALUES(108,1,20510,9,9,9);
INSERT INTO S_ITEM VALUES(101,1,10011,140,150,150);
INSERT INTO S_ITEM VALUES(101,2,10012,175,600,600);
INSERT INTO S_ITEM VALUES(103,1,20106,9,1000,1000);
INSERT INTO S_ITEM VALUES(105,1,20510,9,18,18);
INSERT INTO S_ITEM VALUES(104,2,10021,8,25,25);
