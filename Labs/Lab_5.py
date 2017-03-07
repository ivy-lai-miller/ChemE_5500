import matplotlib.pyplot as plt
import math

raw = open("sin.data", "r").read()

raw = raw.strip()
rows = raw.split("\n")


angle, sine = [],[]

for line in rows:
    angle_temp,sine_temp = line.split()
    angle.append(float(angle_temp))
    sine.append(float(sine_temp))
pi = math.pi

plt.yticks([-1,0,1])
plt.xticks([0,pi/2., pi, 3* pi/2., 2*pi],
            ["$0$", "$\\pi/2$", "$\\pi$", "$\\frac{3\\pi}{2}$", "$2\\pi$"], fontsize=10)
plt.grid(True)
plt.title("Sine Function")
plt.xlabel("$\\theta (rad)$")

plt.ylabel("$sin(\\theta)$")

# cosine = []
# for value in sine:
#     cosine.append((value+pi/2))
#
# fptr = open("Combined.data", "w")


plt.plot(angle, sine, "r-")
fig = plt.gcf()
plt.show()

fig.savefig("sine.png")
