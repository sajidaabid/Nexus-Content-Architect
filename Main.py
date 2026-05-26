class ContentArchitect:
    def __init__(self, text):
        self.text = text

    def analyze(self):
        words = self.text.split()
        word_count = len(words)
        
        # Simple Readability Logic
        readability = "Easy" if word_count < 100 else "Complex"
        
        # CTA Detector
        cta_keywords = ['click', 'contact', 'buy', 'subscribe', 'join']
        has_cta = any(word in self.text.lower() for word in cta_keywords)
        
        return {
            "Word Count": word_count,
            "Readability": readability,
            "CTA Present": has_cta
        }

# Testing the engine
if __name__ == "__main__":
    sample_text = "Welcome to Nexus Automation. Click here to subscribe for updates!"
    architect = ContentArchitect(sample_text)
    print(architect.analyze())
