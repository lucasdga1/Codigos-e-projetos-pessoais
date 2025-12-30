import time

timer = int(input("Defina o tempo do timer em segundos: "))

for s in range(timer, 0, -1):
    segundos = s % 60
    minutos = int(s / 60) % 60
    horas = int(s / 3600)
    time.sleep(1)
    print(f"{horas:02}:{minutos:02}:{segundos:02}")


print("Timer finalizado!")


