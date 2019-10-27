from py_launch import *

MY_LAUNCH = PyLaunch()
#MY_LAUNCH.display_chars("Hello world")

MY_LAUNCH.scroll("hello", direction='X', positive=False)
MY_LAUNCH.scroll("world", direction='Y')
MY_LAUNCH.close_launchpad()
exit()