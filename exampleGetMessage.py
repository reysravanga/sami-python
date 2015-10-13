#!/usr/bin/env python

"""
 The program uses SAMI Python SDK
 It should be in the root directory of SAMI Python SDK

 Usage:
     python exampleGetMessage.py
"""

deviceID = "YOUR DEVICE ID"
deviceToken = "YOUR DEVICE TOKEN"

print 'SAMI Python Example -- Get the last normalized message'
print '-----------------------'
print ''

from samiio import ApiClient
apiClient = ApiClient(apiKey = deviceToken, apiServer = "https://api.samsungsami.io/v1.1")

from MessagesApi import MessagesApi
messagesApi = MessagesApi(apiClient)

from models import *

# Get the latest message:
lastNormalizedMessagesEnvelope = messagesApi.getNormalizedMessagesLast(sdids = deviceID, count = 1)
print 'Got the last normalized message:' + str(lastNormalizedMessagesEnvelope.data[0].data)
