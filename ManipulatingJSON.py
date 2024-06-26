
  "id": "cmpl-7CTIdXA6C2rENhDBNHxHkynyYRWZS",
  "object": "text_completion",
  "created": 1683206919,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nThe goal of OpenAI is to advance digital intelligence in the way that is most likely to benefit humanity as a whole. OpenAI works to build safe artificial general intelligence (AGI) and ensure that AGI's benefits are as widely and equitably distributed as possible. OpenAI also works to research and develop friendly AI, which focuses on how to develop AI systems that align with human values and goals.",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 83,
    "total_tokens": 91
  }
}


# response is a Dictionary-Like Object: Based on the JSON structure you provided. It contains key-value pairs, with each key associated with a specific value.
# "model" is a Key in the Dictionary: The "model" key exists in the dictionary, and it holds a value, which is "text-davinci-003" in this case.
# Square Bracket Subsetting: In Python, you can access the value associated with a key in a dictionary using square bracket subsetting. By specifying response["model"], you are telling Python to retrieve the value associated with the key "model".

# Extract the model from the response:
print(response["model"])

# Extract the total_tokens from the response
print(response["usage"]["total_tokens"])

