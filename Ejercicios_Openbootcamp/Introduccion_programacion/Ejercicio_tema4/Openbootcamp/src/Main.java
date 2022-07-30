public class Main {

    public static void main(String[] args){

        //IF

        var numeroIf = 5;

        if (numeroIf < 0) {
            System.out.println("El numero es negativo");
        } else if (numeroIf > 0) {
            System.out.println("El numero es positivo");
        }else {
            System.out.println("El numero es zero");
        }

        //WHILE

        var numeroWhile = 0;

        while (numeroWhile < 3){
            numeroWhile ++;
            System.out.println(numeroWhile);
        }

        //DO

        do {
            numeroWhile ++;
            System.out.println(numeroWhile);
        } while (numeroWhile < 3);

        //FOR

        for (var numeroFor = 0; numeroFor <= 3;numeroFor ++) {
            System.out.println(numeroFor);
        }

        //SWITCH

        var estacion = "otoño";

        //Si no escribimos exactamente la variable como esta en los casos saldrà el mensaje defaut
        switch (estacion) {
            case "Verano":
                System.out.println("Estamos en el " + estacion);
                break;
            case "Otoño":
                System.out.println("Estamos en el " + estacion);
                break;
            case "Invierno":
                System.out.println("Estamos en el " + estacion);
                break;
            case "Primavera":
                System.out.println("Estamos en el " + estacion);
                break;
            default:
                System.out.println("El valor no es una estacion");
        }

    }

}
