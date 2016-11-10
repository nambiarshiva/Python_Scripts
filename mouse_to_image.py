import struct
import Image
import dpkt
INIT_X, INIT_Y = 0, 0

def print_data(pcap,device):
	picture = Image.new("RGB",(2000, 2000),"white")
	pixels = picture.load()

	x, y = INIT_X, INIT_Y
	for ts,buf in pcap:
		
		device_id = struct.unpack("b", buf[0x13])
		
		if  device_id[0] != device:
			continue

		data = struct.unpack("bbbb", buf[-4:])
		

		status = data[0]
		x = max(x + data[1], 5)
		y = max(y + data[2], 5)

		if (status == 1):
			for i in range(-5, 5):
				for j in range(-5, 5):
					pixels[x + i , y + j] = (0, 0, 0, 0)
		
		else:
			print "x,y" , x, y
			pixels[x, y] = (255, 0, 0, 0)
	picture.save("usbimage.png", "PNG")

if __name__== "__main__":
	f = open("capture.s0i0.pcap", 'rb')
	pcap = dpkt.pcap.Reader(f)
	
	print_data(pcap,3)
	f.close
