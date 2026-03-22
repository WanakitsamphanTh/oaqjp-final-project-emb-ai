from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        text_to_analyze = 'I am glad this happened'
        emotions = emotion_detector(text_to_analyze)
        self.assertEqual(emotions['dominant_emotion'], "joy")
        text_to_analyze = 'I am really mad about this'
        emotions = emotion_detector(text_to_analyze)
        self.assertEqual(emotions['dominant_emotion'], "anger")
        text_to_analyze = 'I feel disgusted just hearing about this'
        emotions = emotion_detector(text_to_analyze)
        self.assertEqual(emotions['dominant_emotion'], "disgust")
        text_to_analyze = 'I am so sad about this'
        emotions = emotion_detector(text_to_analyze)
        self.assertEqual(emotions['dominant_emotion'], "sadness")
        text_to_analyze = 'I am really afraid that this will happen'
        emotions = emotion_detector(text_to_analyze)
        self.assertEqual(emotions['dominant_emotion'], "fear")

unittest.main()