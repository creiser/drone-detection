import os
import random
import string
files = os.listdir('.')
random.shuffle(files)
unique = ''.join(random.choice(string.ascii_uppercase) for _ in range(20))
[os.rename(f, unique + str(i + 1) + os.path.splitext(f)[-1]) for i, f in enumerate(files)]
[os.rename(f, str(i + 1) + os.path.splitext(f)[-1]) for i, f in enumerate(os.listdir('.'))]


