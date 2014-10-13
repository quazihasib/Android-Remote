import RemoteControlServer as RCS

# define the callback function
def sayHello():
    print "Hello! It works!"

# create the button definition
# this is what will be displayed on the phone when it connects to the server
butDef = RCS.ButtonsDefinition()
butDef.addButton("Hello", sayHello)

# create server object
server = RCS.Server(butDef)

# run the server (blocks)
print 'Running server'
server.run()
