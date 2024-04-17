import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil
import urllib
import urllib2
import json


class ModJson(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        global errorOccurred
        try:
            text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            reply = json.loads(text)
            
            # Ensure 'lat' and 'lng' fields are present in the reply
            if 'lat' in reply and 'lng' in reply:
                # Convert 'lat' and 'lng' to float values
                lat = float(reply['lat'])
                lng = float(reply['lng'])
                
                # Construct the 'coords' field as a string in the format "latitude,longitude"
                coords = "{},{}".format(lat, lng)
                reply['coords'] = coords
                
                d = reply['created_at'].split('T')
                reply['opendate'] = d[0]
                
                outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
            else:
                # Handle case where 'lat' or 'lng' fields are missing
                errorOccurred = True
                error_response = {'error': "'lat' or 'lng' fields missing in data"}
                outputStream.write(bytearray(json.dumps(error_response, indent=4).encode('utf-8')))

        except Exception as e:
            errorOccurred = True
            error_response = {'error': str(e)}
            outputStream.write(bytearray(json.dumps(error_response, indent=4).encode('utf-8')))


errorOccurred = False
flowFile = session.get()
if flowFile is not None:
    flowFile = session.write(flowFile, ModJson())
    if errorOccurred:
        session.transfer(flowFile, REL_FAILURE)
    else:
        session.transfer(flowFile, REL_SUCCESS)

