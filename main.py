import openai
from fastapi import FastAPI, Form, Request, WebSocket, WebSocketDisconnect
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from dotenv import load_dotenv

load_dotenv()

openai = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_SECRET_KEY")
)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

chat_responses = []


@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})


chat_log = [{'role': 'system',
             'content': 'You are a helpful assistant speaking like Yoda from Star Wars. You speak briefly '
             }]

@app.websocket("/ws")
async def chat(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            user_input = await websocket.receive_text()
            chat_log.append({"role": "user", "content": user_input})

            response = openai.chat.completions.create(
                model="gpt-4",
                messages=chat_log,
                temperature=0.7
            )

            # Extract AI response (Corrected)
            ai_response = response.choices[0].message.content
            await websocket.send_text(ai_response)  # Send AI response

            chat_log.append({"role": "assistant", "content": ai_response})


    except WebSocketDisconnect:

        print("Client disconnected.")

    except Exception as e:

        print(f"WebSocket error: {e}")

        await websocket.send_text(f"Error: {str(e)}")

    finally:

        await websocket.close()


@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, user_input: Annotated[str, Form()]):

    chat_log.append({'role': 'user', 'content': user_input})
    chat_responses.append(user_input)

    response = openai.chat.completions.create(
        model='gpt-4',
        messages=chat_log,
        temperature=0.6
    )

    bot_response = response.choices[0].message.content
    chat_log.append({'role': 'assistant', 'content': bot_response})
    chat_responses.append(bot_response)

    return templates.TemplateResponse("home.html", {"request": request, "chat_responses": chat_responses})


@app.get("/image", response_class=HTMLResponse)
async def image_page(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})


@app.post("/image", response_class=HTMLResponse)
async def create_image(request: Request, user_input: Annotated[str, Form()]):

    response = openai.images.generate(
        prompt=user_input,
        n=1,
        size="256x256"
    )

    image_url = response.data[0].url
    return templates.TemplateResponse("image.html", {"request": request, "image_url": image_url})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
