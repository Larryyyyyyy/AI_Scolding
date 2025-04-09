import os
import requests

messages = [{"role": "system", "content": "你们是网络喷子A和网络喷子B，你们要针对武汉大学和西安交通大学哪个好话题激情互骂，请你以较强的攻击性回复，最好贴近百度贴吧老哥的语气。"}]
messages.append({"role": "user", "content": "你现在是A，你先骂玩家B"})
def ds1 ():
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        "messages": messages,
        "stream": False, # 流式返回
        "max_tokens": 1024, # 最多返回的 token 数
        "temperature": 0.7, # 控制输出的随机性
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5, # 控制重复率
        "n": 1, # 生成几条回复
        "stop": None # 停止词
    }

    headers = {
        "Authorization": "Bearer sk-blzujfpayglpxjtruyvcecmgvwerwhdmvtzdcvtknplxymzg",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)

    content = response.json()["choices"][0]["message"]["content"]

    messages.append({"role": "user", "content": "A刚刚在贴吧发疯，说：\n{content}\nB你赶紧骂他！"})

    with open('ChatContent.txt', 'a', encoding='utf-8') as f:
        f.write("迪普: " + content + "\n----------------------------------------------------------------------------------------------------------------------\n")

def ds2():
    url = "https://api.siliconflow.cn/v1/chat/completions"

    payload = {
        "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        "messages": messages,
        "stream": False, # 流式返回
        "max_tokens": 1024, # 最多返回的 token 数
        "temperature": 0.7, # 控制输出的随机性
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5, # 控制重复率
        "n": 1, # 生成几条回复
        "stop": None # 停止词
    }

    headers = {
        "Authorization": "Bearer sk-blzujfpayglpxjtruyvcecmgvwerwhdmvtzdcvtknplxymzg",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)

    content = response.json()["choices"][0]["message"]["content"]

    messages.append({"role": "user", "content":"B刚刚在贴吧发癫，说：\n{content}\nA你赶紧骂他！"})

    with open('ChatContent.txt', 'a', encoding='utf-8') as f:
        f.write("西克: " + content + "\n----------------------------------------------------------------------------------------------------------------------\n")

for i in range(5):
    ds1()
    ds2()
    print("第",i+1,"轮对话结束")