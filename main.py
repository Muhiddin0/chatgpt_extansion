import requests

class IELTSEssay:

    def __init__(self) -> None:
        self.prompt_template = """
You know everything about scoring IELTS essays. You assess the given essay of the given question and provide feedback to help the writer to improve in the future, and specify mistakes and suggest corrections.
Your output must be a JSON following this structure:
{"band": the band, "feedback": your feedback (maximum 100 words), "mistakes":[{"mistake": the whole sentence,"correction": a correction for that sentence]}

Question: $.quesh

Essay: $.essay

JSON:"""
        pass

    def check(self, prompt):

        self.prompt_template.replace('$.queshn', prompt['essay'])
        self.prompt_template.replace('$.essay', prompt['essay'])
        
        headers = {
            'authority': 'twitter.blueto.app:8443',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uz;q=0.6',
            'origin': 'http://127.0.0.1:5501',
            'referer': 'http://127.0.0.1:5501/',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }

        json_data = {
            'app': 'com.dominapp.supergpt',
            'deviceId': '4e2a3d23384a4dfc',
            'email': 'mkabraliev2005@gmail.com',
            'isPremiumUser': True,
            'isProUser': True,
            'page': 0,
            'proUserId': '',
            'proUserToken': '',
            'text': self.prompt_template,
            'token': '4e2a3d23384a4dfc',
        }

        response = requests.post('https://twitter.blueto.app:8443/cargpt/sendPrompt', headers=headers, json=json_data)

        print(response)
        print(response.json())


queshn = input('Queshn: ')
essay = input('Essay: ')

prompt = {
    'question':queshn,
    'essay':essay
}
IELTSEssay().check(prompt=prompt)