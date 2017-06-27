#!/usr/bin/python
import ConfigParser

configParser = ConfigParser.ConfigParser(allow_no_value=True)
configParser.read('config.ini')

print configParser.get('natnetConfig', 'natnetIP')

print configParser.get('natnetConfig', 'Version')


a = '10897'

b = int(a)

print type(b)
