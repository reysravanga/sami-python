SAMI Python SDK
================

This SDK helps you connect your Python scripts to SAMI. The SDK helps authenticating with SAMI, exposes a number of methods to easily execute REST API calls to SAMI.

Prerequisites
-------------

 * python 2.7.x: https://www.python.org/download/


Installation
---------------------

Once you have installed the required libraries add the scripts to your project.

```
#!/usr/bin/env python

accessToken = "<sami-access-token>"

print 'SAMI Python Demo Client'
print '-----------------------'

from samiio import ApiClient
apiClient = ApiClient(apiKey=accessToken, apiServer = "https://api.samsungsami.io/v1.1")

from MessagesApi import MessagesApi
messagesApi = MessagesApi(apiClient)

from models import *
message = Message.Message()

message.sdid = "<source-device-id>"
message.type = "message"

# message.data contains the device JSON message
# Data below is JSON for the SAMI Pedometer
message.data = {'numberOfSteps':2000, 'distance': 1.1, 'floorsAscended': 2, 'floorsDescended': 0}

print 'Sending message:'
print message.data

messageIDEnvelope = messagesApi.sendMessageAction(body=message)

print 'Sent.'
print '    Message ID: ' + messageIDEnvelope.data.mid
```

For a more complete list of examples see our demo application at https://github.com/samsungsamiio/sami-python-demo

More about SAMI
---------------

If you are not familiar with SAMI we have extensive documentation at http://developer.samsungsami.io

The full SAMI API specification with examples can be found at http://developer.samsungsami.io/sami/api-spec.html

We blog about advanced sample applications at http://blog.samsungsami.io/

To create and manage your services and devices on SAMI visit developer portal at http://devportal.samsungsami.io

Licence and Copyright
---------------------

Licensed under the Apache License. See LICENCE.

Copyright (c) 2014 Samsung Electronics Co., Ltd.
