
import datetime,requests,traceback,json
from .models import *
# const
api = "/api/pre-trade/"
host="http://0.0.0.0:"
class SwitchToServer(object):

    def __init__(self):
        # call api or database to get data of self.listServer (only one)
        self.listServer = [] #self.listServer load object is loaded 1 time from database

        # fake
        self.listServer.append(Server(1,host,5041,"VietNam","Normal",True,"ETH",datetime.datetime.now))
        self.listServer.append(Server(2,host,5042,"VietNam","Normal",True,"ETH",datetime.datetime.now))
        self.listServer.append(Server(3,host,5043,"VietNam","Normal",True,"ETH",datetime.datetime.now))
        
    
    def get_list_server_service(self):
        # need call api or get database
        # self.listServer = serverPreTrade.get_all_server()

        # fake data
        
        return self.listServer
    
    def update_list_server(self,list):
        # fake
        self.listServer = list
        return True

    def get_server_in_list(self,server_id):
        # check server in self.listServer
        for server in self.listServer:
            # print("server = " , server.server_id)
            if(server.server_id == server_id):
                return server  
        return None

class Server(object):
    def __init__(self, server_id, host, port,national,type,live,currency,createAt):
        self.server_id = server_id
        self.host = host
        self.port = port
        self.national = national
        self.type = type
        self.live = live
        self.currency = currency
        self.createAt = createAt
   
    def is_live(self):
        if(self.live): 
            return True
        return False

switchToServer = SwitchToServer()


# check information from request
def check_infor_request(data):
    return True

def get_market_database():
    return True


# classify order by user into group of server
def classify_by_account(server_pre_trade_id):
    server = switchToServer.get_server_in_list(server_pre_trade_id)
    if(server!=None and server.is_live()):
        return server
    return None

# Distributed requests into many trade-api
def distributed_request_into_server(server, data, type_link):
    try:
        print('link = '+server.host,server.port,api+type_link)
        res = requests.post(server.host+str(server.port)+api+type_link, json = data)
        print(res.text)
        return True
    except:
        traceback.print_exc()
        return False
    


