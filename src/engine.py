class RAGEngine:
    def __init__(self, model_name='gpt-4'):
        self.model = model_name
        print(f'RAG Engine initialized with {model_name}')

    def query(self, text):
        return f'Synthesized response for: {text}'