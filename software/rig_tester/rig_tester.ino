/*code to test the Throclis controller:
- turn on all leds for 1 second
- turn each led in turn for 500 ms 2X
- Turn on the trigger out for 1 second
- turn on trigger out for 400us and off for 1.6ms 100X


Code by AM Chagas 06/12/2021
CC BY SA 4.0

*/

// LEDS
int p1l1 = 19;
int p1l2 = 21;
int p1l3 = 14;
int p1l4 = 27;
int p1l5 = 26;
int p1l6 = 25;

int p2l1 = 15;
int p2l2 = 2;
int p2l3 = 16;
int p2l4 = 17;
int p2l5 = 22;
int p2l6 = 23;

int allLeds[] = {p1l1,p1l2,p1l3,p1l4,p1l5,p1l6,p2l1,p2l2,p2l3,p2l4,p2l5,p2l6};

//TRIGGER OUT
int trigOut = 18;

//BLANK in
// right now blank goes directly to ICs outside microcontroller.

void setup() {
  // put your setup code here, to run once:
  pinMode(p1l1,OUTPUT);
  pinMode(p1l2,OUTPUT);
  pinMode(p1l3,OUTPUT);
  pinMode(p1l4,OUTPUT);
  pinMode(p1l5,OUTPUT);
  pinMode(p1l6,OUTPUT);

  pinMode(p2l1,OUTPUT);
  pinMode(p2l2,OUTPUT);
  pinMode(p2l3,OUTPUT);
  pinMode(p2l4,OUTPUT);
  pinMode(p2l5,OUTPUT);
  pinMode(p2l6,OUTPUT);

  pinMode(trigOut,OUTPUT);

  digitalWrite(p1l1, LOW);
  digitalWrite(p1l2, LOW);
  digitalWrite(p1l3, LOW);
  digitalWrite(p1l4, LOW);
  digitalWrite(p1l5, LOW);
  digitalWrite(p1l6, LOW);

  digitalWrite(p2l1, LOW);
  digitalWrite(p2l2, LOW);
  digitalWrite(p2l3, LOW);
  digitalWrite(p2l4, LOW);
  digitalWrite(p2l5, LOW);
  digitalWrite(p2l6, LOW);
  
  digitalWrite(trigOut, LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("all leds on");
  for (int i=0; i<=11;i=i+1){
      digitalWrite(allLeds[i],HIGH);

  }//end for
  delay(1000);

  Serial.println("all leds OFF");
  for (int i=0; i<=11;i=i+1){
      digitalWrite(allLeds[i],LOW);

  }//end for

  delay(1000);
  Serial.println("leds turning on in turn");
  for (int i=0; i<=11;i=i+1){
      digitalWrite(allLeds[i],HIGH);
      Serial.print("LED on = ");
      Serial.println(i);
      delay(500);
      digitalWrite(allLeds[i],LOW);
      Serial.print("LED off = ");
      Serial.println(i);
  }//end for
  
  delay(1000);
  
  
  Serial.println("trigger out on");
  digitalWrite(trigOut, HIGH);
  delay(1000);
  Serial.println("trigger out off");
  digitalWrite(trigOut, LOW);
  
  delay(1000);
  
  for (int j=0; j<=200;j=j+1){
    for (int i=0; i<=11;i=i+1){
        digitalWrite(trigOut,HIGH);
        delayMicroseconds(400);
        digitalWrite(trigOut,LOW);
        delayMicroseconds(1600);
    }//end for i
    Serial.print("blank loop: ");
    Serial.println(j);
  }//end for j
  
  delay(1000);
}
