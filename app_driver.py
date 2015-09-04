from razor import Razor

myRazor = Razor()

keyInput = ""

print "Shave App at its simplest"
print "enter shave to get instruction, enter quit to stop using app."

while keyInput != "quit":
	keyInput = raw_input(">> ")
	if keyInput == "shave":
		myRazor.shave()

