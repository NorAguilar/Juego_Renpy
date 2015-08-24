﻿# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define N = Character('Nor', color="#0000FF")
define L=Character('Linux', color="#6A6AFF")
define B=Character('Boris', color="#DFE32D")
image fondo="fondo.jpg"
image yo="yo.png"
image boris="boris.png"
image btra= "trabajando.jpg"
image ba="turndown.jpg"
image mas="otro.jpg"
image Linux="Linux.jpg"
image alegre="alegre.png"
image frutas="frutas.jpg"
image vacas="vacas.jpg"
image terne="terne.jpg"
image claro="claro.png"
image pensa="pensando.jpg"
image idea="idea.png"
image pp="pp.png"
image pre="pre.png"
image yeah="yeah.jpg"
image sor="sor.png"
image bebida="12.png"
image si="si.jpg"
image oro="oro.jpg"
image dice="dice.jpg"
image we="we.jpg"
image okay="okay.jpg"
image empleado="empleado.jpg"
image rey="rey.jpg"
image regalo="regalo.jpg"
image reino="R.jpg"
image bor="fboris.jpg"

# The game starts here.
# - El juego comienza aquí.

label start:
    
    play music "Mischa Maisky plays Bach Cello Suite No.1 in G (full).mp3"
    
    scene fondo with fade
    show yo:
        ypos 50 xpos 50
    
    N "Vamos a escuchar una linda historia, asi que presta atencion !!"
    hide yo
    
    with dissolve
    scene bor with dissolve
    N "Hace mucho tiempo en el reino de Baku, vivía un hombre muy trabajador llamado: Boris  "
    hide bor
    
    scene fondo with dissolve
    
    show btra:
        xpos 250 ypos 50
    with dissolve
    N "A Boris le encantaba trabajar la tierra y era uno de los mejores agricultores en todo a quel reino"
    hide btra
    show ba:
        xpos 200 ypos 50
    with dissolve
    N "Tambien Boris era propetario de muchos animales"
    hide ba
    show mas:
        xpos 220 ypos 50
    with dissolve
    N "A pesar de que Boris tenia muchas tierras el quería más, mucho más... Un día "
    hide mas
   
    scene reino with dissolve
    N "Boris tuvo la genial idea de llevar un presente al rey de Baku llamado: Linux"
    hide Linux
    
    scene fondo with dissolve
    N "Linux quedó muy contento con el presente de Boris, pues el regalo consistia en : Las mejores frutas cosechadas en el reino y"
    show frutas with dissolve:
        xpos 190 ypos 50
    hide alegre
    hide frutas
    show vacas with dissolve:
        xpos 190 ypos 50
    show terne with dissolve:
        xpos 190 ypos 50
    N "además  Boris le regalaba 5 de las mejores vacas y 5 de las mejores obejas que tenía"
    hide vacas
    hide terne
    show mas with fade:
        xpos 220 ypos 50
    N "Sin embargo Boris conocía muy bien las riquezas del rey y también su generosidad"
    hide mas
    
    show Linux with fade:
        xpos 200 ypos 50
    hide Linux
    show alegre:
        xpos 200 ypos 50
    scene reino with fade
    L "Boris sois muy generoso al obsequiarme estas cosas... ¿os gustaría quedarte a comer hoy con nosotros?"
    hide alegre
    N "Preguntó el rey"
    scene fondo with dissolve
    show claro with dissolve:
        xpos 220 ypos 50
    B "Claro, me gustaría acompañaros señor"
    hide claro
    show mas:
        xpos 220 ypos 50
    N"Dijo Boris astutamente"
    hide mas
    
    show vacas:
        xpos 190 ypos 50
    
    hide vacas
    show terne:
        xpos 190 ypos 50
    
    hide terne
    show vacas:
        xpos 190 ypos 50
    
    hide vacas
    show rey:
        xpos 220 ypos 50
    N "Después del banquete el rey ordenó a sus sirvientes que se le dieran a Boris 10 vacas y 10 terneros, pero que además de eso... "
    hide rey
    show yeah with fade:
        xpos 200 ypos 50
    N "también le dieran 2 tareas de tierra para que las trabajara...  Todo esto en agradecimiento del obsequio de Boris"
    hide yeah
    
    show pensa with dissolve:
        xpos 190 ypos 50
    N "Al día siguiente, Boris estuvo muy pensativo..."
    N "El quería encontrar la forma de repetir aquella hazaña"
    hide pensa
    
    show idea with dissolve:
        xpos 250 ypos 50
    N " Nuevamente quería duplicar sus obsequios y se le ocurrió la mejor de las ideas posibles que un avaro puede tener"
    hide idea
    show oro with dissolve:
        xpos 250 ypos 50
    N "Boris vendió todas sus tierras, junto con ellas lo que contenian incluyendo su ganado"
    hide oro
    show pp with dissolve:
        xpos 250 ypos 50
    N "Una vez en el reino Boris pidió ver al rey "
    hide pp
    show pre with fade:
        xpos 250 ypos 50
    L "Que os trae por aquí nuevamente Boris?"
    N "Preguntó el rey"
    hide pre
    
    show regalo:
        xpos 250 ypos 50
    B "Os traigo un presente que espero no rechaceis"
    hide regalo
    show yeah:
        xpos 250 ypos 50
    N "Respondió Boris"
    hide yeah
    
    show sor with fade:
        xpos 250 ypos 50
    N "El rey quedó sorprendido ante la serpresa aquella; Boris le estaba regalando una gran cantidad de oro y nuevamente lo invitó a comer con ellos"
    hide sor
    
    show si
    show bebida:
        xpos 250 ypos 50
    N "Sin dudarlo Boris aceptó, pero al finalizar la cena,  el rey muy sabiamente le dijo a Boris: "
    hide si
    hide bebida
    N "Antes de todo lesgustaria saber el final ?"
    
    menu: 
        "por supuesto":
                show dice with fade:
                    xpos 250 ypos 50
                L "Boris sois una persona muy importante; tienes tierras trabajadas, ganado, una enorme casa y una gran cantidad de oro... No hay nada en este reino que se te pueda dar !!"
                hide dice
                show we with dissolve:
                    xpos 250 ypos 50
                L "Pero estoy muy agradecido contigo!"
                hide we
                show okay with fade:
                    xpos 250 ypos 50
    
                hide okay
                show empleado with fade:
                    xpos 250 ypos 50
                N "Moraleja: Hacer bien sin mirar a quien, dar sin esperar nada a cambio"
        
        "no no quiero":
                N "De todas formas se los voy a contar"
                show dice with fade:
                    xpos 250 ypos 50
                L "Boris sois una persona muy importante; tienes tierras trabajadas, ganado, una enorme casa y una gran cantidad de oro... No hay nada en este reino que se te pueda dar !!"
                hide dice
                show we with dissolve:
                    xpos 250 ypos 50
                L "Pero estoy muy agradecido contigo!"
                hide we
                show okay with fade:
                    xpos 250 ypos 50
    
                hide okay
                show empleado with fade:
                    xpos 250 ypos 50
                N "Moraleja: Hacer bien sin mirar a quien, dar sin esperar nada a cambio"
    
    
return

