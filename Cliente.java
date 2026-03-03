// Cliente.java
import java.io.*;
import java.net.*;
import java.time.Instant;

public class Cliente {
    public static void main(String[] args) {
        String servidorIP = "xxx.xxx.xxx"; // IP VPS
        int puerto = 0000; //Ingrese puerto del VPS
        String nombreLogico = "ClienteA";

        try {
            Socket socket = new Socket(servidorIP, puerto);

            // Obtener IP local
            String ipLocal = socket.getLocalAddress().getHostAddress();

            // Enviar nombre lógico
            OutputStream os = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(os, true);
            writer.println(nombreLogico);

            // Recibir respuesta
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String[] data = reader.readLine().split(",");

            double tiempoServidor = Double.parseDouble(data[0]);
            String uuid = data[1];

            double tiempoLocal = (double) Instant.now().getEpochSecond();
            double diferencia = tiempoServidor - tiempoLocal;

            System.out.println("IP Local: " + ipLocal);
            System.out.println("UUID recibido: " + uuid);
            System.out.printf("Diferencia de tiempo: %.2f segundos\n", diferencia);

            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
