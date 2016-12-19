import bluetooth
import lazylights
import binascii
from colour import Color

#------------------------------------------------------------------------------------------------------------
# I use this to manually create a bulb using IP and MAC address.
def createBulb(ip, macString, port = 56700):
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
#------------------------------------------------------------------------------------------------------------

myBulb1 = createBulb('10.0.0.X','XX:XX:XX:XX:XX:XX')  #Bulb for right side of screen
#lazylights requires a 'set' of bulbs as input so I put each one in its own set
bulbs1=[myBulb1]
while True:
	target_name = "Pixel XL"
	target_address = None
	nearby_devices = bluetooth.discover_devices()

	for bdaddr in nearby_devices:
		if target_name == bluetooth.lookup_name( bdaddr ):
			target_address = bdaddr
			break

	if target_address is not None:
		c = Color("green")
		print "***True"
		lazylights.set_state(bulbs1,c.hue*360,(c.saturation),c.luminance,3500,(500),False)
	else:
		c = Color("yellow")
		print "***False"
		lazylights.set_state(bulbs1,c.hue*360,(c.saturation),c.luminance,3500,(500),False)