# Python Plugin for Xiaomi Philips LED Bulb
#
# Author: Shainny 
#
"""
<plugin key="PhilipsBulb" name="Xiaomi Philips LED Bulb" author="Shainny" version="0.0.1">
    <params>
        <param field="Address" label="IP Adress" width="200px" requiered="true" default="192.168.0.0"/>
        <param field="Password" label="Token" width="400px" requiered="true" default="ffffffffffffffffffffffffffffffff"/>
        <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal" default="true"/>
            </options>
        </param>
    </params>
</plugin>
"""
import Domoticz
# Fix import of libs installed with pip as PluginSystem has a wierd pythonpath...
import sys
sys.path.append("/usr/local/lib/python%s.%s/dist-packages" % (sys.version_info.micro, sys.version_info.minor))
import miio

class BasePlugin:
    bulb = None

    def __init__(self):
        return

    def onStart(self):
        debug = 0
        if Parameters["Mode6"] == "Debug" :
            Domoticz.Debugging(1)
            debug = 1

        ip = Parameters["Address"]
        token = Parameters["Password"]
        self.bulb = miio.PhilipsBulb(ip, token, 0, debug)
        Domoticz.Debug("Xiaomi Philips LED Bulb created with address '" + Parameters["Address"] + "' and token '" + token + "'")

        if (len(Devices) == 0) :
            # LimitlessLights / White
            # See https://github.com/domoticz/domoticz/blob/development/hardware/hardwaretypes.h for device types
            Domoticz.Device(Name="LED Bulb", Unit=1, Type=241, Subtype=3).Create()

        DumpConfigToLog()
        return

    def onStop(self):
        Domoticz.Debug("onStop called")
        return

    def onConnect(self, Connection, Status, Description):
        Domoticz.Debug("onConnect called: Connection=" + str(Connection) + ", Status=" + str(Status) + ", Description=" + str(Description))
        return

    def onMessage(self, Connection, Data):
        Domoticz.Debug("onMessage called: Connection=" + str(Connection) + ", Data=" + str(Data))
        return

    def onCommand(self, Unit, Command, Level, Hue):
        Domoticz.Debug("onCommand called: Unit=" + str(Unit) + ", Parameter=" + str(Command) + ", Level=" + str(Level))
        return

    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Debug("Notification: " + Name + "," + Subject + "," + Text + "," + Status + "," + str(Priority) + "," + Sound + "," + ImageFile)
        return

    def onDisconnect(self, Connection):
        Domoticz.Debug("onDisconnect called")
        return

    def onHeartbeat(self):
        #Domoticz.Debug("onHeartbeat called")
        return

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)

def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)

def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

# Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return