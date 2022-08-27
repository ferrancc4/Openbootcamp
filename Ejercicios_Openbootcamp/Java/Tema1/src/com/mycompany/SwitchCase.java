package com.mycompany;

public class SwitchCase {

    public static void main(String[] args) {


        String weather = "sunny";

        switch (weather) {

            case "sunny":
                System.out.println("Esta soleado");
                break; // para que si entra en el caso no ejecute el codigo siguiente
            case "cloudy":
                System.out.println("Esta nublado");
                break;
            default: // para si no entra en ningun caso
                System.out.println("Valor erroneous");
                break;
        }
    }
}
