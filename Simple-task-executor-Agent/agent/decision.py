# Bhai 🔥 ab chain complete karte hain. decision.py ka kaam hai user ke input ko check karke decide karna ki kaunsa task run hoga (summarize, translate, sentiment, ya fallback = echo).

def decide_task(user_input:str) -> str:
    # """
    # Decide which task to perform based on user input keywords.
    
    # Args:
    #     user_input (str): Raw input from user.
    
    # Returns:
    #     str: Task identifier (summarize, translate, sentiment, echo)
    # """
    text = user_input.lower()
    if "summarize" in text or "summary" in text:
        return "summarize"
    elif "translate" in text or "hindi" in text:
        return "translate"
    elif "sentiment" in text or "feeling" in text or "mood" in text:
        return "sentiment"
    else:
        return "echo"