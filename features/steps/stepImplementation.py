import json
from _ast import Assert

import requests
from behave import *

from utilities.Payload import createPayload
from utilities.configFile import *


@given('I have the endpoint for the get pets')
def step_impl(context):
    context.host = getConfig()['API']['host']
    context.endpoint = getConfig()['API']['endpoint']
    context.urlDetails = context.host + context.endpoint
    context.url = context.urlDetails
    print(context.host)
    print(context.endpoint)
    print(context.urlDetails)


@when('I hit the endpoint')
def step_impl(context):
    context.response = requests.get(context.url, headers={"Content-Type": "application/json"})
    print(context.response.text)


@then('I validate the status code as 200')
def step_impl(context):
    response = context.response
    print(response.status_code)


@given('the payload details for the request')
def step_impl(context):
    context.data = createPayload()
    print("Payload is:", context.data)


@when('we execute the Post method')
def step_impl(context):
    context.endpoint = getConfig()['API']['postEndpoint']
    context.response = requests.post(context.endpoint, json=context.data, headers={"Content-Type": "application/json"})


@then('verify the new resource is created a')
def step_impl(context):
    print("Response json is:", context.response.json())
    status_code = context.response.status_code
    print("Status code is :", status_code)
    data_dict = context.response.json()
    print(data_dict['bookingid'])

@then(u'status code of response should be 200')
def step_impl(context):
    assert context.response.status_code == 200
