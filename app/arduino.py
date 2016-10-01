# coding: utf-8
import serial

class Arduino:
   serial = None
   found = False

   def connect(self):
       self.found = False
       for i in range(64):
           try:
               port = "/dev/ttyUSB%d" % i
               self.serial = serial.Serial(port)
               self.found = True
               print "Найден последовательный порт: ", port
           except serial.serialutil.SerialException:
               pass

       if not self.found:
           print "Последовательных портов не обнаружено"

   def get_serial(self):
       return  self.serial

   def is_connect(self):
       return self.found

   def close(self):
       self.serial.close()

   def push(self, message):
       self.serial.write(message)





