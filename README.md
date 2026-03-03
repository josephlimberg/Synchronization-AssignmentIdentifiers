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

*server <img width="595" height="94" alt="Captura de pantalla 2026-03-03 121948" src="https://github.com/user-attachments/assets/3493bc56-f637-4679-88b7-330284fa5304" />
*Cliente <img width="567" height="164" alt="Captura de pantalla 2026-03-03 121954" src="https://github.com/user-attachments/assets/3bf37be9-4f3e-449c-942b-2f5aefee2845" />
*log <img width="623" height="81" alt="Captura de pantalla 2026-03-03 122001" src="https://github.com/user-attachments/assets/4d1a6040-fe4d-417a-8198-eccd78762029" />


