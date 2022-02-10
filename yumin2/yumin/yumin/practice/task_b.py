import os
from symtable import Symbol
import requests
import typing 

class GeckoDriver:
    ENDPOINT:str = "https://api.coingecko.com/api/v3/" # クラスのメンバ

    def __init__(self): # インスタンス化で呼ばれる
        pass

    def ping(self) ->typing.Tuple[str, dict]:
        """
        ping

        the endpoint is https://api.coingecko.com/api/v3/ping

        Returns
        -------
        tuple[requests.codes, dict]
            詰まるところ,APIレスポンスのステータスコードとJSONを返したい

        >>> driver = GeckoDriver()
        >>> status_code, res = driver.ping()
        >>> print(status_code)
        200
        >>> print(res)
        {...}
        

        """
        res = requests.get(os.path.join(self.ENDPOINT, "ping"))
        return res.status_code, res.json()

    def get_coins_list(self) -> typing.Tuple[str, dict]:
        """
        get_coins_list

        the endpoint is https://api.coingecko.com/api/v3/coins/list

        Returns
        -------
        tuple[requests.codes, dict]
            詰まるところ,APIレスポンスのステータスコードとJSONを返したい

        >>> driver = GeckoDriver()
        >>> status_code, res = driver.get_coins_list()
        >>> print(status_code)
        200
        >>> print(res)
        {...}
        """
        res = requests.get(os.path.join(self.ENDPOINT, "coins/list"))
        return res.status_code, res.json()

    def get_coins_symbol(self) -> typing.List[str]:
        """
        get_coins_symbol
            self.get_coins_listを呼び,そのJSONのidの部分だけ取り出すコードを書いてください．
            これはJSONに慣れるためです,

        Returns
        -------
        list[str]
            IDの部分だけ取り出してリストを返したい,

        >>> driver = GeckoDriver()
        >>> status_code, res = driver.ping()
        >>> print(status_code)
        200
        >>> print(res)
        ['01coin', 'zoc', '01coin', '0-5x-long-algorand-token', 'algohalf', ...]
        """
       # _, res = self.get_coins_list()
        
        status_code, res=self.get_coins_list()
        # _,res = self.get_coins_list() _にする理由：使わない変数なのでメモリ削減
        res_list=[coin["symbol"]  for coin in res]
        # 内包表記で上のが見やすくて速い　symbolはidと同じ
        # 辞書(coin)はこうやって書く
        return res_list
        # res_list=[]
        # for i in res:
        #     res_list.append(i['id'])
        # return res_list

driver = GeckoDriver()
res = driver.get_coins_symbol()
print(res)
