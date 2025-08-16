import os
import google.generativeai as genai
from dotenv import load_dotenv
# Yeh file tera LLM API wrapper hoga — matlab ek centralized function jo prompt ko Gemini model pe bhejega aur response wapas karega.
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini client
genai.configure(api_key=api_key)

def llm_call(prompt, model="gemini-1.5-flash", temperature=0.5):
    # i can call Google Generative AI model with a prompt
    #  Args:
        # prompt (str): Input text for the model
        # model (str): Model name (default = gemini-1.5-flash)
        # temperature (float): Creativity level (0 = deterministic, 1 = creative)
    
    # Returns
        # str: Model-generated response or error message
    try:
        response = genai.GenerativeModel(model).generate_content(prompt)

        if response and response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "No response from Model"
    except Exception as e:
        return f"❌ Error calling LLM: {str(e)}"