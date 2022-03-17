DROP TABLE IF EXISTS log;

CREATE TABLE IF NOT exists log(
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  descricao VARCHAR(100) NOT NULL  
);