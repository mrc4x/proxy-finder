import asyncio as a 
from proxybroker import Broker
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('PROXY FINDER'))
print("coded by merc4n.. :)")
print('>>> başlatıldı...')

async def show(pr):
    while True:
        sonuc = await pr.get()
        if sonuc is None:
            print(">>>>>>>>>>- işelem tamamlandı -<<<<<<<<<<")
        print('SONUC >>> %s' % sonuc)


pr = a.Queue() 

broker = Broker(pr)
işlem = a.gather(broker.find(types=['HTTP', 'CONNECT:80', 'SOCKS4', 'SOCKS5', 'HTTPS', 'SMTP'], limit=1000 ), show(pr))

döngü = a.get_event_loop()
döngü.run_until_complete(işlem)
print('>>> tamamlandı :)')