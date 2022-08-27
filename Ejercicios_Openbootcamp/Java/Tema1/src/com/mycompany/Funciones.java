package com.mycompany;

public class Funciones {

    public static void main(String[] args) {

        holaMundo();
        holaMundo("Ferran");
        holaMundo("Fer", "Caubet");


        holaNombre("Ferran");


        String hola = hola();
        System.out.println(hola);

        int a = 5;
        int b = 6;
        suma(a, b);

    }
    /* Una funcion puede ser pública o privada
        - Pública puede acceder des de otro archivo java tipo clase
        - Privada solo se puede acceder des de la su clase

       Static: hace referencia a la clase y se puede invocar sin tener que crear un objeto de la clase
    */
    private static void holaMundo() {
        System.out.println("Hola mundo");
    }

    // Sobrecargar una función es tener la misma función varias veces pero con código diferente
    private static void holaMundo(String name) {
        System.out.println("Hola " + name);
    }

    private static void holaMundo(String name, String surname) {
        System.out.println("Hola " + name);
    }

    private static int suma(int num1, int num2) {
        return num1 + num2;
    }

    public static void holaNombre(String name) {
        System.out.println("Hola " + name);
    }

    // El modificador protected solo las clases hijas o que estén en el mismo paquete van a poder acceder
    // a la función. En este caso todas las que están dentro del paquete com.mycompany
    protected static String hola() {
        return "Hola";
    }

}
