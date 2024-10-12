// Test file - Seeing if wifi connection works with python sending post requests

#include<ESP8266WiFi.h>

const char* ssid="SSID";
const char* password="PASSWORD";

WiFiServer server(80);

String header;
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

  if (client) {
    Serial.println("New Client");
    String currentLine = "";
    currentTime = millis();
    previousTime = currentTime;
    while (client.connected() && currentTime - previousTime <= timeoutTime) {
      currentTime = millis();
      if (client.available()) {
        char c = client.read();
        payload = client.readString();
        Serial.println(payload);
        header += c;
        if (c == '\n') {
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type: text/html");
            client.println("Connection: close");
            client.println();
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }
  }
  header = "";
  client.stop();
  Serial.println("Client Disconnected");
  Serial.println("");
  delay(1000);
}
