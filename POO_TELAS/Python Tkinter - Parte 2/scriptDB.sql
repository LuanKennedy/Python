CREATE SCHEMA bd_contato;
USE bd_contato;

CREATE USER 'PythonProjects'@'localhost' IDENTIFIED BY '123456';
GRANT SELECT, DELETE, INSERT, UPDATE, EXECUTE ON bd_contato.* TO 'PythonProjects'@'localhost';

CREATE TABLE IF NOT EXISTS bd_contato.contatos (
  cpf VARCHAR(14) NOT NULL,
  nome VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  tel VARCHAR(14) NOT NULL,
  PRIMARY KEY (cpf)
);

insert into contatos(cpf, nome, email, tel) values
("408.787.345-01","Paulo Henrique Santana", "phsantana@gmail.com","(11)4673-7643"),
("426.987.923-32","Vitória M", "vimendes@gmail.com","(11)4559-0157"),
("417.985.674-27","Marília Santana", "marilia2001@gmail.com","(11)4712-6924");

select * from contatos;
#Exemplos:
#SELECT * FROM contatos WHERE cpf = '408.787.345-01';
#UPDATE contatos SET nome = "Vitória Mendes" WHERE  cpf = '408.787.345-01';
DELETE FROM contatos WHERE cpf = "123.456.789-00";
#UPDATE contatos SET cpf='cpf',nome='name sobre',email='email',tel='tele' WHERE cpf = 'cpf';

