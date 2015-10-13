SAMI Python SDK
================

This SDK helps you connect your Python scripts to SAMI. The SDK helps authenticating with SAMI, exposes a number of methods to easily execute REST API calls to SAMI.

Prerequisites
-------------

 * python 2.7.x: https://www.python.org/download/


Installation
---------------------

Download the SAMI Python SDK and put it in your Python's search path. Then use SAMI APIs from the SDK in your python scripts.

Example: Send a Message
---------------------

1. Replace "YOUR DEVICE ID" and "YOUR DEVICE TOKEN" in `exampleSendMessage.py` with your device id and token.
2. Run the script in the console and observe the output like the following
~~~
$ python exampleSendMessage.py 
SAMI Python example - Send a message to SAMI
-----------------------

Sending message: {'numberOfSteps': 2000, 'distance': 1.1, 'floorsAscended': 2, 'floorsDescended': 10}
The message was Sent.
    Message ID: c23a819f13fc4d0db4ffb6d83ff9b10d
~~~

Example: Get a Message
---------------------

1. Replace "YOUR DEVICE ID" and "YOUR DEVICE TOKEN" `exampleGetMessage.py` with your device ID and token.
2. Run the script in the console and observe the output like the following
~~~
$ python exampleGetMessage.py 
SAMI Python Tutorial App -- Get a message
-----------------------
Got the last normalized message:{u'distance': 1.1, u'floorsAscended': 2, u'stepCount': 2000, u'floorsDescended': 5}
~~~

For a more complete list of examples see our demo application at https://github.com/samsungsamiio/sami-python-demo

More about SAMI
---------------

If you are not familiar with SAMI we have extensive documentation at http://developer.samsungsami.io

The full SAMI API specification with examples can be found at http://developer.samsungsami.io/sami/api-spec.html

Peek into advanced sample applications at https://developer.samsungsami.io/sami/samples/

To create and manage your services and devices on SAMI visit developer portal at http://devportal.samsungsami.io

Licence and Copyright
---------------------

Licensed under the Apache License. See LICENCE.

Copyright (c) 2015 Samsung Electronics Co., Ltd.
