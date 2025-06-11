import google.generativeai as genai

models = genai.list_models()
print(models)
for model in models:
    print(model)