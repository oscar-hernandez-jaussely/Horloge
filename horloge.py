
import time
import random

global time_h
global time_m
global time_s

time_h = (0)
time_m = (0)
time_s = (0)


def f_time_adjust():
    global time_a
    if time_h < 10 and not time_m < 10 and not time_s < 10 :
        time_a = (str(int(0)) + str(int(time_h)) + ":" + str(int(time_m)) + ":" + str(int(time_s)))
    elif time_h < 10 and time_m < 10 and not time_s < 10 :
        time_a = (str(int(0)) + str(int(time_h)) + ":" + str(int(0)) + str(int(time_m)) + ":" + str(int(time_s)))
    elif time_h < 10 and time_m < 10 and  time_s < 10 :
        time_a = (str(int(0)) + str(int(time_h)) + ":" + str(int(0)) + str(int(time_m)) + ":" + str(int(0)) + str(int(time_s)))
    elif time_h < 10 and not time_m < 10 and time_s < 10 :
        time_a = (str(int(0)) + str(int(time_h)) + ":" + str(int(time_m)) + ":" + str(int(0)) + str(int(time_s)))
    elif not time_h < 10 and time_m < 10 and time_s < 10 :
        time_a = (str(int(time_h)) + ":" + str(int(0)) + str(int(time_m)) + ":" + str(int(0)) + str(int(time_s)))
    elif not time_h < 10 and time_m < 10 and not time_s < 10 :
        time_a = (str(int(time_h)) + ":" + str(int(0)) + str(int(time_m)) + ":" + str(int(time_s)))
    elif not time_h < 10 and not time_m < 10 and time_s < 10 :
        time_a = (str(int(time_h)) + ":" + str(int(time_m)) + ":" +  str(int(0)) + str(int(time_s)))
    else :
        time_a = (str(int(time_h)) + ":" + str(int(time_m)) + ":" + str(int(time_s)))


def f_time_create():

    global time_h
    global time_m
    global time_s

    f_alarme()

    afficher_heure()

    while time_s < 60 :

        time.sleep(1)

        time_s = time_s + 1

        f_time_adjust()

        print("Time is : " +(time_a))
        
        if time_a == alarme_t:
            print("BEEP BEEP BEEP")

        if time_s == 59:
        
            time.sleep(1)

            time_s = 0

            time_m = time_m +1

            f_time_adjust()

            print("Time is : " +(time_a))    
        
        if time_m == 59:
            
            time.sleep(1)

            time_m = 0

            time_h = time_h +1

            f_time_adjust()

            print("Time is : " +(time_a)) 

        if time_h == 24:
            
            time.sleep(1)

            time_h = 0

            f_time_adjust()

            print("Time is : " +(time_a))



def afficher_heure():

    values = input("Entrez l'heure : ")

    heure = tuple(int(val) for val in values.split())

    print("L'heure choisie est : " + str(heure) )

    global time_h
    global time_m
    global time_s

    time_h = heure[0]
    time_m = heure[1]
    time_s = heure[2]

    f_time_adjust()

    print (time_a)


def f_alarme():
    
    val = input("Entrez l'horaire de l'alarme : ")

    alarme = tuple(int(val) for val in val.split())
   
    global time_h
    global time_m
    global time_s

    time_h = alarme[0]
    time_m = alarme[1]
    time_s = alarme[2]

    f_time_adjust()

    global alarme_t
    alarme_t = time_a
    print(alarme_t)



f_time_create()

