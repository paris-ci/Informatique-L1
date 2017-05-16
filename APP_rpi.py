# -*- coding:Utf-8 -*-
# !/usr/bin/env python3.5

"""
Récuperation des mesures de l'Arduino (Ampérage et Voltage)
"""
import logging

import datetime
import serial
import argparse
import time

parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument('-i', '--interactive', action='store_true', help="Activate interactive mode (Ask to get values)")
parser.add_argument('-d', '--debug', action='store_true', help="Activate debug mode")
parser.add_argument('-na','--noarduino', action='store_true', help="Don't force a connexion to the arduino board")
parser.add_argument('--interval', action='store', help='Time in seconds to wait between each measure')

args = parser.parse_args()


v_mark = "V = "
a_mark = "A = "
to  = 2

moisture_sensor = 1 # Port A1 sur la shield
air_sensor = 0 # Port A0 sur la shield

print("hello")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

steam_handler = logging.StreamHandler()
if args.debug:
    steam_handler.setLevel(logging.DEBUG)
else:
    steam_handler.setLevel(logging.INFO)

steam_handler.setFormatter(formatter)
logger.addHandler(steam_handler)
logger.debug("Starting...")

if not args.noarduino:
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=to)
    except serial.serialutil.SerialException:
        ser = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=to)
else:
    ser = open("to_serial.tty", "wb+")


logger.debug("Serial is " + str(ser))
ser.write(b"3") # WTF ? Le truc réponds pas sinon :(

def write_to_csv(volts="", amps=""):
    volts = str(volts)
    amps  = str(amps)
    with open("results.csv", "a") as outfile:
        outfile.write("{d},{a},{v}".format(d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), v=volts, a=amps))

def mainloop():
    status = 0
    while True:
        logger.debug("Looping")

        if status <= 0:

            if args.interactive:

                i = input("Quelle mesure demander (Voltage (1), Ampérage (2), [Tout (3)]) >")
                i = i if i != "" else "3"
                send = bytes(i, "ascii")
            else:
                send = b"3"

            ser.write(send)
            logger.debug("Sent message : " + str(send))
            if int(send.decode()) in [1, 2]:
                status = 1
            else:
                status = 2

        elif status >= 1:
            logger.debug("Waiting for message")
            line = str(ser.readline().decode('utf-8'))
            logger.debug("Got message")
            line = line.replace("\r", "").replace("\n", "")
            logger.debug("[LINE] " + line)

            if line != "" :
                status -= 1
            else:
                logger.warning("got no message, restarting")
                status = 0

            if line.startswith(v_mark):
                line = line.replace(v_mark, "")

                voltage = float(line)
                logger.info("[VOLT] " + str(voltage))

            elif line.startswith(a_mark):
                line = line.replace(a_mark, "")

                amperage = float(line)
                logger.info("[AMPS] " + str(amperage))

            if status == 0:
                time.sleep(args.interval) if args.interval else ""

        #try:
        #    logger.info("[MOIT] " + str(grovepi.analogRead(moisture_sensor)))
        #except IOError as e :
        #    logger.exception("IO" , e)



if __name__ == '__main__':

    mainloop()