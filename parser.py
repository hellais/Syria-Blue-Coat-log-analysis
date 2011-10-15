#!/usr/bin/env python

import re
import gzip

class LogEntry:
  def __init__(self, line):
    parse = line.split(" ")
    self.date = parse[0]
    self.time = parse[1]
    self.time_taken = parse[2]
    self.c_ip = parse[3]
    self.cs_username = parse[4]
    self.cs_auth_group = parse[5]
    self.x_exception_id = parse[6]
    self.sc_filter_result = parse[7]
    self.cs_categories = parse[8]
    self.cs_referrer = parse[9]
    self.sc_status = parse[10]
    # Stupid extra space!
    self.s_action = parse[12]
    self.cs_method = parse[13]
    self.rs_content_type = parse[14]
    self.cs_uri_scheme = parse[15]
    self.cs_host = parse[16]
    self.cs_uri_port = parse[17]
    self.cs_uri_path = parse[18]
    self.cs_uri_query = parse[19]
    self.cs_uri_extension = parse[20]
    self.cs_user_agent = parse[21]
    self.s_ip = parse[22]
    self.sc_bytes = parse[23]
    self.cs_bytes = parse[24]
    self.x_virus_id = parse[25]

  def display(self):
    print "%s %s" % (self.date, self.time)
    print "%s" % (self.cs_host)

fh = gzip.open("SG_main__420722212535.log.gz", "r")

x = fh.next()

hosts = []

while(x.startswith("#")):
  x = fh.next()

i = 0
while x and i < 100000:
  try:
    if (i % 10000) == 0:
      print i
    x = fh.next()
    log = LogEntry(x)
    #log.display()
    if re.match("\d+\.\d+\.\d+\.\d+",log.cs_host):
      hosts.append(log.cs_host)
    else:
      hosts.append(".".join(log.cs_host.split(".")[-2:]))
    i += 1
  except:
    print x
    print "error, never mind skipping..."
    x = fh.next()

hosts.sort()
orig = hosts
cur = hosts.pop()
next = cur
counting = []

while cur is not None:
  while cur == next and hosts:
    next = hosts.pop()
  #print "%s %s" % (next, orig.count(next))
  counting.append((orig.count(next), next))
  if not hosts:
    break
  cur = hosts.pop()
  next = cur

counting.sort()
counting.reverse()

for i in counting:
  print "%s %s" % (i[0], i[1])

