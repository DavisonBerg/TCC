/* 
   Autor: Davison Berg  Data: Outubro de 2017
   
   A UID é um identificador único do cartão, são 4bytes
*/

// --- Montagem dos pinos na Wemos D1 R2 ---
/*Pino SDA ligado na porta SS/D8
  Pino SCK ligado na porta D5
  Pino MOSI ligado na porta D7
  Pino MISO ligado na porta D6
  Pino NC/IRQ – Não conectado
  Pino GND  ligado no pino GND da Wemos
  Pino RST ligado na porta D4 
  Pino 3.3 – ligado ao pino 3.3 V da Wemos*/
// --- Bibliotecas Auxiliares ---
#include <SPI.h>
#include <MFRC522.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <stddef.h>


// --- Mapeamento de Hardware WeMos D1 R2---
#define SS_PIN D8
#define RST_PIN D4
MFRC522 readerRFID(SS_PIN, RST_PIN);   // Cria instância com MFRC522
 

// --- Variáveis Globais --- 
const char* ssid     = "GVT-D60B";
const char* password = "4003000254";
const int http_port = 80;
WiFiClient eclient;

const char* server = "http://davison.pythonanywhere.com";
const unsigned long HTTP_TIMEOUT = 10000;  // max respone time from server
const size_t MAX_CONTENT_SIZE = 300;       // max size of the HTTP response
String tagID;

 
struct UserData{
  int  userID;
  char userName[100];
  int  userCPF;
  char userTag[100];
  int  userLab;
  int  userBancada;
  char userInicio[100];
  char userFim[100];
  char userResponsavel[2];
};
// --- Configurações Iniciais ---

void setup() 
{
  
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);

  
  Serial.begin(115200);     // Inicia comunicação Serial em 115200 baud rate
  SPI.begin();             // Inicia comunicação SPI bus

  //Conectando com Wi-Fi
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  delay(500);

  readerRFID.PCD_Init();   // Inicia MFRC522
  delay(100);
  Serial.println("Aproxime o seu cartao do leitor...");
  Serial.println();

} //end setup


// --- Loop Infinito ---
void loop() 
{
  
  // Verifica novos cartões e Seleciona um dos cartões
  if ( ! readerRFID.PICC_IsNewCardPresent() || ! readerRFID.PICC_ReadCardSerial()) 
  {
    delay(50);
    return;
  }
  
  Serial.print("UID size : ");
  Serial.println(readerRFID.uid.size);
  tagID = ""; 
  for (int i = 0; i <= readerRFID.uid.size; i++) 
  {
    tagID.concat(String(readerRFID.uid.uidByte[i], HEX));
    //tagID.concat(String(1, HEX));
  }
//  int i = strlen(tagID);
//  Serial.print("tamanho da tag :",i);
  // Mostra UID na serial
  Serial.print("UID da tag :");
  Serial.println("Tag Cadastrada: "+ tagID);
  Serial.println();

  
  if(sendConnect(server)){
    //if (sendRequest(server,tagID) && skipResponseHeaders())
    if (sendRequest(server,tagID)) {
        Serial.println("Funcionou");
   }
  
  }
  
  if (tagID.equalsIgnoreCase("F5F788")) //UID 1 - Chaveiro Anderson
  {
    denied();    
  }
 
  if (tagID.equalsIgnoreCase("A0349535")) //UID 2 - Cartao Davison
  {
    released();
  }
  
  serverDisconnect();
  wait();
} //end loop

bool sendConnect(const char* hostName){
   if ( !eclient.connect(server, http_port) ) {
    Serial.println("Falha na conexao com o site ");
    return false;
  }
  return true;
  
}
void released(){
    Serial.println("Cartao identificado");
    Serial.println();
    tagID = "";
    delay(1000);
    
}

void denied(){
    Serial.println("Chaveiro identificado!");
    Serial.println();
    tagID = "";
    delay(1000);
}

bool sendRequest(const char* host,String tagID) {
  HTTPClient http;
  http.begin("http://davison.pythonanywhere.com/api/search/"+tagID+"/");
  int httpCode = http.GET();
  UserData userData;
  if(httpCode){
    String payload = http.getString();
    Serial.println(payload);
    Serial.println(payload.length());
    getJson(payload,&userData);
   
  }
  http.end();

  return true;
}

//Método POST cadastrando um novo professor
bool sendJson(){
   StaticJsonBuffer<300> jsonBuffer;
   JsonObject& root = jsonBuffer.createObject();
   root["nome"] = "Armando";
   root["cpf"] = 12345;
   root["tag"] = "0000000"; 
   char JSONmessageBuffer[300]; 
   root.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
   Serial.println(JSONmessageBuffer);
   HTTPClient http;
   http.begin("URL do webservice");
   http.addHeader("Content-Type", "application/json");
   String postMessage = String ("{'nome': 'Armando','cpf': 1233455,'tag': '189'}");
   int httpCode = http.POST(JSONmessageBuffer);
   String payload = http.getString();

   Serial.println(httpCode);
   Serial.println(payload);
   //http.writeToStream(&Serial);
   http.end();
   delay(30000);

}

//Método GET fazendo uma requisição através da RFID lida pelo sensor
bool getJson(String payload,struct UserData* userData){
   const size_t BUFFER_SIZE = JSON_OBJECT_SIZE(9) + MAX_CONTENT_SIZE;  
        // the root object has 9 elements
        // additional space for strings

  // Allocate a temporary memory pool
    DynamicJsonBuffer jsonBuffer(BUFFER_SIZE);
    int js = payload.length()+1;
    Serial.println(js);
    char json[js];
    payload.toCharArray(json,js);
    JsonObject& root = jsonBuffer.parseObject(json);
    delay(1000);
    if (!root.success()) {
    Serial.println("FALHOUUUU");
    return false;
    }
    if(js>100){
    // Here were copy the strings we're interested in
     strcpy(userData->userName, root["nome"]);
     strcpy(userData->userTag, root["tag"]);
     if (root["professor_responsavel"] != NULL){
       strcpy(userData->userResponsavel, root["professor_responsavel"]);
       Serial.print("Nome = ");
       Serial.println(userData->userName);
       Serial.print("Tag = ");
       Serial.println(userData->userTag);
       Serial.println("Usuário identificado");
       
       digitalWrite(D1, HIGH);  
       delay(2000); 
       digitalWrite(D1, LOW); 
       delay(2000); 

       
       return true;
     }
     else{
       Serial.print("Nome = ");
       Serial.println(userData->userName);
       Serial.print("Tag = ");
       Serial.println(userData->userTag);
       Serial.println("Usuário sem permissão");

       digitalWrite(D2, HIGH);  
       delay(2000); 
       digitalWrite(D2, LOW); 
       delay(2000); 
       
       return false;
     }
    }
    else{
      Serial.println("Usuário não identificado");
      
      digitalWrite(D3, HIGH);  
      delay(2000); 
      digitalWrite(D3, LOW); 
      delay(2000);
      tagID = "";
      return false;
    }
 }


// Print the data extracted from the JSON
void printUserData(const struct UserData* userData) {
  Serial.print("Nome = ");
  Serial.println(userData->userName);
  Serial.print("Tag = ");
  Serial.println(userData->userTag);
}

void serverDisconnect(){
  Serial.println("Disconnect ");
  eclient.stop();
}

void wait(){
  Serial.println("Wait a moment...");
  delay(1000);
  Serial.println("Aproxime o seu cartao do leitor...");
  Serial.println();
  return;
}
