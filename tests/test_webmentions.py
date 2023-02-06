import unittest
import webmentions as wm
import datetime


class MockSearchAdaptor(wm.SearchAdaptorBase):
    pass


class MyTestCase(unittest.TestCase):
    def test_webmentions(self):
        search_adaptor: MockSearchAdaptor = MockSearchAdaptor()
        results: wm.WebmentionCollection = wm.search(search_adaptor=search_adaptor)
        # !!!!!!!!! we were here !!!!!!!!!!
        metadata = {'query': 'query', 'time': datetime.datetime.strptime()}
        self.assertEqual(results, (metadata, df))  # add assertion here


if __name__ == '__main__':
    unittest.main()
