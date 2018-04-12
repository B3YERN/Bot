import discord
from discord.ext import commands
import asyncio
import random
import traceback
import logging
import os
bot = commands.Bot (command_prefix = "m. ")
client = discord.Client()

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def my_background_task():
        await client.wait_until_ready()
        counter = 0
        channel = discord.Object(id='channel_id_here')
        while not client.is_closed:
            counter += 1
            await client.send_message(channel, counter)
            await asyncio.sleep(60) # task runs every 60 seconds


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    #if message.content.upper().startswith('!MUTE'):
        #if 412281191123910656 in [role.id for role in message.author.roles]:
            #await message.delete()
            #args = message.content.split(" ")
            #member = discord.utils.get(message.server.members, mention = args[1])
            #role = discord.utils.get(message.server.roles, name="Muted")
            #await client.add_roles(member, role)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description="Command not found, Try **m.help**.",
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
    
@bot.command
async def on_message_coins(ctx, coins):
    if str(User) in [role.name for role in ctx.author.roles]:
        if message.content == "rules": # # Say the rules! # #
            if str(Admin) in [role.name for role in message.author.roles]:
                rules = discord.Embed(title="- - - - - **RULES** - - - - -",
                                      colour=0x992d22,
                                 description="0.) READ ALL OF THE RULES \n \n 1.) Be Respectful to all beings \n \n 2.) Do not directly use profanity at another person and don't use it excessively \n \n 3.) Put links onl**")           
            await message.channel.send(embed=rules)
            await message.delete() 

    
@bot.command()
async def cookie(ctx):
    """Do you want some cookies?"""
    await ctx.send(":cookie:")
   

@bot.command()
async def lenny(ctx):
    """Lennies intensifies."""
    await ctx.send("( ͡° ͜ʖ ͡°)")
@bot.command()
async def invite(ctx):
    """No invite links are allowed because this bot is Server-only sorry."""
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
@bot.command()
async def dice(ctx, dices):
    """Let's play a dice coded-game."""
    try:
        rolls, limit = map(int, dices.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send('{} '.format(ctx.message.author.mention)+result)
    
    
@bot.command()
async def hello(ctx,member :discord.Member):
    """Say hello to my son. """
    await ctx.send('Hello : '+member.mention+' !')
     
@bot.command()
@commands.is_owner()
async def play(ctx,*game :str):
    """Playing status for the bot {Bot-Owner Only}."""
    print(*game)
    await bot.change_presence(activity=discord.Game(name="with dicks on your fingers"))
    
@bot.command()
@commands.is_owner()
async def stream(ctx,* , title : str):
    await bot.change_presence(activity=discord.Streaming(name=title, url="https://twitch.tv/discordapp"))
    
@bot.command()
@commands.is_owner()
async def listen(ctx,* ,title : str):
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=title))

@bot.command()
@commands.is_owner()
async def watch(ctx,* ,title : str):
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
    await ctx.send(random.choice(["https://i.redd.it/136qbixg5ik01.png" , "https://cdn.discordapp.com/attachments/390888029037789187/420745936545775655/IMG_20171123_193527_619.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/420823120304275466/kre9hovmpri01.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/420223393560920074/42105cb3af307ce157e5f3acff328f80.jpg" , "https://i.redd.it/dslly23bfek01.png" , "https://i.redd.it/2ouazj8a7gk01.jpg" , "https://i.imgur.com/oiFXAJr.png" , "https://cdn.discordapp.com/attachments/390888029037789187/422061129292840961/image-3.jpg" ,"https://cdn.discordapp.com/attachments/236862934632890368/423497646226014218/image.png" , "https://i.imgur.com/X6Ft7Zw.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687359942819850/100_Years.png" , "https://cdn.discordapp.com/attachments/390888029037789187/425687968636862474/Screenshot_20180319-140055.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687968636862475/Screenshot_20180319-141208.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687969253294080/DW9eotsVQAAB6Th.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687969253294081/Screenshot_20180319-143414.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687970025308180/image-3.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687970025308181/a47Gxom_460s.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/425687970570436608/Couldnt_be_Converted.jpg"  , "https://cdn.discordapp.com/attachments/390888029037789187/425688023959863316/Screenshot_20180315-124106.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/425689424236642314/My_fetish.jpg"  , "https://cdn.discordapp.com/attachments/392277475557769216/433991641057984523/Screenshot_20180411-012755.jpg"  , "https://cdn.discordapp.com/attachments/390888029037789187/432643243159846913/unknown.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/432643243767889935/n7d1u62no3q01.png", "https://cdn.discordapp.com/attachments/390888029037789187/432643244711739403/image_2.jpg"  , "https://cdn.discordapp.com/attachments/390888029037789187/432643245235896330/aWlJR7dR_700w_0.jpg", "https://cdn.discordapp.com/attachments/390888029037789187/432643245718110219/Screenshot_20180408-202732.png"  , "https://cdn.discordapp.com/attachments/392277475557769216/433991642500956160/autism.png", "https://cdn.discordapp.com/attachments/392277475557769216/433991642500956161/image-22.jpg"  , "https://cdn.discordapp.com/attachments/392277475557769216/433991642500956161/image-22.jpg", "https://cdn.discordapp.com/attachments/392277475557769216/433992633753403414/E11leYos20jRTGF8QS-bAHy-t_SuSA8bLhF0OlJRjuc-1.png"  , "https://cdn.discordapp.com/attachments/392277475557769216/433992439527899137/Screenshot_20180409-003241.jpg", "https://cdn.discordapp.com/attachments/392277475557769216/433992439523704832/Screenshot_20180408-010940.jpg"  , "https://cdn.discordapp.com/attachments/392277475557769216/433992439078846464/Screenshot_20180409-005331.jpg", "https://cdn.discordapp.com/attachments/392277475557769216/433992438470803458/980x.png"  , "https://cdn.discordapp.com/attachments/392277475557769216/433992437900509186/Screenshot_20180409-002224.jpg", "https://cdn.discordapp.com/attachments/392277475557769216/433992437900509186/Screenshot_20180409-002224.jpg"  , "", ""  , "" ]))
    
@bot.command()
async def joke(ctx):
    """"""
    await ctx.send(random.choice(["I want to eat on the soft juicy part of the anus. The part that smells bad." ,]))
                                 
                                 
@bot.command()
async def warns(self, ctx, user: discord.Member):
    """Checks how many warns a user has"""
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("Sorry! You must have the **Manage Messages** permission to use this command!")
        return
    db = dataset.connect("sqlite:///servers/{}.db".format(ctx.guild.id))
    table = db["warns"]
    if not table.find_one(user=user.id):
        await ctx.send("This user has **0** warns!")
    else:
        await ctx.send("This user has **{}** warns!".format(table.find_one(user=user.id)["warns"]))

@bot.command()
async def report(self, ctx, userToReport: discord.Member, reason: str):
        """Reports a user to the moderators."""
        config = dataset.connect("sqlite:///servers/{}.db".format(ctx.guild.id))["config"]
        for user in ctx.guild.members:
            if config.find_one(key="report_role") is None:
                role = discord.utils.get(user.roles, name="Admin")
            else:
                role = discord.utils.get(user.roles, name=config.find_one(key="report_role")["value"])
            if role:
                message = """**User Reported!**\n**Reportee**: {}\n**User Reported**: {}\n**Reason**: {}\n**Channel**: {}""".format(ctx.author.display_name, userToReport.display_name, reason, ctx.channel.name)
                await user.send(message)
                
@bot.command()
@commands.cooldown(1,10.0,type=commands.BucketType.user)
async def ping(ctx):
    resp = await ctx.send('Pong! Loading...')
    diff = resp.created_at - ctx.message.created_at
    await resp.edit(content=f'Pong! That took {1000*diff.total_seconds():.1f}ms.') 
    
@bot.command()
async def stephenhawking(ctx):
    """ In love of Steven Hawkings 1942-2018 <3"""
    await ctx.send("Dad is going to heaven "
                   "https://cdn.discordapp.com/attachments/361128774928171008/423823373127122944/aa37207.png")
        
@bot.command(pass_context=True)
async def avatar(ctx,*,user:discord.Member=None):
    if user==None or type(user)==str:
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
    await ctx.send(message)
   
bot.run(os.getenv('TOKEN'))
