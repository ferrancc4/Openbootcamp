public class Main {

    public static void main(String[] args){
        Persona Persona1 = new Persona();

        Persona1.setEdad(28);
        Persona1.setNombre("Ferran");
        Persona1.setTelefono(659874181);

        System.out.println("El usuario uno se llama: " + Persona1.getNombre() +
                "\n" + Persona1.getNombre() + " tiene: " + Persona1.getEdad() + " años\n" +
                "y su numero de telefono es: " + Persona1.getTelefono());
    }
}

class Persona {
    private int edad;
    private String nombre;
    private int telefono;

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public int getEdad() {
        return edad;
    }

    public String getNombre() {
        return nombre;
    }

    public int getTelefono() {
        return telefono;
    }
}