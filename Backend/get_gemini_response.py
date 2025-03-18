import google.generativeai as genai
import os

GOOGLE_API_KEY='AIzaSyB2Hbwe_EcdHw6ctrUJBOlt00X_rgQogFM'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("""how much is 1 + 1""")
print(response.candidates)
print(response.resolve())
print(dir(response))
