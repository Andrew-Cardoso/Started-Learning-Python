# import sys
# print( sys.builtin_module_names )

import time
# print(dir(time))
# print(help(time.sleep))

import os

# new packages
# py -m pip install package-name    or     pip install package-name

count_iterations = 0
while True:
     if os.path.exists("vegatables.txt"):
          print(2)
     print(count_iterations)
     count_iterations += 1
     time.sleep(.5)
     