package com.mycompany;

public class StringMain {

    public static void main(String[] args) {

        // La clase String

        /*
            length()
            startsWith("")
            endsWith("")
            indexOf("")
            subString(1,5)
            trim()
            equals()
            compareTo()
         */

        String mensaje = "Hola mundo";

        System.out.println(mensaje.length());
        String mensajeMAY = mensaje.toUpperCase();
        System.out.println(mensajeMAY);

        String otro = "HOLA MUNDO";
        if(mensaje.equals(mensajeMAY)){
            System.out.println("Verdadero!");
        }

        if(mensaje.equalsIgnoreCase(mensajeMAY)){
            System.out.println("Verdadero!");
        }
    }
}
