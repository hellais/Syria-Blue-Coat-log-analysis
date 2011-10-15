#!/usr/bin/env python
# This is used to fetch the categories from OpenDNS

import urllib2,csv
from BeautifulSoup import BeautifulSoup          # For processing HTML
from BeautifulSoup import BeautifulStoneSoup     # For processing XML

def get_category(site):
    page = urllib2.urlopen("http://domain.opendns.com/"+site)
    soup = BeautifulSoup(page)
    cat = ['unknown']
    thetable = soup.find('table', {'class' : "ccb"})
    try:
        for x in thetable.findAll('tr'):
            tds = x.findAll('td')
            if len(tds) > 1:
                try:
                    if tds[2].text != 'Rejected':
                        print tds[2].text
                        if tds[2].text.startswith('Approved'):
                            return [tds[1].find('b').text]
                        else:
                            if tds[1].find('b'):
                                cat.append(tds[1].find('b').text)
                except:
                    return ['unknown']
    except:
        return ['unknown']
    return cat
            #print tds[2].text

r = csv.reader(open('output-denied.csv', 'r'), delimiter=',')

domains = []
for row in  r:
    if len(row) > 3:
        domain = row[4].replace('"""','').strip()
        if domain != '-':
            domain = ".".join(domain.split('.')[-2:])
            domains.append(domain)

uniques = []
for d in domains:
    if d not in uniques:
        uniques.append(d)

rfile = open('recurrency-cat-table', 'w')
rec_table = []
for d in uniques:
    print "getting category of %s..." % d
    cat = '|'.join(get_category(d))
    print cat
    row = (domains.count(d),d,cat)
    rec_table.append(row)
    rfile.write(str(row[0])+", " + str(row[1]) + ", "+ str(row[2])+"\n")
    print "%s (%s): %s" % (d, cat, domains.count(d))

rfile.close()

print rec_table

#print get_category(domain)

