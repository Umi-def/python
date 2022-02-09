import os

import requests


class GeckoDriver:
    ENDPOINT: str = "https://api.coingecko.com/api/v3"

    def __init__(self):
        pass

    def ping(self) -> tuple[requests.codes, dict]:
        """
        ping

        the endpoint is `https://api.coingecko.com/api/v3/ping`

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

        Personのデータコレクションを返す
        public class Person
            {
            public int Id { get; set; }
            public string Name { get; set; }
            }

        public class PersonsController : ApiController
            {
                public IEnumerable<Person> Get()
                {
                    var list = new List<Person>()
                    {
                        new Person() { Id = 1, Name = "taro" },
                        new Person() { Id = 2, Name = "hanako" }
                    };
                    return list;
                }
            }
        objectがたを返す
        public object Get()
            {
            string[] members = new string[] {"taro", "hanako"};
            return new { name = "groupA", members = members };
            }

        """
        res = requests.get(os.path.join(self.ENDPOINT, "ping"))
        return res.status_code, res.json()

    def get_coins_list(self) -> tuple[requests.codes, dict]:
        """
        get_coins_list

        the endpoint is `https://api.coingecko.com/api/v3/coins/list`

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

    def get_coins_symbol(self) -> list[str]:
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
        
        public Customer GetCustomer(int id)
            {
                // Customersテーブルから、idが一致するデータを取得
                Customer customer = db.Customers.Find(id);
                if (customer == null)
                    {
                        // 一致するデータ存在しない場合は、ステータス・コード404を返す
                        throw new HttpResponseException(Request.CreateResponse(HttpStatusCode.NotFound)); // ……（1）
                    }
                // Customerデータを返す
                return customer;
            }
        
        
        
        """
