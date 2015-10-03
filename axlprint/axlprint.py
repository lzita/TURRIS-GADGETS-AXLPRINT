"""
Script pro zapinani a vypinani dvou tiskaren podle stavu jednotlivych pocitacu ktere je pouzivaji.
pc1 pouziva tiskarnu zapojenou do AC-88 PGX
pc2 a pc3 pouzivaji tiskarnu zapojenou do AC-88 PGY
Script je volan z cronu kazdych 5 minut a podle stavu pocitacu zapne/vypne prislusnou tiskarnu.
Konfigurace a logika je primo v kodu ("stavy pc" a "nastaveni zasuvek")
Pokud je script spusten s parametrem "1" je na STDOUT poskytovan log o prubehu operace.

Script je provozovan a sponzorovan delaerem Jablotronu firmou AXL electronics (http://www.axlelectronics.cz)

(c) 2015 Ludek ZITA
"""

from __future__ import print_function
import sys
import datetime
import time
import os

from device import Device

if __name__ == "__main__":
    # ----- konfigurace --------------------------------------------
    prx = 0
    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            prx = 1
    if prx == 1:
        print("START")
    #------- konstanty ---------------------------------------------
    cmd1 = "TX ENROLL:0"
    cmd2 = ""
    cmd3 = ""
    cmd4 = "ALARM:0 BEEP:NONE"
    #------- stavy pc ---------------------------------------------
    pc1 = os.system("ping -q -c 1 192.168.1.5 > null")
    pc2 = os.system("ping -q -c 1 192.168.1.8 > null")
    pc3 = os.system("ping -q -c 1 192.168.1.125 > null")
    #--------------------------------------------------------------
    if prx == 1:
        if pc1 == 0:
            print("PC1 ZAP")
        else:
            print("PC1 VYP")
        if pc2 == 0:
            print("PC2 ZAP")
        else:
            print("PC2 VYP")
        if pc3 == 0:
            print("PC3 ZAP")
        else:
            print("PC3 VYP")
    #------- nastaveni zasuvek ---------------------------------------------
    if pc1 == 0:
        cmd2 = "PGX:1"
    else:
        cmd2 = "PGX:0"

    if pc2 == 0 or pc3 == 0:
        cmd3 = "PGY:1"
    else:
        cmd3 = "PGY:0"
    
    #--------------------------------------------------------------
    if prx == 1:
        print("Zasuvky:",cmd2,cmd3)
    #------- sestaveni cmd line ---------------------------------------------
    c = cmd1 + " " + cmd2 + " " + cmd3 + " " + cmd4
    #------- odeslani cmd line ---------------------------------------------
    device = Device(device="/dev/ttyUSB0")
    reader = device.gen_lines(timeout=20)
    if prx == 1:
        print("SENDING:", c)
    device.send_command(c)
    r = reader.next()
    if prx == 1:
        print("REPLY:",r)
    time.sleep(0.3)
    if prx == 1:
        print("SENDING:", c)
    device.send_command(c)
    r = reader.next()
    if prx == 1:
        print ("REPLY:",r)
    time.sleep(0.4)
    if prx == 1:
        print("SENDING:", c)
    device.send_command(c)
    r = reader.next()
    if prx == 1:
        print ("REPLY:",r)
    if prx == 1:
        print("KONEC")
