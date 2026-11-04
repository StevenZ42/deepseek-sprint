import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
c = OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")
r = c.chat.completions.create(
    model="deepseek-flash",
    messages=[{"role": "user", "content": "用一句话解释什么是 KV Cache"}],
)
print(r.choices[0].message.content)
print(r.usage)
rc = getattr(r.choices[0].message, "reasoning_content", None)
print("有推理过程:", bool(rc), "字符数:", len(rc or ""))