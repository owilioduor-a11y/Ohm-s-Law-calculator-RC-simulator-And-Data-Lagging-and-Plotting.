## Lab 1: Ohm's Law Calculator
## Goal: Write a Python program that calculates current using Ohm's Law.
##  I = V/R

## Modify the code to allow multiple calculations in a loop.
## Add exception handling for invalid inputs.
## Extend program to calculate power: P = V x I.



voltage = float (input ("Enter voltage (V) : ") )
resistance = float (input ("Enter resistance (0hms) : ") )

if resistance != 0:
   current = voltage / resistance
   print ("Current (A) :", current)
else :
    print ("Error: Resistance cannot be zero")
    



# Modified code with loop, exception handling, and power calculation

while True:
      try:
         voltage = float(input("Enter voltage (V) : "))
         resistance = float(input("Enter resistance (Ohms) : "))
         
         if resistance == 0:
               raise ValueError("Resistance cannot be zero.")
         
         current = voltage / resistance
         power = voltage * current
         
         print(f"Current (A): {current}")
         print(f"Power (W): {power}")
         
      except ValueError as e:
         print(f"Input error: {e}")
      
      cont = input("Do you want to perform another calculation? (y/n): ")
      if cont.lower() != 'y':
         break
