public class Main {

    public static void main(String[] args){
        Cliente cliente = new Cliente(28, "Ferran", 658796244, 5000);
        System.out.println("Edad del cliente: " + cliente.edad + "\n" +
                "Nombre cliente: " + cliente.nombre + "\n" +
                "Telefono cliente: " + cliente.telefono + "\n" +
                "Credito cliente: " + cliente.Credito);

        Trabajador trabajador = new Trabajador(28, "Ferran", 658796244, 20000);
        System.out.println("Edad del trabajador: " + trabajador.edad + "\n" +
                "Nombre trabajador: " + trabajador.nombre + "\n" +
                "Telefono trabajador: " + trabajador.telefono + "\n" +
                "Credito trabajador: " + trabajador.Salario);

    }
}

class Persona {
    int edad;
    String nombre;
    int telefono;
}

class Cliente extends Persona {
    int Credito;

    public Cliente (int edad, String nombre, int tel, int credit) {
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = tel;
        Credito = credit;
    }
}

class Trabajador extends Persona {
    int Salario;

    public Trabajador (int edad, String nombre, int tel, int salary) {
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = tel;
        Salario = salary;
    }
}