from deepface import DeepFace

class EmotionDetector:
    def __init__(self):
        self.actions = ['emotion']

    def analyze_frame(self, frame):
        try:
            result = DeepFace.analyze(frame, actions=self.actions, enforce_detection=False)
            return result[0]['dominant_emotion']
        except Exception as e:
            return f"Error: {e}"