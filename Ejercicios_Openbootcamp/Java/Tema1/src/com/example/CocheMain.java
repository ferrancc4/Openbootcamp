package com.example;

public class CocheMain {


    public static void main(String[] args) {


        String coche = "tesla";
        //Coche cocheObj = new Coche();


        //Coche cocheObj2 = new Coche("azul", "Tesla", "Model Y", 1900.9,4.75);

        //cocheObj2.acelerar(50);

        //System.out.println(cocheObj2);

        CocheElectrico cocheElectrico = new CocheElectrico();

        cocheElectrico.motorElectrico = "Motor potente";

        System.out.println(cocheElectrico);

        CocheElectrico cocheElectrico2 = new CocheElectrico("azul", "Tesla", "Model Y",
                1900.9,4.75,"performance");

        System.out.println(cocheElectrico2);

        cocheElectrico2.acelerar(50);

        System.out.println(cocheElectrico2);
    }
}
