import unittest
from searcher import Searcher


class MyTestCase(unittest.TestCase):
    def test_something(self):
        mySearcher = Searcher(
            "https://www.gosh.nhs.uk",
            "ef99b91a0209431cb66dd4d32a0b20c6"
        )
        search_term = "location of GOSH"

        mySearcher.search(search_term, 10)
        print("Q: " + search_term)
        print("A: ")
        for r in mySearcher.get_search_results(3):
            print(r)
        mySearcher.save_search_result()
        assert True


if __name__ == '__main__':
    unittest.main()
