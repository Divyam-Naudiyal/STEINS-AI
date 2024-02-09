import os
import openai
from configtest import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Write a email to my boss for resignation?"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
'''
{
  "id": "chatcmpl-8k3tq0xUFKf8vptmeoHD9YT1EuxEV",
  "object": "chat.completion",
  "created": 1705988770,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Subject: Formal Resignation - [Your Name]\n\nDear [Boss's Name],\n\nI hope this email finds you well. I am writing to formally tender my resignation from my position at [Company Name], effective [last working day, e.g., two weeks from now, or a specific date if agreed upon]. Please accept this email as my formal notice in accordance with the terms of my contract.\n\nIt is with mixed emotions that I make this decision. During my time at [Company Name], I have had the opportunity to work with some incredibly talented individuals and engage in meaningful projects. The professional growth and personal development gained in this role has been invaluable, and I am grateful for the opportunities I have been provided.\n\nHowever, after careful consideration and evaluation of my career goals, I have decided to pursue a new endeavor, which aligns more closely with my long-term aspirations. This decision has not been made lightly, and I assure you that I have given it considerable thought.\n\nTo ensure a smooth transition, I am committed to completing any pending projects and ensuring that all my responsibilities are properly handed over to a suitable replacement. I am open to discussion regarding a reasonable transition plan, and I am more than willing to offer support during the transition period. Please let me know how I can"
      },
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 16,
    "completion_tokens": 256,
    "total_tokens": 272
  },
  "system_fingerprint": null
}
'''