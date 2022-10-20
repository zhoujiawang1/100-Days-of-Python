from calibration import CalibSettings

DEFAULT_GRATING = 600
DEFAUULT_ENERGY = 20  # mJ
DEFAUULT_REPREATE = 5  # hZ

calcium = CalibSettings(energy=DEFAUULT_ENERGY, repRate=DEFAUULT_REPREATE,
                        grating=DEFAULT_GRATING, wavelength=420, gain=1750,
                        width=1500, delay=260, expo_time=60)

lithium = CalibSettings(energy=DEFAUULT_ENERGY, repRate=DEFAUULT_REPREATE,
                        grating=DEFAULT_GRATING, wavelength=650, gain=100,
                        width=2000, delay=280, expo_time=75)

potassium = CalibSettings(energy=DEFAUULT_ENERGY, repRate=DEFAUULT_REPREATE,
                          grating=DEFAULT_GRATING, wavelength=750, gain=100,
                          width=4000, delay=350, expo_time=80)

magnesium = CalibSettings(energy=DEFAUULT_ENERGY, repRate=DEFAUULT_REPREATE,
                          grating=DEFAULT_GRATING, wavelength=500, gain=2000,
                          width=1500, delay=240, expo_time=100)

manganese = CalibSettings(energy=DEFAUULT_ENERGY, repRate=DEFAUULT_REPREATE,
                          grating=DEFAULT_GRATING, wavelength=400, gain=1850,
                          width=1500, delay=260, expo_time=100)


elements = {
    "Ca": calcium,
    "Li": lithium,
    "K": potassium,
    "Mg": magnesium,
    "Mn": manganese
}

# TODO READ THROUGH FILE TO GET SETTINGS
