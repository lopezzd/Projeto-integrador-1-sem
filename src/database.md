CREATE DATABASE escola;

USE escola;

CREATE TABLE stockprime (

id                INT AUTO_INCREMENT,
nome_produto      VARCHAR(50) NOT NULL, 
descricao_produto VARCHAR(255) NOT NULL,
cp_valor          DECIMAL (10,2) NOT NULL,

#				  DADOS EM PORCENTAGEM BASEADOS NO CUSTO DO PRODUTO

cf                DECIMAL (3,0) NOT NULL,
cv                DECIMAL (3,0) NOT NULL,
iv                DECIMAL (3,0) NOT NULL, 
ml                DECIMAL (3,0) NOT NULL,

#				  DADOS EM VALORES

pv_valor	      DECIMAL (10,2) AS (cp_valor / (1 - ((cf + cv + iv + ml) / 100))) STORED,
rb_valor		  DECIMAL (10,2) AS (pv_valor - cp_valor) STORED,
cf_valor          DECIMAL (10,2) AS (pv_valor * (cf/100)) STORED, 
cv_valor          DECIMAL (10,2) AS (pv_valor * (cv/100)) STORED, 
iv_valor          DECIMAL (10,2) AS (pv_valor * (iv/100)) STORED,
og_valor 		  DECIMAL (10,2) AS (cf_valor + cv_valor + iv_valor) STORED,	 
rt_valor          DECIMAL (10,2) AS (rb_valor - og_valor) STORED,
lucro			  VARCHAR (255) NOT NULL,

#				  DADOS EM PORCENTAGEM

pv_porc	          DECIMAL (3,0) AS ((pv_valor / pv_valor) * 100) STORED,
cp_porc           DECIMAL (3,0) AS ((cp_valor / pv_valor) * 100) STORED,
rb_porc		      DECIMAL (3,0) AS ((rb_valor / pv_valor) * 100) STORED,
cf_porc           DECIMAL (3,0) AS ((cf_valor / pv_valor) * 100) STORED, 
cv_porc           DECIMAL (3,0) AS ((cv_valor / pv_valor) * 100) STORED, 
iv_porc           DECIMAL (3,0) AS ((iv_valor / pv_valor) * 100) STORED,
og_porc 		  DECIMAL (3,0) AS ((og_valor / pv_valor) * 100) STORED,	 
rt_porc           DECIMAL (3,0) AS (rb_porc - og_porc) STORED,

#				  Outros

quantidade 		  DECIMAL (10,0),


PRIMARY KEY (id)
) DEFAULT CHARSET = utf8mb4;
