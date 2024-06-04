import requests
import json 

def get_resp():
    cookies = {
        '_gcl_au': '1.1.370638235.1709837911',
        '_fbp': 'fb.1.1709837910805.1432773877',
        '_hjSessionUser_1484802': 'eyJpZCI6ImViNjliYzAyLTA1NTItNTBiYy05MjNlLTM3MTNjYTY0NTFkNCIsImNyZWF0ZWQiOjE3MDk4Mzc5MTA4NDYsImV4aXN0aW5nIjp0cnVlfQ==',
        'didomi_token': 'eyJ1c2VyX2lkIjoiMThlMmU1MmQtOTViOS02Y2EwLTk2YTctNjhiNmNlOTA1OWM5IiwiY3JlYXRlZCI6IjIwMjQtMDMtMTFUMTY6MjI6NDUuMzM5WiIsInVwZGF0ZWQiOiIyMDI0LTA1LTE0VDEwOjAzOjA3LjU3NFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiYzpzZW50cnkiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiIsImM6Z29vZ2xlYWRzLU03anpMMnlkIiwiYzptaXhwYW5lbC1iV0x5YmhOVSIsImM6ZmFjZWJvb2tjLWM4SGhpenFhIiwiYzptaWNyb3NvZnQtYnhqUXFpaWYiLCJjOmZhY2Vib29rcy1jOXlnQU14ayIsImdvb2dsZSJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJwcm9jZXNzZXNfYW5kX2Vuc3VyZXNfYmFua2luZ190cmFuc2FjdGlvbl9zZWN1cml0eSIsInByb3RlY3RzX2FnYWluc3Rfb25saW5lX3RocmVhdHNfYW5kX2VuaGFuY2VzX3JlbGlhYmlsaXR5IiwicHJldmVudF91c2Vfb2ZfZm9ybXNfYnlfdW5xdWFsaWZpZWRfdXNlcnMiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiYzpnb29nbGVtYXAtamlGalFhZUEiLCJjOnN0cmlwZXBheS1EWmZ6WlBDYSIsImM6aW5zaWRlcndlLURNajlIRkhKIiwiYzpjbG91ZGZsYXJlLVFLN2ZMeHJCIiwiYzpnb29nbGVyZWMtTFhQbkdGNk4iLCJnb29nbGUiXX0sInB1cnBvc2VzX2xpIjp7ImVuYWJsZWQiOlsiZ2VvbG9jYXRpb25fZGF0YSIsInByb2Nlc3Nlc19hbmRfZW5zdXJlc19iYW5raW5nX3RyYW5zYWN0aW9uX3NlY3VyaXR5IiwicHJvdGVjdHNfYWdhaW5zdF9vbmxpbmVfdGhyZWF0c19hbmRfZW5oYW5jZXNfcmVsaWFiaWxpdHkiLCJwcmV2ZW50X3VzZV9vZl9mb3Jtc19ieV91bnF1YWxpZmllZF91c2VycyJdfSwidmVyc2lvbiI6Mn0=',
        'euconsent-v2': 'CP7Tt8AP-mp8AAHABBENAzEkAP_AAELgAAAAF5wAQF5gXnABAXmAAAAA.f_gACFwAAAAA',
        'predis': 'faca57aec111e567d04fbe0f0f823308f7ee6226~session-06c08c088933982d238a3aa1b3d3d47d',
        'session': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MTY5MDY5OTAsImV4cCI6MTcxNjkxNDE5MCwiY2xpZW50X2lkIjoxOH0.lPs1D23_ddkld8bZgqWw-GrA8ugTQY8slOhWwJHA16_p9bzyNfxR3OOF_ljAD6FjOYfllxFfoPv5BTAijMmRUIq1HSp8HUgj80TIpdme1lky3O2S6V49dHiFGUE0vWWlBrgo_Ff93zwmlNp-77ijJZcYV4-BxDossa4XPXiVh-Af2RBby_NN8K-JnyXPu4gwnRwnpTbNzwyR6DPco6_vPRGl3pM5SRpIkhvn7-Vx2sQpyP39q6JMZUBml3dEXZ0h2As_NEorx57p5yZ-SIC-FBJHG7DlYmA_nLkY5HCZVXsug4-VwQ2UMzyeKw84L2w1lz8XQVUpz34MrtaCA7fuhB_WhdtPgP7MQJjthnWbaeWhHqUPK41I5tspTDeKnCYR1MTND30D0QNJPuCb4CErxEDuJthTM2ycLiiIx0h_YlIm6QZE0F2DVacdtS27njXDsHGuhvzCGV6HhI2V0OQRPsLGPCpvNLFB6lmt5mELOx71hgl-oSQvXbWAbCb05qRHjjRndR8wTDFFBxXxXXIWqjf82_g4gT9hha_s4Uu0Xj5KeTz3V77DRnapmRBt819V9qi2vSKBi9AoXOrMb3Dq8kzqI-HZlBBb1OSwrn55MlpvivxfLKRVsHuKA4tI3PEJfPRzV7758TFq3CADv5A-dHdGhlrkEFerAcFqOMbwFTo',
        '_gid': 'GA1.2.2020450051.1716906992',
        '_clck': '8m2kye%7C2%7Cfm5%7C0%7C1527',
        '_hjSession_1484802': 'eyJpZCI6IjBjMjcyY2UwLTljNDgtNDBkMC1hMmJmLTlkNjg3ZTNhYWJmMSIsImMiOjE3MTY5MDY5OTQ1NDcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
        'mp_f2064d7940f793a1cc5fdeada3099825_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18e1a48021d3c4-05a5fe7c067a74-1d525637-13c680-18e1a48021d3c4%22%2C%22%24device_id%22%3A%20%2218e1a48021d3c4-05a5fe7c067a74-1d525637-13c680-18e1a48021d3c4%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
        '_ga': 'GA1.1.725817014.1709837911',
        '_clsk': '65axv7%7C1716907031825%7C2%7C1%7Cz.clarity.ms%2Fcollect',
        '_ga_M62J0E1SG8': 'GS1.1.1716906991.5.1.1716907039.12.0.0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.370638235.1709837911; _fbp=fb.1.1709837910805.1432773877; _hjSessionUser_1484802=eyJpZCI6ImViNjliYzAyLTA1NTItNTBiYy05MjNlLTM3MTNjYTY0NTFkNCIsImNyZWF0ZWQiOjE3MDk4Mzc5MTA4NDYsImV4aXN0aW5nIjp0cnVlfQ==; didomi_token=eyJ1c2VyX2lkIjoiMThlMmU1MmQtOTViOS02Y2EwLTk2YTctNjhiNmNlOTA1OWM5IiwiY3JlYXRlZCI6IjIwMjQtMDMtMTFUMTY6MjI6NDUuMzM5WiIsInVwZGF0ZWQiOiIyMDI0LTA1LTE0VDEwOjAzOjA3LjU3NFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiYzpzZW50cnkiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiIsImM6Z29vZ2xlYWRzLU03anpMMnlkIiwiYzptaXhwYW5lbC1iV0x5YmhOVSIsImM6ZmFjZWJvb2tjLWM4SGhpenFhIiwiYzptaWNyb3NvZnQtYnhqUXFpaWYiLCJjOmZhY2Vib29rcy1jOXlnQU14ayIsImdvb2dsZSJdfSwicHVycG9zZXMiOnsiZW5hYmxlZCI6WyJwcm9jZXNzZXNfYW5kX2Vuc3VyZXNfYmFua2luZ190cmFuc2FjdGlvbl9zZWN1cml0eSIsInByb3RlY3RzX2FnYWluc3Rfb25saW5lX3RocmVhdHNfYW5kX2VuaGFuY2VzX3JlbGlhYmlsaXR5IiwicHJldmVudF91c2Vfb2ZfZm9ybXNfYnlfdW5xdWFsaWZpZWRfdXNlcnMiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiYzpnb29nbGVtYXAtamlGalFhZUEiLCJjOnN0cmlwZXBheS1EWmZ6WlBDYSIsImM6aW5zaWRlcndlLURNajlIRkhKIiwiYzpjbG91ZGZsYXJlLVFLN2ZMeHJCIiwiYzpnb29nbGVyZWMtTFhQbkdGNk4iLCJnb29nbGUiXX0sInB1cnBvc2VzX2xpIjp7ImVuYWJsZWQiOlsiZ2VvbG9jYXRpb25fZGF0YSIsInByb2Nlc3Nlc19hbmRfZW5zdXJlc19iYW5raW5nX3RyYW5zYWN0aW9uX3NlY3VyaXR5IiwicHJvdGVjdHNfYWdhaW5zdF9vbmxpbmVfdGhyZWF0c19hbmRfZW5oYW5jZXNfcmVsaWFiaWxpdHkiLCJwcmV2ZW50X3VzZV9vZl9mb3Jtc19ieV91bnF1YWxpZmllZF91c2VycyJdfSwidmVyc2lvbiI6Mn0=; euconsent-v2=CP7Tt8AP-mp8AAHABBENAzEkAP_AAELgAAAAF5wAQF5gXnABAXmAAAAA.f_gACFwAAAAA; predis=faca57aec111e567d04fbe0f0f823308f7ee6226~session-06c08c088933982d238a3aa1b3d3d47d; session=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MTY5MDY5OTAsImV4cCI6MTcxNjkxNDE5MCwiY2xpZW50X2lkIjoxOH0.lPs1D23_ddkld8bZgqWw-GrA8ugTQY8slOhWwJHA16_p9bzyNfxR3OOF_ljAD6FjOYfllxFfoPv5BTAijMmRUIq1HSp8HUgj80TIpdme1lky3O2S6V49dHiFGUE0vWWlBrgo_Ff93zwmlNp-77ijJZcYV4-BxDossa4XPXiVh-Af2RBby_NN8K-JnyXPu4gwnRwnpTbNzwyR6DPco6_vPRGl3pM5SRpIkhvn7-Vx2sQpyP39q6JMZUBml3dEXZ0h2As_NEorx57p5yZ-SIC-FBJHG7DlYmA_nLkY5HCZVXsug4-VwQ2UMzyeKw84L2w1lz8XQVUpz34MrtaCA7fuhB_WhdtPgP7MQJjthnWbaeWhHqUPK41I5tspTDeKnCYR1MTND30D0QNJPuCb4CErxEDuJthTM2ycLiiIx0h_YlIm6QZE0F2DVacdtS27njXDsHGuhvzCGV6HhI2V0OQRPsLGPCpvNLFB6lmt5mELOx71hgl-oSQvXbWAbCb05qRHjjRndR8wTDFFBxXxXXIWqjf82_g4gT9hha_s4Uu0Xj5KeTz3V77DRnapmRBt819V9qi2vSKBi9AoXOrMb3Dq8kzqI-HZlBBb1OSwrn55MlpvivxfLKRVsHuKA4tI3PEJfPRzV7758TFq3CADv5A-dHdGhlrkEFerAcFqOMbwFTo; _gid=GA1.2.2020450051.1716906992; _clck=8m2kye%7C2%7Cfm5%7C0%7C1527; _hjSession_1484802=eyJpZCI6IjBjMjcyY2UwLTljNDgtNDBkMC1hMmJmLTlkNjg3ZTNhYWJmMSIsImMiOjE3MTY5MDY5OTQ1NDcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; mp_f2064d7940f793a1cc5fdeada3099825_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18e1a48021d3c4-05a5fe7c067a74-1d525637-13c680-18e1a48021d3c4%22%2C%22%24device_id%22%3A%20%2218e1a48021d3c4-05a5fe7c067a74-1d525637-13c680-18e1a48021d3c4%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga=GA1.1.725817014.1709837911; _clsk=65axv7%7C1716907031825%7C2%7C1%7Cz.clarity.ms%2Fcollect; _ga_M62J0E1SG8=GS1.1.1716906991.5.1.1716907039.12.0.0',
        'origin': 'https://chargemap.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://chargemap.com/cities/warszawa-PL',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
    'city': 'Warszawa',
    'NELat': '52.33764663',
    'NELng': '21.17099762',
    'SWLat': '52.25365796',
    'SWLng': '20.92723846',
    'zoom': '12',
    }


    response = requests.post('https://chargemap.com/json/charging/pools/get_from_areas', cookies=cookies, headers=headers, data=data)
    return response

def parse_response(response):
    chargers = {i+1:{'lat':response.json()['items'][i]['lat'], 'lon':response.json()['items'][i]['lng']} for i in range(len(response.json()['items']))}
    return chargers

def run():
    resp = get_resp()
    chargers = parse_response(resp)
    with open('chargers7.json','w') as f:
        json.dump(chargers, f , indent=2)

run()

