from marvelmind import MarvelmindHedge
from time import sleep
import sys
import serial
import time


def main():
    hedge = MarvelmindHedge(tty="/dev/ttyACM0", adr=None, debug=False)  # create MarvelmindHedge thread

    if (len(sys.argv) > 1):
        hedge.tty = sys.argv[1]
    with serial.Serial("/dev/ttyS0", 9600,
                       timeout=.1) as arduino:  # on tente de se connecter à l'arduino via le port ttyS0
        time.sleep(0.1)
        if arduino.isOpen():  # si il est ouvert on commence le thread marvelmind
            hedge.start()  # start thread
            while True:
                try:
                    hedge.dataEvent.wait(1)
                    hedge.dataEvent.clear()

                    if (hedge.positionUpdated):  # ici on va envoyer la position si la position a changer

                        test = ""
                        test = test + "x" + str(hedge.position()[1]) + "y" + str(hedge.position()[2]) + "z" + str(
                            hedge.position()[3]) + "f"
                        test = test + "\n"
                        print(test)
                        # on va envoyer une chaine sous le format x2.559y-1.428z-0.665f et l'arduino va split cette chaine
                        arduino.write(test.encode())
                        hedge.print_position()

                    if (hedge.distancesUpdated):
                        hedge.print_distances()

                    if hedge.rawImuUpdated:
                        hedge.print_raw_imu()

                    if (hedge.fusionImuUpdated):
                        hedge.print_imu_fusion()

                    if (hedge.telemetryUpdated):
                        hedge.print_telemetry()

                    if (hedge.qualityUpdated):
                        hedge.print_quality()

                    if (hedge.waypointsUpdated):
                        hedge.print_waypoint()
                except KeyboardInterrupt:
                    hedge.stop()  # stop and close serial port
                    sys.exit()


main()
