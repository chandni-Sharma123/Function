def sp(speed):
    if speed<=70:
        print("ok")
    else:
         speed2=(speed-70)//5
         if speed2<=12:
             print(f"point:{speed2}")
         else:
             print("license suspend")
enter=sp(int(input("enter speed:")))







