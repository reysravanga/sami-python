#!/usr/bin/env python

"""
 The program uses SAMI Python SDK
 It should be in the root directory of SAMI Python SDK

 Usage:
     python exampleSendMessage.py
"""

deviceID = "YOUR DEVICE ID"
deviceToken = "YOUR DEVICE TOKEN"

print 'SAMI Python example - Send a message to SAMI'
print '-----------------------'
print ''

from samiio import ApiClient
apiClient = ApiClient(apiKey = deviceToken, apiServer = "https://api.samsungsami.io/v1.1")

from MessagesApi import MessagesApi
messagesApi = MessagesApi(apiClient)

from models import *
message = Message.Message()

message.sdid = deviceID
message.type = "message"

# message.data contains the device JSON message
# Data below is JSON for the SAMI Demo Pedometer
message.data = {'numberOfSteps':2000, 'distance': 1.1, 'floorsAscended': 2, 'floorsDescended': 10}

print 'Sending message: ' + str(message.data)

messageIDEnvelope = messagesApi.postMessage(body=message)

print 'The message was Sent.'
print '    Message ID: ' + messageIDEnvelope.data.mid

