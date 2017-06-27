import json
send_msg = {}

header = {}
header['FrameNumber'] = 1
header['MarkerSetCount'] = 2
header['rigidBodyCount'] = 3
header['timestamp'] = 4
send_msg["Header"+str(4)] = header

print json.dumps(send_msg)