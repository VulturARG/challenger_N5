# Propuesta de implementación en AWS

## Consideraciones generales
Al no conocer la posible demanda de uso del sistema es difícil presentar una propuesta concreta, ya que en un caso real hay muchos aspectos a tener en cuenta.
En AWS se puede implementar una misma solución de distintas maneras.

Por ejemplo podríamos tener algunos de estos casos:
- El monto diario de multas son 50 por día. Los oficiales de policía cuentan con una plataforma remota en línea. El ingreso de las infracciones se distribuye en 24 horas.
- El monto diario de multas son 50000 por día. Los oficiales de policía cuentan con una plataforma remota fuera de línea. El ingreso de las infracciones se concentra en tres horarios pico.

Por esta situación describo 3 posibles casos teóricos. Una implementación real implicaría un análisis de costos detallado.

## Caso 1: Baja demanda de la aplicación. Sistema minimo
La demanda prevista utiliza una instancia EC2 para colocar el sistema por completo en la misma.
Debería contar con:
- NGINX como proxy inverso y balanceador de cargas.
- El sistema propiamente dicho.
- La base de datos.
- Sistema de backup automático.
- Gestion de DNS propia.

Dentro de ciertos límites por el tema de costos y recursos el sistema puede escalar horizontalmente mediante el uso de varios contenedores manejados por NGINX y verticalmente, usando una instancia con más recursos.

## Caso 2: Demanda media y alta.
Por razones de costos o requerimientos del sistema podríamos tener esta configuración:
- **EC2**: Una o varias instancias EC2 para manejar un mayor tráfico.
- **Elastic Load Balancer**: Para distribuir el tráfico entre múltiples instancias EC2.
- **RDS**: Una instancia de base de datos RDS para Postgres.
- **Auto Scaling Group**: Para escalar automáticamente las instancias EC2 según la demanda.
- **S3**: Para almacenar archivos estáticos, de media y backups.
- **IAM**: Gestión de usuarios y permisos.
- **Route 53**: Gestión del DNS.
- **CloudWatch**: Para monitoreo y logging.
- - **Secrets Manager**: Para gestionar credenciales y secretos.

## Caso 3: Demanda media y alta usando kubernetes.
- **EKS Cluster**: Para ejecutar y administrar contenedores de Kubernetes.
- **EC2**: Para los nodos de trabajo del clúster de Kubernetes.
- **RDS**: Una instancia de base de datos RDS para Postgres.
- **S3**: Para almacenar archivos estáticos, de media y backups.
- **Route 53**: Gestión del DNS.
- **Elastic Load Balancer**: Para distribuir el tráfico de los servicios de Kubernetes.
- **IAM**: Gestión de usuarios y permisos.
- **CloudWatch**: Para monitoreo y logging.
- **Secrets Manager**: Para gestionar credenciales y secretos.
