This is a dump of the code I wrote to produce the pretty chart you can see at
http://hellais.github.com/syria-censorship

You may not be able to reproduce since it was really a hack and the code in this
repo may not include random BASH script-fu.

Here is a list of what the various scripts do:
 * parser.py - The main parser for Blue Coat style logs
 * outputter.py - Used to convert the logs to .csv (that is what I mainly used for making the charts).
    By default it only select POLICY DENIED, but I am sure anyone can figure out how to make it do anything else ;)
 * category-fetcher.py  - Used to  fetch the categories of the various websites from OpenDNS
 * datanal.py - Used to count the unique recurrence of certain elements
 * piecharting.py - Used to convert the count of categories to percentages in the format wanted by Highcharts

If somebody is interested in knowing more I will be glad to be more specific.
Just drop me an email art@globaleaks.org.

