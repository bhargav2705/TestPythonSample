import json


def createPayload():
    f = open('utilities/payloadData/samplePayload.json')
    data = json.load(f)
    return data
