
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

x = []
y3 = []
y8 = []
x1 = []
y1 = []
y1.append(1.1)
y1.append(0.85)
y1.append(0.5)
y1.append(0.2)
y1.append(0.15)
y1.append(0.1)
x1.append(0.1)
x1.append(0.2)
x1.append(0.4)
x1.append(1)
x1.append(1.05)
x1.append(1.3)


x.append(10)
x.append(20)
x.append(30)
x.append(40)
x.append(50)
y3.append(1.13)
y3.append(1)
y3.append(0.98)
y3.append(0.87)
y3.append(0.85)
y8.append(0.98)
y8.append(0.88)
y8.append(0.83)
y8.append(0.8)
y8.append(0.78)
plt.xlabel('mg/L')
plt.ylabel('Rs/Ro')
plt.ylim((0.1,1.1))
plt.xlim((0.1,1.3))
dashes = [10, 5, 10, 5]
#plt.loglog(x1, y1, basex=10)
line1, = plt.loglog(x1, y1, basex=10, color = "red", label = 'Alcohol', linewidth = 2.5)
#line2, = plt.loglog(x, y8, color = "red", label = '85%''RH', linewidth = 2.5)
line1.set_dashes(dashes)
#line2.set_dashes(dashes)
plt.legend(handler_map={line1: HandlerLine2D(numpoints=16)}, frameon = False)
#plt.legend(handler_map={line2: HandlerLine2D(numpoints=16)}, frameon = False)
plt.grid(True, which="both", ls="-")
plt.show()

#Senstvity, Thresh
#0.1-10mg/l
