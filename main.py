from searcher import Searcher

mySearcher = Searcher(
    input("Site: "),
    "ef99b91a0209431cb66dd4d32a0b20c6"
)

while(True):
    mySearcher.search(input("Q: "), 3)
    result = mySearcher.get_search_results()[0]
    print("A: You might find this page helpful")
    print(result["name"])
    print("source: " + result["url"])
    print("context: " + result["snippet"])
    mySearcher.save_search_result()
