import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
states = pandas.read_csv("50_states.csv")
correct_ans = []
game_is_on = True
while game_is_on:
    ans_state = screen.textinput(title=f"{score}/50 are correct", prompt="What's another state's name?").title()

    if ans_state == "Exit":
        break
    for state in states["state"]:
        if ans_state == state:
            x = int(states[states["state"] == ans_state]["x"])
            y = int(states[states["state"] == ans_state]["y"])
            tim = turtle.Turtle()
            tim.penup()
            tim.goto(x, y)
            tim.hideturtle()
            tim.write(f"{ans_state}", align="center", font=("Courier", 8, "bold"))
            correct_ans.append(ans_state)
            score += 1
        else:
            pass

data = []
states_remain = pandas.DataFrame(data)
states_remain.to_csv("states_to_learn.csv")
# print(states["state"])
for state in states["state"]:
    if state not in correct_ans:
        with open("states_to_learn.csv", "a") as file:
            file.write(state+"\n")


# if ans_state == states["state"]:
#     print(ans_state)
# else:
#     pass
# To get the coordinates of states:

# def get_mouse_coor(x, y):
#     print(x, y)
#     # This function basically prints the coordinates of the place where we click from our mouse.
#
#
# turtle.onscreenclick(get_mouse_coor)

