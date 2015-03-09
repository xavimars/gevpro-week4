#!/usr/bin/env python

import sys
import json
from collections import namedtuple

vergelijkings_lijst = []

with open('blood-die.json') as bloody_file:
	loaded_file = json.load('bloody_file')
	jason_derulo.close()
	
	for x in jason:
		bloed_woorden = x[2].split()
		dood_woorden = x[3].split()
		
		if bloed_woorden == dood_woorden:
			vergelijkings_lijst.append(dood_woorden)
			print(vergelijkings_lijst)
