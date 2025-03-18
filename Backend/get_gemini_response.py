import google.generativeai as genai

# Set up your API key
GOOGLE_API_KEY = 'AIzaSyB2Hbwe_EcdHw6ctrUJBOlt00X_rgQogFM'
PROMPT_WRAP = "Write a script that {prompt_request}. dont write anything else since im going to run it exactly as you give it to me. Wrap the code with ```code <put code here>``` and NOTHING ELSE."

# Configure the API with the provided key
genai.configure(api_key=GOOGLE_API_KEY)

# Define the function to get the Gemini response
def get_gemini_response(prompt: str) -> str:
    wrapped_prompt = PROMPT_WRAP.format(prompt_request=prompt)
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error generating prompt response: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter prompt: ")
    result = get_gemini_response(user_prompt)
    print("Gemini Response:", result)
