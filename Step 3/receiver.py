# Project 1 --- ES2
# Microbit Reciever

# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Ethan Donnelly/Joshua Balbi
# NUMBER OF HOURS TO COMPLETE: 1
# YOUR COLLABORATION STATEMENT(s): Ethan Donnelly and Joshua Balbi.
#
#
#*****************************************


import microbit as mb

import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=71, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()



while True:
   
#This while statement shows a heart while the code is running and data is being recieved from the logger.
    incoming = radio.receive()  # Read from radio

    if incoming is not None:  # message was received
#       print("receiving info")
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        x = eval(incoming)
        print(x)
    mb.sleep(10)
