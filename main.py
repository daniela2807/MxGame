import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "croquis-de-mexico-mapa.gif"
screen.addshape(image)

turtle.shape(image)
adivinados = []
restantes = []


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
restantes = all_states

def get_mouse_click_coor(x, y):
    print(x, y)

while len(adivinados) < 32:
    turtle.onscreenclick(get_mouse_click_coor)
    answer_state = screen.textinput(title=f"{len(adivinados)}/32 estados correctos", prompt="Ingresa un estado: ").title()
    if answer_state.title() == "Exit":
        df = pandas.DataFrame(restantes)
        df.to_csv("restantes.csv",index=False)
        print(df)
        break
    elif answer_state in all_states:
        restantes.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        adivinados.append(answer_state)



screen.exitonclick()