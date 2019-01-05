from . import Micro
import traceback

# open account
import uuid, random
from sqlalchemy import func
from sqlalchemy.sql import label
import sys

from .process import *


@Micro.typing('/api/trade/buy-sell/buy-coin')
@Micro.json
def buy_coin(account_no=None, status=None, symbol='BTC', side='', type='Buyer', time_in_force="Null",price='0',order_qty='0',fee='0',is_from_market_maker='false',target_order="false"):
    """received request from node Auth-api-trex => order buy coin 
    
    Arguments:
        account_no {[type]} -- [description]
    
    Keyword Arguments:
        account_no = Column(Integer, ForeignKey('users.id'))
        status = Column(String(1), nullable=False, default='0', index=True)
        symbol = Column(String(12), nullable=False)
        side = Column(String(1), nullable=False)
        type = Column(String(1), nullable=False, default='2')
        time_in_force = Column(String(1), nullable=False, default='1')
        price = Column(Integer, nullable=False, default=0)
        order_qty = Column(Integer, nullable=False)
        fee = Column(Integer, nullable=False, default=0)
        is_from_market_maker = Column(Boolean, default=False)
        target_order = string, orderID of target order, default =False
    Example json accept:
        {
            "account_no": "1122",
            "status": "Waiting Seller",
            "symbol": "BTC",
            "side": "Buyer",
            "type": "2",
            "time_in_force": 1,
            "price": "9000",
            "order_qty": "100",
            "fee": fee,
            "is_from_market_maker": false,
            "target_order": 1
        }
    """
    data={
        "account_no": account_no,
        "status": status,
        "symbol": symbol,
        "side": side,
        "type": type,
        "time_in_force": 1,
        "price": price,
        "order_qty": order_qty,
        "fee": fee,
        "is_from_market_maker": is_from_market_maker,
        "target_order": target_order
    }
    print(data)
    if(check_infor_request(data)):
        # fake server_pre_trade_id
        server_pre_trade_id = 1
        # processing 

        result = distributed_request_into_server(classify_by_account(server_pre_trade_id), data, 'buy-sell/process-buy-coin')
        if(result):
            return {
                "is_ok": True,
                "log":"buy_coin ok"
                }
        return {
            "is_ok": False,
            "log":"buy_coin fail"
            }
    else:
        return {
            "is_ok": False,
            "log":"data is incorrect"
        }
    

@Micro.typing('/api/trade/buy-sell/sell-coin')
@Micro.json
def sell_order(account_no=None, status=None, symbol='BTC', side='', type='Buyer', time_in_force="Null",price='0',order_qty='0',fee='0',is_from_market_maker='false',target_order="false"):
    data={
        "account_no": account_no,
        "status": status,
        "symbol": symbol,
        "side": side,
        "type": type,
        "time_in_force": 1,
        "price": price,
        "order_qty": order_qty,
        "fee": fee,
        "is_from_market_maker": is_from_market_maker,
        "target_order": target_order
    }
    print(data)
    # processing 

    if(check_infor_request(data)):
        # fake server_pre_trade_id
        server_pre_trade_id = 1
        # processing 

        result = distributed_request_into_server(classify_by_account(server_pre_trade_id), data, 'buy-sell/process-sell-coin')
        if(result):
            return {
                "is_ok": True,
                "log":"sell_coin ok"
            }
        return {
            "is_ok": False,
            "log":"sell_coin fail"
        }
    else:
        return {
            "is_ok": False,
            "log":"data is incorrect"
        }


@Micro.typing('/api/trade/buy-sell/cancel-order')
@Micro.json
def cancel_order(account_no=None, order_id= None, type_order="buy_sell",target_order="false"):
    data={
        "account_no": account_no,
        "order_id": order_id,
        "type_order": type_order,
        "target_order": target_order
    }
    print(data)
    # process

    if(check_infor_request(data)):
        # fake server_pre_trade_id
        server_pre_trade_id = 1
        # processing 

        distributed_request_into_server(classify_by_account(server_pre_trade_id), data, 'buy-sell/process-cancel-order')

        return {
            "log":"cancel ok"
        }
    else:
        return {
            "log":"data is incorrect"
        }
    

@Micro.typing('/api/trade/order-book/order-buy-coin')
@Micro.json
def order_buy_coin(account_no=None, status=None, symbol='BTC', side='', type='Buyer', time_in_force="Null",price='0',order_qty='0',fee='0',is_from_market_maker='false',target_order="false",username="Person"):
    data={
        "account_no": account_no,
        "status": status,
        "symbol": symbol,
        "side": side,
        "type": type,
        "time_in_force": 1,
        "price": price,
        "order_qty": order_qty,
        "fee": fee,
        "is_from_market_maker": is_from_market_maker,
        "target_order": target_order,
        "username":username
    }
    print(data)
    # processing 
    if(check_infor_request(data)):
        # fake server_pre_trade_id
        server_pre_trade_id = 1
        # processing 

        distributed_request_into_server(classify_by_account(server_pre_trade_id), data, 'order-book/process-order-buy-coin')

        return {
            "is_ok": True,
            "log":"Order Success!"
        }
    else:
        return {
            "is_ok": False,
            "log":"Order Fail!"
        }

@Micro.typing('api/trade/order-book/order-sell-coin')
@Micro.json
def order_sell_coin(account_no=None, status=None, symbol='BTC', side='', type='Buyer', time_in_force="Null",price='0',order_qty='0',fee='0',is_from_market_maker='false',target_order="false",username="Person"):
    data={
        "account_no": account_no,
        "status": status,
        "symbol": symbol,
        "side": side,
        "type": type,
        "time_in_force": 1,
        "price": price,
        "order_qty": order_qty,
        "fee": fee,
        "is_from_market_maker": is_from_market_maker,
        "target_order": target_order,
        "username":username
    }
    print(data)
    # processing 

    if(check_infor_request(data)):
        # fake server_pre_trade_id
        server_pre_trade_id = 1
        # processing 

        distributed_request_into_server(classify_by_account(server_pre_trade_id), data, 'order-book/process-order-sell-coin')

        return {
            "is_ok": True,
            "log":"Order Success!"
        }
    else:
        return {
            "is_ok": False,
            "log":"Order Fail!"
        }


@Micro.typing('/api/trade/order-book/cancel-order-book')
@Micro.json
def cancel_order_book(account_no=None, order_id= None, type_order="order",target_order="false"):
    
    data={
        "account_no": account_no,
        "order_id": order_id,
        "type_order": type_order,
        "target_order": target_order
    }
    print(data)
    # process
    if(check_infor_request(data)):
        # fake server_pre_trade_id
        server_pre_trade_id = 1
        # processing 

        distributed_request_into_server(classify_by_account(server_pre_trade_id), data, 'order-book/process-cancel-order-book')

        return {
            "log":"cancel order ok"
        }
    else:
        return {
            "log":"data is incorrect"
        }
