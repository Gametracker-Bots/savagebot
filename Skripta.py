import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms")

@client.command(aliases=["eightball"])
async def _eightball(ctx, *,question):
    responses = ["Yes",
                 "No",
                 "Maybe",
                 "Try agin later"]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")

@client.command()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_nema, member_descriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discirminator) == (member_name, member_disciminator): 
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

client.run("NjMxMTU4NDc2NDM2OTMwNTgw.XZ3DZQ.LJn8qRcx88AOkWc7smwinixVNn0")

