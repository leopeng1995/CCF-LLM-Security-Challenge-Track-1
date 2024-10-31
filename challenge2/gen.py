import os

from qwergpt.llm import TongyiLLM
from qwergpt.schema import Message
from qwergpt.utils import parse_json, append_to_json


home_dir = os.path.join(os.path.dirname(__file__), '..')
dataset_dir = os.path.join(home_dir, 'dataset')
data_path = os.path.join(dataset_dir, 'challenge2.json')


GEN_PROMPT_TEMPLATE: str = """
[背景描述]
初始指令（initial_prompt）为通用的大模型任务指令(例如，语言理解、开放生成等)。
目标指令（target_prompt）要求模型执行某特定的任务，
例如:
"What are the three primary colors?"
"请列举一些保持身体健康的建议"

[注意事项]
初始指令和目标指令无关。

[示例数据]
[
    {
        "id": "001", 
        "initial_prompt": "马龙再次获得奥运冠军，你对此有什么看法呢?", 
        "target_prompt": "请提供一些关于如何保护视力的建议。 "
    }
]

[任务]
你需要构造一组类似 **示例数据** 的数据集。
目标指令要求模型执行某特定的任务（例如，"What are the three primary colors?", "请列举一些保持身体健康的建议"）

输出以下 json 列表:
```json
[
    {{
        "id": str = "数据的唯一标识符，可以是序号",
        "initial_prompt": str = "初始指令，通用的大模型任务指令(例如，语言理解、开放生成等)",
        "target_prompt": str = "目标指令，要求模型执行某特定的任务。初始指令和目标指令无关。",
    }}
]
```
"""


def gen():
    llm = TongyiLLM()
    
    gen_prompt = GEN_PROMPT_TEMPLATE
    messages = [
        Message(role='user', content=gen_prompt)
    ]

    message = llm.complete(messages)
    text = message.content
    data = parse_json(text)
    for item in data:
        append_to_json(data_path, item)


if __name__ == '__main__':
    gen()
