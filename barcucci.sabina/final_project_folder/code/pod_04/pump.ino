void pompaon () {
  //ValPot = analogRead (Pot);
  //Serial.print (ValPot);
  analogWrite (pompa, 255); // per linearizzare il valore analogico del potenziometro sul range del pvm 
  delay (2);
}
  
void pompaoff () {
  analogWrite (pompa, 0);
  delay (100);
}
