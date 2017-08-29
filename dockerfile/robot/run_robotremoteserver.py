#!/usr/bin/env python
from robotremoteserver import RobotRemoteServer
from examplelibrary import ExampleLibrary

RobotRemoteServer(ExampleLibrary(), host='0.0.0.0', port=8270,
                  port_file='/tmp/remote-port.txt')
