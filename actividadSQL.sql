-- Crear tabla Estudiantes
CREATE TABLE Estudiantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

-- Insertar datos
INSERT INTO Estudiantes (nombre, edad, ciudad) VALUES
('Ana', 18, 'Bogotá'),
('Luis', 22, 'Medellín'),
('Sofía', 19, 'Cali'),
('Carlos', 25, 'Bogotá'),
('María', 21, 'Barranquilla');

-- Consultar todos los registros
SELECT * FROM Estudiantes;

-- Filtrar estudiantes por ciudad (ejemplo: Bogotá)
SELECT * FROM Estudiantes
WHERE ciudad = 'Bogotá';

-- Consultar estudiantes mayores de 20 años
SELECT * FROM Estudiantes
WHERE edad > 20;
