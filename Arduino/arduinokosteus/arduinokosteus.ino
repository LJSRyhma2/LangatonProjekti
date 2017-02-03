const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to

int sensorValue = 0;        
int outputValue = 0;        

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(analogInPin);

  outputValue = map(sensorValue, 0, 1023, 20, 90);

  Serial.println(outputValue);
  
  delay(1000);
}
