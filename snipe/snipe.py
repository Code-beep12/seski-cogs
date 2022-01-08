from discord.ext import commands
import discord
import time
from discord.member import Member
from redbot.core import commands

def setup(bot: commands.Bot):
        bot.add_cog(snipe(bot))
        bot.add_cog(esnipe(bot))
        #bot.add_cog(rsnipe(bot))


class snipe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

    @commands.command(name="snipe")
    async def snipe(self, ctx:commands.Context):
        if not self.last_msg:
            await ctx.send("Uhh nothing to snipe here")
            return #so that rest of it doesnt execute

        author = self.last_msg.author
        content = self.last_msg.content
        msgtime = int(self.last_msg.created_at.timestamp())
        channel = self.last_msg.channel

        embed= discord.Embed(title=f"Message Content (Sent <t:{msgtime}:R>)",description=f"{content}",colour=author.colour)
        embed.set_author(name=author,icon_url=author.avatar_url)
        embed.add_field(name="Channel", value=channel.mention)
        embed.add_field(name="Deleted_at", value=f"<t:{msgtime}:R>")
        
        await ctx.send(embed=embed)

class esnipe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.old_msg= None
        self.new_msg= None

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        self.old_msg = before
        self.new_msg= after

    @commands.command(name="esnipe")
    async def esnipe(self, ctx:commands.Context):
        if not self.old_msg:
            await ctx.send("Uhh nothing to see here")
            return #so that rest of it doesnt execute

        author = self.new_msg.author
        old_content = self.old_msg.content
        new_content = self.new_msg.content
        old_msgtime = int(self.old_msg.created_at.timestamp())
        new_msgtime = int(time.time())
        channel = self.new_msg.channel

        embed= discord.Embed(title=f"Message Content",description=f"**Before:**\n{old_content} (<t:{old_msgtime}:R>)\n**After:**\n{new_content} (<t:{new_msgtime}:R>)",colour=author.colour)
        embed.set_author(name=author,icon_url=author.avatar_url)
        embed.add_field(name="Channel", value=channel.mention)
        
        await ctx.send(embed=embed)

"""class rsnipe(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.lastmsg= None
    @commands.Cog.listener()
    async def on_raw_message_delete(self,payload: discord.RawMessageDeleteEvent):
        self.lastmsg=payload
    @commands.command(name="rsnipe")
    async def rsnipe(self, ctx: commands.Context):
        if not self.lastmsg:
            await ctx.send("Uhh nothing to see here")
            return #so that rest of it doesnt execute
        await ctx.send(f"Channel - {self.lastmsg.channel_id}\nMessageid - {self.lastmsg.message_id}\nMessage - {self.lastmsg.cached_message}")"""
