# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:35:13 2019

@author: puppy
"""
#!/bin/python3
from turtle import*
from random import*
#variables
playerscore = 0
play = 1
bye = 'none'
  #making the game replayable
while True:
  i = 0
  x = 0
  Toro = Turtle()
  Jasper = Turtle()
  Koda = Turtle()
  win = 'none'
  guess = 'no guess'
  #Setting the stage
  hideturtle()
  penup()
  speed(4)
  #fallback for ending
  ##exitonclick()
  #Toro
  Toro.shape('turtle')
  Toro.color('#7D9AA6')
  Toro.penup()
  Toro.goto(-160,130)
  Toro.pendown()
  goto (80, 130)
  write("Toro")
  #Jasper
  Jasper.shape('turtle')
  Jasper.color('#52DCF5')
  Jasper.penup()
  Jasper.goto(-160,110)
  Jasper.pendown()
  goto (80, 110)
  write("Jasper")
  #Koda
  Koda.shape('turtle')
  Koda.color('#4A1B8B')
  Koda.penup()
  Koda.goto(-160,90)
  Koda.pendown()
  goto (80, 90)
  write("Koda")
  #Creating the X & Y
  goto(-150,150)
  while i < 11:
    write(i, align='center')
    right(90)
    penup()
    forward(10)
    pendown()
    forward(80)
    penup()
    backward(90)
    left(90)
    forward(20)
    i += 1
  #Finishline
  write('FIN!', align = 'center')
  right(90)
  forward(10)
  pendown()
  forward(80)
  hideturtle()
  #Who will win?
  guess = input("Who do you think will win?")
  print("Your guess is: ")
  print(guess)
  #Race
  for turn in range(80):
    Toro.forward(randint(1,5))
    Jasper.forward(randint(1,5))
    Koda.forward(randint(1,5))
    #finishline celebration w/ setting variable
    if Toro.pos() > (70, 129):
      while x < 6:
        Toro.right(60)
        x = x + 1
        if x == 6:
          print('Toro wins!')
          win = ('Toro')
    if Jasper.pos() > (70, 109):
      while x < 6:
        Jasper.right(60)
        x = x + 1
        if x == 6:
          print('Jasper wins!')
          win = ('Jasper')
    if Koda.pos() > (70, 89):
      while x < 6:
        Koda.right(60)
        x = x + 1
        if x == 6:
          print('Koda wins!')
          win = ('Koda')
  if win == guess:
    print('You guessed correctly!')
    playerscore = playerscore + 1
  else: 
    print('Sorry!')
  print('Your score is: ')
  print(playerscore)
  play = input('Play again? 0 for no, 1 for yes -')
  if play == '0':
    print('Goodbye!')
    break
  reset()
  Toro.reset()
  Jasper.reset()
  Koda.reset()
#Telling the program to stop running
done()