package com.example;

public class TipoDatos {

    public static void main(String[] args) {

        // enteros
        byte number1 = 1; // 1 byte
        System.out.println(number1);
        short number2 = 2; // 2 byte
        System.out.println(number2);
        int number3 = 3; // 4 byte
        System.out.println(number3);
        long number4 = 5; // 8 byte
        System.out.println(number4);

        // punto flotante
        float decimal1 = 4.9f;
        System.out.println(decimal1);
        double decimal2 = 9.99d;
        System.out.println(decimal2);

        // caracter
        char caracter1 = 'a';
        System.out.println(caracter1);

        // boleanos
        boolean verdadero = true;
        System.out.println(verdadero);
        boolean falso = false;
        System.out.println(falso);

        // cadenas de texto
        String nombre = "Ferran";
        System.out.println(nombre);
        String apellido = "Caubet";
        System.out.println(apellido);

        //tipos envoltorios
        Integer numero = null;
        System.out.println(numero);
        Long numero2 = 2L;
        System.out.println(numero2);

    }
}
