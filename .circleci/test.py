#!/usr/bin/env python

import os

# The drivers must be on path
here = os.path.dirname(os.path.abspath(__file__))
os.environ['PATH'] = "%s:%s" %(here, os.environ['PATH'])

url = 'http://localhost:9999/CITapp.html'

from browser import TestRobot
driver = TestRobot()
result = driver.run_tests(url)
