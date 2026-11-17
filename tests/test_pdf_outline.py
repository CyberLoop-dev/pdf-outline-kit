import unittest
from pdf_outline import flatten_outline,to_markdown

class Destination:
    def __init__(self,title): self.title=title

class OutlineTests(unittest.TestCase):
    def test_nested_outline_and_one_based_pages(self):
        top=Destination("Start"); child=Destination("Setup")
        result=flatten_outline([top,[child]],lambda item: 0 if item is top else 3)
        self.assertEqual(result[0]["page"],1)
        self.assertEqual(result[1]["depth"],1)
        self.assertEqual(result[1]["page"],4)

    def test_markdown_output(self):
        text=to_markdown([{"title":"Intro","page":2,"depth":0}],"Guide")
        self.assertIn("- Intro (p. 2)",text)

if __name__=="__main__": unittest.main()
