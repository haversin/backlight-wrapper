#!/usr/bin/env python

import sys
import subprocess

# $ cat /sys/class/backlight/intel_backlight/max_brightness 
# 852
BRIGHT_MAX_ABS = 852
BRIGHT_MAX = BRIGHT_MAX_ABS*0.01

# generated by generateSteps.py
STEPS = [0,1,2,4,8,15,25,39,57,81,110,145,187,237,295,362,439,525,623,731,852]
NSTEPS = len(STEPS)-1

def getXBacklight():
	x = subprocess.run(['xbacklight', '-get'], stdout=subprocess.PIPE).stdout
	return float(x)

def fromPercentToAbs(percent):
	return int(round(percent*BRIGHT_MAX))

def determineStep(percent):
	current = fromPercentToAbs(percent)
	current_step = 0
	dist = 1000
	for n, x in enumerate(STEPS):
		if(abs(x-current) > dist):
			break
		dist = abs(x-current)
		current_step = n
	return current_step

def printHelp():
	print(
		'hav\'s xbacklight wrapper for T450s\n'
		'usage:\n'
		f'{sys.argv[0]} [+-]\n'
		f'{sys.argv[0]} 0-{NSTEPS}'
		)

def main():
	if len(sys.argv) > 2:
		printHelp()
		return 1
	
	cmd = None
	if len(sys.argv) == 2:
		cmd = sys.argv[1]

	current_step = determineStep(getXBacklight())
	
	if cmd is not None:
		if cmd == '+' and current_step < NSTEPS:
			new = STEPS[current_step+1]
		elif cmd == '-' and current_step > 0:
			new = STEPS[current_step-1]
		elif cmd.isdigit():
			if int(cmd) >= 0 and int(cmd) <= NSTEPS:
				new = STEPS[int(cmd)]
		else:
			printHelp()
			return 1

		subprocess.run(['xbacklight', '-set', f'{new/BRIGHT_MAX}'])
	else:
		bri = getXBacklight()
		print(f'{determineStep(bri)}  abs:{fromPercentToAbs(bri)}  {bri}%')


if __name__ == "__main__":
    main()