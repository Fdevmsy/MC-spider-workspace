from NatNetClient import NatNetClient
import paho.mqtt.client as paho
import json
import configparser

configParser = configparser.ConfigParser(allow_no_value=True)
configParser.read('config.ini')

broker = configParser.get('mqttConfig', 'brokerIP')
port = configParser.get('mqttConfig', 'brokerport')
mytopic = configParser.get('mqttConfig', 'topic')

def on_publish(client,userdata,result):             

	print("data published \n")
	
def on_connect():
    print("Connected!")
## # create client object
#client1= paho.Client("control1") 
## # assign function to callback                          
#client1.on_publish = on_publish 
#client1.on_connect = on_connect   
## # establish connection                         
#client1.connect("127.0.0.1",1883)                              

send_msg = {}
# This is a callback function that gets connected to the NatNet client and called once per mocap frame.
def receiveNewFrame( inMarkerModelName, inMarkerset, markerCount, frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
                    labeledMarkerCount, latency, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged ):
    # print( "Received frame", frameNumber )
    header = {}
    header['FrameNumber'] = frameNumber
    header['MarkerSetCount'] = markerSetCount
    header['markerCount'] = markerCount
    # header['timestamp'] = timestamp
    header['labeledMarkerCount'] = labeledMarkerCount
    header['unlabeledMarkersCount'] = unlabeledMarkersCount
    header['inMarkerset'] = inMarkerset
    header['inMarkerModelName']  = inMarkerModelName
    send_msg["Header"] = header
    # client1.publish('time', payload=json.dumps(send_msg))
    # print(send_msg)
# This is a callback function that gets connected to the NatNet client. It is called once per rigid body per frame
def receiveRigidBodyFrame( id, position, rotation ):

    # print( "Received frame for rigid body", id )
    # rigidBodyInfo = {}
    # rigidBodyInfo['id'] = id
    # rigidBodyInfo['position'] = position
    # rigidBodyInfo['rotation'] = rotation
    # send_msg["Rigid-"+str(id)] = rigidBodyInfo

    
    # print(send_msg)
	# send_msg = {}
    pass

# This will create a new NatNet client
streamingClient = NatNetClient()

# Configure the streaming client to call our rigid body handler on the emulator to send data out.
streamingClient.newFrameListener = receiveNewFrame
streamingClient.rigidBodyListener = receiveRigidBodyFrame

# Start up the streaming client now that the callbacks are set up.
# This will run perpetually, and operate on a separate thread.
# 
print("before running")
streamingClient.run()







