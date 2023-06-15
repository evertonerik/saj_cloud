import requests,json

session = requests.Session()

login = {
    'lang': 'en',
    'username': 'liliana161270@gmail.com',
    'password': 'lili2305',
    'rememberMe': 'false',
}

session.post('https://fop.saj-electric.com/saj/login', data=login)

data = {
    'plantuid': 'A97D6A0C-4076-410D-885D-E2D20CB4706D',
    'clientDate': '2023-06-15'
}

plant_info = session.post(
    'https://fop.saj-electric.com/saj/monitor/site/getPlantDetailInfo',
    data=data,
)

#print(json.dumps(plant_info.json(), indent=1))

params = {
    'plantuid': 'A97D6A0C-4076-410D-885D-E2D20CB4706D',
    'chartDateType': '1',
    'energyType': '0',
    'clientDate': '2023-06-15',
    'deviceSnArr': 'R5X2602J2308E13612',
    'chartCountType': '2',
    'previousChartDay': '2023-06-14',
    'nextChartDay': '2023-06-16',
    'chartDay': '2023-06-15',
    'previousChartMonth': '2023-05',
    'nextChartMonth': '2023-07',
    'chartMonth': '2023-06',
    'previousChartYear': '2022',
    'nextChartYear': '2024',
    'chartYear': '2023',
}

plant_detail = session.get(
    'https://fop.saj-electric.com/saj/monitor/site/getPlantDetailChart2',
    params=params,
)

print(json.dumps(plant_detail.json(), indent=1))