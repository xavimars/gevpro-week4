#!/usr/bin/env python3
#Xavier Marseille

import xml.etree.ElementTree as ET
import sys

def main(argv):
		tree = ET.parse(argv[1])
		root = tree.getroot()

		for POINT in root.findall('POINT'):
			BOTTOM_HZ = float(POINT.find('BOTTOM_HZ').text)
			TOP_HZ = float(POINT.find('TOP_HZ').text)
			F0_START = float(POINT.find('F0_START').text)
			F0_END = float(POINT.find('F0_END').text)
		
			if ((F0_START < BOTTOM_HZ) or (F0_START > TOP_HZ) or (F0_END < BOTTOM_HZ) or (F0_END > TOP_HZ)):
				root.remove(POINT)
		
		tree.write(argv[2])

if __name__ == '__main__':
	main(sys.argv)
	
