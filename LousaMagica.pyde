# Licença GPL3 - mas atribuição é apreciada!
"""
Desenho com potenciômetros
    Arduino + Firmata All Inputs + 6 pots e um interruptor de mercúrio com pull down
    Alexandre Villares http://abav.lugaralgum.com
    arteprog - arte e programação http://arteprog.space
    Apresentada originalmente na inauguraço do SESC 24 de maio com Estúdio Hacker
    http://estudiohacker.io
    http://twitter.com/estudiohacker
"""

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

for num, porta in enumerate(Arduino.list()):  # Enumera portas seriais
    println(str(num)+":"+porta)               # Mostra no console
NUM_PORTA = 0  # Precisa mudar! Leia a lista no console para descobrir

def setup():
    global arduino
    size(1024, 1024)
    colorMode(HSB)  # para usar HSB em vez de RGB!
    frameRate(30)
    noStroke()
    background(0)
    arduino = Arduino(this, Arduino.list()[NUM_PORTA], 57600)


def draw():
    pot_5= arduino.analogRead(5) # pino A5 (analógico)
    pot_4 = arduino.analogRead(4)
    pot_3 = arduino.analogRead(3)
    pot_2 = arduino.analogRead(2)
    pot_1 = arduino.analogRead(1)
    pot_0 = arduino.analogRead(0)
    tilt = arduino.digitalRead(13) # pino 13 (digital)
    if tilt:
        background(0) # limpa o canvas com preto
    X = pot_5
    Y = pot_0
    tam = pot_1 / 10 # Tamanho
    sat = pot_2 / 4 # Saturação
    opa = pot_3 / 4 # Opacidade/Alpha

    F = frameCount
    fill(F % 255, sat, 255, opa)  # Note modo HSB no setup! (Matiz, Saturação, Brilho, Alfa)
    ellipse(X, Y, tam, tam)
    #print(pot_0, pot_1, pot_2, pot_3, pot_4, pot_5, tilt)
