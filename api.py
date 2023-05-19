from fastapi import FastAPI, Request, Response
import uvicorn
from pyngrok import ngrok
import nest_asyncio


api =  FastAPI()
@api.get('/')
def index(request : Request):
    return """
    BabyNest
    """
@api.get('/bmi')
def bmi_calculator(request : Request, height : str, weight : str):
    bmi = float(weight) / float(height) ** 2
    return f"Your BMI is{bmi}"

#ruun api

if __name__ == "__main__":
    ngrok_tunnel = ngrok.connect(5050)
    print(f"Your domain name is{ngrok_tunnel.public_url}")
    nest_asyncio.apply()
    uvicorn.run(api, host= "localhost",port=5050)