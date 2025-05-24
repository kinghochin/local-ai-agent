from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

cache_dir = "./local_model_cache"


class FlanT5Model:
    def __init__(self, model_name="google/flan-t5-small"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name, cache_dir=cache_dir
        )
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def generate(self, prompt: str, max_tokens: int = 100) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
