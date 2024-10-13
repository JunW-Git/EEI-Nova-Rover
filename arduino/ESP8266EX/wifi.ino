#include <ESP8266WiFi.h>
#include <WiFiUDP.h>

// Replace these with your network credentials
const char* ssid = "SSID";
const char* password = "PASSWORD";

const int PIN_0 = 0; //GPIO0 BLUE CABLE
const int PIN_2 = 2; // GPIO2 GREY CABLE
const int PIN_3 = 3; // GPIO3 or RX YELLOW CABLE
const int PIN_16 = 16; // GPIO16 or RST GREEN CABLE

// UDP settings
unsigned int localUdpPort = 4210;  // Local port to listen on
char incomingPacket[255];  // Buffer for incoming packets
WiFiUDP udp;

String message;
String previous = "";

void setup() {
  Serial.begin(9600);
  
  // Change all IO pins to output
  pinMode(PIN_0, OUTPUT);
  pinMode(PIN_2, OUTPUT);

  pinMode(PIN_3, FUNCTION_3);
  pinMode(PIN_3, OUTPUT);

  pinMode(PIN_16, OUTPUT);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
//    Serial.println("Connecting to WiFi...");
  }
  
//  Serial.print("Connected to ");
//  Serial.println(ssid);
//  Serial.print("IP Address: ");
//  Serial.println(WiFi.localIP());

  // Start listening for UDP packets
  udp.begin(localUdpPort);
//  Serial.printf("UDP listening on IP: %s, Port: %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
}

void loop() {
  int packetSize = udp.parsePacket();
  if (packetSize) {
    // Read the packet into the buffer
    int len = udp.read(incomingPacket, 255);
    if (len > 0) {
      incomingPacket[len] = 0;  // Null-terminate the string
    }
    
    Serial.println(incomingPacket);
    message = incomingPacket;
    message.trim();

    // Only change signals when the message changes
    if (!message.equals(previous)) {
      // Send different GPIO signals based off direction
      if (message.equals("w")) { // 1 0 0 0
        digitalWrite(PIN_0, HIGH);
        digitalWrite(PIN_2, LOW);
        digitalWrite(PIN_3, LOW);
        digitalWrite(PIN_16, LOW);
      } else if (message.equals("a")) { // 0 1 0 0
        digitalWrite(PIN_0, LOW);
        digitalWrite(PIN_2, HIGH);
        digitalWrite(PIN_3, LOW);
        digitalWrite(PIN_16, LOW);
      } else if (message.equals("s")) { // 0 0 1 0
        digitalWrite(PIN_0, LOW);
        digitalWrite(PIN_2, LOW);
        digitalWrite(PIN_3, HIGH);
        digitalWrite(PIN_16, LOW);
      } else if (message.equals("d")) { // 0 0 0 1
        digitalWrite(PIN_0, LOW);
        digitalWrite(PIN_2, LOW);
        digitalWrite(PIN_3, LOW);
        digitalWrite(PIN_16, HIGH);
      } else if (message.equals("wa")) { // 1 1 0 0
        digitalWrite(PIN_0, HIGH);
        digitalWrite(PIN_2, HIGH);
        digitalWrite(PIN_3, LOW);
        digitalWrite(PIN_16, LOW);
      } else if (message.equals("wd")) { // 0 1 1 0
        digitalWrite(PIN_0, LOW);
        digitalWrite(PIN_2, HIGH);
        digitalWrite(PIN_3, HIGH);
        digitalWrite(PIN_16, LOW);
      } else if (message.equals("sa")) { // 0 0 1 1
        digitalWrite(PIN_0, LOW);
        digitalWrite(PIN_2, LOW);
        digitalWrite(PIN_3, HIGH);
        digitalWrite(PIN_16, HIGH);
      } else if (message.equals("sd")) { // 1 1 1 0
        digitalWrite(PIN_0, HIGH);
        digitalWrite(PIN_2, HIGH);
        digitalWrite(PIN_3, HIGH);
        digitalWrite(PIN_16, LOW);
      } else {
        digitalWrite(PIN_0, LOW);
        digitalWrite(PIN_2, LOW);
        digitalWrite(PIN_3, LOW);
        digitalWrite(PIN_16, LOW);
      }
    }

    previous = message;
  }
}
