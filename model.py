# Data contract is validating the frontend request making sure the frontend and backend are in sync
from pydantic import BaseModel
from typing import List
class AIRequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool
