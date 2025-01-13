import function_definitions
import config
import openai
import json

class OpenAIClient:
    def __init__(self, api_key, instructions = ""):
        self.messages = []
        openai.api_key = api_key
        self.model="gpt-4"
        self.temperature=0.7
        self.max_tokens=1024
        self.top_p=1.0
        self.frequency_penalty=0.0
        self.presence_penalty=0.0
        self.function_call="auto"

        if instructions:
            self.messages.append({"role": "system", "content": instructions})

    def call_chatgpt(
        self,
        input_messages,
        role="user",
        functions=[]
    ):
        self.messages.append({"role": role, "content": input_messages})
        return self._do_call_gpt(self.messages, functions)
        
    def call_chatgpt_with_function_response(
            self, 
            function_name, 
            args, 
            api_result,
            functions
    ):
        self.messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": json.dumps(api_result)
            }
        )
        return self._do_call_gpt(self.messages,functions)
    
    def _do_call_gpt(self, messages, functions=None, function_call=None):
        response = openai.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            functions=functions,
            function_call=self.function_call
        )

        response_message = response.choices[0].message

        if response_message.function_call is None:   
            self.messages.append({"role": "assistant", "content": response_message.content})
        else:
            function_name = response_message.function_call.name
            raw_args = response_message.function_call.arguments

            messages.append({
                "role": "assistant",
                "content": None,
                "function_call": {
                    "name": function_name,
                    "arguments": json.dumps(json.loads(raw_args))
                },
            })
        
        return response

    
