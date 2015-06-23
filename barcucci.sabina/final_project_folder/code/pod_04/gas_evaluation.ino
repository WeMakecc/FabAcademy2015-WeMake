void gasreport () {
  
  if (valgas <= 200)
  {
    ambient = 0;
  }
  
  else if (valgas > 200 && valgas < 250) 
  {
    ambient = 10;
  }
  
  else if (valgas > 250)
  {
    ambient = 20;
  }
}
  
    
  
  
