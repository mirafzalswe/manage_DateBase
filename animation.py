import time
import sys

def loading_animation(duration):
    animation = "|/-\\"
    for _ in range(duration * 10):
        time.sleep(0.1)
        sys.stdout.write("\rPlease wait " + animation[_ % len(animation)])
        sys.stdout.flush()

    sys.stdout.write("\rThank for your wait!    \n")