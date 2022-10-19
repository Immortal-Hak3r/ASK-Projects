num = int(input("Masukan satu nombor: "))
if num == 0:
  exit ()
else:
  if num > 0:
    print ("Nombor", num, "ialah nombor positif.")
    
    if (num % 2) == 0:
      print ("Nombor", num, "ialah nombor genap.")
    else:
      print ("Nombor", num, "ialah nombor ganjil.")
      
else:
  print ("Nombor", num, "ialah nombor negatif.")
  exit
  
