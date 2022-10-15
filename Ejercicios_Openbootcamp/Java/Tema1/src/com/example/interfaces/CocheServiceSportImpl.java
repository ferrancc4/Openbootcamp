package com.example.interfaces;

import com.example.Coche;
import com.example.CocheElectrico;

public class CocheServiceSportImpl implements CocheService{
    @Override
    public Coche crearCocheDemo() {
        System.out.println("Creando coche de carreras");
        return new CocheElectrico();
    }
}
