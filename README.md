# Client-Server System: Synchronization and Assignment of Identifiers
# Sistema Cliente-Servidor: Sincronización y Asignación de Identificadores

## Descripción
Este proyecto es una implementación de un sistema distribuido utilizando una arquitectura cliente-servidor entre dos lenguajes distintos (Python y Java). Fue desarrollado para demostrar conceptos clave en sistemas distribuidos

**Servidor (Python):**
* Escucha en una dirección IP y el puerto definido.
* Al recibir una conexión de cliente, registra: 
  * La dirección IP del cliente.
  * Un identificador único generado para el cliente (UUID).
  * El nombre lógico del cliente (enviado por el cliente).
* Devuelve al cliente: la hora actual del servidor (timestamp) y el identificador asignado.
* Guarda esta información en un archivo de log.

**Cliente (Java):**
* Se conecta al servidor usando su dirección IP y puerto.
* Envía su nombre lógico (por ejemplo, "ClienteA").
* Recibe del servidor: la hora del servidor y su identificador asignado.
* Calcula la diferencia entre su reloj local y el del servidor.
* Muestra en consola: su dirección IP local, el identificador recibido y la diferencia de tiempo con el servidor.