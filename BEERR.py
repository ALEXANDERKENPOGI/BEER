import os, platform, time, sys
os.system('xdg-open https://www.facebook.com/alexanderkenpogi')
#os.system('xdg-open https://chat.whatsapp.com/LVHHgKJW6EQHb20n6R4Du8')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m64Bit Found')
 import Beerr64
elif bit == '32bit':
 print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m32Bit Found')
 import Beerr32
