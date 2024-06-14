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

pv_valor	        DECIMAL (10,2) AS (cp_valor / (1 - ((cf + cv + iv + ml) / 100))) STORED,
rb_valor		      DECIMAL (10,2) AS (pv_valor - cp_valor) STORED,
cf_valor          DECIMAL (10,2) AS (pv_valor * (cf/100)) STORED, 
cv_valor          DECIMAL (10,2) AS (pv_valor * (cv/100)) STORED, 
iv_valor          DECIMAL (10,2) AS (pv_valor * (iv/100)) STORED,
og_valor 		      DECIMAL (10,2) AS (cf_valor + cv_valor + iv_valor) STORED,	 
rt_valor          DECIMAL (10,2) AS (rb_valor - og_valor) STORED,
lucro			        VARCHAR (255) NOT NULL,

#				  DADOS EM PORCENTAGEM

pv_porc	          DECIMAL (3,0) AS ((pv_valor / pv_valor) * 100) STORED,
cp_porc           DECIMAL (3,0) AS ((cp_valor / pv_valor) * 100) STORED,
rb_porc		        DECIMAL (3,0) AS ((rb_valor / pv_valor) * 100) STORED,
cf_porc           DECIMAL (3,0) AS ((cf_valor / pv_valor) * 100) STORED, 
cv_porc           DECIMAL (3,0) AS ((cv_valor / pv_valor) * 100) STORED, 
iv_porc           DECIMAL (3,0) AS ((iv_valor / pv_valor) * 100) STORED,
og_porc 		      DECIMAL (3,0) AS ((og_valor / pv_valor) * 100) STORED,	 
rt_porc           DECIMAL (3,0) AS (rb_porc - og_porc) STORED,
lc_porc			      DECIMAL (3,0) AS (((preco_de_venda - cp_valor) / preco_de_venda) * 100) STORED,

#				  Outros

quantidade 		  DECIMAL (10,0),


PRIMARY KEY (id)
) DEFAULT CHARSET = utf8mb4;

UPDATE escola.stockprime
SET lucro = 
    CASE 
        WHEN lc_porc > 20 THEN 'Lucro alto'
        WHEN lc_porc BETWEEN 10 AND 20 THEN 'Lucro médio'
        WHEN lc_porc > 0 AND lc_porc < 10 THEN 'Lucro baixo'
        WHEN lc_porc = 0 THEN 'Lucro baixo'
        ELSE 'Sem lucro'
    END;


INSERT INTO stockprime ( nome_produto, descricao_produto, cp_valor, cf, cv, iv, ml, lucro, quantidade) VALUES ( 'Cadeira', 'Cadeira para diversos usos', 50, 30, 17, 20, 6, 'teste lucro', 23);
INSERT INTO stockprime ( nome_produto, descricao_produto, cp_valor, cf, cv, iv, ml, lucro, quantidade) VALUES ( 'Mesa', 'Mesa de escritório', 15, 15, 8, 20, 35, 'teste lucro', 43);
INSERT INTO stockprime ( nome_produto, descricao_produto, cp_valor, cf, cv, iv, ml, lucro, quantidade) VALUES ( 'Mouse', 'Mouse para computador', 36, 15, 5, 12, 20, 'teste lucro', 45);

SELECT * FROM stockprime;

DROP TABLE stockprime;
DROP DATABASE escola;