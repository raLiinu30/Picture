"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
lightblue = Color(0xBFEFFF,1.0)
brown = Color(0x8B4726, 1.0)
grey = Color(0x8B8989, 1.0)
red = Color(0xCD2626, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, grey)
thinline1 = LineStyle(1, black)

tank = RectangleAsset(900,600, thinline, lightblue)
pebbles = RectangleAsset(900, 45, thinline, brown)
castle = RectangleAsset(350, 190, thinline, grey)
castletop = PolygonAsset([(40,60), (80,-45), (120,60)],thinline, red)
castletop1 = PolygonAsset([(40,60), (62.5,-30), (85,60)],thinline, red)
centertower = RectangleAsset(150, 140, thinline, grey)
centertower1 = RectangleAsset(45, 50, thinline, grey)
tower = RectangleAsset(80, 100, thinline, grey)
ridge = RectangleAsset(10, 25, thinline, lightblue)
ridge1 = RectangleAsset(8, 20, thinline, lightblue)
windows = RectangleAsset(130, 130, thinline, black)
windows2 = EllipseAsset(60, 80, thinline1, black)

Sprite(tank, (100,110))
Sprite(pebbles, (100,665))
Sprite(castle, (600,480))
Sprite(tower, (600,390))
Sprite(castletop, (600,285))
Sprite(tower, (870,390))
Sprite(castletop, (870,285))
Sprite(centertower, (700,350))
Sprite(tower, (735,280))
Sprite(castletop1, (750,140))
Sprite(centertower1, (750,230))
Sprite(ridge, (708,350))
Sprite(ridge, (738,350))
Sprite(ridge, (768,350))
Sprite(ridge, (798,350))
Sprite(ridge, (828,350))
Sprite(ridge1, (740,280))
Sprite(ridge1, (760,280))
Sprite(ridge1, (780,280))
Sprite(ridge1, (800,280))
Sprite(windows, (710,540))
Sprite(windows2, (714,505))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
