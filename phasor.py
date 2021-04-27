import math

class phasor:

    def __init__(self,vals,issrect):
        self.vals = vals
        self.issrect = issrect


    def rect(self):
        rectf = self.vals
        if self.issrect == False:
            rectf = [self.vals[0] * math.cos(self.vals[1]), self.vals[0]*math.sin(self.vals[1])]
            self.vals = rectf
        self.issrect = True   
        return rectf

    def polar(self):
        polar = self.vals
        if self.issrect:
            if self.vals[0] > 0:
                polar = [math.sqrt(self.vals[0]**2 + self.vals[1]**2),math.atan(self.vals[1]/self.vals[0])]
            else:
                polar = [math.sqrt(self.vals[0]**2 + self.vals[1]**2), 180+math.atan(self.vals[1]/self.vals[0])]
        
            self.vals = polar
        self.issrect = False
        
        return polar

    def isrect(self):
        return self.issrect


            

#values = input("[1, 2, p (polar) or r (rectangular)]")
values = [72,12,'r']
vals = values[0:2]

if values[2] == 'p':
    isrect = False
else:
    isrect = True


phasor1 = phasor(vals,isrect)

print(phasor1.polar)
