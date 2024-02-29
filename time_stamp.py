from datetime import datetime
import pytz
import random
def set_time():
    #Definir la zona horaria requerida
    zona_horaria_argentina = pytz.timezone('America/Argentina/Buenos_Aires')
    #Obtener fecha y hora actual en UTC
    fecha_hora_utc = datetime.utcnow()
    #Asignar la zona horaria utc a la zona horaria UTC
    fecha_hora_utc =pytz.utc.localize(fecha_hora_utc)
    #Convertirlo a la zona horaria argentina
    fecha_hora_argentina = fecha_hora_utc.astimezone(zona_horaria_argentina)
    strong =f'Hora en Argentina {fecha_hora_argentina.strftime("%Y-%m-%d %H:%M:%S")} and {fecha_hora_argentina.date()}'
    print(strong)
    return fecha_hora_argentina

set_time()

def horario(fecha_hora:datetime):
    day = fecha_hora.date()
    if day.weekday() == 3:
        #print("Es jueves")
        if fecha_hora.strftime("%H:%M:%S") == "16:15:00":
            print("Es verdadero")
            #number = random.randint(1,4)
            number = random.choice([1,2,3,4,9])
            return number
    elif day.weekday() != 3 and day.weekday() != 5:
        #print("Es otro día")
        if fecha_hora.strftime("%H:%M:%S") == "08:00:00":
            #print("es another day")
            return 7
        if fecha_hora.strftime("%H:%M:%S") == "12:00:00":
            #print("es hi")
            return 5
        if fecha_hora.strftime("%H:%M:%S") == "20:00:00":
            #print("es gif")
            return 6
    if day.weekday() == 5:
            if fecha_hora.strftime("%H:%M:%S") == "22:00:00":
                return 8
    if fecha_hora.strftime("%m-%d %H:%M:%S") == "03-8 14:00:00":
        return 10