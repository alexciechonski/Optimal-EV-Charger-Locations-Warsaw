import requests
import json
import pandas as pd

class getStations:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_data(self):
        """returns a dataframe of closest 200 transformer stations to a specified coordinate point"""
        session_url = "https://m40.targeo.pl/TargeoLoader_1_7.html?gz=0&fx=&ln=&k=ODY2NzI1YjgzOWFlMWM4YjM5Zjc2N2U5MTAzNjY1Y2Q5MTE2ODA0NQ==&vn=2_5&v=full&f=ModulesInitialize&jq=&e=mapa-polski-targeo&m=1&elemsent=1"
        api_url = "https://m44.targeo.pl/service.html"

        res = {}
        counter = 1

        params = {
            "xhr": "1",
            "djson": "djson_1709163040015_5184459181087188",
            "rpc": "FTS",
            "q": "Trafostacja",
            "c": f'{{"x":{self.x}, "y":{self.y}}}',
            "z": "23",
            "querysource": "link",
            "area": '{"l":0, "t":0, "r":3768, "b":1188}',
            "mapbounds": f'{{"minX":{self.x-0.2957725}, "minY":{self.y-0.063519}, "maxX":{self.x+0.3510475}, "maxY":{self.y+0.065603}}}',
            "availarea": '{"t":35, "l":50, "b":1173, "r":3396}',
            "querytype": "OTHER",
            "crevgeo": "true",
            "mod": "fts",
            "suggesterCounter": "0",
            "suggester_index": "-1",
            "request_source": "mapa",
            "premium": "1",
            "_data": "{}",
            "tmk": "TargeoMap",
            "k": "ODY2NzI1YjgzOWFlMWM4YjM5Zjc2N2U5MTAzNjY1Y2Q5MTE2ODA0NQ==",
            "vn": "2_5",
            "uu": "f820ae2bd2ffd5bc10ed391484399fe5",
            "ln": "pl",
        }

        with requests.session() as s:
            t = s.get(session_url).text
            params["uu"] = s.cookies["U"]

            data = s.get(api_url, params=params).json()
            # print(data)
            for i in data["items"]["list"]["values"]:
                # print(i["xy"])
                res[counter] = i['xy']
                counter += 1
        
        df = pd.DataFrame(res)
        return df.transpose()
