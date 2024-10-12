// Test file - Seeing if wifi connection works with python sending post requests

#include<ESP8266WiFi.h>

const char* ssid="SSID";
const char* password="PASSWORD";

WiFiServer server(80);

String payload;

unsigned long currentTime = millis();
unsigned long previousTime = 0;
const long timeoutTime = 2000;

void setup() {
  // put your setup code here, to run once:
  delay(800); // Give some time when connecting to power

  Serial.begin(9600);
  Serial.println();
  Serial.print("Connecting to WiFi..");
  Serial.print(ssid);

  WiFi.begin(ssid, password);

  Serial.println();
  Serial.print("Connecting");

  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(". ");
  }
  Serial.println("WiFi Connected");
  Serial.println("IP Address: ");
  Serial.print(WiFi.localIP());
  server.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  WiFiClient client = server.available(); // Listen for incoming clients

  // Connect new client
  if (client) {
    String currentLine = "";
    currentTime = millis();
    previousTime = currentTime;

    // Make sure client is still connected
    while (client.connected() && currentTime - previousTime <= timeoutTime) {
      currentTime = millis();
    
      // Check if client sent byte(s)
      if (client.available()) {
        char c = client.read(); // read byte
        payload = client.readString(); // read message sent
        Serial.println(payload); // Send message to arduino
        
        // If byte is a newline character
        if (c == '\n') {

          // End of HTTP request => send response and close connection
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
            break;
          } 
          
          // If just newline then clear currentline
          else {
            currentLine = "";
          }
        } 
        
        // If there is anything but a carriage return character
        else if (c != '\r') {
          currentLine += c; // add it to the end of currentline
        }
      }
    }
  }
  client.stop();
  Serial.println("");
}
