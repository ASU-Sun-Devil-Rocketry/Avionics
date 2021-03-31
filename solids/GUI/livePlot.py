import random
from itertools import count
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d

plt.style.use("fivethirtyeight")
x_values = []
y_values = []
#z_values = []
#q_values = []
counter = 0
index = count()


def animate(i):
    # print(counter)

    x = next(index)  # counter or x variable -> index
    counter = next(index)
    print(counter)
    x_values.append(x)


    y = 3*random.random()
    #z = 4*random.random()+3
    #q = 3*random.random()+7
    # append values to keep graph dynamic
    # this can be replaced with reading values from a csv files also
    # or reading values from a pandas dataframe
    y_values.append(y)
    #z_values.append(z)
    #q_values.append(q)

    if counter > 100:

        x_values.pop(0)
        y_values.pop(0)
        #z_values.pop(0)
        #q_values.pop(0)
        # counter = 0
        plt.cla()  # clears the values of the graph

    plt.plot(x_values, y_values, linestyle='-')
    #plt.plot(x_values, z_values, linestyle='-')
    #plt.plot(x_values, q_values, linestyle='-')



    #time.sleep(.25)  # keep refresh rate of 0.25 seconds

fig, ax = plt.subplots()
ax.legend(["Value 1 ", "Value 2", "Value 3"])
ax.set_xlabel("X values")
ax.set_ylabel("Vals")
plt.title('Dynamic line graphs')

ani = FuncAnimation(plt.gcf(), animate)
plt.tight_layout()
plt.show()


'''import time
from matplotlib import pyplot as plt
import numpy as np


def live_update_demo(blit = False):
    x = np.linspace(0,50., num=100)
    fig = plt.figure()
    ax2 = fig.add_subplot(2, 1, 2)



    line, = ax2.plot([], lw=3)
    text = ax2.text(0.8,0.5, "")

    ax2.set_xlim(x.min(), x.max())
    ax2.set_ylim([-1.1, 1.1])

    fig.canvas.draw()   # note that the first draw comes before setting data


    if blit:
        # cache the background
        ax2background = fig.canvas.copy_from_bbox(ax2.bbox)

    plt.show(block=False)


    t_start = time.time()
    k=0.

    i = 0.

    while True:
        line.set_data(x, np.sin(x/3.+k))
        try:
            tx = 'Mean Frame Rate:\n {fps:.3f}FPS'.format(fps= ((i+1) / (time.time() - t_start)) )
            text.set_text(tx)
            #ax2.set_xlim(i-50, i)
        except:
            print('ERROR')
        #print tx
        k+=0.11
        if blit:
            # restore background
            fig.canvas.restore_region(ax2background)

            # redraw just the points
            ax2.draw_artist(line)
            ax2.draw_artist(text)

            # fill in the axes rectangle
            fig.canvas.blit(ax2.bbox)

            # in this post http://bastibe.de/2013-05-30-speeding-up-matplotlib.html
            # it is mentionned that blit causes strong memory leakage.
            # however, I did not observe that.

        else:
            # redraw everything
            fig.canvas.draw()

        fig.canvas.flush_events()
        #alternatively you could use
        #plt.pause(0.000000000001)
        # however plt.pause calls canvas.draw(), as can be read here:
        #http://bastibe.de/2013-05-30-speeding-up-matplotlib.html
        i+=1


live_update_demo(True)   # 175 fps
#live_update_demo(False) # 28 fps'''