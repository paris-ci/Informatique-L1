# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""

"""

import colorsys
from tkinter import *
from tkinter.filedialog import askopenfilename

import webcolors
from PIL import Image, ImageTk


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


if __name__ == "__main__":
    root = Tk()
    liste_val = []

    # setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E + W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N + S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N + S + E + W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH, expand=1)

    # adding the image
    File = askopenfilename(parent=root, initialdir="/Users/arthur/", title='Choisir une image.')
    image = Image.open(File)
    img = ImageTk.PhotoImage(image)
    pix = image.convert('RGB').load()
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))


    # function to be called when mouse is clicked
    def printinfos(event):
        # outputting x and y coords to console
        print("Les coordonnées du pixel sont : ({x},{y})".format(**{
            "x": event.x,
            "y": event.y
            }))
        print("Les couleurs de ce pixel sont (rvb) : " + str(pix[event.x, event.y]))

        r, g, b = pix[event.x, event.y]

        couleur_rgb = (int(r), int(g), int(b))

        ### METHODE 1

        print("méthode 1")

        r /= 255.0
        g /= 255.0
        b /= 255.0

        [h, s, v] = colorsys.rgb_to_hsv(r, g, b)

        # assert h*360 < 270

        lo_1 = 620 - 170 / 270 * h * 360

        print("Les couleurs de ce pixel sont (hsv) : " + str((h, s, v)))

        print("Soit une valeur de \"hue\" de " + str(h * 360))

        print("Nous pouvons donc estimer la valeur de la longueur d'onde à " + str(lo_1))

        ### METHODE 2

        print("méthode 2")

        actual_name, closest_name = get_colour_name(couleur_rgb)

        color_name = actual_name if actual_name else closest_name

        print("Nom de la couleur : " + actual_name if actual_name else (closest_name + " (c)"))
        lo_2 = None
        if color_name == "black":
            lo_2_min, lo_2_max = 0, 0
        elif color_name in ["red", "firebrick", "palevioletred"]:
            lo_2_min, lo_2_max = 650, 780
        elif color_name in ["chocolate", "darkorange", "darksalmon", "orangered"]:
            lo_2_min, lo_2_max = 595, 650
        elif color_name in ["yellow", "gold", "palegoldenrod", "moccasin", "darkolivegreen", "lemonchiffon"]:
            lo_2_min, lo_2_max = 560, 595
        elif color_name in ["yellowgreen", "mediumseagreen", "forestgreen"]:
            lo_2_min, lo_2_max = 500, 560
        elif color_name in ["green", "darkseagreen", "seagreen", "darkcyan", "lime"]:
            lo_2_min, lo_2_max = 490, 500
        elif color_name in ["darkturquoise", "lightseagreen", "lightsteelblue", "royalblue", "cyan"]:
            lo_2_min, lo_2_max = 480, 490
        elif color_name in ["steelblue", "darkblue", "navy", "darkslateblue", "midnightblue", "blue"]:
            lo_2_min, lo_2_max = 435, 480
        elif color_name in ["indigo", "purple", "darkorchid"]:
            lo_2_min, lo_2_max = 380, 435
        else:
            lo_2_min, lo_2_max = lo_1, lo_1

        lo_2 = (lo_2_min + lo_2_max) / 2

        lo_1 = int(lo_1)
        lo_2 = int(lo_2)

        print("La longueur d'onde est de {lo} (moyene de {min} et {max}) nm".format(**{
            "lo": lo_2,
            "min": lo_2_min,
            "max": lo_2_max
            }))

        print("Pour résumer, la longueur d'one trouvée avec la premiere méthode est {m1} et celle avec la deuxieme méthode est {m2}".format(**{
            "m1": lo_1,
            "m2": lo_2
            }))

        return lo_1, lo_2




    def printcoords(event):

        lo_1, lo_2 = printinfos(event)

        # e = ((2k+1)*LO)/4n

        n = 1.3  # indice de réfraction du liquide
        k = int(input("Entrez la valeur de k (nombre de franges avant celles-ci + 1) : >>"))

        e_1 = ((2 * k + 1) * lo_1) / 4 * n + k * 115
        e_2 = ((2 * k + 1) * lo_2) / 4 * n + k * 115

        print("Avec la premiere méthode on trouve {m1} nm d'épaisseur, et avec la deuxieme méthode {m2} nm d'épaisseur".format(**{
            "m1": e_1 / 2 * n,
            "m2": e_2 / 2 * n
            }))

        liste_val.append((int(event.y), int(((e_1 / 2 * n) + (e_2 / 2 * n))/2)))


    # mouseclick event
    canvas.bind("<Button 1>", printcoords)
    canvas.bind("<Button 2>", printinfos)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        raise
    finally:
        print("Liste val" + str(liste_val))

        # import matplotlib.pyplot as plt
        # plt.plot(*zip(*liste_val))
        # plt.title('Epaisseur en fonction de la distance')
        # plt.xlabel('Distance au haut de la photo (pixel)')
        # plt.ylabel('Epaisseur estimée (nm)')
        # plt.show()