<?php

error_reporting(0);

# Name     : Unlimited Reverse IP
# Vendor   : Zerobyte.ID
# Coded by : @Cepotdotid
# Issued June 29th, 2021
# Tested on Ubuntu 20.04.1 LTS
# Recoded? only changed and delete copyright? Don't be a bastardd dude!

Class ReverseIP
{
    
    public function __construct()
    {
        $this->Banner();
        $this->MASK();
        $this->Rev();
    }
    
    public function color($color = "random", $text)
    {
        if (true == true) {
            $arrayColor = array(
                'grey' => '1;30',
                'red' => '1;31',
                'green' => '1;32',
                'yellow' => '1;33',
                'blue' => '1;34',
                'purple' => '1;35',
                'nevy' => '1;36',
                'white' => '1;1',
                'bgred' => '1;41',
                'bggreen' => '1;42',
                'bgyellow' => '1;43',
                'bgblue' => '1;44',
                'bgpurple' => '1;45',
                'bgnavy' => '1;46',
                'bgwhite' => '1;47'
            );
            if ($color == 'random') {
                $arrayColor         = array(
                    'red' => '1;31',
                    'green' => '1;32',
                    'yellow' => '1;33',
                    'nevy' => '1;36',
                    'white' => '1;1'
                );
                $arrayColor[$color] = $arrayColor[array_rand($arrayColor)];
                $res .= "\033[" . $arrayColor[$color] . "m" . $text . "\033[0m";
                
            } else if ($color == 'string') {
                $arrayColor = array(
                    'grey' => '1;30',
                    'red' => '1;31',
                    'green' => '1;32',
                    'yellow' => '1;33',
                    'blue' => '1;34',
                    'purple' => '1;35',
                    'nevy' => '1;36',
                    'white' => '1;1'
                );
                foreach (str_split($text) as $key => $value) {
                    $arrayColor[$color] = $arrayColor[array_rand($arrayColor)];
                    $res .= "\033[" . $arrayColor[$color] . "m" . $value . "\033[0m";
                }
                
            } else {
                
                $res .= "\033[" . $arrayColor[$color] . "m" . $text . "\033[0m";
                
            }
            return $res;
        } else {
            return $text;
        }
        
    }

    public function RemoveSubdomain($urls)
    {
        $url = "http://";
        $url .= $urls;
        $pieces = parse_url($url);
        $domain = isset($pieces['host']) ? $pieces['host'] : '';
        if (preg_match('/(?P<domain>[a-z0-9][a-z0-9\-]{1,63}\.[a-z\.]{2,6})$/i', $domain, $regs))
        {
            return $regs['domain'];
        }
        return false;
    }

    public function Banner()
    {
        echo "
        _..._
      .'     '.      _  
     /    .-\"\"-\   _/ \  ┌──────────────────────────────────────────────┐
  .-|   /:.    |  |   |  │  HELLO," . $this->color("green", " Zerobyte.ID") . " Wuz here!                │
  |  \  |:.    /.-'-./   │  Dont forget, still autis on cyberspace!     │
  | .-'-;:__ .'    =/    │                                              │
  .'=  *=|     _.='      │  " . $this->color("green", "© Zerobyte.ID 2021 All rights reserved. ") . "    │ 
  /   _.  |    ;         └──────────────────────────────────────────────┘
 ;-.-'|    \   |
/   | \    _\  _\
\__/'._;.  ==' ==\
         \    \   |
         /    /   /
         /-._/-._/
         \   `\  \
          `-._/._/ " . PHP_EOL . PHP_EOL;
        $this->iplist = readline("# Enter ur IP list => ");
        if (!file_exists($this->iplist))
            die("file " . $this->color("red", $this->iplist) . " not available!" . PHP_EOL);
        $this->list = preg_split('/\r\n|\r|\n/', file_get_contents($this->iplist));
        system('clear');
    }
    
    public function MASK()
    {
        echo "┌─────────────────────────┬───────────────────────────┬────────────────────────────┐
│     " . $this->color("blue", "MASK") . " 30 = " . $this->color("green", "4") . "  IP     │     " . $this->color("blue", "MASK") . " 25 = " . $this->color("green", "127") . "  IP     │     " . $this->color("blue", "MASK") . " 20 = " . $this->color("green", "4061") . "  IP     │
│     " . $this->color("blue", "MASK") . " 29 = " . $this->color("green", "8") . "  IP     │     " . $this->color("blue", "MASK") . " 24 = " . $this->color("green", "253") . "  IP     │     " . $this->color("blue", "MASK") . " 19 = " . $this->color("green", "8116") . "  IP     │
│     " . $this->color("blue", "MASK") . " 28 = " . $this->color("green", "16") . " IP     │     " . $this->color("blue", "MASK") . " 23 = " . $this->color("green", "506") . "  IP     │     " . $this->color("blue", "MASK") . " 18 = " . $this->color("green", "16244") . " IP     │
│     " . $this->color("blue", "MASK") . " 27 = " . $this->color("green", "32") . " IP     │     " . $this->color("blue", "MASK") . " 22 = " . $this->color("green", "1016") . " IP     │     " . $this->color("blue", "MASK") . " 17 = " . $this->color("green", "32411") . " IP     │
│     " . $this->color("blue", "MASK") . " 26 = " . $this->color("green", "64") . " IP     │     " . $this->color("blue", "MASK") . " 21 = " . $this->color("green", "2036") . " IP     │     " . $this->color("blue", "MASK") . " 16 = " . $this->color("green", "49802") . " IP     │" . PHP_EOL . "├─────────────────────────┴───────────────────────────┴────────────────────────────┤" . PHP_EOL;
        echo "│    NOTE: [ " . $this->color("red", "the bigger number you choosing will take more time per request !") . "]     │" . PHP_EOL;
        echo "└──────────────────────────────────────────────────────────────────────────────────┘" . PHP_EOL;
        $this->mask = readline("# Enter ur MASK => ");
        if ($this->mask > 30 || $this->mask < 16) {
            die(PHP_EOL . $this->color("red", "the number option you put is incorrect!") . PHP_EOL . PHP_EOL);
        }
    }
    
    public function Rev()
    {
        foreach ($this->list as $key => $ip) {
            
            $ch = curl_init();
            
            curl_setopt($ch, CURLOPT_URL, "https://omnisint.io/reverse-dns-lookup/" . $ip . "/" . $this->mask);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
            
            curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');
            
            $headers   = array();
            $headers[] = 'Authority: sonar.omnisint.io';
            $headers[] = 'Cache-Control: max-age=0';
            $headers[] = 'Connection: keep-alive';
            $headers[] = 'Sec-Ch-Ua: \"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"';
            $headers[] = 'Sec-Ch-Ua-Mobile: ?0';
            $headers[] = 'Upgrade-Insecure-Requests: 1';
            $headers[] = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36';
            $headers[] = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9';
            $headers[] = 'Sec-Fetch-Site: none';
            $headers[] = 'Sec-Fetch-Mode: navigate';
            $headers[] = 'Sec-Fetch-User: ?1';
            $headers[] = 'Sec-Fetch-Dest: document';
            $headers[] = 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8';
            $headers[] = 'Cookie: _ga=GA1.2.1243590311.1615035294; _gid=GA1.2.1342632335.1615035294';
            curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
            
            $result = curl_exec($ch);
            if (preg_match('/"Message": "invalid CIDR address:/', $result)) {
                echo "IP => " . $this->color("green", $ip) . $this->color("red", " INVALID!") . " => [ " . $this->color("red", "0"). " DOMAIN ] REASON: ". $this->color("red", "invalid CIDR address") . ": ".$ip."/".$this->mask.PHP_EOL;
            } else {
                $grabbed = json_decode($result, true);
            }
            foreach ($grabbed as $key => $value) {
                if (count($value) > 10) {
                    echo PHP_EOL . "FROM IP " . $this->color("green", $ip) . " RANGE TO IP " . $this->color("green", $key) . " SUCCESS! => [ " . $this->color("green", count($value)) . " DOMAIN ] |" . $this->color("yellow", " Zerobyte.ID REVERSE IP");
                }
            foreach ($value as $save)
                {
                    $delete = $this->RemoveSubdomain($save) . PHP_EOL;
                    $save = @fopen(".tmp", "a+");
                    fwrite($save, $delete . "\n");
                    fclose($save);
                }
            }
        }
    }
    
    public function __destruct()
    {
        if ($this->mask > 30 || $this->mask < 16) {
            die();
        }
        echo "Please wait. delete duplicate line!".PHP_EOL;
        sleep(5);
        $lines = file(".tmp");
        $lines = array_unique($lines);
        
        $file = fopen("ZB-REV.txt", "a+");
        fwrite($file, implode("", $lines));
        fclose($file);
        unlink('.tmp');
        echo "All Done! you got ".$this->color("green", count(file('ZB-REV.txt'))). " Domain list".PHP_EOL;
    }
}

$ini = new ReverseIP();
$ini->Rev();
