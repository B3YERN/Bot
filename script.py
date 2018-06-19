import discord
from discord.ext import commands
import asyncio
import requests
import random
import time
import traceback
import logging
import os
import json
import inspect
bot = commands.Bot (command_prefix = "m. ")
client = discord.Client()

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
                              colour=000000)
        await ctx.send(embed=embed)


@bot.event
async def on_member_join(member):
    await member.guild.get_channel(416870728839856129).send(f"Welcome to the Server, <@{member.id}>. Enjoy your stay!")
    

@bot.event
async def on_member_remove(member):
    await member.guild.get_channel(416870728839856129).send(f"<@{member.id}> Just left **{member.guild}**, {member.mention}. Hope you enjoyed your stay!")


@bot.command()
async def invite(ctx):
    """Join the Dev's server."""
    await ctx.send("```Here we go , you fuckin' randie ``` "
                   "https://discord.gg/dQEatw4")
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
    embed = discord.Embed(colour=000000)
    embed.add_field(name="__Bots Uptime!__", value=f"Week: {week},\nDay: {day},\nHours: {hour},\nMinutes: {minute},\nSeconds: {second}")
    embed.set_footer(text="Memes Bot™ | Uptime Status!")
    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_owner()
async def source(ctx, *, text: str):
    """Shows source code of a command."""
    nl2 = '`'
    nl = f"``{nl2}"
    source_thing = inspect.getsource(bot.get_command(text).callback)
    await ctx.send(f"{nl}py\n{source_thing}{nl}") 
    
   
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
    if "Staff" in [role.name for role in ctx.author.roles]:
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
    if "Staff" in [role.name for role in ctx.author.roles]:
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
async def warn(ctx, member: discord.Member = None,*, reason="Please read the rules again!"):
    """Warns a user (staff-only)"""
    if not ("Staff" in [role.name for role in ctx.message.author.roles]):
        embed=discord.Embed(title='No perms!', description='Sorry you dont have perms to do this!', color=000000)
        return await ctx.send(embed=embed)
    if member == None:
        embed = discord.Embed(title='How to use',color=mc, description='Guide on how to warn: do `%warn <member> [reason]` where <> is requiered and [] is optinal.')
        return await ctx.send(embed=embed)
    if len(warnmngr.get_warns(userid=member.id)) == 2:
        embed=discord.Embed(title='You got kicked!', description='Due to lots of warns u have been kicked... u can re-join at https://discord.gg/dQEatw4 thou xD', color=000000)
        try:
            await member.send(embed=embed)
        except:
            pass    
        await member.kick(member)
    if len(warnmngr.get_warns(userid=member.id)) == 5:
        embed=discord.Embed(title='Cya m8', description='Due to rule breaking we decided to auto banned you. DM 9oXD in Kikto get yourself unbanned!', color=000000)
        try:
            await member.send(embed=embed)
        except:
            pass
        await ctx.guild.ban(member)
    try:
        warnmngr.warn(member.name, member.id, reason)
        embed=discord.Embed(title='WARNED', description='{} has been warned successfully!'.format(member.name), color=000000)
        await ctx.send(embed=embed)
        embed=discord.Embed(title='WARNED', description=f"You got warned by {ctx.message.author.name} for {reason}!", color=000000)
        try:
            await member.send(embed=embed)
        except:
            pass
    except Exception as e:
        embed=discord.Embed(title='UUPS', description='Something went wrong... We reported it to the team to take care!', color=000000)
        await ctx.send(embed=embed)
        print("EXEPTION in warn!!! ")
        raise(e)      

@bot.command()
@commands.is_owner()              
async def die(ctx): 
        """Safely shuts down the bot"""

        await ctx.send("Shutting down...")
        await bot.logout()        
        
@bot.command(aliases=["memes"])
async def meme(ctx):
    """You gonna enjoy some shitpost"""
    embed = discord.Embed(colour=000000)
    embed.set_image(url=random.choice(["https://i.redd.it/136qbixg5ik01.png" , "https://cdn.discordapp.com/attachments/390888029037789187/420745936545775655/IMG_20171123_193527_619.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/420823120304275466/kre9hovmpri01.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/420223393560920074/42105cb3af307ce157e5f3acff328f80.jpg" , "https://i.redd.it/dslly23bfek01.png" , "https://i.redd.it/2ouazj8a7gk01.jpg" , "https://i.imgur.com/oiFXAJr.png" , "https://cdn.discordapp.com/attachments/390888029037789187/422061129292840961/image-3.jpg" ,"https://cdn.discordapp.com/attachments/236862934632890368/423497646226014218/image.png" , "https://i.imgur.com/X6Ft7Zw.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687359942819850/100_Years.png" , "https://cdn.discordapp.com/attachments/390888029037789187/425687968636862474/Screenshot_20180319-140055.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687968636862475/Screenshot_20180319-141208.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687969253294080/DW9eotsVQAAB6Th.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687969253294081/Screenshot_20180319-143414.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687970025308180/image-3.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/425687970025308181/a47Gxom_460s.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/425687970570436608/Couldnt_be_Converted.jpg"  , "https://cdn.discordapp.com/attachments/390888029037789187/425688023959863316/Screenshot_20180315-124106.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/425689424236642314/My_fetish.jpg"  , "https://imgur.com/0tnZ7nF.jpg"  , "https://b.thumbs.redditmedia.com/oLOHGAufL58oegCHbcbobtwiBykQmVrqav_G98tKmOI.jpg"  , "https://b.thumbs.redditmedia.com/LAVU1JKcXxmz0wOzSg_WYUGkw9saC2CY3zG936NOrpU.jpg" , "https://i.redd.it/8qkzeb0eh1y01.jpg" , "https://i.redd.it/5nm83ejrgzx01.jpg" , "https://i.redd.it/r6rns00q00y01.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/445957265439064064/DdPoThFXUAAMyad.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/445193042992037889/BoilingAngelicCapybara-max-1mb.gif" , "https://cdn.discordapp.com/attachments/390888029037789187/445397754181582849/24-english-memes-1.jpg"  , "https://cdn.discordapp.com/attachments/390888029037789187/445192613981585418/20180507_010158.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/444705897717956608/20180511_213703.JPG" , "https://cdn.discordapp.com/attachments/390888029037789187/443994005705981953/when-he-tells-you-his-favorite-hentali-category-is-loli-30404082.png" , "https://cdn.discordapp.com/attachments/390888029037789187/442467966941134854/Dcb8N09WkAAyxm0.jpg"  , "https://cdn.discordapp.com/attachments/356638847603441665/436662548658520104/60679a9f3fbbcec3b28c85bd2a7b1457.gif" , "https://cdn.discordapp.com/attachments/390888029037789187/441336919557668864/Db8x1qSX0AAhBFv.jpgq" , "https://cdn.discordapp.com/attachments/390888029037789187/441357048891047967/Db1eDgSWAAADqEe.jpg" , "https://cdn.discordapp.com/attachments/390888029037789187/441357067723210763/image_2.png"  , "https://cdn.discordapp.com/attachments/390888029037789187/442440906482647050/download_30.jpeg" , "https://media.discordapp.net/attachments/390888029037789187/444567175655850015/DczbGHsWkAArecA.jpg" , "https://i.redd.it/mhfa3z74h3y01.jpg" , "https://i.redd.it/5heu9rwmhzx01.png"  , "https://i.redd.it/44m6dda6q0y01.png" ,"https://cdn.discordapp.com/attachments/443714829199343616/448208995006808064/FB_IMG_15256004955617945.jpg" , "https://cdn.discordapp.com/attachments/443714829199343616/448209329741627403/29196249_444393689312259_153003597125124096_n.jpg" , "https://cdn.discordapp.com/attachments/443714829199343616/448209500810248202/db528lex5xk01.jpg" , "https://cdn.discordapp.com/attachments/443714829199343616/448209703772880896/28685326_206257853336105_6988838270872322048_n.jpg" , "https://media.discordapp.net/attachments/443714829199343616/448210659180675073/chats-wife-online-our-daughter-lost-her-first-tooth-7-38-32643898.png?width=371&height=676" , "https://cdn.discordapp.com/attachments/447809619541360650/450534615250239488/r1jxhmvc9tb01.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450534935715905546/slow-computer-meme-funny.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450534935715905546/slow-computer-meme-funny.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450534935715905547/d3abfb2223e98bdde487a1d66da9bc98d6cdae36def600591153f151930e693a.gif" , "https://i.redd.it/5kcegdc70f011.png" , "https://i.redd.it/cpzcen89ue011.png" , "https://i.redd.it/kuqzrbt5ag011.jpg" , "https://i.redd.it/q3dtcnfv9i011.png" , "https://cdn.discordapp.com/attachments/447809619541360650/450542747485470721/8mWdz35.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450542747980660760/otyl2wtqs0vz.jpg" , "https://cdn.discordapp.com/attachments/447809619541360650/450542747980660763/dark-humour-memes-10.jpg" , "https://i.redd.it/1g984z0ibh011.jpg" , "https://cdn.discordapp.com/attachments/445806579137249296/450542754750267412/image-2.png" , "https://cdn.discordapp.com/attachments/449979940050567168/450544658020433921/image-9-1.png" , "https://cdn.discordapp.com/attachments/449979940050567168/450544658020433920/images_8.jpeg"]))
    await ctx.send(embed=embed)
    
                
@bot.command()
@commands.cooldown(1,10.0,type=commands.BucketType.user)
async def ping(ctx):
    """Checks how long did you and the bot reply"""
    resp = await ctx.send('Pong! Loading...')
    diff = resp.created_at - ctx.message.created_at
    await resp.edit(content=f'Pong! That took {1000*diff.total_seconds():.1f}ms.') 
    
        
@bot.command(pass_context=True)
async def avatar(ctx,*,user:discord.Member=None):
    """Checks client's profile picture"""
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
    """Whatever the fuck you say and  bot will say it aswell"""
    await ctx.send(message)
    
@bot.command(pass_context=True)
async def coinflip(ctx):
    """Flip the coin for luck"""
    coin = ['Heads', 'Tails']
    embed=discord.Embed(title='**Coinflip**', description='The coin landed on {}!'.format(random.choice(coin)), color=000000)
    await ctx.channel.send(embed=embed)

@bot.command()
async def warns(ctx, member: discord.Member = None):
    """
    Checks the warns of a user (staff-only)
    """
    if not ("Staff" in [role.name for role in ctx.message.author.roles]):
        embed=discord.Embed(title='No perms!', description='Sorry you dont have perms to do this!', color=000000)
        return await ctx.send(embed=embed)
    if member == None:
        embed = discord.Embed(title='How to use',color=mc, description='Guide on how to see the users warns: do `%warns <member>`')
        return await ctx.send(embed=embed)
    warnlist = warnmngr.get_warns(userid=member.id)
    embed=discord.Embed(title=f'Warns for {member.name}', color=000000)
    newWarns = []
    for i in range(len(warnlist)):
        cw = warnlist[i]
    embed.add_field(name=str(i+1), value=str(cw[2]), inline=False)
    await ctx.send(embed=embed)
 
    
@bot.command(aliases=["fortnite", "fort", "fn", "fnstats"])
async def ftn(ctx, platform=None, *, player=None):
    if platform is None:
        el = discord.Embed(title="Error:", description="You didn't specify a platform: w/ftn <platform> <username>",
                           color=000000)
        return await ctx.send(embed=el)  # Adding return here ends the script from executing further within the func.
    if player is None:
        ell = discord.Embed(title="Error:", description="You didn't specify a username: w/ftn <platform> <username>",
                            color=000000)
        return await ctx.send(embed=ell)

    msg = await ctx.send("This command can be very slow, please be patient :slight_smile:")
    headers = {'TRN-Api-Key': '6213ef07-38e1-4520-8c1a-93f756016770'}
    r = requests.get(f'https://api.fortnitetracker.com/v1/profile/{platform}/{player}', headers=headers)
    stats = json.loads(r.text)
    stats = stats["stats"]

    # What we want to do here is create a list of three Embeds to send. You're going to treat each section of the JSON response individually.
    # Instead of viewing the error as a whole, we can see each "p" section (p2, p9, etc) as its own response, by setting up three try/except blocks.
    # If one is successful, we move on to the next. Same goes if one fails.
    # At the end, we'll check to see if ALL of them failed and if so, that account does not exist.
    # This way, as long as one response is valid, the command returns successfully.

    list_of_embeds = []

    # Solos
    try:
        Solo = stats["p2"]
        KDSolo = Solo["kd"]
        KDSolovalue = KDSolo["value"]
        TRNSoloRanking = Solo["trnRating"]
        winsDataSolo = Solo["top1"]
        Soloscore = Solo["score"]
        SoloKills = Solo["kills"]
        SoloMatches = Solo["matches"]
        SoloKPG = Solo["kpg"]
        SoloTop10 = Solo["top10"]

        SoloTop25 = Solo["top25"]

        embed = discord.Embed(colour=000000)
        embed.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Solo stats:")
        embed.add_field(name="K/D", value=KDSolovalue)
        embed.add_field(name="Score", value=Soloscore["value"])
        embed.add_field(name="Wins", value=winsDataSolo["value"])
        embed.add_field(name="TRN Rating", value=TRNSoloRanking["value"])
        embed.add_field(name="Kills", value=SoloKills["value"], inline=True)
        embed.add_field(name="Matches Played:", value=SoloMatches["value"], inline=True)
        embed.add_field(name="Kills Per Game:", value=SoloKPG["value"], inline=True)
        embed.add_field(name="Top 10:", value=SoloTop10["value"])
        embed.add_field(name="Top 25:", value=SoloTop25["value"])
        list_of_embeds.append(
            embed)  # Using the list.append(item) command will add (append) an entry to a list, here a discord.Embed.
    except KeyError:
        pass  # Using a pass expression essentially tells the script "Ignore this and continue as usual".

    # As you can see, if things go well, we have one embed appended to the list. If not, we have none.
    # We'll do this for the next two now.

    # Duos
    try:
        Duo = stats["p10"]
        KDDuo = Duo["kd"]
        KDDuovalue = KDDuo["value"]
        TRNDuoRanking = Duo["trnRating"]
        winsDataDuo = Duo["top1"]
        Duoscore = Duo["score"]
        DuoKills = Duo["kills"]
        DuoMatches = Duo["matches"]
        DuoKPG = Duo["kpg"]
        DuoTop5 = Duo["top5"]
        DuoTop12 = Duo["top12"]

        duo = discord.Embed(color=000000)
        duo.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Duo stats:")
        duo.add_field(name="K/D", value=KDDuovalue)
        duo.add_field(name="Score", value=Duoscore["value"])
        duo.add_field(name="Wins", value=winsDataDuo["value"])
        duo.add_field(name="TRN Rating", value=TRNDuoRanking["value"])
        duo.add_field(name="Kills", value=DuoKills["value"], inline=True)
        duo.add_field(name="Matches Played:", value=DuoMatches["value"], inline=True)
        duo.add_field(name="Kills Per Game:", value=DuoKPG["value"], inline=True)
        duo.add_field(name="Top 5:", value=DuoTop5["value"])
        duo.add_field(name="Top 12:", value=DuoTop12["value"])
        list_of_embeds.append(duo)
    except KeyError:
        pass

    # Squads
    try:
        Squad = stats["p9"]
        KDSquad = Squad["kd"]
        KDSquadvalue = KDSquad["value"]
        TRNSquadRanking = Squad["trnRating"]
        winsDataSquad = Squad["top1"]
        Squadscore = Squad["score"]
        SquadKills = Squad["kills"]
        SquadMatches = Squad["matches"]
        SquadKPG = Squad["kpg"]
        SquadTop3 = Squad["top3"]
        SquadTop6 = Squad["top6"]

        squad = discord.Embed(color=000000)
        squad.set_author(icon_url="https://i.ebayimg.com/images/g/6ekAAOSw3WxaO8mr/s-l300.jpg", name="Squad stats:")
        squad.add_field(name="K/D", value=KDSquadvalue)
        squad.add_field(name="Score", value=Squadscore["value"])
        squad.add_field(name="Wins", value=winsDataSquad["value"])
        squad.add_field(name="TRN Rating", value=TRNSquadRanking["value"])
        squad.add_field(name="Kills", value=SquadKills["value"], inline=True)
        squad.add_field(name="Matches Played:", value=SquadMatches["value"], inline=True)
        squad.add_field(name="Kills Per Game:", value=SquadKPG["value"], inline=True)
        squad.add_field(name="Top 3:", value=SquadTop3["value"])
        squad.add_field(name="Top 6:", value=SquadTop6["value"])
        list_of_embeds.append(squad)
    except KeyError:
        pass

    # Now that we've gone through all three sections, we need to make sure that there is at least one embed that did not fail.
    # Basically, we need to make sure that the list of embeds is not empty.

    if not list_of_embeds:  # For whatever reason, Python treats empty arrays as False literals. Use it to your advantage!
        await msg.delete()
        error = discord.Embed(color=0xE73C24)
        error.add_field(name="Error:", value="Invalid username, please try again with another name")
        await ctx.send(embed=error)
        print(error)
    else:
        # If the embed list if not empty, we'll create a for loop and send each.
        await msg.delete()
        for embed in list_of_embeds:
            await ctx.send(embed=embed)
            
            
            
@bot.command(aliases=["si", "serverinformation"])
async def serverinfo(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(icon_url=ctx.message.guild.icon_url, name="{}'s info".format(ctx.message.guild.name))
        embed.add_field(name="Name:", value=ctx.message.guild.name, inline=True)
        embed.add_field(name="ID:", value=ctx.message.guild.id, inline=True)
        embed.add_field(name="Region:", value=ctx.message.guild.region, inline=True)
        embed.add_field(name="Members:", value=len(ctx.message.guild.members), inline=True)
        embed.add_field(name="Humans:", value=ctx.message.guild.member_count, inline=True)
        bot_count = sum(m.bot for m in ctx.guild.members)
        embed.add_field(name="Bots:", value=bot_count, inline=True)
        embed.add_field(name="Roles:", value=len(ctx.message.guild.roles), inline=True)
        embed.add_field(name="Text channels:", value=len(ctx.guild.text_channels))
        embed.add_field(name="Categories", value=len(ctx.guild.categories))
        embed.add_field(name="Owner ID:", value=ctx.guild.owner.id)
        embed.add_field(name="Server Created At:", value=str(ctx.guild.created_at)[:19], inline=True)
        embed.add_field(name="Owner:", value=ctx.message.guild.owner, inline=True)
        embed.set_thumbnail(url=ctx.message.guild.icon_url)
        embed.set_footer(icon_url=ctx.message.guild.icon_url, text=f"{ctx.message.guild.name} | By: {ctx.guild.owner.name}#{ctx.guild.owner.discriminator}")
        await ctx.send(embed=embed)
        
        
                
bot.run(os.getenv('TOKEN'))
