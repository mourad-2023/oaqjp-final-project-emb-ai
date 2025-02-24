import unittest
from EmotionDetection.emotion_detection import emotion_detector

expected_dominant_emotions = {
        "I am glad this happened"                   :	"joy",
        "I am really mad about this"                :	"anger",
        "I feel disgusted just hearing about this"	:   "disgust",
        "I am so sad about this"                    :	"sadness",
        "I am really afraid that this will happen"	:   "fear",
}

class TestEmotionDetector(unittest.TestCase):
    def test_dominant_emotion(self):
        for statement, exp_dom_em in expected_dominant_emotions.items():
            self.assertEqual(emotion_detector(statement)['dominant_emotion'], exp_dom_em)

if __name__ == '__main__':
    unittest.main()