import serial
import MySQLdb
import datetime
import time
from decimal import Decimal

connected = False
ser = serial.Serial('/dev/ttyACM0', 9600)



dbc = ("localhost", "root", "ryhma7", "projekti")
db = MySQLdb.connect(dbc[0],dbc[1],dbc[2],dbc[3])
curs = db.cursor()

idQuery = "SELECT id FROM Mittaukset ORDER BY id DESC LIMIT 1"
curs.execute(idQuery)

viiminen = int(curs.fetchone()[0])



#-------------------------------------------------------------------------------------------------------







tiedot = ("INSERT INTO Mittaukset" 
            "(id, aika, lampo, kosteus)"
            "VALUES (%s,%s,%s,%s)")
laskuri = 0 
laskuri = viiminen

while not connected:
        serin = ser.read()
        connected = True

if (connected == True):
        print "Connected!"

else:
        print "NOT Connected!"



while 1:
        laskuri = laskuri + 1 
    
    
    
    
        ts = time.time()

        tm = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


        arvot = ser.readline()
        kosteus, lampo = arvot.split(",")

        kosteus = float(kosteus)
        lampo = float(lampo)

    #   print "Huoneen lampo: %.2f"  % lampo
    #   print "Huoneen kosteus: %.2f" % kosteus

        data_tiedot = (laskuri,tm,lampo,kosteus)

        try:
            curs.execute (tiedot,data_tiedot)
            db.commit()
        except:
            print "meni vituiksi"
            db.rollback()
        if laskuri >= 100:
            curs.execute("TRUNCATE TABLE Mittaukset")
            laskuri = 1
                                                                                                                                                                                                

