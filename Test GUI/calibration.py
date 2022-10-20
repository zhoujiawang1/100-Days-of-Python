from turtle import delay, width
from tkinter import Tk, simpledialog
from pywinauto import Application
import os

PATH_CONFIG = ""
PATH_MOTOR = "C:/Hyperterminal/hypertrm.exe"
PATH_ORIEL = "C:/Hyperterminal/Oriel.ht"


class CalibSettings:

    def __init__(self):
        self.energy = -1
        self.repRate = -1
        self.grating = -1
        self.wavelength = -1
        self.gain = -1
        self.pulse_width = -1
        self.pulse_delay = -1
        self.expo_time = -1
        self.motor_pos = ""

    def load_config(self, element):
        path = PATH_CONFIG + "\\" + element + ".txt"
        file = open(file=path, mode='r')
        # TODO Make a format OR read format for element.cfg
        config = []
        lines = file.readlines()

        for line in lines:
            empty_str = ""
            for c in line:
                if c.isdigit() == True:
                    empty_str += c
            if empty_str.isdigit():  # only puts numbers in the list
                config.append(int(empty_str))

        self.energy = config[0]
        self.repRate = config[1]
        self.grating = config[2]
        self.wavelength = config[3]
        self.gain = config[4]
        self.pulse_width = config[5]
        self.pulse_delay = config[6]
        self.expo_time = config[7]
        self.motor_pos = "G"+str(config[8])

        file.close()

    def place_motor(self):
        app = Application().start(PATH_MOTOR)
        app.top_window_().CancelButton().click()
        app.NewConnection.menu_item(u"&File->&Open")
        app.top_window_().type_keys(PATH_ORIEL)
