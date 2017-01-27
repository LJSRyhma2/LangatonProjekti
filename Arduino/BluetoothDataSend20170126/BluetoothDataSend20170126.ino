#include <CurieBLE.h>

BLEPeripheral blePeripheral;       // BLE Peripheral Device
BLEService dataService("180F");    // BLE Data Service

// BLE Battery Level Characteristic"
BLEUnsignedCharCharacteristic dataChar("2A19",  // standard 16-bit characteristic UUID
    BLERead | BLENotify);     // remote clients will be able to
// get notifications if this characteristic changes

int oldData = 0;  // last battery level reading from analog input
long previousMillis = 0;  // last time the battery level was checked, in ms

void setup() {
  Serial.begin(9600);    // initialize serial communication
  pinMode(13, OUTPUT);   // initialize the LED on pin 13 to indicate when a central is connected

  /* Set a local name for the BLE device
     This name will appear in advertising packets
     and can be used by remote devices to identify this BLE device
     The name can be changed but maybe be truncated based on space left in advertisement packet */
  blePeripheral.setLocalName("Ryhma2BLE");
  blePeripheral.setAdvertisedServiceUuid(dataService.uuid());  // add the service UUID
  blePeripheral.addAttribute(dataService);   // Add the BLE data service
  blePeripheral.addAttribute(dataChar); // add the data characteristic
  dataChar.setValue(oldData);   // initial value for this characteristic

  /* Now activate the BLE device.  It will start continuously transmitting BLE
     advertising packets and will be visible to remote BLE central devices
     until it receives a new connection */
  blePeripheral.begin();
  delay(4000);
  Serial.println("Bluetooth device active, waiting for connections...");
}

void loop() {
  // listen for BLE peripherals to connect:
  BLECentral central = blePeripheral.central();

  // if a central is connected to peripheral:
  if (central) {
    Serial.print("Connected to central: ");
    // print the central's MAC address:
    Serial.println(central.address());
    // turn on the LED to indicate the connection:
    digitalWrite(13, HIGH);

    // check the battery level every 200ms
    // as long as the central is still connected:
    while (central.connected()) {
      long currentMillis = millis();
      // if 200ms have passed, check the battery level:
      if (currentMillis - previousMillis >= 200) {
        previousMillis = currentMillis;
        updateData();
      }
    }
    // when the central disconnects, turn off the LED:
    digitalWrite(13, LOW);
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
}

void updateData() {
  int rawData = random(0,1023);       // read the data
  int filteredData = map(rawData, 0, 1023, 0, 100); // map the data to something sensible

  if (filteredData != oldData) {      // if the data has changed
    Serial.print("New reading: ");    // print it
    Serial.println(filteredData);
    dataChar.setValue(filteredData);  // and update the data characteristic
    oldData = filteredData;           // save the data for next comparison
  }
}

