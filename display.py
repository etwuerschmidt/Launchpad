import py_launch

MY_LAUNCH = py_launch.PyLaunch()
MY_LAUNCH.scroll("hello", direction='X', positive=False)
MY_LAUNCH.scroll("world", direction='Y')
MY_LAUNCH.close_launchpad()
exit()