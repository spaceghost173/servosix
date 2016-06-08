# Use the following keys to move servos 1 to 4
#
# Servo 1 2 3 4
# Up    q w e r
# Down  a s d f


import sys
import tty
import termios
from servosix import ServoSix

angles = [90, 90, 90, 90]
ss = ServoSix()

def inc_angle(servo):
    if angles[servo-1] < 180:
        angles[servo-1] += 5
        ss.set_servo(servo, angles[servo-1])


def dec_angle(servo):
    if angles[servo-1] > 0:
        angles[servo-1] -= 5
        ss.set_servo(servo, angles[servo-1])

# These functions allow the program to read your keyboard
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows


try: 
    while True:
        k = readkey()
        if k == 'q':
            inc_angle(1)
        elif k == 'a':
        	    dec_angle(1)

except KeyboardInterrupt:
    pass
