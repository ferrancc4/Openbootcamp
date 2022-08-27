package com.mycompany;

public class While {

    public static void main(String[] args) {


        int count = 0;
        while (count < 10){

            count++;

            if(count == 6)
                continue; // Pasa a la siguiente iteración sin ejecutar el código por debajo de continue

            if(count == 8)
                break; // Rompe el bucle

            System.out.println(count);
        }
    }
}
