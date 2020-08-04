import sys
import time

# Load the API library
sys.path.append("../../lib/")
from migratorydata_client_python import *


# Define the listener to handle live message and status notifications
class MyListener(MigratoryDataListener):
    def __init__(self):
        pass

    def on_status(self, status, info):
        print("Got status " + status + " - " + info)

    def on_message(self, message):
        print("Got message " + str(message))


if len(sys.argv) != 4:
    print("Usage: python3 publish_subscribe_timer.py HOST PORT SUBJECT")
    quit()

subject = str(sys.argv[3])
server = str(sys.argv[1]) + ":" + str(sys.argv[2])

# create a MigratoryData client
client = MigratoryDataClient()

# attach the entitlement token
client.set_entitlement_token("some-token")

# attach your MigratoryDataListener
client.set_listener(MyListener())

# set server to connect to the MigratoryData server
client.set_servers([server])

#  connect to the MigratoryData server
client.connect()

# subscribe
client.subscribe([subject])

time.sleep(1)

# publish a message every 3 seconds
count = 1
while True:
    content = "data - " + str(count)
    closure = "id" + str(count)
    client.publish(MigratoryDataMessage(subject, content.encode('utf-8'), closure))
    count += 1
    time.sleep(2)

# disconnect client from server
client.disconnect()
