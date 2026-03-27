from httpx import AsyncClient
from Validator import LanguageEnum

class AIService:
    def __init__(self,client:AsyncClient, token:str, API_URL:str):
        self.client = client
        self.token = token
        self.API_URL = API_URL

    def clean_ai_answer(self, text: str):
        if "</think>" in text:
            text = text.split("</think>")[-1]
        return text.strip()
    async def send_request(self,feed_text:str,country_code:LanguageEnum):
        response = {
            "model": "deepseek-ai/DeepSeek-R1:fastest",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "Ты анализируешь отзывы о товаре и пишешь краткую характеристику товара. "
                        "Отвечай только итоговым ответом. "
                        "Не пиши объяснения. "
                        "Не пиши рассуждения. "
                        "Не используй <think>. "
                        "Не упоминай отзывы. "
                        "Разложеный ответ."
                        "Вывод в конце."
                        f"Напиши ответ на {country_code}."
                    )
                },
                {
                    "role": "user",
                    "content": f"Отзывы:\n{feed_text}"
                }
            ]
        }
        response = await self.client.post(self.API_URL, headers={"Authorization": f"Bearer {self.token}",}, json=response)
        result = response.json()["choices"][0]["message"]["content"]
        return {"Response":self.clean_ai_answer(result)}


