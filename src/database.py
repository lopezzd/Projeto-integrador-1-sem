import mysql.connector

mydb = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "Lop&s546",
  database = ""
)

mycursor = mydb.cursor()

sql = """

CREATE DATABASE escola;

USE escola;

CREATE TABLE stockprime (
id                INT AUTO_INCREMENT,
nome_produto      VARCHAR(50) NOT NULL, 
descricao_produto VARCHAR(255) NOT NULL,
cp_valor          DECIMAL (10,2) NOT NULL,

#				  DADOS EM PORCENTAGEM BASEADOS NO CUSTO DO PRODUTO

cf                DECIMAL (6,3) NOT NULL,
cv                DECIMAL (6,3) NOT NULL,
iv                DECIMAL (6,3) NOT NULL, 
ml                DECIMAL (6,3) NOT NULL,

#				  DADOS EM VALORES

pv_valor	        DECIMAL (10,2) AS (cp_valor / (1 - ((cf + cv + iv + ml) / 100))) STORED,
rb_valor		      DECIMAL (10,2) AS (pv_valor - cp_valor) STORED,
cf_valor          DECIMAL (10,2) AS (pv_valor * (cf/100)) STORED, 
cv_valor          DECIMAL (10,2) AS (pv_valor * (cv/100)) STORED, 
iv_valor          DECIMAL (10,2) AS (pv_valor * (iv/100)) STORED,
og_valor 		      DECIMAL (10,2) AS (cf_valor + cv_valor + iv_valor) STORED,	 
rt_valor          DECIMAL (10,2) AS (rb_valor - og_valor) STORED,
lucro			        VARCHAR (255) NOT NULL,

#				  DADOS EM PORCENTAGEM

pv_porc	          DECIMAL (10,2) AS ((pv_valor / pv_valor) * 100) STORED,
cp_porc           DECIMAL (10,2) AS ((cp_valor / pv_valor) * 100) STORED,
rb_porc		        DECIMAL (10,2) AS ((rb_valor / pv_valor) * 100) STORED,
cf_porc           DECIMAL (10,2) AS ((cf_valor / pv_valor) * 100) STORED, 
cv_porc           DECIMAL (10,2) AS ((cv_valor / pv_valor) * 100) STORED, 
iv_porc           DECIMAL (10,2) AS ((iv_valor / pv_valor) * 100) STORED,
og_porc 		      DECIMAL (10,2) AS ((og_valor / pv_valor) * 100) STORED,	 
rt_porc           DECIMAL (10,2) AS (rb_porc - og_porc) STORED,

PRIMARY KEY (id)
) DEFAULT CHARSET = utf8mb4;

INSERT INTO STOCKPRIME ( nome_produto, descricao_produto, cp_valor, cf, cv, iv, ml, lucro) VALUES ( 'Cadeira', 'Cadeira para diversos usos', 50, 30, 17, 20, 6, 'teste lucro');
INSERT INTO STOCKPRIME ( nome_produto, descricao_produto, cp_valor, cf, cv, iv, ml, lucro) VALUES ( 'Mesa', 'Mesa de escritório', 15, 15, 8, 20, 35, 'teste lucro');
INSERT INTO STOCKPRIME ( nome_produto, descricao_produto, cp_valor, cf, cv, iv, ml, lucro) VALUES ( 'Mouse', 'Mouse para computador', 36, 15, 5, 12, 20, 'teste lucro');
"""
 
mycursor.execute(sql)