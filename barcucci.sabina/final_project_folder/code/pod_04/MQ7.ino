int leggigas () {
  gas = analogRead (MQ7);
  Serial.println (gas);
  return gas;
}