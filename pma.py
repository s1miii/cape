import requests
class pma:
    def __init__(self, url):
        self.url = url
        self.path = ['/phpmyadmin/']
        self.user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        if '://' not in self.url:
            self.url = 'http://{}'.format(self.url)
        
        if self.url.endswith('/'):
            self.url = self.url[:-1]
    
    def check(self):
        back = False
        headers   = {
            'User-Agent': self.user_agent
        }
        for i in self.path:
            try:
                url = '{url}{path}'.format(url=self.url, path=i)
                get = requests.get(url, headers=headers, verify=False, allow_redirects=False, timeout=3)
                if '200' in str(get.status_code):
                    back = url
                    break
            except:
                pass
        return back