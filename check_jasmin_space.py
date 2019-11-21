#! /usr/bin/python2.7

# check_jasmin_space script to check the space used on JASMIN and provide the output to Nagios
# This program should be called: ./check_jasmin_space.py -w WARNING_VALUE -c CRITICAL_VALUE -p PROJECT_NAME
# Format of the input from the URL needs to be: total space, used space, free space, percentage used, location
# This script has been written by Andy Bowery (Oxford University, 2019)

import urllib2,sys,re

if __name__=="__main__":

  warning = int(sys.argv[2])
  critical = int(sys.argv[4])
  project_name = sys.argv[6]

  target_url = 'TARGET_URL_HERE'+project_name

  # Open the URL
  try:
    url_output = urllib2.urlopen(target_url)
  except:
    print "CRITICAL - cannot access %s"%target_url
    sys.exit(2)

  # Split up output by whitespace
  for line in url_output:
    output = line.split()

  # Remove '%' symbol
  percentage_used = int(re.sub('[%]','',output[3]))

  if percentage_used > critical:
    print "CRITICAL - %s of disk space used, %s free space in %s" % (output[3],output[2],output[4])
    sys.exit(2)
  elif percentage_used > warning:
    print "WARNING - %s of disk space used, %s free space in %s" % (output[3],output[2],output[4])
    sys.exit(1)
  else:
    print "OK - %s of disk space used, %s free space in %s" % (output[3],output[2],output[4])
    sys.exit(0)
