import requests
import json


class Searcher:

    def __init__(self, search_site, subscription_key):
        self.search_results = None
        self.subscription_key = subscription_key
        self.endpoint_url = "https://api.bing.microsoft.com/v7.0/search"
        self.search_site = search_site

    def search(self, search_term, search_count=1):
        query = search_term + "site:" + self.search_site

        headers = {"Ocp-Apim-Subscription-Key": self.subscription_key}
        params = {
            "q": query,
            "textDecorations": False,
            "textFormat": "RAW",
            "count": search_count,
            "safeSearch": "Moderate"
        }
        response = requests.get(self.endpoint_url, headers=headers, params=params)
        response.raise_for_status()
        self.search_results = response.json()
        return "success"

    def get_top_search_result_snippet(self):
        return self.search_results["webPages"]["value"][0]["snippet"]

    def get_search_results(self, count=1):
        results = self.search_results["webPages"]["value"][:count]
        # results = map(lambda r: {
        #     "name": r["name"],
        #     "url": r["url"],
        #     "snippet": r["snippet"]
        # }, results)
        return results

    def save_search_result(self, location="result.json"):
        with open(location, "w") as outfile:
            json.dump(self.search_results, outfile)
