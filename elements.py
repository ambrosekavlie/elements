#!/usr/local/bin/python3
# Elements: a small program to make memorizing the elements of the periodic table easy

import os
import time

# SETTINGS
SET_BACK = 5 # the amount of elements it will bring you back if you get one wrong
START_ELEMENT = 1 # the element you start at. 1 is Hydrogen.
YOU_WIN_MSG = "You memorized all 118 elements!" # the message displayed at the end if you win
YOU_WIN_SPEED = 0.02 # the speed at which the message is printed. Lower is faster since it is the time slept between prints.
# if you want to rename any elements for whatever reason, or edit what the correct answers are, feel free to do so below.
ELEMENTS = (
    "1 Hydrogen H",
    "2 Helium He",
    "3 Lithium Li",
    "4 Beryllium Be",
    "5 Boron B",
    "6 Carbon C",
    "7 Nitrogen N",
    "8 Oxygen O",
    "9 Flourine F",
    "10 Neon Ne",
    "11 Sodium Na",
    "12 Magnesium Mg",
    "13 Aluminium Al",
    "14 Silicon Si",
    "15 Phosphorus P",
    "16 Sulfur S",
    "17 Chlorine Cl",
    "18 Argon Ar",
    "19 Potassium K",
    "20 Calcium Ca",
    "21 Scandium Sc",
    "22 Titanium Ti",
    "23 Vanadium V",
    "24 Chromium Cr",
    "25 Manganese Mn",
    "26 Iron Fe",
    "27 Cobalt Co",
    "28 Nickel Ni",
    "29 Copper Cu",
    "30 Zinc Zn",
    "31 Gallium Ga",
    "32 Germanium Ge",
    "33 Arsenic As",
    "34 Selenium Se",
    "35 Bromine Br",
    "36 Krypton Kr",
    "37 Rubidium Rb",
    "38 Strontium Sr",
    "39 Yttrium Y",
    "40 Zirconium Zr",
    "41 Niobium Nb",
    "42 Molybdenum Mo",
    "43 Technetium Tc",
    "44 Ruthenium Ru",
    "45 Rhodium Rh",
    "46 Palladium Pd",
    "47 Silver Ag",
    "48 Cadmium Cd",
    "49 Indium In",
    "50 Tin Sn",
    "51 Antimony Sb",
    "52 Tellurium Te",
    "53 Iodine I",
    "54 Xenon Xe",
    "55 Caesium Cs",
    "56 Barium Ba",
    "57 Lanthanum La",
    "58 Cerium Ce",
    "59 Praseodymium Pr",
    "60 Neodymium Nd",
    "61 Promethium Pm",
    "62 Samarium Sm",
    "63 Europium Eu",
    "64 Gadolinium Gd",
    "65 Terbium Tb",
    "66 Dysprosium Dy",
    "67 Holmium Ho",
    "68 Erbium Er",
    "69 Thulium Tm",
    "70 Ytterbium Yb",
    "71 Lutetium Lu",
    "72 Hafnium Hf",
    "73 Tantalum Ta",
    "74 Thungsten W",
    "75 Rhenium Re",
    "76 Osmium Os",
    "77 Iridium Ir",
    "78 Platinum Pt",
    "79 Gold Au",
    "80 Mercury Hg",
    "81 Thallium Tl",
    "82 Lead Pb",
    "83 Bismuth Bi",
    "84 Polonium Po",
    "85 Astatine At",
    "86 Radon Rn",
    "87 Francium Fr",
    "88 Radium Ra",
    "89 Actinium Ac",
    "90 Thorium Th",
    "91 Protactinium Pa",
    "92 Uranium U",
    "93 Neptunium Np",
    "94 Plutonium Pu",
    "95 Americium Am",
    "96 Curium Cm",
    "97 Berkelium Bk",
    "98 Californium Cf",
    "99 Einsteinium Es",
    "100 Fermium Fm",
    "101 Mendelevium Md",
    "102 Nobelium No",
    "103 Lawrencium Lr",
    "104 Rutherfordium Rf",
    "105 Dubnium Db",
    "106 Seaborgium Sg",
    "107 Bohrium Bh",
    "108 Hassium Hs",
    "109 Meitnerium Mt",
    "110 Darmstadtium Ds",
    "111 Roentgenium Rg",
    "112 Copernicium Cn",
    "113 Nihonium Nh",
    "114 Flerovium Fl",
    "115 Moscovium Mc",
    "116 Livermorium Lv",
    "117 Tennessine Ts",
    "118 Oganesson Og"
)

# you win message
def you_win():
    partial = ""
    for i in YOU_WIN_MSG:
        partial += i
        print(partial)
        time.sleep(YOU_WIN_SPEED)

if __name__ == "__main__":
    os.system("clear")
    i = START_ELEMENT - 1
    print(f"You are at element {i+1}.")
    while i < len(ELEMENTS):
        element = ELEMENTS[i]
        element_input = input()
        if element_input == element:
            # if is correct, move on to next element
            i += 1
        else:
            # if not correct move back SET_BACK elements and clear screen. Display incorrect message.
            input(f"Incorrect, the answer is {element}.")
            os.system("clear")
            i -= SET_BACK
            # make sure i is > 0 in case it sets back before Hydrogen we don't go farther than that
            if i <= 0:
                i = 0
                print("You are at element 1.")
            else:
                print(f"You are at element {i+1}. The previous element is {ELEMENTS[i-1]}.")
    you_win()