public class Main {

    public static void main(String[] args){
        suma(5, 15, 20);

        Coche miCoche = new Coche();
        miCoche.PonerPuertas();
        miCoche.PonerPuertas();
        System.out.println("El coche tiene: " + miCoche.puertas + " puertas");

    }

    public static void suma(int a, int b, int c){
        System.out.println(a + b+ c);
    }

}

class Coche {
    public  int puertas = 0;

    public void PonerPuertas() {
        this.puertas++;
    }
}