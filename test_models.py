import google.generativeai as genai

# API Key'inizi buraya yazın
API_KEY = "AIzaSyBB1Y3jtp4SlALJ2iIX5ExH7tFaMskGAjg"

genai.configure(api_key=API_KEY)

# Mevcut modelleri listele
print("Mevcut modeller:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
