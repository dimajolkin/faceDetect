from arduino import Arduino

class Eye:
    def __int__(self):
        self.arduino = Arduino()
    def look(self, x, y):
        self.arduino.push(x + " " + y + " +")