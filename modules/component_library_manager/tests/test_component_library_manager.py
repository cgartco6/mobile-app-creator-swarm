import unittest
from component_library_manager import ComponentLibraryManager

class TestComponentLibraryManager(unittest.TestCase):
    def setUp(self):
        self.manager = ComponentLibraryManager(library_dir="test_lib")

    def test_add_and_get_component(self):
        self.manager.add_component("TestBtn", "code here", props=["onClick"])
        comp = self.manager.get_component("TestBtn")
        self.assertIsNotNone(comp)
        self.assertEqual(comp["name"], "TestBtn")

    def tearDown(self):
        import shutil
        shutil.rmtree("test_lib", ignore_errors=True)

if __name__ == '__main__':
    unittest.main()
