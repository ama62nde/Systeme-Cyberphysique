void setup() {
  Serial.begin(9600);
  Serial2.begin(9600);
}

void loop() {
  if (Serial.available()) {      // If anything comes in Serial (USB),
    Serial2.write(Serial.read());   // read it and send it out Serial1 (pins 0 & 1)
  }

  if (Serial2.available()) {     // If anything comes in Serial1 (pins 0 & 1)
    String trame=Serial2.readString();
   // Serial.write(Serial2.read());// read it and send it out Serial (USB)
    int indexx = trame.indexOf('x');
    int indexy = trame.indexOf('y');
    int indexz = trame.indexOf('z');
    int indexf = trame.indexOf('f');
    float x=trame.substring(indexx+1,indexy-1).toFloat();
    float y=trame.substring(indexy+1,indexz-1).toFloat();
    float z=trame.substring(indexz+1,indexf-1).toFloat();
    Serial.println(x);
    Serial.println(y);
    Serial.println(z);
  }
}