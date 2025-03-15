Yoda Chatbot
Because wise, you must sound.

Overview
This repository holds a FastAPI-based chatbot that channels the wisdom (and grammar) of Master Yoda from Star Wars. It uses OpenAI’s GPT-4 under the hood for text generation, and also has an endpoint for generating images using the OpenAI Image API.

Features
Yoda-Style Chat: GPT-4 responds as if it were Yoda, brief and wise, hmmm!
Real-Time Communication: Uses WebSockets (/ws) for live chat.
Image Generation: The /image endpoint can conjure up pictures from text prompts (thanks, DALL·E).
HTML Templates: Simple Jinja2 templates for chat and image pages.

Requirements
Python 3.9+ (3.10 or later recommended)
OpenAI API Key (store in a .env file)
Packages:
fastapi
uvicorn
jinja2
python-dotenv
openai (the official Python library)
(Check requirements.txt for the full list.)

Usage
Chat Page: Type your message and watch Yoda respond.
WebSocket Magic: Real-time updates without page reload.
Image Generation: Visit http://127.0.0.1:8000/image to create AI-generated images from your text prompts.
Contributing
Pull requests and issues are welcome! Just remember: “Code reviews lead to the path of better software, they do.”

Disclaimer
Not affiliated with Star Wars, Lucasfilm, or Disney. This project is purely for educational and entertainment purposes.
Keep your OpenAI API key secret like the location of Dagobah.
License
This project is provided under the MIT License. Use the Force responsibly!
