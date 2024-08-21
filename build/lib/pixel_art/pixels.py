from colorama import init, Back, Style

init(autoreset=True)

BLACK = Back.BLACK + '  '
RED = Back.RED + '  '
GREEN = Back.GREEN + '  '
YELLOW = Back.YELLOW + '  '
BLUE = Back.BLUE + '  '
MAGENTA = Back.MAGENTA + '  '
CYAN = Back.CYAN + '  '
WHITE = Back.WHITE + '  '

COLORS_DICT = {
  'black' : BLACK,
  'red' : RED,
  'green' : GREEN,
  'yellow' : YELLOW,
  'blue' : BLUE,
  'magenta' : MAGENTA, 
  'cyan' : CYAN,
  'white' : WHITE
}

class Image():
  def __init__(self, w=7, h=7):
    self.width = w
    self.height = h
    self.img = self.init_list()

  def init_list(self):
    lst = []
    for row in range(self.height):
      lst.append([])
    return lst

  def display(self):
    for row in self.img:
      self.display_row(row)

  def display_row(self, row):
    for pixel in row:
      print(pixel, end='')
    print()

  def convert_color(self, str_clr):
    return COLORS_DICT.get(str_clr, BLACK)

  def add_row(self, *args):
    if len(args) == 2:
      colors = [self.convert_color(args[1]) for i in range(self.width)]
      self.img[args[0]] = colors
    else:
      color_params = args[1:]
      colors = [self.convert_color(arg) for arg in color_params]
      self.img[args[0]] = colors
