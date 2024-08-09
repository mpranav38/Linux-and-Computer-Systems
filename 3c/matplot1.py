#! /usr/bin/env python
import matplotlib.animation as animation
import matplotlib.pyplot as plt

bg = plt.figure()

def draw(i):
    cox = []
    coy = []

    txtdata = open('network-test-latency.txt', 'r').read()
    listdata = txtdata.split('\n')

    plt.xlabel('DNS Names')
    plt.ylabel('RTT')
    plt.title('Graph of DNS names vs RTT')

    for line in listdata:
        if len(line) > 1:
            xco, yco = line.split(' ')
            cox.append(xco)
            coy.append(float(yco))

    plt.plot(cox, coy)

xyz = animation.FuncAnimation(bg, draw, interval=2000)

plt.show()

