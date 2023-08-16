import os
import requests
import json
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# from background import keep_alive


api_token = ''
bot = Bot(token=api_token)
dispatcher = Dispatcher(bot)

football_leagues = [
    ("Premier League", "🇬🇧"),
    ("La Liga", "🇪🇸"),
    ("Serie A", "🇮🇹"),
    ("Bundesliga", "🇩🇪"),
    ("Ligue 1", "🇫🇷"),
    ("MLS", "🇺🇸"),
    ("Russian Premier League", "🇷🇺"),
    ("Israeli Premier League", "🇮🇱"),
    ("Portuguese Primeira Liga", "🇵🇹"),
    ("Turkish Super Lig", "🇹🇷"),
    ("Ukrainian Premier League", "🇺🇦"),
    ("Greek Super League", "🇬🇷"),
    ("Belgian First Division A", "🇧🇪"),
    ("Dutch Eredivisie", "🇳🇱"),
    ("Swiss Super League", "🇨🇭"),
    ("Austrian Bundesliga", "🇦🇹"),
    ("Scottish Premiership", "🏴󠁧󠁢󠁳󠁣󠁴󠁿"),
    ("Swedish Allsvenskan", "🇸🇪"),
    ("Danish Superliga", "🇩🇰"),
    ("Norwegian Eliteserien", "🇳🇴"),
    ("Finnish Veikkausliiga", "🇫🇮"),
    ("Faroe Islands Premier League", "🇫🇴"),
    ("Irish Premier Division", "🇮🇪"),
    ("Polish Ekstraklasa", "🇵🇱"),
    ("Hungarian Nemzeti Bajnokság I", "🇭🇺"),
    ("Luxembourg National Division", "🇱🇺"),
    ("Brazilian Série A", "🇧🇷"),
    ("Argentine Primera División", "🇦🇷"),
    ("Saudi Professional League", "🇸🇦"),
]
football_cups = [
    ("UEFA Champions League", "🇪🇺"),
    ("UEFA Europa League", "🇪🇺"),
    ("UEFA Conference League", "🇪🇺"),
    ("FA Cup", "🇬🇧"),
    ("EFL Cup", "🇬🇧"),
    ("Copa del Rey", "🇪🇸"),
    ("Coppa Italia", "🇮🇹"),
    ("DFB-Pokal", "🇩🇪"),
    ("Coupe de France", "🇫🇷"),
]
hockey_leagues = [
    ("KHL", "🇷🇺"),
    ("NHL", "🇺🇸"),
]


async def get_football_results(league_or_cup):
    """Gets the results of football matches for the specified league or cup"""
    if league_or_cup in football_leagues:
        url = f'https://api.football-data.org/v2/competitions/{league_or_cup}/matches'
    elif league_or_cup in football_cups:
        url = f'https://api.football-data.org/v2/competitions/{league_or_cup}/matches'
    else:
        raise ValueError(f'Invalid league or cup: {league_or_cup}')

    response = requests.get(url)
    data = json.load(response.content)
    return data['matches']


@dispatcher.message_handler(commands=['start'])
async def star_command(message: types.Message):
    """create start command"""
    # send a welcome message to the user
    await message.reply("Hi! I'm a football ⚽ and hockey 🏒 results bot.\n"
                        "You can use me to get the latest results of any league or cup.\n"
                        "Just type /football or /hockey, followed by the name of league or cup you want to know about\n"
                        "For example, to get the latest results from the Premier League, type /football Premier League")


if __name__ == '__main__':
    # using method executor from aiogram.utils asking
    # Dispatcher expect command /start
    # keep_alive()
    executor.start_polling(dispatcher)
