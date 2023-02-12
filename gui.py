from tkinter.tix import MAX
from main import display_mandelbrot

import pygame
import PySimpleGUI as gui


# Set GUI theme
gui.theme("SystemDefaultForReal")


# Return position of mouse for use in zooming/rendering fractals.
def zoom_to_mouse(x, y):
    return (pygame.mouse.get_pos[0], pygame.mouse.get_pos[1])


# Draw GUI with capability of taking user input.
def display_gui():
    # Layout of upper menu bar.
    menu = [
        ["&Help", ["&Mandelbrots"]],
        ["&About"]
    ]

    inputs = [
        [gui.Text("Resolution: "), gui.Input(size = (5, 1), key="_RES_")],
        [gui.Text("(x, i): "), gui.Input(size = (1, 1), key="_ICORD_"), gui.Text(",", pad=(0,0)), gui.Input(size = (1, 1), key="_XCORD_")],
        #[gui.Text("x-coordinate: "), gui.Input(size = (5, 1), key="_XCORD_")],
        [gui.Text("Displacement: "), gui.Input(size = (5, 1), key="_DIS_")],
        [gui.Text("Zoom: "), gui.Slider(range=(1, 4), orientation="horizontal", default_value=2, resolution=0.1, border_width=0, enable_events=True, size=(10,10), key="_ZOOM_")],
    ]

    generate_column = [
        [gui.Button("Generate", key="_GEN_")]
    ]

    # Layout of main GUI.
    layout = [
        [gui.Menu(menu)],
        [gui.Column(inputs), gui.Column(generate_column)]
        
    ]

    sg_window = gui.Window("Mandelbrots!", layout, size=(250, 150))

    run = True
    while run:
        event, values = sg_window.read()
        if event in (gui.WIN_CLOSED, 'Exit'):
            break

        if event == "Mandelbrots":
            print(values["_ZOOM_"])
        elif event == "About":
            print("about feature")
        elif event == "_GEN_":
            print("gen")
            print(values["_XCORD_"])
            print(values["_ICORD_"])
            print(values["_ZOOM_"])
            
            x = float(values["_XCORD_"]) 
            i = float(values["_ICORD_"]) 
            displacement = float(values["_DIS_"])
            zoom = float(values["_ZOOM_"])

            bounds = x + displacement/2, i + displacement/2, displacement
            display_mandelbrot(bounds, zoom)

    sg_window.close()


display_gui()
