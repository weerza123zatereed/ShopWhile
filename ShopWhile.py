username = ""
password = ""
while username != "weer" or password != "1234":
    username = input("USERNAME : ")
    password = input("PASSWORD : ")
    if username == "weer" and password == "1234":
        print("DONE !!!")
        amount1=0
        amount2=0
        amount3=0
        while True:
            print("------------------")
            print("Banana     10THB >>>1")
            print("Apple      20THB >>>2")
            print("Chocolate  30THB >>>3")
            userSelected = input(">>>")
            if userSelected == "1":
                amount1=int(input("How many? :"))
                print("Price :",str(10*amount1)+"THB")
            elif userSelected == "2":
                amount2=int(input("How many? :"))
                print("Price :",str(20*amount2)+"THB")
            elif userSelected == "3":
                amount3=int(input("How many? :"))
                print("Price :",str(30*amount3)+"THB")
            else:
                print("กรอกเลขให้ถูกต้อง!!!!!!!!!!!")
                continue
            userLoop=str(input("หากต้องการซื้อเพิ่มกด 1 หาต้องการจบการสั่งซื้อกด 2:"))
            if userLoop == "1":
                continue
            elif userLoop == "2":
                break
            else:
                print("ทำรายการสินค้าใหม่อีกครั้ง ตรวจพบเลขผิดพลาด")
        print("--------------------")
        print("      Pay Slip      ")
        print("Banana      x",amount1,    str(10*amount1)+"THB")
        print("Apple       x",amount2,    str(20*amount2)+"THB")
        print("Chocolate   x",amount3,    str(30*amount3)+"THB")
        print("Total Price :",            str(10*amount1+20*amount2+30*amount3)+"THB")
    else:
        print("---ERROR---")