#!/usr/bin/env python3
import time
import string
import config
from psu import PSU

psu = PSU()

def main():
    print("TTi PSU Remote Test")
    print("1. Connect")
    print("2. Turn On")
    print("3. Turn Off")
    print("4. Set Voltage to 7V")
    print("5. Set Voltage1 to 13V")
    print("6. Quit")

    while True:
        inp = input(":> ")
        if inp == "1":
            psu.connect()
        elif inp == "2":
            psu.turn_on()
        elif inp == "3":
            psu.turn_off
        elif inp == "4":
            psu.set_voltage(7)
        elif inp == "5":
            psu.set_voltage(13)
        elif inp == "6":
            quit()

if __name__ == '__main__':
    main()
