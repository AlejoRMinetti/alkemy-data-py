-- Aca vamos poninedo las sentencias SQL de la creacion de tablas
-- Bajas los archivos csv de las paginas fuente para conoces los keys

-- Table: tableCreation for museum (TODO by Alejo)

CREATE TABLE provincia (
  id INT NOT NULL AUTO_INCREMENT,
  provincia VARCHAR(125) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE departamento (
  id INT NOT NULL AUTO_INCREMENT,
  departamento VARCHAR(125) NOT NULL,
  provincia_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (provincia_id) REFERENCES provincia(id));

CREATE TABLE localidad (
  id INT NOT NULL AUTO_INCREMENT,
  localidad VARCHAR(125) NOT NULL,
  departamento_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (departamento_id) REFERENCES departamento(id));

CREATE TABLE categoria (
  id INT NOT NULL AUTO_INCREMENT,
  categoria VARCHAR(125) NOT NULL,
  PRIMARY KEY (id));

CREATE TABLE museo (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  direccion VARCHAR(125) NOT NULL,
  codigo_postal VARCHAR(8) NOT NULL,
  codigo_area VARCHAR(4) NOT NULL,
  telefono VARCHAR(8) NOT NULL,
  email VARCHAR(225) NOT NULL,
  web VARCHAR(255) NOT NULL,
  localidad_id INT NOT NULL,
  provincia_id INT NOT NULL,
  categoria_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (localidad_id) REFERENCES localidad(id),
  FOREIGN KEY (provincia_id) REFERENCES provincia(id),
  FOREIGN KEY (categoria_id) REFERENCES categoria(id));

-- Table Biblioteca (TODO: by Vlady)


