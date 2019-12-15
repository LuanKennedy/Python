CREATE SCHEMA bd_escola;
USE bd_escola;

CREATE USER 'PythonProjects'@'localhost' IDENTIFIED BY '123456';
GRANT SELECT, DELETE, INSERT, UPDATE, EXECUTE ON bd_escola.* TO 'PythonProjects'@'localhost';

CREATE TABLE IF NOT EXISTS bd_escola.aluno (
  idaluno INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  dtnasc DATE NOT NULL,
  endereco VARCHAR(50) NOT NULL,
  cidade VARCHAR(50) NOT NULL,
  estado VARCHAR(2) NOT NULL,
  email VARCHAR(100) NOT NULL,
  PRIMARY KEY (idaluno)
);

insert into aluno(idaluno, nome, dtnasc, endereco, cidade, estado, email) values
(default,"Paulo Henrique Santana", '2000-03-05', "Rua A nº 125", "Osasco","SP","phsantana@gmail.com"),
(default,"Vitória M", '2000-04-09', "Rua B nº 234", "Embu das Artes","SP","vimendes@gmail.com"),
(default,"Marília Santana", '2001-07-03', "Rua C nº 354", "São Paulo","SP","marilia2001@gmail.com");

select * from aluno;
#Exemplos:
#SELECT * FROM aluno WHERE idaluno = 1;
#SELECT * FROM aluno WHERE nome like '%PA%';
#UPDATE aluno SET nome = "Vitória Mendes" WHERE idaluno = 2;
#UPDATE aluno SET nome = 'Vitória Mendes' WHERE nome like '%Vitória%';
#INSERT INTO aluno(idaluno, nome, dtnasc, endereco, cidade, estado, email) VALUES(default,'Manuela Gonçalves','1998-05-27','Rua da ETEC Nº 50','Embu','SP','manu_go@gmail.com');
#DELETE FROM aluno WHERE idaluno = 4;


