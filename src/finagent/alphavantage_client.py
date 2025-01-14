import requests

class AlphaVantageClient:
    ALPHAVANTAGE_BASE_URL = "https://www.alphavantage.co/query"

    def __init__(self, api_key):
        self.api_key = api_key

    def call_alpha_vantage(self, function_name: str, params: dict) -> dict:
        query_params = params.copy()
        query_params["apikey"] = self.api_key
        alpha_function = function_name.replace("get_", "", 1).upper()

        if alpha_function is None:
            raise ValueError(f"No known alpha_vantage function mapping for: {function_name}")

        data_type = query_params.get("datatype", "json")  # either 'json' or 'csv'

        url = f"{self.ALPHAVANTAGE_BASE_URL}?function=" + alpha_function
        for key, value in query_params.items():
            url += f"&{key}={value}"
        print("URL:", url)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()
