import random
import PySimpleGUI as sg

if __name__ == '__main__':

    events = {
        "exit": "-EXIT-",
        "clear": "-CLEAR-",
        "reload": "-RELOAD-"
    }

    blocks = ["B", "R", "W", "W", "Y"]

    _colors = {
        "W": "White",
        "R": "Red",
        "B": "Blue",
        "Y": "#ffcc00"
    }

    frame_layout = [
        [sg.T('', font='Any 340', background_color="grey", key="-TOUT-", size=(3, 1))],
    ]

    layout_l = [[
            sg.T("Расположение грузов в зоне хранения:"),
            sg.Button(" "*10, key="-B1-", button_color="grey"),
            sg.Button(" "*10, key="-B2-", button_color="grey"),
            sg.Button(" "*10, key="-B3-", button_color="grey"),
            sg.Button(" "*10, key="-B4-", button_color="grey"),
            sg.Button(" "*10, key="-B5-", button_color="grey")
    ]]

    layout_r = [[
            sg.Button("Обновить", key=events.get("reload")),
            sg.Button("Очистить", key=events.get("clear")),
            sg.Button("Выход", key=events.get("exit"))
    ]]

    layout = [
        [sg.Frame('Цвет груза и позиция для выгрузки', frame_layout, font='Any 12', title_color='white')],
        [sg.Col(layout_l, p=0), sg.Push(), sg.Col(layout_r, p=0)]
    ]

    # Create the window
    window = sg.Window("Генератор задания", layout, margins=(50, 50), finalize=True, element_justification='c')
    window.bind('<F10>', events.get("exit"))
    window.bind('<F5>', events.get("reload"))
    window.bind('<F6>', events.get("clear"))

    # Create an event loop
    while True:
        event, values = window.read()

        print(event)
        if event == events.get("reload"):
            position = random.randint(1, 5)
            colors = (_colors["R"], _colors["B"], _colors["Y"])
            color = random.randint(0, 2)
            random.shuffle(blocks)
            print(colors[color], position, blocks)
            window["-TOUT-"].update(f"{position:3}", background_color=colors[color])
            for b, block in enumerate(blocks):
                print(b, block)
                window[f"-B{b+1}-"].update(button_color=_colors[block])
        if event == events.get("clear"):
            window["-TOUT-"].update("", background_color="Grey")
            for b, block in enumerate(blocks):
                window[f"-B{b + 1}-"].update(button_color="Grey")
        if event in (sg.WIN_CLOSED, events.get("exit")):
            break

window.close()

