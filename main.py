import random
import PySimpleGUI as sg

if __name__ == '__main__':

    events = {
        "exit": "-EXIT-",
        "reload": "-RELOAD-"
    }

    frame_layout = [
        [sg.T('', font='Any 340', background_color="red", key="-TOUT-", size=(3, 1))],
        # [sg.CB('Check 1'), sg.CB('Check 2')],
    ]

    layout = [
        [sg.Frame('Позиция для выгрузки', frame_layout, font='Any 12', title_color='black')],
        [sg.Button("Обновить", key=events.get("reload")), sg.Button("Выход", key=events.get("exit"))]
    ]

    # Create the window
    window = sg.Window("Генератор позиции для выгрузки", layout, margins=(50, 50), finalize=True)
    window.bind('<F10>', events.get("exit"))
    window.bind('<F5>', events.get("reload"))

    # Create an event loop
    while True:
        event, values = window.read()

        print(event)
        if event == events.get("reload"):
            position = random.randint(1, 5)
            print(position)
            window["-TOUT-"].update(f"{position:3}")
        if event in (sg.WIN_CLOSED, events.get("exit")):
            break

window.close()

