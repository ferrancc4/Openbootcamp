package com.mycompany;

import com.example.Coche;
import com.example.CocheElectrico;
import com.example.CocheHibrido;

import java.util.ArrayList;
import java.util.List;

public class ListMain {

    public static void main(String[] args) {


        List<String> nombres = new ArrayList<>();

        nombres.add("Nombre1");
        nombres.add("Nombre2");
        nombres.add("Nombre3");
        nombres.add("Nombre4");

        System.out.println(nombres);

        for (String nombre : nombres) {
            System.out.println(nombre);
        }

        List<Coche> coches = new ArrayList<>();

        coches.add(new CocheElectrico());
        coches.add(new CocheHibrido());

        System.out.println(coches);
    }
}
