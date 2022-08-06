import time

tiempoSalida = 19
hora = int(time.strftime("%H"))


if hora < tiempoSalida:
    restahora = tiempoSalida - hora
    restaminutos = 60 - int(time.strftime("%M"))
    tiempoRestante = "{}:{}".format(restahora, restaminutos)
    print("Faltan", tiempoRestante, "horas para ir a casa")
else:
    print("Ya puedes ir a casa")


