from matplotlib import pyplot as plt

x_min = -2
x_max = 1
x_step = 0.005

y_min = -1
y_max = 1
y_step = 0.005

apple_man = []

max_iter = 100
threshold = 2


def mandelbrot(c):
    z = 0
    for n in range(max_iter):
        z = z**2 + c
        if abs(z) >= threshold:
            return n                # divergent
    return max_iter                 # convergent


def color(i):
    return i / max_iter
    # return abs((i / max_iter) - 1)    # invert color map


yn = 0
y = y_min
while y <= y_max:
    x = x_min
    apple_man.append([])
    while x <= x_max:
        complex_number = x + y*1j
        iterations = mandelbrot(complex_number)
        apple_man[yn].append(color(iterations))
        x += x_step
    y += y_step
    yn += 1
    print(y)


def on_xlims_change(axes):
    print("updated xlims: ", ax.get_xlim())


def on_ylims_change(axes):
    print("updated ylims: ", ax.get_ylim())


def press(event):
    if event.key == "a":
        print("a pressed")
        print(ax.get_xlim(), ax.get_ylim())
        exit()


fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', press)
ax.callbacks.connect('xlim_changed', on_xlims_change)
ax.callbacks.connect('ylim_changed', on_ylims_change)

ax.xaxis.tick_top()
ax.set_title("APPLE MAN")
ax.imshow(apple_man, cmap="seismic")   # other color maps: https://matplotlib.org/tutorials/colors/colormaps.html

plt.show()
