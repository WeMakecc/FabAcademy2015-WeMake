int valvola = 13; // pin digitale dove collego valvola
int pompa = 3; // posiziona pin pwn su arduino _ pin1 su fabkit
//int Pot = A0; // connesso su analogico pin 0
//int ValPot = 0; //inizializa la lettrua a zero

int MQ7 = A1; // su analog non ho bisognpo di specificare se ooutput o input
int gas = 0; //inizializa la lettrua a zero
int valgas = 0; //inizializa la lettrua a zero
int ambient = 0;

int ledR = 12; // pin digitale dove ci saràil R del LED
int ledR1 = 11;
int ledR2 = 10;

int ledB = 9;
int ledB1 = 8;
int ledB2 = 7;

int ledG = 6;
int ledG1 = 5;
int ledG2 = 4;



void setup () {
  
  Serial.begin (9600);
  
  pinMode (valvola, OUTPUT);
  pinMode (pompa, OUTPUT);
  
  pinMode (ledR, OUTPUT);
  pinMode (ledR1, OUTPUT);
  pinMode (ledR2, OUTPUT);
  
  pinMode (ledG, OUTPUT);
  pinMode (ledG1, OUTPUT);
  pinMode (ledG2, OUTPUT);
  
  pinMode (ledB, OUTPUT);
  pinMode (ledB1, OUTPUT);
  pinMode (ledB2, OUTPUT);
  
  
  //digitalWrite (valvola, LOW);
  digitalWrite (valvola, HIGH);
  analogWrite (pompa, 0);
  //ValPot = analogRead (Pot);
  
}
  
void loop () {

  // We read the gas data, and behave accordingly
  gas = leggigas();

  if (gas < 500)
    {
      // do Thing A
    }
   else if (gas >= 1000)
    {
      // do Thing B
    }
   else
    {
      // do Thing C
    }
  
  //ValPot = analogRead (Pot);
  pompaon (); // fa partire il void della scheda Pompa
  digitalWrite (valvola, HIGH); // apre la vlvola
  ledRon () ; 
  digitalWrite (valvola, LOW); // apre la vlvola
  delay (8000); // questo valore è quello che serve al muscolo per gonfiarsi che trovo empiricamente
  ledRoff;
  pompaoff (); //digitalWrite (valvola, LOW);
  ledGon ();
  delay (10000);
  ledGoff ();
  digitalWrite (valvola, HIGH);
  ledBon ();
  delay (10000); 
  ledBoff ();


ledBon();
delay (5000);
ledBoff ();
ledRon();
delay (5000);                                                 
ledRoff ();
ledGon();
delay (5000);
ledGoff ();


/*
leggigas ();
gasreport (); 
*/


}
  
  
