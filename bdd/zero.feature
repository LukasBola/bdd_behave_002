#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Feature: Test of car dealer site

	Scenario: log in 
		Given the page "http://salon.rpgit.pl/" is loaded	
		When I type "lukasz.bola" in "id_username" input
		And I type "Welcome1" in "id_password" input
		And I click "id_login_btn" button
		Then the home page is diplayed

	Scenario: add a new car
		When I click "add-new-car" button
		And I select "Audi" from "id_marka" select
		And I type "R8" in "id_model" input
		And I type "2018" in "id_rocznik" input
		And I click "Zapisz" button2
		Then there is a car: brand "Audi", model "R8", year "2018"
