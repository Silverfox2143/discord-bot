import discord
from discord.ext import commands
from passgen import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def he(ctx, count_he = 5):
    await ctx.send("he" * count_he)

@bot.command()
async def generate_password(ctx, length: int):
   await ctx.send(f'kamu ingin membuat karakter dengan {length} karakter, berikut passwordnya:')
   pwd = gen_pass(length)
   await ctx.send(pwd)

@bot.command()
async def add(ctx, a: int, b: int):
    result = a + b
    await ctx.send(f'hasil {a} dan {b} adalah {result}.')

@bot.command()
async def minus(ctx, a: int, b: int):
    result = a - b
    await ctx.send(f'hasil {a} dan {b} adalah {result}.')

@bot.command()
async def multiply(ctx, a: int, b: int):
    result = a * b
    await ctx.send(f'hasil {a} dan {b} adalah {result}.')

@bot.command()
async def divide(ctx, a: int, b: int):
    result = a / b
    await ctx.send(f'hasil {a} dan {b} adalah {result}.')

@bot.command()
async def meme(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def tips(ctx):
    with open( 'contoh.txt', 'r', encoding='utf-8') as b:
        solusi = b.read()
    await ctx.send(solusi)

bot.run("enter_your_bot_token_here")