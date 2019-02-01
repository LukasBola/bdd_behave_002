#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from behave import *
import time

@given('the page "{url}" is loaded')
def step_impl(context, url): 
	context.browser.get(url)
	time.sleep(1)
	
@when('I type "{text}" in "{input_id_field}" input')
def step_impl(context, text, input_id_field):
	input_field = context.browser.find_element_by_xpath('//input [@id = "{}"]'.format(input_id_field))
	input_field.send_keys(text)
	time.sleep(1)

@when('I click "{button_id}" button')
def step_impl(context, button_id):
	button = context.browser.find_element_by_xpath('//button [@id = "{}"]'.format(button_id))
	button.click()
	time.sleep(1)
