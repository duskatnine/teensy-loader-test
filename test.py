#import subprocess

#subprocess.call(teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex)
#subprocess.call(./teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex)
#subprocess.call('./teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex')
#subprocess.call("'./teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex'")
#subprocess.call('"./teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex"')
#subprocess.call(['teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex'])
#subprocess.call(['./teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex'])
#subprocess.call(['./teensy_loader_cli.exe --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex'])


#import os
#os.system('./teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex')

import subprocess
subprocess.call('./teensy_loader_cli --mcu=mk20dx256 -s -v blink_slow_Teensy32.hex', shell=True)