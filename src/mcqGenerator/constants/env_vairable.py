# Loading OPENAI_API_KEY
from dotenv import load_dotenv
import os
# take environment variables from .env.
load_dotenv()  

KEY=os.getenv("OPENAI_API_KEY")