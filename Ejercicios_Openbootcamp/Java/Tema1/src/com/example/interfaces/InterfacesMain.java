package com.example.interfaces;

import com.example.Coche;

public class InterfacesMain {

    public static void main(String[] args) {


        CocheService service1 = new CocheSerciceClassicImpl();
        CocheService service2 = new CocheServiceSportImpl();

        Coche coche1 = service1.crearCocheDemo();
        Coche coche2 = service2.crearCocheDemo();
    }
}
