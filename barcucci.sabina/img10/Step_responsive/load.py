#
# hello.load.45.py
#
# receive and display loading step response
# hello.step.45.py serial_port
#
# Neil Gershenfeld
# CBA MIT 10/29/10
#
# (c) Massachusetts Institute of Technology 2010
# Permission granted for experimental and personal use;
# license for commercial sale available from MIT
#

from Tkinter import *
import serial

WINDOW = 600 # window size
eps = 0.5 # filter time constant
filter1 = 0.0 # filtered value
filter2 = 0.0 # filtered value
filter3 = 0.0 # filtered value

def idle(parent,canvas):
   global filter1, filter2, filter3, eps
   #
   # idle routine
   #
   byte2 = 0
   byte3 = 0
   byte4 = 0
   ser.flush()
   #
   # find framing 
   #
   while 1:
      byte1 = byte2
      byte2 = byte3
      byte3 = byte4
      byte4 = ord(ser.read())
      if ((byte1 == 1) & (byte2 == 2) & (byte3 == 3) & (byte4 == 4)):
         break
   #
   # read and plot
   #
   up_low1 = ord(ser.read())
   up_high1 = ord(ser.read())
   down_low1 = ord(ser.read())
   down_high1 = ord(ser.read())
   up_low2 = ord(ser.read())
   up_high2 = ord(ser.read())
   down_low2 = ord(ser.read())
   down_high2 = ord(ser.read())
   up_low3 = ord(ser.read())
   up_high3 = ord(ser.read())
   down_low3 = ord(ser.read())
   down_high3 = ord(ser.read())
   up_value1 = 256*up_high1 + up_low1
   down_value1 = 256*down_high1 + down_low1
   up_value2 = 256*up_high2 + up_low2
   down_value2 = 256*down_high2 + down_low2
   up_value3 = 256*up_high3 + up_low3
   down_value3 = 256*down_high3 + down_low3
   value1 = (up_value1 + (1023 - down_value1))/2.0
   value2 = (up_value2 + (1023 - down_value2))/2.0
   value3 = (up_value3 + (1023 - down_value3))/2.0
   filter1 = (1-eps)*filter1 + eps*value1
   filter2 = (1-eps)*filter2 + eps*value2
   filter3 = (1-eps)*filter3 + eps*value3
   x1 = int(.2*WINDOW + (.9-.2)*WINDOW*filter1/1023.0)
   x2 = int(.2*WINDOW + (.9-.2)*WINDOW*filter2/1023.0)
   x3 = int(.2*WINDOW + (.9-.2)*WINDOW*filter3/1023.0)
   canvas.itemconfigure("text1",text="%.1f"%filter1)
   canvas.itemconfigure("text2",text="%.1f"%filter2)
   canvas.itemconfigure("text3",text="%.1f"%filter3)
   canvas.coords('rect11',.2*WINDOW,.05*WINDOW,x1,.2*WINDOW)
   canvas.coords('rect12',x1,.05*WINDOW,.9*WINDOW,.2*WINDOW)
   canvas.coords('rect21',.2*WINDOW,.3*WINDOW,x2,.45*WINDOW)
   canvas.coords('rect22',x2,.3*WINDOW,.9*WINDOW,.45*WINDOW)
   canvas.coords('rect31',.2*WINDOW,.55*WINDOW,x3,.7*WINDOW)
   canvas.coords('rect32',x3,.55*WINDOW,.9*WINDOW,.7*WINDOW)
   canvas.update()
   parent.after_idle(idle,parent,canvas)

#
#  check command line arguments
#
if (len(sys.argv) != 2):
   print "command line: hello.load.45.py serial_port"
   sys.exit()
port = sys.argv[1]
#
# open serial port
#
ser = serial.Serial(port,9600)
ser.setDTR()
#
# set up GUI
#
root = Tk()
root.title('hello.load.45.py (q to exit)')
root.bind('q','exit')
canvas = Canvas(root, width=WINDOW, height=.75*WINDOW, background='white')
#
canvas.create_text(.1*WINDOW,.125*WINDOW,text="1",font=("Helvetica", 24),tags="text1",fill="#0000b0")
canvas.create_rectangle(.2*WINDOW,.05*WINDOW,.3*WINDOW,.2*WINDOW, tags='rect11', fill='#b00000')
canvas.create_rectangle(.3*WINDOW,.05*WINDOW,.9*WINDOW,.2*WINDOW, tags='rect12', fill='#0000b0')
#
canvas.create_text(.1*WINDOW,.375*WINDOW,text="2",font=("Helvetica", 24),tags="text2",fill="#0000b0")
canvas.create_rectangle(.2*WINDOW,.3*WINDOW,.3*WINDOW,.45*WINDOW, tags='rect21', fill='#b00000')
canvas.create_rectangle(.3*WINDOW,.3*WINDOW,.9*WINDOW,.45*WINDOW, tags='rect22', fill='#0000b0')
#
canvas.create_text(.1*WINDOW,.625*WINDOW,text="3",font=("Helvetica", 24),tags="text3",fill="#0000b0")
canvas.create_rectangle(.2*WINDOW,.55*WINDOW,.3*WINDOW,.7*WINDOW, tags='rect31', fill='#b00000')
canvas.create_rectangle(.3*WINDOW,.55*WINDOW,.9*WINDOW,.7*WINDOW, tags='rect32', fill='#0000b0')
canvas.pack()
#
# start idle loop
#
root.after(100,idle,root,canvas)
root.mainloop()
