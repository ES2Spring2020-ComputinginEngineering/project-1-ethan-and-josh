# Project 1 --- ES2
# Microbit Logger

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Ethan Donnelly/Joshua Balbi
# NUMBER OF HOURS TO COMPLETE: 2.5
# YOUR COLLABORATION STATEMENT(s): Ethan Donnelly and Joshua Balbi.
#
#
#*****************************************

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=71, length=100)

#We ran into trouble with the reciever so we decided to try a channel that would likely have no one else on it.

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again



while not mb.button_a.is_pressed():

#This while loop sends acceleration data to the reciever microbit every 5 milliseconds and the data is sent as a string.

    mb.sleep(5)
    time1 = mb.running_time() #get the current running time
    elapsed_time = (time1 / 1000) #total time passed
    x = mb.accelerometer.get_x()
    y = mb.accelerometer.get_y()
    z = mb.accelerometer.get_z()
    message = (str(x) + "," + str(y) + "," +  str(z) + "," +  str(elapsed_time))
    
    radio.send(message)
    mb.sleep(5)

mb.display.show(mb.Image.SQUARE)  # Display Square when program ends
