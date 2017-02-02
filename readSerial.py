import serial
import MySQLdb
import datetime
import time
from decimal import Decimal
import smbus



connected = True
ser = serial.Serial('/dev/ttyACM0', 9600)


dbc = ("localhost", "root", "raspberry", "projekti")
db = MySQLdb.connect(dbc[0],dbc[1],dbc[2],dbc[3])
curs = db.cursor()

idQuery = "SELECT id FROM Mittaukset ORDER BY id DESC LIMIT 1"
curs.execute(idQuery)

viiminen = int(curs.fetchone()[0])



# GPS Maarritykset
bus = smbus.SMBus(1)

address = 0x68



#-------------------------------------------------------------------------------------------------------


tiedot = ("INSERT INTO Mittaukset" 
            "(id, aika, kosteus,latitudeDegree,latitude,longitudedegree,longitude)"
            "VALUES (%s,%s,%s,%s,%s,%s,%s)")
laskuri = 0 
laskuri = viiminen

while not connected:
        serin = ser.read()
        connected = True

if (connected == True):
        print "Connected!"

else:
        print "NOT Connected!"


def get_single(register):
    try:
            value = bus.read_byte_data(address, register)
            return value
    except:
        print 'get Single, Oops!'
        return 0





def get_double(register):
    try:
        value1 = bus.read_byte_data(address, register)
        value2 = bus.read_byte_data(address, register+1)
        value = (value1 * 10) + value2
        return value
    except:
        print "GET_double, OOPS!"
        return 0






while 1:
        laskuri = laskuri + 1 
    
    
    
    
        ts = time.time()

        tm = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        # Read time from module and display
        hours = get_double(0)
        minutes = get_double(2)
        seconds = get_double(4)
        print hours,':',minutes,':',seconds

        time.sleep(1)

        # Read Heading from module and display
        heading = float(get_single(44))*100
        heading += float(get_single(45))*10
        heading += float(get_single(46))
        heading += float(get_single(47))/10
       # print 'heading: %.1f' %(heading)

        time.sleep(1)
        # Read speed from module and display
        speed = float(get_single(52))*100
        speed += float(get_single(53))*10
        speed += float(get_single(54))
        speed += float(get_single(55))/10
        #print 'speed: %.1f' %(speed)

        time.sleep(1)

    # Read latitude from module and display
        latitude_degrees = get_double(14)
        latitude_minutes = float(get_double(16))
        latitude_minutes += float(get_single(18))/10
        latitude_minutes += float(get_single(19))/100
        latitude_minutes += float(get_single(20))/1000
        latitude_minutes += float(get_single(21))/10000
        latitude_direction = chr(get_single(22))
    #    print 'latitude: %.0f %.5f %s' %(latitude_degrees,latitude_minutes,latitude_direction)

        time.sleep(1)

    # Read longitude from module and display
        longitude_degrees = get_single(23)*100
        longitude_degrees += get_double(24)
        longitude_minutes = float(get_double(26))
        longitude_minutes += float(get_single(28))/10
        longitude_minutes += float(get_single(29))/100
        longitude_minutes += float(get_single(30))/1000
        longitude_minutes += float(get_single(31))/10000
        longitude_direction = chr(get_single(32))
     #   print 'longitude: %.0f %.5f %s' %(longitude_degrees,longitude_minutes,longitude_direction)

        time.sleep(1)                                                                                                                  


        latitudeDeg = latitude_degrees
        latitude = latitude_minutes
        longitudeDeg = longitude_degrees
        longitude = longitude_minutes

        #print latitude
        #print longitude


        kosteus = ser.readline()
        #kosteus = arvot

        
        latitudeDeg = int(latitudeDeg)
        latitude = float(latitude)

        longitudeDeg = int(latitudeDeg)
        longitude = float(latitude)        

        kosteus = float(kosteus)
    #   lampo = float(lampo)
        
    #   print "Huoneen lampo: %.2f"  % lampo
        print "Huoneen kosteus: %.2f" % kosteus
        
           

        data_tiedot = (laskuri,tm,kosteus,latitudeDeg,latitude,longitudeDeg,longitude)

        try:
            curs.execute(tiedot,data_tiedot)
            db.commit()
        except:
            print "meni vituiksi"
            db.rollback()
        if laskuri >= 100:
            curs.execute("TRUNCATE TABLE Mittaukset")
            laskuri = 1
                                                                                                                                                     
