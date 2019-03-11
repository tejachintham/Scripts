from skpy import Skype
import time
sk = Skype("usename", "password")
ch = sk.contacts["profile of friend"].chat
check=ch.getMsgs()
val=check[0]
for i in range(3600):
    sk = Skype("usename", "password")
    ch = sk.contacts["profile of friend"].chat
    check=ch.getMsgs()   
    if(str(val)!=str(check[0])):
        import playsound
        while(1):            
            playsound.playsound('alarm.wav', True)
    val=check[0]    
    time.sleep(15)    
