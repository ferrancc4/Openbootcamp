package com.mycompany;

public class PruebaFunciones {

    public static void main(String[] args) {

        // Si intentamos llamar a una funcion privada no podremos
        // Funciones.holaMundo();

        // Si es pública si podemos llamarla
        Funciones.holaNombre("Ferran");

        // Función protected como está en el mismo paquet podemos acceder
        Funciones.hola();
    }
}
