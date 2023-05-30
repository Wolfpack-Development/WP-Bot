import discord
import json
from discord.ext import commands
from discord.commands import slash_command
from discord import FFmpegAudio




class pingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @slash_command()
    @discord.option(type=discord.SlashCommandOptionType.user, name="member")
    async def caps(self, ctx, member:discord.Member):
        with open('caps.json', 'r') as f:
            data = json.load(f)
        caps = data[str(member.id)]["Caps"]
        nocaps = data[str(member.id)]["NoCaps"]


        embed=discord.Embed(title="caps", color=discord.Color.random())
        embed.add_field(name="caps", value=f'{caps}', inline=True)
        embed.add_field(name="Keine caps", value=f'{nocaps}')
        await ctx.respond(embed=embed)







def setup(bot):
    bot.add_cog(pingCommand(bot))