#Subconsultas y JOINs:
#Dada una tabla ventas con columnas id, producto_id y cantidad, y otra 
#tabla productos con columnas id y nombre, escribe una consulta SQL para 
#obtener el nombre de todos los productos que se han vendido más de 100 unidades.

SELECT productos.nombre
FROM ventas
JOIN productos ON ventas.producto_id = productos.id
GROUP BY productos.nombre
HAVING SUM(ventas.cantidad) > 100;

#Manipulación de datos:
#Supongamos que tienes una tabla empleados con columnas id, nombre, 
#salario y departamento_id, y una tabla departamentos con columnas id 
#y nombre. Escribe una consulta SQL para aumentar el salario de todos 
#los empleados en el departamento de "Ventas" en un 10%.

UPDATE empleados
SET salario = salario * 1.1
WHERE departamento_id = (SELECT id FROM departamentos WHERE nombre = 'Ventas');

#Operaciones de pivote y desvinculación:
#Dada una tabla ventas con columnas id, producto_id, cantidad y 
#fecha, escribe una consulta SQL para obtener el total de ventas 
#de cada producto en cada mes del año actual, mostrando los 
#resultados en un formato de tabla pivote.

SELECT 
    producto_id,
    MONTH(fecha) AS mes,
    SUM(cantidad) AS total_ventas
FROM ventas
WHERE YEAR(fecha) = YEAR(CURRENT_DATE)
GROUP BY producto_id, MONTH(fecha)
ORDER BY producto_id, MONTH(fecha);

#Funciones de agregación avanzadas:
#Supongamos que tienes una tabla registros con columnas id, usuario_id 
#y fecha_registro. Escribe una consulta SQL para calcular el promedio 
#de días que los usuarios tardan en registrarse después de que se les 
#ha enviado un correo electrónico de confirmación, excluyendo los casos 
#en los que no se ha completado el registro.

SELECT AVG(DATEDIFF(fecha_registro, fecha_envio)) AS promedio_dias_registro
FROM registros
WHERE usuario_id IN (SELECT usuario_id FROM correos_enviados WHERE completado = 1);

#Seguridad de datos:
#Imagina que tienes una tabla usuarios con columnas id, 
#nombre, correo_electronico y contraseña. ¿Cómo diseñarías 
#una consulta SQL segura para verificar las credenciales de 
#un usuario que intenta iniciar sesión sin exponer la 
#contraseña en texto plano en la consulta?

SELECT id, nombre, correo_electronico
FROM usuarios
WHERE correo_electronico = 'correo@ejemplo.com'
AND contraseña = SHA2(CONCAT('salt', 'contraseña'), 256);

#Optimización de consultas:
#Para mejorar el rendimiento de una consulta en una tabla grande, 
#podrías considerar las siguientes técnicas:
#Asegurarte de que existan índices en las columnas utilizadas en cláusulas WHERE y JOIN.
#Evitar el uso de funciones en cláusulas WHERE que puedan impedir el uso de índices.
#Dividir la consulta en partes más pequeñas si es posible.
#Optimizar las subconsultas utilizando JOINs en su lugar.
#Analizar el plan de ejecución de la consulta para identificar 
#cuellos de botella y áreas de mejora.

SELECT *
FROM tabla_grande
WHERE columna1 = 'valor'
AND columna2 LIKE 'prefijo%';

#A algo como esto:
SELECT *
FROM tabla_grande
WHERE columna1 = 'valor';

SELECT *
FROM tabla_grande
WHERE columna2 LIKE 'prefijo%';

#Manejo de fechas:
#Supongamos que tienes una tabla pedidos con columnas id, 
#fecha_pedido y total_pedido. Escribe una consulta SQL para 
#calcular el promedio de ventas diarias en los últimos 30 días.

SELECT AVG(total_pedido) AS promedio_ventas_diarias
FROM pedidos
WHERE fecha_pedido >= CURDATE() - INTERVAL 30 DAY;

#Uso de funciones de ventana:
#Dada una tabla ventas con columnas id, producto_id, cantidad 
#y fecha, escribe una consulta SQL para calcular la suma 
#acumulativa de las ventas diarias para cada producto.

SELECT fecha, producto_id, cantidad,
       SUM(cantidad) OVER (PARTITION BY producto_id ORDER BY fecha) AS ventas_acumuladas
FROM ventas;

#Búsqueda de patrones:
#Imagina que tienes una tabla clientes con columnas id, 
#nombre y correo_electronico. Escribe una consulta SQL 
#para encontrar todos los clientes cuyas direcciones de 
#correo electrónico terminen con "@gmail.com".

SELECT *
FROM clientes
WHERE correo_electronico LIKE '%@gmail.com';

#Jerarquías y relaciones recursivas:
#Supongamos que tienes una tabla empleados con columnas id, 
#nombre y gerente_id, donde gerente_id es el ID del supervisor 
#directo de cada empleado. Escribe una consulta SQL para mostrar 
#la jerarquía de empleados utilizando un recorrido recursivo.

WITH RECURSIVE jerarquia_empleados AS (
    SELECT id, nombre, gerente_id, 0 AS nivel
    FROM empleados
    WHERE gerente_id IS NULL
    UNION ALL
    SELECT e.id, e.nombre, e.gerente_id, je.nivel + 1
    FROM empleados e
    INNER JOIN jerarquia_empleados je ON e.gerente_id = je.id
)
SELECT id, nombre, gerente_id, nivel
FROM jerarquia_empleados;

#Unión de tablas y subconsultas:
#Dadas dos tablas estudiantes y calificaciones con columnas 
#apropiadas, escribe una consulta SQL para encontrar el nombre 
#de todos los estudiantes que obtuvieron una calificación 
#mayor que 90 en matemáticas.

SELECT nombre
FROM estudiantes
WHERE id IN (SELECT estudiante_id FROM calificaciones WHERE materia = 'Matemáticas' AND calificacion > 90);


#Optimización de consultas avanzada:
#Imagina que tienes una consulta SQL que involucra múltiples JOINs 
#y funciones de agregación en tablas grandes. ¿Cómo podrías refactorizar 
#la consulta para mejorar su rendimiento sin sacrificar 
#la precisión de los resultados?

#Por ejemplo, podrías refactorizar una consulta compleja así:

SELECT columna1, columna2, SUM(columna3) AS suma_columna3
FROM tabla_grande1
JOIN tabla_grande2 ON tabla_grande1.id = tabla_grande2.id
GROUP BY columna1, columna2;

#A algo como esto:

WITH datos_filtrados AS (
    SELECT columna1, columna2, columna3
    FROM tabla_grande1
    JOIN tabla_grande2 ON tabla_grande1.id = tabla_grande2.id
    WHERE condicion = 'alguna_condicion'
)
SELECT columna1, columna2, SUM(columna3) AS suma_columna3
FROM datos_filtrados
GROUP BY columna1, columna2;

