#!/usr/bin/env python3
import unittest
from ai_video_creator import AIVideoCreator

class TestAIVideoCreator(unittest.TestCase):
    def setUp(self):
        self.creator = AIVideoCreator(output_dir="test_generated")

    def test_generate_video(self):
        result = self.creator.generate_video("Test prompt", duration=30)
        self.assertEqual(result["status"], "success")
        self.assertIn("video_name", result)
        self.assertIn("shots", result)

    def test_full_project(self):
        result = self.creator.create_full_project("Test project", num_clips=2)
        self.assertEqual(result["status"], "success")
        self.assertEqual(len(result["clips"]), 2)

    def tearDown(self):
        import shutil
        shutil.rmtree("test_generated", ignore_errors=True)

if __name__ == '__main__':
    unittest.main()
