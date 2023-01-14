import random
import PySimpleGUI as sg

if __name__ == '__main__':

    frame_layout = [
        [sg.T('', font='Any 340', background_color="red", key="-TOUT-", size=(3, 1))],
        # [sg.CB('Check 1'), sg.CB('Check 2')],
    ]

    layout = [
        [sg.Frame('Позиция для выгрузки', frame_layout, font='Any 12', title_color='black')],
        [sg.Button("Обновить"), sg.Button("Выход")]
    ]

    # Create the window
    window = sg.Window("Генератор позиции для выгрузки", layout, margins=(50, 50), finalize=True)
    window.bind('<F10>', 'Выход')
    window.bind('<F5>', 'Обновить')

    # Create an event loop
    while True:
        event, values = window.read()

        print(event)
        if event == "Обновить":
            position = random.randint(1, 5)
            print(position)
            window["-TOUT-"].update(f"{position:3}")
        if event in (sg.WIN_CLOSED, "Выход"):
            break

window.close()

