CREATE DATABASE mercado;

USE mercado;


CREATE TABLE tbl_produtos(
	id_produtos INT not null auto_increment primary key,
    nome_produtos VARCHAR(50) not null,
    data_recebimento DATETIME not null DEFAULT NOW(),
    data_validade VARCHAR(50) not null,
    preco_produto DECIMAL not null,
    quantidade INT not null
);

CREATE TABLE tbl_vendas(
	id_venda INT NOT NULL PRIMARY KEY auto_increment,
    nome_venda VARCHAR(50),
    preco_venda VARCHAR (600) ,
    quantidade_venda VARCHAR(700) ,
    franquia varchar(400)
);

CREATE TABLE tbl_usuario(
	id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    login_usuario VARCHAR(35) NOT NULL,
    senha_usuario VARCHAR(35) NOT NULL,
    email_usuario VARCHAR(45) NOT NULL
);

CREATE TABLE tbl_loja(
	id_loja INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    franquia INT NOT NULL
);

   insert into tbl_usuario(login_usuario, senha_usuario, email_usuario)
   values('brenogay', '2424', 'brenogay@dabumbum.cu');
   
   insert into tbl_produtos(nome_produtos,preco_produto,data_validade,quantidade) values ('oi',26,'11/09/2001',2);
   
   select * from tbl_usuario;
   
	 insert into tbl_usuario(login_usuario, senha_usuario, email_usuario)
   values('gg', '123', 'brenogay@dabumbum.cu');
   
   #drop database mercado;
   
   update tbl_produtos set quantidade = quantidade -1 where nome_produtos = '';