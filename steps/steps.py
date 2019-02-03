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

@then('the home page is diplayed')
def step_impl(context):
	context.browser.find_element_by_xpath('//table [@id = "customers"]')
	time.sleep(1)

@when('I select "{value}" from "{select_id}" select')
def step_impl(context,value,select_id):
	sel = context.browser.find_element_by_xpath(
		'//select [@id = "{}"] / option [text() = "{}"]'.format(select_id, value))
	sel.click()
	time.sleep(1)

@when('I click "{save}" button2')
def step_impl(context, save):
	save_button = context.browser.find_element_by_xpath('//button [text() = "{}"]'.format(save))
	save_button.click()
	time.sleep(1)

@then('there is a car: brand "{brand}", model "{model}", year "{year}"')
def step_impl(context, brand, model, year):
	context.browser.find_element_by_xpath(
		'//table [@id = "customers"]//tr[td[@class = "brand"][text() = "{}"]]'.format(brand)
		)
	context.browser.find_element_by_xpath(
		'//table [@id = "customers"]//tr[td[@class = "model"][text() = "{}"]]'.format(model)
		)
	context.browser.find_element_by_xpath(
	'//table [@id = "customers"]//tr[td[@class = "year"][text() = "{}"]]'.format(year)
	)


