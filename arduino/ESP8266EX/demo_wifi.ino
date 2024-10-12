#include <ESP8266WiFi.h>
#include <WiFiUDP.h>

// Replace these with your network credentials
const char* ssid = "SSID";
const char* password = "PASSWORD";

// UDP settings
unsigned int localUdpPort = 4210;  // Local port to listen on
char incomingPacket[255];  // Buffer for incoming packets
WiFiUDP udp;

void setup() {
  Serial.begin(9600);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  
  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  // Start listening for UDP packets
  udp.begin(localUdpPort);
  Serial.printf("UDP listening on IP: %s, Port: %d\n", WiFi.localIP().toString().c_str(), localUdpPort);
}

void loop() {
  int packetSize = udp.parsePacket();
  if (packetSize) {
    // Read the packet into the buffer
    int len = udp.read(incomingPacket, 255);
    if (len > 0) {
      incomingPacket[len] = 0;  // Null-terminate the string
    }
    
    Serial.printf("Received UDP packet from %s, port %d\n", udp.remoteIP().toString().c_str(), udp.remotePort());
    Serial.printf("Packet contents: %s\n", incomingPacket);
  }
}
