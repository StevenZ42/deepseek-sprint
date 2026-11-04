## 2026-11-04 · M1 第一次基线
- 做了什么：跑通 deepseek-flash 调用
- 观察到什么：打印了 usage(prompt_tokens=36, completion_tokens=77, total_tokens=113, prompt_cache_hit_tokens=0，cost=$0.0000516)
- 一个反例：如果把 .env 里的 key 删掉，会报 AuthenticationError 401
- 一句话结论：环境配好了，API 能跑通。模型默认开启了思考模式，产生了 44 个 reasoning_tokens。
- 没懂的地方：暂无