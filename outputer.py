#!/usr/bin/env python

import re
import gzip

class LogEntry:
  def __init__(self, line):

    toparse = line.split(" ")
    parse = []
    flag = False
    tmp = ""
    for i in toparse:
        if i.startswith("\"") or flag:
            if not flag:
                #print "Opened!"
                tmp += " " + i.replace("\"","")
                flag = True
                if i.endswith("\""):
                    #print "Closed!"
                    parse.append(tmp)
                    flag = False
                    tmp = ""
                    continue
                else:
                    continue
            else:
                if i.endswith("\""):
                        #print "Closed!"
                        flag = False
                        parse.append(tmp+" "+i.replace("\"", ""))
                        tmp = ""
                else:
                    if flag:
                        tmp += i
        else:
            parse.append(i)

    self.raw = parse
    self.p = {}
    self.p['date'] = parse[0]
    self.p['time'] = parse[1]
    self.p['time_taken'] = parse[2]
    self.p['c_ip'] = parse[3]
    self.p['cs_username'] = parse[4]
    self.p['cs_auth_group'] = parse[5]
    self.p['x_exception_id'] = parse[6]
    self.p['sc_filter_result'] = parse[7]
    self.p['cs_categories'] = parse[8]
    self.p['cs_referrer'] = parse[9]
	# Stupid extra space!
    self.p['sc_status'] = parse[11]
    self.p['s_action'] = parse[12]
    self.p['cs_method'] = parse[13]
    self.p['rs_content_type'] = parse[14]
    self.p['cs_uri_scheme'] = parse[15]
    self.p['cs_host'] = parse[16]
    self.p['cs_uri_port'] = parse[17]
    self.p['cs_uri_path'] = parse[18]
    self.p['cs_uri_query'] = parse[19]
    self.p['cs_uri_extension'] = parse[20]
    self.p['cs_user_agent'] = parse[21]
    self.p['s_ip'] = parse[22]
    self.p['sc_bytes'] = parse[23]
    self.p['cs_bytes'] = parse[24]
    self.p['x_virus_id'] = parse[25]


  def display(self):
    print "%s %s" % (self.date, self.time)
    print "%s" % (self.cs_host)

fh = gzip.open("SG_main__420722212535.log.gz", "r")

x = fh.next()

hosts = []

while(x.startswith("#")):
  x = fh.next()

i = 0
outputfile = open("output-denied.csv", "w")

while x:
    x = fh.next()
    log = LogEntry(x)
    if log.p['sc_filter_result'].strip() == "DENIED":
        for key, value in log.p.items():
            outputfile.write("\"\"\""+value.strip().replace(",","\\,")+"\"\"\", ")
            #print "%s: %s" % (key,value)

    outputfile.write("\n")
    i += 1
    if (i % 10000) == 0:
        print i
    """
    for y in log.raw:
        print "\"\"\"%s\"\"\"," % y,
    print "\n\n
    """

outputfile.close()

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

