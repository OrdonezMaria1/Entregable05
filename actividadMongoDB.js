// Crear la colección "Estudiantes" e insertar documentos
db.Estudiantes.insertMany([
  { "nombre": "Juan", "edad": 20, "ciudad": "Bogotá" },
  { "nombre": "Ana", "edad": 22, "ciudad": "Medellín" },
  { "nombre": "Luis", "edad": 19, "ciudad": "Cali" }
]);

// Todos los estudiantes
db.Estudiantes.find();

//Estudiantes por ciudad = Bogotá
db.Estudiantes.find({ ciudad: "Bogotá" });

// Estudiantes mayores a 20
db.Estudiantes.find({ edad: { $gt: 20 } });