import json
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import OutputStreamCallback
from org.apache.nifi.processor.io import StreamCallback

class WriteJSONContent(StreamCallback):
    def __init__(self, content):
        self.content = content

    def process(self, inputStream, outputStream):
        json_content = json.dumps(self.content, indent=4)  # Serialize the content to JSON string
        outputStream.write(bytearray(json_content, 'utf-8'))

file_path = "/home/mohamed/peoplepipeline/results.json"
def replace_values(obj):
    if isinstance(obj, dict):
	return {key: replace_values(value) for key, value in obj.items()}
    elif isinstance(obj, list):
	return [replace_values(item) for item in obj]
    elif obj == "true":
	return True
    elif obj == "false":
	return False
    elif obj == "null":
	return None
    else:
	return obj
# Read the JSON file
with open(file_path, 'r') as file:
    results = json.load(file)
    results=replace_values(results)
    results=json.loads(results)
# Check if "success" key exists and its value is False
    if not results["success"]:
        result = {"result": "fail"}
    else:
        result = {"result": "pass"}

# Create a flow file and write the JSON content
flowFile = session.create()
flowFile = session.write(flowFile, WriteJSONContent(result))
session.transfer(flowFile, REL_SUCCESS)

