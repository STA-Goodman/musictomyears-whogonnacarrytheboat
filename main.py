import winsound
import time

# "Row, Row, Row Your Boat" as played by WinSound.
# However, WinSound queues and plays beeps VERY slowly, so it frequently skips notes.
# I (Thomas Kahler) have tried to find solutions to notes skipping but the Internet has no solution.
# Therefore, this is basically the best we have.

for i in range(4):
    winsound.Beep(523, 800) #Row
    winsound.Beep(523, 800) #Row
    winsound.Beep(523, 800) #Row
    winsound.Beep(587, 300) #Your
    winsound.Beep(657, 500) #Boat
    time.sleep(0.5) # (short pause)

    winsound.Beep(659, 800) #Gent-
    winsound.Beep(587, 300) #-ly
    winsound.Beep(659, 800) #Down
    winsound.Beep(698, 300) #the
    winsound.Beep(783, 1600) #Stream
    time.sleep(1) # (pause)

    winsound.Beep(1046, 300) #Merr-
    winsound.Beep(1046, 300) #il-
    winsound.Beep(1046, 300) #ly

    winsound.Beep(783, 300) #Merr-
    winsound.Beep(783, 300) #il-
    winsound.Beep(783, 300) #ly-

    winsound.Beep(659, 300) #Merr-
    winsound.Beep(659, 300) #il-
    winsound.Beep(659, 300) #ly-

    winsound.Beep(523, 300) #Merr-
    winsound.Beep(523, 300) #il-
    winsound.Beep(523, 300) #ly-
        
    winsound.Beep(783, 500) #Life
    winsound.Beep(698, 300) #is
    winsound.Beep(659, 500) #but
    winsound.Beep(587, 300) #a
    winsound.Beep(523, 1600) #Dream
    time.sleep(1.5) # (shortly longer pause)