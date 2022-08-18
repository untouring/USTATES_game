import turtle
from turtle import Screen
import pandas
import pygame
import time

screen = Screen()
screen.title("U.S. States Game")
screen.setup(800, 600)
img = "blank_states_img.gif"
screen.addshape(img)

image = turtle.Turtle()

image.shape(img)

pygame.init()
pygame.mixer.music.load("anthem.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
time.sleep(0.02)

fifty_states = pandas.read_csv('50_states.csv')

all_states = fifty_states.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    state_answer = turtle.textinput(title=f"{len(guessed_states)}/States Correct",
                                    prompt="What's another state?").title()
    if state_answer == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        print(missed_states)
        #missing_states = pandas.DataFrame(missed_states)
        #missing_states.to_csv("states_to_learn.csv")
        break
    if state_answer in all_states:
        guessed_states.append(state_answer)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = fifty_states[fifty_states.state == state_answer]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(state_answer, font=("Verdana", 8, "bold"))


