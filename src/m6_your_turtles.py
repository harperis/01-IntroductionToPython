"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Isaac Harper.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
##############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

john = rg.SimpleTurtle('turtle')
john.pen = rg.Pen('pink', 4)
john.speed = 10

size = 200

for k in range(8) :
    john.draw_square(size)

    john.pen_up()
    john.left(20)
    john.forward(15)
    john.right(20)

    john.pen_down()
    size = size - 8

susan = rg.SimpleTurtle('turtle')
susan.pen = rg.Pen('blue', 4)
susan.speed = 10
size = 200

for k in range(8) :
    susan.draw_square(size)
    susan.pen_up()
    susan.right(20)
    susan.forward(15)
    susan.left(20)
    susan.pen_down()
    size = size - 6
window.close_on_mouse_click()