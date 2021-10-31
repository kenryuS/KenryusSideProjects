#define BUTTON_PIN 2

#define KEYCODE_A 0x04

uint8_t buf[8] = {0};

int dotLength = 200;
unsigned long start_t, end_t;
String symbolBuffer = "";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (!signalIncoming()) { }
  start_t = millis();
  while (signalIncoming()) { }
  end_t = millis();

  unsigned long duration = end_t - start_t;

  delay(50);
  if (duration < 20) {
    return;
  }

  char morseChar = charFromSignalDuration(duration);
  symbolBuffer += morseChar;

  while ((millis() - end_t) < dotLength * 3){
    if (signalIncoming()) {return;}  
  }

  int index = morseToCharacterIndex(symbolBuffer);

  symbolBuffer = "";

  if (index < 0) {return;}

  sendChar(KEYCODE_A + index);

  // Wait to see if we're continuing on the same word
  // If we fall out of this loop, we'll append a space
  while ((millis() - end_t) < dotLength * 7) {
    if (signalIncoming()) {
      return;
    }
  }

  sendChar(0x2C);
}

void sendChar(uint8_t code) {
  buf[2] = code;
  Serial.write(buf, 8);
  delay(200);

  buf[2] = 0;
  Serial.write(buf, 8);
  delay(200);
}

int morseToCharacterIndex(const String& morse) {
  static char letters[][5] = {".-", "-...", "-.-.", "-..", ".",
                              "..-.", "--.", "....", "..", ".---",
                              "-.-", ".-..", "--", "-.", "---",
                              ".--.", "--.-", ".-.", "...", "-",
                              "..-", "...-", ".--", "-..-",
                              "-.--", "--..", "E"
                             };

  int i = 0;
  while (String(letters[i]) != "E") {
    if (String(letters[i]) == morse) {
      return i;
    }
    i++;
  }
  return -1;
}

char charFromSignalDuration(unsigned long duration) {
  return (duration < dotLength * 1.5) ? '.' : '-';  
}

bool signalIncoming() {
  return digitalRead(BUTTON_PIN)== LOW;
}
