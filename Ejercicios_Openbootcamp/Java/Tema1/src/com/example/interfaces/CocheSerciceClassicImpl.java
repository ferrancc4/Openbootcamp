package com.example.interfaces;

import com.example.Coche;
import com.example.CocheElectrico;

public class CocheSerciceClassicImpl implements CocheService {
    @Override
    public Coche crearCocheDemo() {
        System.out.println("Creando coche clasico");
        return new CocheElectrico();
    }
}
