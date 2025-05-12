/*
SERIAL COMMAND FOR ARDUINO MEGA-MEGA 2560.
Used in conjunction with capture.py
Assigns each GPIO to an LED (oriented orbiting around the device if inserted the correct side, though not imperative)
*/

int ledPins[] = {36,38,40,42,44,46,48,50,52,53,51,49,47,45,43,41,39,37,35,34}; //desired sequence of LEDs - clockwise beginning at ref LED
int numLEDs = 20;

void setup(){
  for (int i=0; i<numLEDs; i++){
    pinMode(ledPins[i], OUTPUT); //set each pin as output
  }
  Serial.begin(115200);
  while (!Serial) { //initialise this way
  }
}

void loop(){
  if (Serial.available()>0){
    //Read command
    String command = Serial.readStringUntil('\n');
    
    //Comma index
    int commaIndex = command.indexOf(',');

    //get index and state
    if (commaIndex > 0){
      int ledIndex = command.substring(0,commaIndex).toInt();
      int ledState = command.substring(commaIndex+1).toInt();
      
      //Set state
      if (ledIndex >= 0 && ledIndex <= numLEDs){
        digitalWrite(ledPins[ledIndex], ledState ? HIGH:LOW);
        
        //Message to python
        Serial.print("LED ");
        Serial.print(ledIndex);
        Serial.print(" set to ");
        Serial.println(ledState ? "ON":"OFF");
      } else{
        Serial.println("Invald LED index given");
      }
    } else{
      Serial.println("Invalid command format give");
    }
  }
}
