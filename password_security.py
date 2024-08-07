import random as rd
print("Welcome to the Password Security Checker!")
print()
x = input("Enter a password: ")
print()
ucl = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"
lcl = ucl.lower()
special_chars = ''',!.:;?-""(){}[]%@#$%^*_+=<>'''
UC = LC = Digits = specs = 0

for char in x:
  if char.isupper():
    UC = UC + 1
  elif char.islower():
    LC = LC + 1
  elif char.isdigit():
    Digits = Digits + 1
  elif char in special_chars:
    specs = specs + 1

total_chars = (UC + LC + Digits + specs)

print("Number of Uppercase characters:", UC)
print("Number of Lowercase characters:", LC)
print("Number of digits:", Digits)

print("Number of Special Characters:", specs)
print("Length of Password:", total_chars)
print()

if specs >= 2 and Digits >= 3 and UC >= 1 and LC >= 1 and total_chars >= 8:
  print("Password is secure.")

else:
  print("PASSWORD IS NOT SECURE.")
  print()
  print("Password must contain:")
  print()
  print("A total of at least 8 - 26 characters")
  print("At least 2 special characters")
  print("At least 3 numbers, and")
  print("At least 1 Uppercase and 1 Lowercase letter")
  print()

  opt = input("Press any key to generate a new password.\nType \"Stop\" to exit: ")
  if opt.upper() == "STOP":
    print("Thank you for using the PassCal 3900. Stay safe!")
  else:
    ch = int(input("Choose the length for your password (Password should be between 8 - 20 characters): "))
    if ch < 8:
      print("Password must be atleast 8 characters long.")

    elif ch == 8:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      new_psw = ucl1 + lcl2 + lcl1 + spec1 + n1 + n2 + n3 + spec2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 9:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl) 
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      new_psw = ucl1 + lcl2 + lcl1 + ucl2 + spec1 + n1 + n2 + n3 + spec2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 10:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl) 
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      new_psw = ucl1 + lcl2 + lcl1 + ucl2 + lcl3 + spec1 + n1 + n2 + n3 + spec2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 11:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars) 
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      new_psw = lcl3 + spec3 + ucl1 + lcl2 + lcl1 + ucl2 + spec1 + n1 + n2 + n3 + spec2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 12:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      ucl3 = rd.choice(ucl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      new_psw = ucl3 + spec3 + ucl1 + lcl2 + lcl1 + ucl2 + spec1 + n1 + lcl3 + n3 + spec2 + n2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 13:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      ucl3 = rd.choice(ucl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      n4 = str(rd.randint(0, 9))
      new_psw = ucl3 + spec3 + n4 + ucl1 + lcl2 + lcl1 + ucl2 + spec1 + n1 + lcl3 + n3 + spec2 + n2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 14:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      lcl0 = rd.choice(lcl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      lcl4 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      n4 = str(rd.randint(0, 9))
      new_psw = spec3 + n4 + ucl1 + lcl2 + lcl4 + lcl1 + ucl2 + spec1 + n1 + lcl3 + n3 + lcl0 + spec2 + n2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 16:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars)
      spec4 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      ucl3 = rd.choice(ucl)
      lcl0 = rd.choice(lcl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      lcl4 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      n4 = str(rd.randint(0, 9))
      new_psw = spec3 + n4 + ucl1 + lcl2 + spec4 + ucl3 + lcl4 + lcl1 + ucl2 + spec1 + n1 + spec4 + lcl3 + n3 + spec2 + n2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 17:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars)
      spec4 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      ucl3 = rd.choice(ucl)
      lcl0 = rd.choice(lcl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      lcl4 = rd.choice(lcl)
      lcl5 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      n4 = str(rd.randint(0, 9))
      new_psw = spec3 + n4 + ucl1 + lcl2 + spec4 + ucl3 + lcl4 + lcl1 + ucl2 + lcl5 + spec1 + n1 + spec4 + lcl3 + n3 + spec2 + n2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 18:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars)
      spec4 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      ucl3 = rd.choice(ucl)
      lcl0 = rd.choice(lcl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      lcl4 = rd.choice(lcl)
      lcl5 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      n4 = str(rd.randint(0, 9))
      n5 = str(rd.randint(0, 9))
      new_psw = spec3 + n5 + ucl3 + lcl4 + lcl1 + ucl2 + n4 + ucl1 + lcl2 + spec4 + lcl5 + spec1 + n1 + spec4 + lcl3 + n3 + spec2 + n2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 19:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars)
      spec4 = rd.choice(special_chars)
      spec5 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      ucl3 = rd.choice(ucl)
      lcl0 = rd.choice(lcl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      lcl4 = rd.choice(lcl)
      lcl5 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      n4 = str(rd.randint(0, 9))
      n5 = str(rd.randint(0, 9))
      new_psw = n4 + ucl1 + spec3 + lcl2 + spec3 + lcl2 + spec4 + n5 + ucl3 + lcl4 + lcl1 + ucl2 + spec5 + lcl5 + spec4 + spec1 + n1 +lcl3 + n3 + spec2 + n2
      print(f"Newer, secure password: {new_psw}")

    elif ch == 20:
      spec1 = rd.choice(special_chars)
      spec2 = rd.choice(special_chars)
      spec3 = rd.choice(special_chars)
      spec4 = rd.choice(special_chars)
      spec5 = rd.choice(special_chars)
      ucl1 = rd.choice(ucl)
      ucl2 = rd.choice(ucl)
      ucl3 = rd.choice(ucl)
      ucl4 = rd.choice(ucl)
      lcl0 = rd.choice(lcl)
      lcl1 = rd.choice(lcl)
      lcl2 = rd.choice(lcl)
      lcl3 = rd.choice(lcl)
      lcl4 = rd.choice(lcl)
      lcl5 = rd.choice(lcl)
      n1 = str(rd.randint(0, 9))
      n2 = str(rd.randint(0, 9))
      n3 = str(rd.randint(0, 9))
      n4 = str(rd.randint(0, 9))
      n5 = str(rd.randint(0, 9))
      new_psw = spec3 + n4 + ucl1 + lcl2 + spec4 +  ucl4 + n5 + ucl3 + lcl4 + lcl1 + lcl5 + ucl2 + spec5 + spec1 + n1 + spec4 + lcl3 + n3 + spec2 + n2
      print(f"Newer, secure password: {new_psw}")

    else:
      print("Password too long.")
