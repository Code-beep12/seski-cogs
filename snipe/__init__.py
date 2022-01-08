from discord.ext import commands
import discord
import time
from discord.member import Member


def setup(bot: commands.Bot):
        bot.add_cog(snipe(bot))
        bot.add_cog(esnipe(bot))
        #bot.add_cog(rsnipe(bot))
