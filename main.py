import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)
@client.event
async def on_ready():
    print(f'logged as {client.user}.')
@client.slash_command()
async def help(ctx):
    embed = nextcord.Embed(
        title="your title",
        description="your message",
        color=nextcord.Color.gold()
    )
    embed.add_field(name="/help", value="put here what u want", inline=False)
    await ctx.send(embed=embed)
client.run('TOKEN')
