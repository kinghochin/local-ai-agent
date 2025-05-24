# from fastapi import FastAPI
import gradio as gr

from pydantic import BaseModel
from model_runner import FlanT5Model
import json

# app = FastAPI(
#    title="Wine Spec Generator",
#    description="Generate wine flavor profiles with food pairing suggestions.",
#    version="1.0.0",
# )
model = FlanT5Model()


# class WineRequest(BaseModel):
#    description: str
#    max_tokens: int = 100


few_shot_template = """Convert the following wine descriptions into structured JSON with keys "flavors" and "finish".

Description: "This wine has flavors of cherry and oak with a smooth finish."
Specs:
{{
  "flavors": ["cherry", "oak"],
  "finish": "smooth",
  "food_pairing": ["grilled salmon", "roast duck"]
}}

Description: "A bold red wine with hints of blackberry and vanilla."
Specs:
{{
  "flavors": ["blackberry", "vanilla"],
  "finish": "bold",
  "food_pairing": ["beef stew", "dark chocolate"]
}}
Description: {user_input}
Specs:"""


# @app.post("/wine-spec")
def generate_wine_spec(description):
    # Create prompt with few-shot examples + user input
    prompt = few_shot_template.format(user_input=description)
    output = model.generate(prompt=prompt, max_tokens=100)
    output_wrapped = "{" + output.strip().strip(",") + "}"
    wine_spec = json.loads(output_wrapped)
    return {"wine_spec": wine_spec}


iface = gr.Interface(
    fn=generate_wine_spec,
    inputs="text",
    outputs="text",
    title="Wine Spec Generator",
    description="Enter wine description to get structured wine specs in JSON format. e.g. 'This wine has flavors of cherry and oak with a smooth finish.', 'A bold red wine with hints of blackberry and vanilla.",
)

iface.launch()
