import asyncio
import random
import time
import discord
import nekos
from discord.ext import commands


class HelpFormat:
    def __init__(self):
        self.raw_colors = ['discord.Colour.blue()', 'discord.Colour.blurple()', 'discord.Colour.dark_blue()', 'discord.Colour.dark_gold()', 'discord.Colour.dark_green()', 'discord.Colour.dark_grey()', 'discord.Colour.dark_magenta()', 'discord.Colour.dark_orange()', 'discord.Colour.dark_purple()', 'discord.Colour.dark_red()', 'discord.Colour.dark_teal()','discord.Colour.darker_grey()', 'discord.Colour.gold()', 'discord.Colour.green()', 'discord.Colour.greyple()', 'discord.Colour.light_grey()', 'discord.Colour.lighter_grey()', 'discord.Colour.magenta()', 'discord.Colour.orange()', 'discord.Colour.purple()', 'discord.Colour.red()', 'discord.Colour.teal()']


    async def get_colors(self):
        return self.raw_colors

    async def commands(self):
        return {'Anime':[],'Fun':[]}


class Mod(HelpFormat):
    def __init__(self,obj): 
        self.msg=obj
    async def over_all(self):
        emb=discord.Embed(title='Mod Commands')
        emb.set_thumbnail(url=self.msg.guild.icon)
        emb.add_field(name='',value='')
        emb.add_field(name='',value='')
        emb.add_field(name='',value='')
        emb.add_field(name='',value='')
        emb.add_field(name='',value='')
        emb.add_field(name='',value='')
        emb.set_footer(text='Use s.help {command_name} to get more details on a command')
        message=await self.msg.send(embed=emb)
        return message.id
    



class Fun(HelpFormat):
    def __init__(self,obj):
        super().__init__()
        self.msg=obj


    async def command_name(self,name:str):
        await eval(f"{'self'}.{name}()")

    async def command_list(self):
        return ['lizard', 'dog', 'neko_gif', 'lewd', 'holo', 'slap', 'why', 'waifu', '8ball', 'joke', 'erofeet', 'poke', 'avatar', 'cat', 'kemonomimi',
         'pi', 'owoify', 'randomshow', 'randomfact', 'randomanime', 'textcat', 'randommovie', 'neko1', 'neko', 'fox_girl', 'fox', 'hug',
          'pfp', 'wallpaper', 'meow', 'tickle', 'gecg', 'kiss', 'add_adatus', 'feed']

    async def over_all(self,owner_icon):
        emb=discord.Embed(title='Fun Commands',colour=eval(random.choice(self.raw_colors)))
        emb.set_thumbnail(url=self.msg.guild.icon_url)
        emb.add_field(name='Lizard',value='s.lizard')
        emb.add_field(name='Dog',value='s.dog')
        emb.add_field(name='Neko Gif',value='s.neko-gif')
        emb.add_field(name='Lewd',value='s.lewd')
        emb.add_field(name='Holo',value='s.holo')
        emb.add_field(name='Slap',value='s.slap @User1 @User2')
        emb.add_field(name='Why',value='s.why')
        emb.add_field(name='Waifu',value='s.waifu')
        emb.add_field(name='8ball',value='s.8ball Will I pass the exam?')
        emb.add_field(name='Joke',value='s.joke')
        emb.add_field(name='Erofeet',value='s.erofeet')
        emb.add_field(name='Poke',value='s.poke @User1 @User2')
        emb.add_field(name='Avatar',value='s.avatar')
        emb.add_field(name='Cat',value='s.cat')
        emb.add_field(name='Kemonomimi',value='s.kemonomimi')
        emb.add_field(name='Pi',value='s.pi')
        emb.add_field(name='Owoify',value='s.owoify Hello there, how are you?')
        emb.add_field(name='Random_Show',value='s.randomshow')
        emb.add_field(name='Random_Fact',value='s.randomfact')
        emb.add_field(name='Random_Anime',value='s.randomanime')
        emb.add_field(name='Random_Movie',value='s.randommovie')
        emb.add_field(name='TextCat',value='s.textcat')
        emb.add_field(name='Neko1',value='s.neko1')
        emb.add_field(name='Neko',value='s.neko')
        emb.add_field(name='Fox_Girl',value='s.fox_girl')
        emb.add_field(name='Fox',value='s.fox')
        emb.add_field(name='Hug',value='s.hug @User1 @User2')
        emb.add_field(name='Pfp', value='s.pfp @User1 @User2')
        emb.add_field(name='Wallpaper', value='s.wallpaper')
        emb.add_field(name='Meow',value='s.meow')
        emb.add_field(name='Tickle',value='s.tickle @User1 @User2')
        emb.add_field(name='Gecg',value='s.gecg')
        emb.add_field(name='Kiss',value='s.kiss @User1 @User2')
        # emb.add_field(name='Add_Status',value='s.add_status League of Legends')
        emb.add_field(name='Feed',value='s.feed @User1 @User2')
        emb.set_footer(text='Use s.help {command_name} to get more details on a command (s.help fox)',icon_url=owner_icon)
        message=await self.msg.send(embed=emb)
        return message.id


    async def kiss(self):
        emb=discord.Embed(title='Kiss',description='Sends a kiss gif to a person tagged',colour=eval(random.choice(self.raw_colors)))
        emb.set_thumbnail(url=nekos.img('kiss'))
        emb.add_field(name='s.kiss',value='s.kiss @Cheng Yue#2945')
        emb.set_footer(text='More than one person can be mentioned for this command')
        await self.msg.send(embed=emb)


    async def add_status(self):
        emb=discord.Embed(title='add_status',description='Submit a status for the bot',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.add_status',value='s.add_status *watching* Hello Kitty')
        emb.set_footer(text='Indicate the status type before the status name')
        await self.msg.send(embed=emb)

    async def neko(self):
        emb = discord.Embed(title='Neko', description='Sends a neko picture', colour=eval(random.choice(self.raw_colors)))
        emb.set_thumbnail(url=nekos.img('neko'))
        emb.add_field(name='s.neko', value='s.neko')
        await self.msg.send(embed=emb)

    async def why(self):
        emb=discord.Embed(title='Why',description='Sends a question starting with why',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.why',value='s.why')
        await self.msg.send(embed=emb)

    async def eball(self):
        emb=discord.Embed(title='8ball',description='Ask a yes or no question',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.8ball',value='s.8ball Will I pass the exam tomorrow?')
        await self.msg.send(embed=emb)

    async def erofeet(self):
        emb=discord.Embed(title='erofeet',description='Sends a ero feet of a random anime character',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.erofeet',value='s.erofeet')
        await self.msg.send(embed=emb)

    async def avatar(self):
        emb=discord.Embed(title='s.avatar',description='Generates a random aniem girl and sends it in embed',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.avatar',value='s.avatar @Cheng Yue#2945')
        emb.set_footer(text='You can mention more than 1 user by adding space')
        await self.msg.send(embed=emb)

    async def kemonomimi(self):
        emb=discord.Embed(title='s.kemonomimi',description='Sends a kemonomimi, give it a try',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.kemonomimi', value='s.kemonomimi')
        await self.msg.send(embed=emb)

    async def owoify(self):
        emb=discord.Embed(title='Owoify',description='Replaces certain words to make it look like owo, give it a try!',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.owoify',value='s.owoify Hello there Alice, how are you today?')
        await self.msg.send(embed=emb)

    async def randomfact(self):
        emb=discord.Embed(title='randomfact',description='Sends a randomfact to you about something random',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.randomfact',value='s.randomfact')
        await self.msg.send(embed=emb)


    async def textcat(self):
        emb=discord.Embed(title='Textcat',description='Sends a text cat emoji',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.textcat',value='s.textcat')
        await self.msg.send(embed=emb)


    async def neko1(self):
        emb=discord.Embed(title='Neko1',description='Sends you a neko picture, can be a little lewd',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.neko1',value='s.neko1')
        await self.msg.send(embed=emb)


    async def fox_girl(self):
        emb=discord.Embed(title='Fox Girl',description='Sends you a picture of a fox girl, like neko except fox',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.fox_girl',value='s.fox_girl or s.fox-girl')
        await self.msg.send(embed=emb)

    async def hug(self):
        emb=discord.Embed(title='Hug',description='Sends a hug gif adds the names of the user(s) you mention',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.hug',value='s.hug @Cheng Yue#2945 @Alice#3545')
        emb.set_footer(text='You can mention more than 1 user by adding space')
        await self.msg.send(embed=emb)


    async def wallpaper(self):
        emb = discord.Embed(title='Wallpaper', description='Sends you a random picture for a wallpaper',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.wallpaper',value='s.wallpaper')
        await self.msg.send(embed=emb)

    async def meow(self):
        emb = discord.Embed(title='Meow', description='Sends a random picture of a cat',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.meow', value='s.meow')
        await self.msg.send(embed=emb)


    async def tickle(self):
        emb = discord.Embed(title='Tickle', description='Sends an embed tickle gif with the names of the users you mentioned',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='',value='')
        await self.msg.send(embed=emb)


    async def gecg(self):
        emb = discord.Embed(title='Gecg', description='Sends a funny post about genetically engineered cat-girls',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.gecg',value='s.gecg, cat-girl, or cat_girl')
        await self.msg.send(embed=emb)


    async def holo(self):
        emb = discord.Embed(title='Holo', description='Sends a picture of the anime character Holo',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.holo',value='s.holo')
        await self.msg.send(embed=emb)


    async def feed(self):
        emb = discord.Embed(title='Feed', description='Sends an gif of feeding someone and adds the users you mentioned in the embed',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='',value='s.feed @Cheng Yue#2945 @Alice#2352')
        emb.set_footer(text='More than 1 user can be mentioned by adding space')
        await self.msg.send(embed=emb)

    async def lizard(self):
        emb = discord.Embed(title='Lizard', description='Sends a picture of a lizard :)',colour=eval(random.choice(self.raw_colors)))
        emb.set_thumbnail(url=nekos.img('lizard'))
        emb.add_field(name='s.lizard',value='s.lizard')
        await self.msg.send(embed=emb)


    async def dog(self):
        emb = discord.Embed(title='Dog', description='Sends a picture of a dog, sometimes a gif',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.dog',value='s.dog')
        await self.msg.send(embed=emb)


    async def neko_gif(self):
        emb = discord.Embed(title='Neko Gif', description='Sends a gif of a neko',colour=eval(random.choice(self.raw_colors)))
        emb.set_thumbnail(url=nekos.img('neko'))
        emb.add_field(name='s.neko-gif',value='s.neko_gif, s.nekogif, or s.neko-gif')
        await self.msg.send(embed=emb)


    async def lewd(self):
        emb = discord.Embed(title='Lewd', description='Send a NSFW lewd (mostly anime)picture, sometimes gif',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.lewd',value='s.lewd')
        emb.set_footer(text='Channel must have NSFW enabled for this command to work')
        await self.msg.send(embed=emb)


    async def slap(self):
        emb = discord.Embed(title='Slap', description='Sends a slap gif and adds the name(s) of the user(s) you mention',colour=eval(random.choice(self.raw_colors)))
        emb.set_thumbnail(url=nekos.img('slap'))
        emb.add_field(name='s.slap',value='s.slap @Cheng Yue#2945 @Jayce#2342')
        emb.set_footer(text='More than one user can be mentioned')
        await self.msg.send(embed=emb)


    async def waifu(self):
        emb = discord.Embed(title='Waifu', description='Sends a random anime waifu girl',colour=eval(random.choice(self.raw_colors)))
        emb.set_thumbnail(url=nekos.img('waifu'))
        emb.add_field(name='s.waifu',value='s.waifu')
        await self.msg.send(embed=emb)


    async def joke(self):
        emb = discord.Embed(title='Joke', description='Generates a random joke, sometimes funny ,but not always',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.joke',value='s.joke')
        await self.msg.send(embed=emb)


    async def poke(self):
        emb = discord.Embed(title='Poke', description='Generates a poke gif and adds the names of the users you mentioned',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='',value='s.poke @Cheng Yue#2923 @Katie#2334')
        await self.msg.send(embed=emb)


    async def cat(self):
        emb = discord.Embed(title='Cat', description='Generates a random cat picture',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.cat',value='s.cat')
        await self.msg.send(embed=emb)


    async def pi(self):
        emb = discord.Embed(title='Pi', description='Sends a random pi fact',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.pi',value='s.pi')
        await self.msg.send(embed=emb)


    async def randomshow(self):
        emb = discord.Embed(title='Random Show', description='Generates a random show',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.randomshow',value='s.randomshow')
        await self.msg.send(embed=emb)


    async def randomanime(self):
        emb = discord.Embed(title='Random Anime', description='Generates a random anime',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.randomanime',value='s.randomanime, s.random_anime, or s.random-anime')
        await self.msg.send(embed=emb)


    async def randommovie(self):
        emb = discord.Embed(title='Random Movie', description='Generates a random movie',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.randommovie',value='s.randommovie, s.random_movie, or s.random-movie')
        await self.msg.send(embed=emb)


    async def fox(self):
        emb = discord.Embed(title='Fox', description='Generates a random fox picture',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.fox',value='s.fox')
        await self.msg.send(embed=emb)


    async def pfp(self):
        emb = discord.Embed(title='Pfp', description='Sends the URL picture of the mentioned user(s)',colour=eval(random.choice(self.raw_colors)))
        emb.add_field(name='s.pfp',value='s.pfp @Cheng Yue#2341 @Katie#2341')
        emb.set_footer(text='More than one user can be mentioned by adding space')
        await self.msg.send(embed=emb)




class League(HelpFormat):
    def __init__(self,obj):
        self.msg=obj
    async def over_all(self):
        emb = discord.Embed(title='League Commands')
        emb.set_thumbnail(url=self.msg.guild.icon)
        emb.add_field(name='', value='')
        emb.add_field(name='', value='')
        emb.add_field(name='', value='')

        emb.set_footer(text='Use s.help {command_name} to get more details on a command')

        message=await self.msg.send(embed=emb)
        return message.id


class Anime(HelpFormat):
    def __init__(self,obj):
        self.msg=obj
    async def over_all(self,owner_icon):
        emb=discord.Embed(title='Anime Commands')
        emb.set_thumbnail(url=self.msg.guild.icon)
        emb.add_field(name='',value='')
        emb.add_field(name='',value='')
        emb.add_field(name='',value='')
        emb.set_footer(text='Use s.help {command_name} to get more details on a command',icon_url=owner_icon)

        message=await self.msg.send(embed=emb)
        return message.id



class Help(commands.Cog):
    def __init__(self,client):
        self.bot=client
        #NOTE: Only fun commands are added in the list at the moment
        self.commands=['fun','mod','anime','lizard', 'dog', 'neko_gif', 'lewd', 'holo', 'slap', 'why', 'waifu', '8ball', 'joke', 'erofeet', 'poke', 'avatar', 'cat', 'kemonomimi', 'pi', 'owoify', 'cms', 'randomshow', 'randomfact', 'randomanime', 'textcat', 'randommovie', 'neko1', 'neko', 'fox_girl', 'fox', 'hug', 'pfp', 'wallpaper', 'meow', 'tickle', 'gecg', 'kiss', 'add_adatus', 'feed']
        self.help_message={}
        self.raw_colors=None
        self.command_list=None
        asyncio.run(self.tasks())


    async def set_color(self):
        self.raw_colors=await HelpFormat().get_colors()

    async def help_commands(self):
        self.command_list=await HelpFormat().commands()


    async def tasks(self):
        tks=[self.set_color,self.help_commands]
        for i in tks:
            await i()

    #TODO: Add a time of when the help command was requested from the user or when the help message was created

    async def adding_command_list(self):
        """
        Add all the command names into the self.commands variable
        """
        command_aliases=['anime','fun','mod','nekogif'] #This includes the aliases and the cog names
        #NOTE: fun command added
        for i in self.bot.commands:
            self.commands.append(i.name)
        
        for i in command_aliases:
            self.commands.append(i)


    """
    External None Discord Events
    """
    async def clear_help_messages(self):
        while True:
            await asyncio.sleep(10)
            for i in self.help_message:
                if self.help_message[i]['time'] <= time.time():
                    del self.help_message[i]
                    await self.help_message[i]['msg'].delete()


    @commands.Cog.listener('on_ready')
    async def help_ready(self):
        # background_events=asyncio.wait([self.clear_help_messages()])
        # await background_events
        print("Help commands ready!")

    async def fun_commands(self,msg):
        emb=discord.Embed(title='Anime Commands',colour=discord.Colour.blue())
        emb.set_thumbnail(url=msg.guild.icon)
        emb.add_field(name='cmd1',value='description')
        emb.set_footer(text=f'Requested by: {msg.author.name}',icon_url=msg.author.avatar_url)



    # @commands.Cog.listener('on_reaction_add')
    # async def help_reaction_add(self,emote,user):
    #     me = self.bot.get_user(185181025104560128).avatar_url
    #     if emote.emoji == '❤' and emote.message.id == self.help_message[user.id].id:
    #         await Fun(emote.channel).over_all(me)
    #     if emote.emoji == '💚' and emote.message.id == self.help_message[user.id].id:
    #         await Anime(emote.channel).over_all(me)


    async def help_alone(self,msg):
        # help_emotes = ['❤', '💚']
        emb=discord.Embed(title='Help Menu',colour=eval(random.choice(self.raw_colors)),description='s.help {command_name}')
        emb.set_thumbnail(url=msg.guild.icon_url)
        # emb.add_field(name='Anime Commands', value='s.help anime',inline=True)
        emb.add_field(name='Fun Commands', value='s.help fun')
        emb.set_footer(text=f'{msg.message.created_at} UTC',icon_url=msg.author.avatar_url)
        message=await msg.send(embed=emb)
        self.help_message[msg.author.id]={'time':time.time()+300,'msg':message}

        # for i in help_emotes:
            # await message.add_reaction(i)
        self.help_message[msg.author.id]=[message.id,time.time()+300]

    async def help_command(self,msg,name):
        me=self.bot.get_user(185181025104560128)
        if name.lower() not in self.commands:
            await msg.send(f"Command **{name}** is not found")
        

        if name.lower() == 'mod':
            await Mod(msg).over_all()

        if name.lower() == 'anime':
            await Anime(msg).over_all(me)

        if name.lower() == 'fun':
            await Fun(msg).over_all(me.avatar_url)

        else:
            if name.lower() in await Fun(msg).command_list():
                await Fun(msg).command_name(name.lower())

    @commands.command()
    async def help(self,msg,*,name=None):
        if name == None:
            await self.help_alone(msg)

        if name != None:
            await self.help_command(msg,name)



def setup(bot):
    bot.add_cog(Help(bot))
