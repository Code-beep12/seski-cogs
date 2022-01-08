from discord.ext import commands
import discord
import time
from discord.member import Member
from .snipe import snipe
from redbot.core.bot import Red

async def setup(bot: Red) -> None:
     bot.add_cog(snipe(bot))
     #bot.add_cog(rsnipe(bot))
