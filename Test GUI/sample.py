from datetime import today
import os
from tkinter import Tk, simpledialog
from pywinauto import Application
from pynput.keyboard import Controller, Key
import tkinter as tki

from calibration import CalibSettings


PATH_CALIB = ""
PATH_BOUCLE = "boucle_run.pgm"
root = Tk()


class Sample:

    def __init__(self):
        self.element = ""
        self.settings = CalibSettings()
        self.sample_quantity = 5  # number of replicas by default
        self.id = ""
        self.concentration = -1

    def ctrl_key(self, key):
        keyboard = Controller()

        keyboard.press(Key.ctrl)
        keyboard.press(key)
        keyboard.release(Key.ctrl)
        keyboard.release(key)

    def open_solis(self):  # DONE
        '''
        Opens Andor Solis and will return an application object
        '''
        # TODO Test if works
        return Application().start(cmd_line="AndorSolis.exe")

    def set_cam_temp(self, solis_app):
        # solis_app.connect()  # NOTES MAY NOT BE NECESSARY
        self.ctrl_key("t")

        # TODO need to check if a box to check to modify temperature

        # TODO Object will be Tempature, needs to find id of temp box
        # NOTES ou remplacer TempControl avec top_window()
        solis_app.TemperatureControl.Temperature.type_keys("-15")
        solis_app.OKButton.click()

    def ask_element(self):  # DONE
        self.element = simpledialog.askstring(
            "What is the full name of the element of your sample? (format ex. Calcium)"
        ).lower().capitalize()

    def check_todays_folder(self):  # DONE
        '''
        Checks if the folder for the current day exists for the calibration.
        if does not exist, will create one "Calib_%b_%d_%y"
        '''
        self.settings.load_settings(self.element)
        path = PATH_CALIB + self.element + "/_" + today.strftime("%d%b%y")
        if not (os.path.exists(path)):
            os.makedirs(path)

    def launch_bg_acq(self, solis_app):  # DONE
        solis_app.AndorSolis.menu_item(
            u"&Acquisition->&Take Background->&Photo-Cathode On")
        solis_app.top_window_().OKButton.click()

    def ask_concentration_id(self):  # DONE
        '''
        Creates a popup window that asks the user to enter the concentration
        and the name of the current sample
        '''
        # TODO IMPLEMENT POPUP WINDOW THAT ASKS THOSE QUESTIONS DONE
        self.concentration = simpledialog.askstring(
            "What is the concentration (ppm) of your sample? ( format ex. 01000ppm)")
        self.id = simpledialog.askstring(
            "What is the id of your sample? (format ex. S01)")

    def disp_settings(self):
        # TODO PRINT ON A POPUP WINDOW

        settings = self.settings
        question = f"Energy (mJ): {settings.energy}\nRepetition Rate(Hz): {settings.repRate}\nGrating: {settings.grating}\nWavelength(nm): {settings.wavelength}\nGain: {settings.gain}\nWidth(ns): {settings.pulse_width}\nDelay(ns): {settings.pulse_delay}\nExposure Time(s): {settings.expo_time}\n"
        question += "Would you like to change the current settings?"
        self.ask_modify_settings(question)
        root.mainloop()

    def modify_settings(self):
        setting = CalibSettings()
        # energy
        setting.energy = simpledialog.askstring(
            "What is the energy of your laser in mJ? (format ex. 20)")
        # repRate
        setting.repRate = simpledialog.askstring(
            "What is the repetition rate of your laser in Hz? (format ex. 5)")
        # grating
        setting.grating = simpledialog.askstring(
            "What is the grating of your setup? (format ex. 600)")
        # wavelength
        setting.wavelength = simpledialog.askstring(
            "What is the central wavelength of your element in nm? (format ex. 420)")
        # gain
        setting.gain = simpledialog.askstring(
            "What is the gain of your camera? (format ex. 1750)")
        # pulse_width
        setting.pulse_width = simpledialog.askstring(
            "What is the pulse width of your camera in nm? (format ex. 260)")
        # pulse delay
        setting.pulse_delay = simpledialog.askstring(
            "What is the pulse delay of your camera in nm? (format ex. 1500)")
        # exposure time
        setting.expo_time = simpledialog.askstring(
            "What is the exposure time of your camera in s? (format ex. 60)")
        # motor position
        setting.motor_pos = simpledialog.askstring(
            "What is the motor position of the optic fiber? (format ex. G3750)")
        root.destroy()

    def ask_modify_settings(self, question, root):

        # text for the popup window + button
        label = tki.Label(root, text=question)
        # TODO make function to modify settings DONE
        bYes = tki.Button(root, text="Yes", command=self.modify_settings)
        bNo = tki.Button(
            root, text="No", command=root.destroy)  # TODO find another alternative for this command

        for el in [label, bYes, bNo]:
            el.pack()

    def configurate_settings(self, solis_app):
        solis_app.menu_item(u"&Acquisition->&Acquisition Settings")
        # TODO Check how to interact with the popup page

    def create_routine(self):
        '''
        will create a routine script for the sampling loop
        '''
        file = open(PATH_BOUCLE, "w")
        file.write(f"for counter = 1 to {self.sample_quantity}")
        file.write("run()")
        file.write("print(count)")
        file.close()

    def take_sampling(self, solis_app):
        '''
        execute the sampling loop
        '''
        if self.id == "S00":
            self.sample_quantity = 10
        self.create_routine()

        # TODO needs to put settings in the configurations

        # OPENS ROUTINE FILE
        solis_app.menu_item(u"&File->&Open... Ctrl+O")
        solis_app.type_keys(PATH_BOUCLE)
        solis_app.OpenButton.click()
        self.ctrl_key("e")  # RUNS THE ROUTINE
