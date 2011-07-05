from scavenger import Scavenger, shutdown, scavenge
from time import sleep

# Sleep for a little while to allow surrogates to be discovered.
print "Sleeping for a little while...",
sleep(1.2)
print "done"
print "Found", len(Scavenger.get_peers()), "surrogates"

@scavenge('0.00001', '0.00001', False, "www.testip.com", True)
def add(x, y):
    return x + y


@scavenge("0.0001", "0.0001")
def calc(x,y):
	x = x*y*x*y*x*y
	x += 74
	return x*x*x*x*y

surrogates = Scavenger.get_peers()
for surrogate in surrogates:
	print surrogate.name, "---", surrogate.address

print "Scavenging a little..."
print add(1,2)
print add(3,4)
print calc(5738,6623)
print "done"


print 'Doing some manual "scavenging"'
print Scavenger.scavenge('daimi.test.add', [1,2], """
def perform(x,y):
    return x+y
""")
print Scavenger.scavenge('daimi.test.add', [2,3])
print "done"

shutdown()
    

