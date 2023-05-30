import discord
import ezcord
import os
import json
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = ezcord.Bot(intents=intents)

with open('config.json', 'r') as c:
    config = json.load(c)

with open('caps.json', 'r') as f:
    data = json.load(f)

eins = discord.Color.blue()
zwei = discord.Color.green()
drei = discord.Color.gold()
vier = discord.Color.red()
fünf = discord.Color.magenta()
sechs = discord.Color.yellow()
sieben = discord.Color.purple()
acht = discord.Color.dark_teal()
neun = discord.Color.fuchsia()

ausnahmen=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

@bot.event
async def on_message(message: discord.Message):
    if str(message.author.id) not in data:
        data[str(message.author.id)] = {"Caps": 0, "NoCaps": 0}
    channel = bot.get_channel(1110218235892203610)

    if message.author != bot.user:


        lower = 0
        upper = 0
        for i in message.content:
            if i in ausnahmen:
                return
            if i.isupper():
                upper += 1
            else:
                lower += 1

        if lower + upper >= 11:

            if (lower + upper) * 0.2 > upper > lower * 0.1:
                color = eins
                print("10-20")
            elif (lower + upper) * 0.3 > upper > lower * 0.2:
                color = zwei
                print("20-30")
            elif (lower + upper) * 0.4 > upper > lower * 0.3:
                color = drei
                print("30-40")
            elif (lower + upper) * 0.5 > upper > lower * 0.4:
                color = vier
                print("40-50")
            elif (lower + upper) * 0.6 > upper > lower * 0.5:
                color = fünf
                print("50-60")
            elif (lower + upper) * 0.7 > upper > lower * 0.6:
                color = sechs
                print("60-70")
            elif (lower + upper) * 0.8 > upper > lower * 0.7:
                color = sieben
                print("70-80")
            elif (lower + upper) * 0.9 > upper > lower * 0.8:
                color = acht
                print("80-90")
            elif (lower + upper) * 1.0 >= upper > lower * 0.9:
                color = neun
                print("90-100")
        upperr = data[str(message.author.id)]["Caps"]
        upperr += 1
        data[str(message.author.id)]["Caps"] = upperr
        embed = discord.Embed(title=f'CAPS!!', color=color)
        embed.add_field(name="user", value=f'{message.author}')
        embed.add_field(name="zeit", value=f'{discord.utils.format_dt(discord.utils.utcnow(), style="R")}')
        embed.add_field(name="message", value=f'{message.content}\n'
                                              f'{message.jump_url}', inline=False)
        embed.add_field(name="buchstaben in caps", value=f'{upper}')
        embed.add_field(name="buchstaben nicht in caps", value=f'{lower}')
        print(config["configs"]["logchannel"])
        channel = bot.get_channel(config["configs"]["logchannel"])
        await channel.send(embed=embed)
        with open('caps.json', 'w') as f:
            json.dump(data, f, indent=4)


bot.load_cogs("commands", subdirectories=True)


load_dotenv()
bot.run(os.getenv("TOKEN"))
