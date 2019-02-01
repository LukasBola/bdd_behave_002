#!/usr/bin/env python3
# -*- coding: utf-8 -*-
### Author: Łukasz Bola

Feature: Test of car dealer site

	Scenario: log in 
		Given the page "http://salon.rpgit.pl/" is loaded	
		When I type "lukasz.bola" in "id_username" input
		And I type "Welcome1" in "id_password" input
		And I click "id_login_btn" button
		# Then the home page is diplayed


