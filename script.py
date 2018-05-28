import discord
from discord.ext import commands
import asyncio
import random
import time
import traceback
import logging
import os
bot = commands.Bot (command_prefix = "m. ")
client = discord.Client()
bot.remove_command('help')
async def loop():
    while True:
        await bot.change_presence(activity=discord.Streaming(name="My Stream", url="https://twitch.tv/discordapp"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Moaning"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Meme Bot 2.0"))
        await asyncio.sleep(5)

@bot.event
async def on_ready():
    print("Bot is ready")
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description="Command not found, Try **m. help**.",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:",
                              description=f"{error}",
                              colour=0xe73c24)
        await ctx.send(embed=embed)


@bot.event
async def on_member_join(member):
    await member.guild.get_channel(416870728839856129).send(f"Welcome to the Server, <@{member.id}>. Enjoy your stay!")
    

@bot.event
async def on_member_remove(member):
    await member.guild.get_channel(416870728839856129).send(f"Just left **{ctx.guild}**, {member.mention}. Hope you enjoyed your stay!")


@bot.command()
async def invite(ctx):
    """Join the Dev's server."""
    await ctx.send("```Here we go , you fuckin' randie ``` "
                   "https://discord.gg/dQEatw4")
@bot.command()
async def AlphaServer(ctx):
    """Join Alpha Wolf's Server."""
    await ctx.send("```Join my Wolf's server```"
          "https://discord.gg/v2tbReT")
@bot.command()
async def developed(ctx):
    """Who developed the bot?"""
    await ctx.send("```Developed by B3YERN and his coding team.```")
    
start_time = time.time()

@bot.command(pass_context=True)
async def uptime(ctx):
    """Checks how long the bot ran"""
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(colour=0x2EFF00)
    embed.add_field(name="__Bots Uptime!__", value=f"Week: {week},\nDay: {day},\nHours: {hour},\nMinutes: {minute},\nSeconds: {second}")
    embed.set_footer(text="Memes Bot™ | Uptime Status!")
    await ctx.send(embed=embed)
@bot.command()
async def RDNG(ctx, dices):
    """Pick a random number generator."""
    try:
        rolls, limit = map(int, dices.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send('{} '.format(ctx.message.author.mention)+result)
 
     
@bot.command()
@commands.is_owner()
async def play(ctx,*game :str):
    """Playing status for the bot {Bot-Owner Only}."""
    print(*game)
    await bot.change_presence(activity=discord.Game(name="m. help | playing in gas chambers "))
    
@bot.command()
@commands.is_owner()
async def stream(ctx,* , title : str):
    """Streaming status for the bot {Bot-Owner Only}."""
    await bot.change_presence(activity=discord.Streaming(name=title, url="https://twitch.tv/discordapp"))
    
@bot.command()
@commands.is_owner()
async def listen(ctx,* ,title : str):
     """Listening status for the bot {Bot-Owner Only}."""
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=title))

@bot.command()
@commands.is_owner()
async def watch(ctx,* ,title : str):
     """Watching status for the bot {Bot-Owner Only}."""
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=title))

@bot.command()
async def prune(ctx, number: int, user: discord.Member = None):
    """Deletes the specified amount of messages."""
    lim = 0
    if number is None:
        await ctx.send("Please specify a number of messages to be deleted.")
    else:
        async for x in ctx.history(limit=5000, before=ctx.message.created_at):
            if lim > number:
                break
            if user:
                if x.author == user:
                    await x.delete()
                else:
                    pass
            else:
                await x.delete()
            lim += 1
            

@bot.command()
async def kick(ctx, *, member : discord.Member = None):
    """Kick the client at the server."""
    try:
        await member.kick()
        await ctx.send(ctx.message.author.mention + "Done, This motherfucker already wanted some smoke!")
    except discord.errors.Forbidden:
        await ctx.send('I don\'t have perms')
        
        
        
@bot.command()
async def mute(ctx, member:discord.Member):
    """Mute the client on the server."""
    if "Furry boii (Manager)" in [role.name for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        for each in ctx.guild.channels:
                await each.set_permissions(member, overwrite=overwrite) 

@bot.command()
async def unmute(ctx, member:discord.Member):
    """Unmute the client on the server."""
    if "Furry boii (Manager)" in [role.name for role in ctx.author.roles]:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = None
        for each in ctx.guild.channels:
            await each.set_permissions(member, overwrite=overwrite)
            
@bot.command()
async def ban (ctx, member:discord.Member):
    """Bans the client with mention."""
    await ctx.guild.ban(member)
    await ctx.send(f"Bitch,{member.mention} has been banned!")
    
@bot.command()
async def dolphin(ctx):
    """Dolphin is love, Dolphin is life."""
    await ctx.send(random.choice(["https://cdn.discordapp.com/attachments/411463762445598720/418670078951686144/dolphin.gif", "https://media.giphy.com/media/FR3IRCWC9faRG/giphy.gif", "http://i0.kym-cdn.com/photos/images/original/000/238/610/3fe.gif"]))

@bot.command()
async def warn(ctx, user: discord.Member, *, reason: str):
    """Warns the client straight away"""
    await ctx.send(f'{ctx.author.mention} You have successfully warned **{user.mention}** for `{reason}`.')
    await ctx.send(f'{user} You have been warned for `{reason}` in `{ctx.guild.name}`.')
    warning = open("warned.txt", "a+")
    warning.write(f' {user} has been warned for `{reason}` `this was done by {ctx.author.mention}`') 
    warning.close()
    await ctx.send(f":warning: {user.mention} had been warned")      

@bot.command()
@commands.is_owner()              
async def die(ctx): 
        """Safely shuts down the bot"""

        await ctx.send("Shutting down...")
        await bot.logout()        
        
@bot.command()
async def meme(ctx):
    """You gonna enjoy some shitpost"""
    embed = discord.Embed(colour=000000)
    embed.set_image(url=random.choice(["https://i.redd.it/136qbixg5ik01.png" , "https://cdn.discordapp.com/attachments/390888029037789187/420745936545775655/IMG_20171123_193527_619.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/420823120304275466/kre9hovmpri01.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/420223393560920074/42105cb3af307ce157e5f3acff328f80.jpg" , "https://i.redd.it/dslly23bfek01.png" , "https://i.redd.it/2ouazj8a7gk01.jpg" , "https://i.imgur.com/oiFXAJr.png" , "https://cdn.discordapp.com/attachments/390888029037789187/422061129292840961/image-3.jpg" ,"https://cdn.discordapp.com/attachments/236862934632890368/423497646226014218/image.png" , "https://i.imgur.com/X6Ft7Zw.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687359942819850/100_Years.png" , "https://cdn.discordapp.com/attachments/390888029037789187/425687968636862474/Screenshot_20180319-140055.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687968636862475/Screenshot_20180319-141208.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687969253294080/DW9eotsVQAAB6Th.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687969253294081/Screenshot_20180319-143414.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687970025308180/image-3.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687970025308181/a47Gxom_460s.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/425687970570436608/Couldnt_be_Converted.jpg"  , "https://cdn.discordapp.com/attachments/390888029037789187/425688023959863316/Screenshot_20180315-124106.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/425689424236642314/My_fetish.jpg"  , "https://imgur.com/0tnZ7nF.jpg"  , "https://b.thumbs.redditmedia.com/oLOHGAufL58oegCHbcbobtwiBykQmVrqav_G98tKmOI.jpg"  , "https://b.thumbs.redditmedia.com/LAVU1JKcXxmz0wOzSg_WYUGkw9saC2CY3zG936NOrpU.jpg" , "Fuck you and no memes for you tonight" , "I want to eat on the soft juicy part of the anus. The part that smells bad." , "https://i.redd.it/8qkzeb0eh1y01.jpg" , "https://i.redd.it/5nm83ejrgzx01.jpg" , "https://i.redd.it/r6rns00q00y01.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/445957265439064064/DdPoThFXUAAMyad.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/445193042992037889/BoilingAngelicCapybara-max-1mb.gif" , "https://cdn.discordapp.com/attachments/390888029037789187/445397754181582849/24-english-memes-1.jpg"  , "https://cdn.discordapp.com/attachments/390888029037789187/445192613981585418/20180507_010158.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/444705897717956608/20180511_213703.JPG" , "https://cdn.discordapp.com/attachments/390888029037789187/443994005705981953/when-he-tells-you-his-favorite-hentali-category-is-loli-30404082.png" , "https://cdn.discordapp.com/attachments/390888029037789187/442467966941134854/Dcb8N09WkAAyxm0.jpg"  , "https://cdn.discordapp.com/attachments/356638847603441665/436662548658520104/60679a9f3fbbcec3b28c85bd2a7b1457.gif" , "https://cdn.discordapp.com/attachments/390888029037789187/441336919557668864/Db8x1qSX0AAhBFv.jpgq" , "https://cdn.discordapp.com/attachments/390888029037789187/441357048891047967/Db1eDgSWAAADqEe.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/441357067723210763/image_2.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/442440906482647050/download_30.jpeg" , "https://media.discordapp.net/attachments/390888029037789187/444567175655850015/DczbGHsWkAArecA.jpg" , "https://i.redd.it/mhfa3z74h3y01.jpg" , "https://i.redd.it/5heu9rwmhzx01.png"  , "https://i.redd.it/44m6dda6q0y01.png" ,"https://cdn.discordapp.com/attachments/443714829199343616/448208995006808064/FB_IMG_15256004955617945.jpg" , "https://cdn.discordapp.com/attachments/443714829199343616/448209329741627403/29196249_444393689312259_153003597125124096_n.jpg" , "https://cdn.discordapp.com/attachments/443714829199343616/448209500810248202/db528lex5xk01.jpg" , "https://cdn.discordapp.com/attachments/443714829199343616/448209703772880896/28685326_206257853336105_6988838270872322048_n.jpg" , "https://media.discordapp.net/attachments/443714829199343616/448210659180675073/chats-wife-online-our-daughter-lost-her-first-tooth-7-38-32643898.png?width=371&height=676" , "https://cdn.discordapp.com/attachments/447809619541360650/450534615250239488/r1jxhmvc9tb01.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450534935715905546/slow-computer-meme-funny.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450534935715905546/slow-computer-meme-funny.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450534935715905547/d3abfb2223e98bdde487a1d66da9bc98d6cdae36def600591153f151930e693a.gif" , "https://i.redd.it/5kcegdc70f011.png" , "https://i.redd.it/cpzcen89ue011.png" , "https://i.redd.it/kuqzrbt5ag011.jpg" , "https://i.redd.it/q3dtcnfv9i011.png" , "https://cdn.discordapp.com/attachments/447809619541360650/450542747485470721/8mWdz35.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450542747980660760/otyl2wtqs0vz.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450542747980660763/dark-humour-memes-10.jpg" , "https://i.redd.it/1g984z0ibh011.jpg" , "https://cdn.discordapp.com/attachments/445806579137249296/450542754750267412/image-2.png" , "https://cdn.discordapp.com/attachments/449979940050567168/450544658020433921/image-9-1.png" , "https://cdn.discordapp.com/attachments/449979940050567168/450544658020433920/images_8.jpeg"]))
    await ctx.send(embed=embed)

@bot.command()
async def discord(ctx):
    """Servers dying in everywhere"""
    embed = discord.Embed(colour=000000)
    embed.set_image(url=random.choice([""]))
    await ctx.send(embed=embed)
    
                
@bot.command()
@commands.cooldown(1,10.0,type=commands.BucketType.user)
async def ping(ctx):
    """Checks how long did you and the bot reply"""
    resp = await ctx.send('Pong! Loading...')
    diff = resp.created_at - ctx.message.created_at
    await resp.edit(content=f'Pong! That took {1000*diff.total_seconds():.1f}ms.') 
    
        
@bot.command()
async def avatar(ctx, user:discord.Member=None):
    """Checks client's profile picture"""
    if not user:
        await ctx.send("Please Ping the user you wish to see the avatar of.")
    else:
        try:
            em=discord.Embed()
            em.title=str(user)
            em.set_image(url=user.avatar_url)
            print(user.avatar_url)
            await ctx.send(embed=em)
        except:
            await ctx.send("There appears to have been an Error. Please make sure you ping the user you want the avatar of.") 

@bot.command()
async def say(ctx, *, message):
    """Whatever the fuck you say, bot will say it aswell"""
    await ctx.send(message)
    
@bot.command(pass_context=True)
async def coinflip(ctx):
    """Flip the coin for luck"""
    coin = ['Heads', 'Tails']
    embed=discord.Embed(title='**Coinflip**', description='The coin landed on {}!'.format(random.choice(coin)), color=0x3b1261)
    await ctx.channel.send(embed=embed)
    
    
@bot.command()
async def bomb(ctx):
    message = 'Hi,Im just testing my DM bomber.'
    user = await bot.get_user_info('user_id')
    i=0
    while i < 25:
        await ctx.send(user, message)
        i = i + 1 
@bot.command(pass_context=True)
async def type(ctx, user : str):
    await ctx.send(":typing: {} is typing...".format(user))
        
        
        
        
bot.run(os.getenv('TOKEN'))
