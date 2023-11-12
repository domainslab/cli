from typing import List
import openai
from dotenv import dotenv_values

from .printer import Printer

GPT_4_MSG = f"Model gpt-4 is not available for provided API key. Reverting " \
            "to gpt-3.5-turbo. Sign up for the GPT-4 wait list here: " \
            "https://openai.com/waitlist/gpt-4-api\n"


# TODO: Add CLI option to provide TLDs
VALID_TLDS = [input('enter tlds')]


class AI:
    def __init__(self, temperature=0.1):
        self.printer = Printer('[ChatGPT]')
        self.temperature = temperature
        self.model = self.__get_model()
        config = dotenv_values('.env')
        self.api_key = config['OPEN_AI_API_KEY']

    def print(self, *args):
        return self.printer.print(*args)

    def next(self, desc: str, page_size=input('enter size number')) -> List[str]:
        prompt = ''
        with open("prompts/default", "r") as file:
            prompt = file.read()
            prompt = prompt.replace("{page_size}", str(page_size))
            prompt = prompt.replace("{desc}", desc)
            prompt = prompt.replace("{tlds}", ', '.join(VALID_TLDS))

        self.printer.print(f" Using prompt => {prompt}")
        response = openai.ChatCompletion.create(
            messages=[{"role": "user", "content": prompt}],
            model=self.model,
            temperature=self.temperature,
        )

        # TODO: Make sure content is a plain list of domain names
        # There could be a case it would return some explanation along the way
        content = response.choices[0].message.content
        return list(map(lambda item: item.split('. ')[-1], content.split('\n')))

    def __get_model(self) -> str:
        try:
            openai.Model.retrieve('gpt-4')
            return 'gpt-4'
        except openai.InvalidRequestError as _e:
            self.printer.print_warning(GPT_4_MSG)
            return "gpt-3.5-turbo"
