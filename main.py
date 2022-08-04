import nextcord
import asyncio
from nextcord.ext import commands
from fastapi import FastAPI




app = FastAPI()
intents=nextcord.Intents.all()

bot=commands.Bot(command_prefix='$',intents=intents)
bot.remove_command("help")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(bot.start('token'))

