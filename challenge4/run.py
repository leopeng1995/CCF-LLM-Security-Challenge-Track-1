import os
import json
import argparse

from qwergpt.llm import TongyiLLM
from qwergpt.schema import Message
from qwergpt.prompt import Prompt
from qwergpt.utils import read_input_file

from constants import hijack_prompt_zh, hijack_prompt_en


def parse_args():
    parser = argparse.ArgumentParser(description='Run challenge with language selection')
    parser.add_argument('--lang', type=str, choices=['zh', 'en'], default='zh',
                       help='Language selection: zh (Chinese) or en (English)')
    return parser.parse_args()


def main():
    args = parse_args()

    llm = TongyiLLM()

    home_dir = os.path.dirname(__file__)
    dataset_dir = os.path.join(home_dir, '..', 'dataset')

    # 根据语言选择提示词和数据集
    dataset_path = os.path.join(dataset_dir, f'challenge4-{args.lang}.json')
    lines = read_input_file(dataset_path)

    hijack_prompt = hijack_prompt_zh if args.lang == 'zh' else hijack_prompt_en

    PROMPT_TEMPLATE = "{initial} {hijack} {target}"
    query_prompt = Prompt(PROMPT_TEMPLATE)

    def handle_line(line: str):
        data = json.loads(line)
        initial_prompt = data['initial_prompt']
        target_prompt = data['target_prompt']

        query = query_prompt.compose(
            initial=initial_prompt, 
            hijack=hijack_prompt,
            target=target_prompt
        )

        print('初始任务指令:')
        print(initial_prompt)

        print('目标任务指令:')
        print(target_prompt)

        messages = [
            Message(role='user', content=query)
        ]
        message = llm.complete(messages)
        print('大模型输出:')
        print(message.content)
        print('---------------------')

    for line in lines:
        handle_line(line)
        break


if __name__ == '__main__':
    main()
