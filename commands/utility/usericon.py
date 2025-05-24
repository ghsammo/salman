# commands/utility/usericon.py
import discord
from discord.ext import commands

class UserIcon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='usericon', help='Displays a user\'s icon.')
    async def usericon(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        embed = discord.Embed(
            title=f' <:Multipurpose:1373371000271409416> {member.display_name}\'s Icon',
            color=discord.Color.blue()
        )
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(UserIcon(bot)) 