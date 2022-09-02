student = []
Ronald = ["8","j","bl","bh"]
Dario = ["60","j","h","br"]
Azael = ["61","sh","h","bh"]
Nathan = ["8","sh","a","bh"]
Vanessa = ["7","swe","h","o"]
Ace = ["8","sh","h","bh"]
Dayveon = ["4","swe","bl","bh"]
Sirod = ["61","sh","bl","bh"]
Pray = ["4","j","a","bh"]
Kug = ["5","j","a","bh"]
Colin = ["6","j","wh","db"]
Emmanuel = ["8","sh","bl","bh"]
Joshua = ["10","sh","h","o"]
Kofi = ["61","j","bl","bh"]
Andrew = ["10","j","a","bh"]
Roshaun = ["61","sh","bl","o"]
Ashton = ["9","j","wh","bl"]
def main():
  height=input("how tall are you? put 0-11 if you're 5'0\"-5'11\", put a 4 along with the letter if you're below 5 feet tall, or a 6 if you're above (65,43,68,etc):  ")
  print("")
  student.append(height)
  pants=input("Do you wear jeans(j), shorts(sh), or sweatpants(swe): ")
  print("")
  student.append(pants)
  race=input("Are you white(wh), hispanic(h), black(bl), asian(a), or other(o): ")
  print("")
  student.append(race)
  hair=input(" Do you have black hair(bh), blonde hair(bl), dirty blonde hair(db), brown hair(br) or other(o) :")
  print("")
  student.append(hair)
  if student == Dario:
   print("Dario Lopez Gomez")
  elif student == Ronald:
   print("Ronald Suggs III")
  elif student == Azael:
    print("Azael Gomez")
  elif student == Nathan:
    print("Nathan Andrews")
  elif student == Ace:
    print("Ace-Zeus Nieves")
  elif student == Vanessa:
    print ("Vanessa Torres")
  elif student == Dayveon:
    print ("Dayveon Anderson")
  elif student == Sirod:
    print ("Si\'rod Bethany")
  elif student == Pray:
    print ("Pray Reh")
  elif student == Kug:
    print ("Kug Kim")
  elif student == Colin:
    print ("Colin Wagner")
  elif student == Emmanuel:
    print("Emmanuel Cockrell")
  elif student == Joshua :
    print ("Joshua James")
  elif student == Kofi :
    print ("Kofi Bekoe")
  elif student == Andrew :
    print ("Andrew Chau")
  elif student == :
    print ("Roshaun Sanders")
  elif student == Ashton:
    print ("Ashton Baker")
  else:
   print("I don't see you in the system")
main()

