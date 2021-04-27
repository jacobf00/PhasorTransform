import sys

sys.path.append(r'C:\Users\Jacob\Documents\Projects\PhasorTransform')




values = input("[1, 2, p (polar) or r (rectangular)]")

vals = values[0:2]

if values[2] == 'p':
    isrect = False
else:
    isrect = True


phasor1 = phasor(vals,isrect)
