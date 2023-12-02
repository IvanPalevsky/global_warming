import discord
import os
from discord.ext import commands
from random import choice
import requests
from settings import TOKEN
from cl_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user} и я помогу вам избежать глобального потепления!')
    await ctx.send("Чтобы не вредить природе, нужно соблюдать очень простые правила!")
    await ctx.send("Введите команду /nature, чтобы получить информацию.")

@bot.command()
async def nature(ctx):
    await ctx.send('Как спасти природу: 8 шагов, которые может сделать каждый')
    await ctx.send('1.ЭКОНОМЬТЕ РЕСУРСЫ')
    await ctx.send('2.РАЗДЕЛЯЙТЕ МУСОР')
    await ctx.send('3.СДАВАЙТЕ ВТОРСЫРЬЁ')
    await ctx.send('4.ВЫБИРАЙТЕ ЭКОЛОГИЧНЫЙ ТРАНСПОРТ')
    await ctx.send('5.ИСПОЛЬЗУЙТЕ ПОВТОРНО И НЕ БЕРИТЕ ЛИШНЕЕ')
    await ctx.send('6.ВНЕДРЯЙТЕ ЭКО-ПРИВЫЧКИ НА РАБОТЕ')
    await ctx.send('7.ОБРАТИТЕ ВНИМАНИЕ НА ПИТАНИЕ')
    await ctx.send('8.ПОСТАРАЙТЕСЬ ОТВЫКНУТЬ ОТ ПЛАСТИКА')
    await ctx.send("Вставьте картинку с мусором и введите команду /garbage, чтобы получить информацию о мусоре.")

@bot.command()
async def garbage(ctx):
    if ctx.message.attachments:
       for attachment in ctx.message.attachments:
           file_name = attachment.filename
           file_url = attachment.url
           image_path = (f'images1/{file_name}')
           await attachment.save(image_path)
           await ctx.send(get_class(model_path='model/keras_model.h5', labels_path='model/labels.txt', image_path = image_path))  
           os.remove(image_path)
    else:
        await  ctx.send('Вы забыли загрузить картинку')

bot.run(TOKEN)

