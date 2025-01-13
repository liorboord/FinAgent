import openai_client
import function_definitions
import alphavantage_client
import config
import json

class Agent:
    def __init__(self):
        openai_client_instructions = "You are a helpful assistant. You can call functions to get stock data when needed."
        self.openai_client = openai_client.OpenAIClient(config.OPENAI_API_KEY, openai_client_instructions)
        self.alphav_client = alphavantage_client.AlphaVantageClient(config.ALPHAV_API_KEY)
        self.functions = function_definitions.functions

    def run_conversation(self, user_input: str, functions: list = [], alpha_api_key: str = "demo"):
        first_response = self.openai_client.call_chatgpt(
            input_messages=user_input,
            functions= self.functions
        )

        first_message = first_response.choices[0].message

        if first_message.function_call is not None:
            function_name = first_message.function_call.name
            raw_args = first_message.function_call.arguments

            args = json.loads(raw_args)

            api_result = self.alphav_client.call_alpha_vantage(
                function_name=function_name,
                params=args
            )

            answer = self.openai_client.call_chatgpt_with_function_response(function_name, args, api_result, self.functions)
            assistant_answer = answer.choices[0].message.content
        else:
            assistant_answer = first_message.content
        
        return assistant_answer

    def main(self):
        print("Type 'quit' or 'exit' to stop.\n")

        while True:
            user_input = input("User: ")
            if user_input.strip().lower() in ("quit", "exit"):
                print("Goodbye!")
                break

            assistant_answer = self.run_conversation(
                user_input=user_input,
                functions=function_definitions.functions,
                alpha_api_key=config.ALPHAV_API_KEY
            )

            print("GPT:", assistant_answer, "\n")

if __name__ == "__main__":
    agent = Agent()
    agent.main()
