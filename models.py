from pydantic import  BaseModel

# Pydantic model for input
class ItemInput(BaseModel):
    name: str

# Pydantic model for output
class ItemOutput(BaseModel):
    name: str
    description: str