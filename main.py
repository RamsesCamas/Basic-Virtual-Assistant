import pyttsx3 
import speech_recognition as sr
import datetime

ENGINE = pyttsx3.init()
ENGINE.setProperty('rate',170)

MONTHS = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
          'Agosto','Septiembre','Octubre','Noviembre','Diciembre')

get_month = lambda month:MONTHS[month-1] 


def run():
    #sentence = input("Ingresa una frase: ")
    #speak(sentence,ENGINE)
    get_time()
    #get_date()

def speak(sentence):
    ENGINE.say(sentence)
    ENGINE.runAndWait()

def get_time():
    c_time = datetime.datetime.now().strftime("%H:%M")
    hours = c_time[0:2] + ' horas'
    time_of_day = int(c_time[0:2])
    greetins(time_of_day)
    minutes = c_time[3::] + ' minutos'
    speech = 'Son las ' + hours + ' con ' + minutes
    speak(speech)

def get_date():
    date = datetime.datetime.now()
    year = date.year
    month =  date.month
    month = get_month(month)
    day = date.day
    date = f'Es el {day} de {month} del {year}'
    speak(date)

def greetins(time_of_day):
    speech = ''
    if time_of_day >=5 and time_of_day <12:
        speech = 'Buenos días, Señor'
    elif time_of_day >=12 and time_of_day <19:
        speech = 'Buenas tardes, Señor'
    elif time_of_day >= 19 and time_of_day <=24:
        speech = 'Buenas noches, Señor'
    else:
        speech = 'Debería estar durmiendo, Señor'
    speak(speech)

def get_commands():
    pass


if __name__ == "__main__":
    run()