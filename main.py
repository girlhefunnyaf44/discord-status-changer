import discord

NAME = input("What do you want to stream: ")
LINK = input("URL to stream to (may not work if not twitch): ")

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(activity=discord.Streaming(name=NAME, url=LINK))

client.run(input("Token: ").strip("\""), bot=False)
