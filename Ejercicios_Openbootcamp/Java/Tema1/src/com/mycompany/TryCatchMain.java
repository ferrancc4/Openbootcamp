package com.mycompany;

public class TryCatchMain {

    public static void main(String[] args) {


        try{
            int resut = 5 / 5;
        } catch (ArithmeticException e) {
            e.printStackTrace();// si no imprimim els erros pareix que no passe res
        } finally {
            System.out.println("Cierre de recursos"); // sexecuta sempre
        }

        System.out.println("fin");
    }
}
