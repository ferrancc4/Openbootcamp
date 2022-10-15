package com.mycompany;

import java.util.Scanner;

public class ScannerMain {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce un nombre");
        String nombre = scanner.nextLine();
        System.out.println("Introduce el DNI");
        int numero = scanner.nextInt();

        System.out.println("El nombre es: " + nombre);
        System.out.println("El DNI de " + nombre + " es: " + numero);


        System.out.println("Hola mundo");
    }
}
