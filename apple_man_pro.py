# apple_man_pro
# version 2.0
# Copyright 2018 Andreas Schadli

from matplotlib import pyplot as plt

# global counter for figures
FIGURE_NUMBER = 1
# constants
MAX_ITER = 100
THRESHOLD = 2
DEFAULT_RESOLUTION = 500
REPAINT_KEY_DIRECT = 'a'
REPAINT_KEY_FORMAT = 'b'
SAVE_KEY = 'c'


class AppleMan:
    def __init__(self, x_section, y_section, resolution):
        self.max_iter = MAX_ITER
        self.threshold = THRESHOLD
        self.repaint_key_direct = REPAINT_KEY_DIRECT
        self.repaint_key_format = REPAINT_KEY_FORMAT
        self.save_key = SAVE_KEY
        self.resolution = resolution

        # variable values
        self.x_min = x_section[0]
        self.x_max = x_section[1]
        self.y_min = y_section[0]
        self.y_max = y_section[1]
        self.step, self.x_diff, self.y_diff = self.cal_step()

        # list for apple man image
        self.apple_man = []

    def cal_step(self):
        x_diff = abs(self.x_max - self.x_min)
        y_diff = abs(self.y_max - self.y_min)
        s = ((x_diff ** 2 + y_diff ** 2) ** 0.5) / self.resolution
        return s, x_diff, y_diff

    def mandelbrot(self, c):
        z = 0
        for n in range(self.max_iter):
            z = z ** 2 + c
            if abs(z) >= self.threshold:
                return n  # divergent
        return self.max_iter  # convergent

    def color(self, i):
        return i / self.max_iter
        # return abs((i / self.max_iter) - 1)    # invert color map

    def paint(self):
        yn = 0
        y = self.y_min
        while y <= self.y_max:
            self.apple_man.append([])
            x = self.x_min
            while x <= self.x_max:
                complex_number = x + y * 1j
                iterations = self.mandelbrot(complex_number)
                self.apple_man[yn].append(self.color(iterations))
                x += self.step
            yn += 1
            y += self.step

        def on_x_change(axes):
            pass

        def on_y_change(axes):
            pass

        def press(event):
            if event.key == self.repaint_key_direct:
                new_x_section = ()
                new_x_section += (ax.get_xlim()[0] / (self.x_diff / self.step) * self.x_diff + self.x_min,)
                new_x_section += (ax.get_xlim()[1] / (self.x_diff / self.step) * self.x_diff + self.x_min,)
                new_y_section = ()
                new_y_section += (ax.get_ylim()[1] / (self.y_diff / self.step) * self.y_diff + self.y_min,)
                new_y_section += (ax.get_ylim()[0] / (self.y_diff / self.step) * self.y_diff + self.y_min,)
                new_apple_man(new_x_section, new_y_section)
            elif event.key == self.repaint_key_format:
                width = int(input('Calculate how many points in x direction? '))
                height = int(input('Calculate how many points in y direction? '))
                res = (width ** 2 + height ** 2) ** 0.5
                
                x_begin = ax.get_xlim()[0] / (self.x_diff / self.step) * self.x_diff + self.x_min
                x_end = ax.get_xlim()[1] / (self.x_diff / self.step) * self.x_diff + self.x_min
                y_begin = ax.get_ylim()[1] / (self.y_diff / self.step) * self.y_diff + self.y_min
                y_end = y_begin + height / width * abs(x_begin - x_end)
                new_x_section = ()
                new_x_section += (x_begin,)
                new_x_section += (x_end,)
                new_y_section = ()
                new_y_section += (y_begin,)
                new_y_section += (y_end,)
                new_apple_man(new_x_section, new_y_section, res)
            elif event.key == self.save_key:
                dpi_factor = float(input('Switch the picture to full screen! '
                                         'Enter a scaling factor for your screen dpi: '))
                plt.savefig('Apple Man.png', bbox_inches='tight', pad_inches=0, dpi=fig.dpi * dpi_factor)

        # make plot interactive
        fig, ax = plt.subplots()
        fig.canvas.mpl_connect('key_press_event', press)
        ax.callbacks.connect('xlim_changed', on_x_change)
        ax.callbacks.connect('ylim_changed', on_y_change)

        # ax.xaxis.tick_top() TODO neccessary

        # color maps: 'seismic', 'hot' or https://matplotlib.org/stable/tutorials/colors/colormaps.html
        ax.imshow(self.apple_man, cmap='hot')

        # makes the image big as possible in the matplotlib frame
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                            hspace=0, wspace=0)
        plt.axis('off')

        plt.show()


def new_apple_man(x_section=(-2., 1.), y_section=(-1., 1.), resolution=DEFAULT_RESOLUTION):
    global FIGURE_NUMBER
    print('coordinates of figure', FIGURE_NUMBER, '(x_min, x_max), (y_min, y_max):', x_section, y_section)
    FIGURE_NUMBER += 1
    a = AppleMan(x_section, y_section, resolution)
    a.paint()


new_apple_man()
# new_apple_man((-0.7182049647852089, -0.6641146512912729), (-0.4882296284289145, -0.4533326519812138))
# (-0.9140868442109342, -0.9140867984031853), (-0.2793404180229928, -0.27934036831671205)
# (-0.8406253743030859, -0.8374017862497465), (-0.21486638113274203, -0.21326860270630424)
# (-0.7182049647852089, -0.6641146512912729), (-0.4882296284289145, -0.4533326519812138)
