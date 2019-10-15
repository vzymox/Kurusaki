import nekos
import string
import discord
from discord.ext import commands
import asyncio
import json
import requests as rq
import random


"""
This class of `discord.commands.Cog` mainly consists of functions from the library `nekos`
"""


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lewdImages=json.load(open('lewdImages.json'))
        self.chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.nsfw = ['feet', 'yuri', 'trap', 'erofeet', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'lewdk', 'lewd', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'nsfw_avatar','gasm', 'anal', 'hentai', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'femdom', 'spank', 'erok', 'boobs', 'smallboobs', 'ero',]
        self.sfw = ['ngif', 'waifu', 'lizard', 'holo', 'slap', 'poke', 'kemonomimi', 'gecg', 'pat','feed', 'tickle', 'meow', 'wallpaper', 'hug', 'fox_girl', '8ball', 'cuddle', 'kiss', 'neko']
        self.facts = json.load(open('facts.json', encoding='utf-8'))
        self.raw_color=['discord.Colour.blue()', 'discord.Colour.blurple()', 'discord.Colour.dark_blue()', 'discord.Colour.dark_gold()', 'discord.Colour.dark_green()', 'discord.Colour.dark_grey()', 'discord.Colour.dark_magenta()', 'discord.Colour.dark_orange()', 'discord.Colour.dark_purple()', 'discord.Colour.dark_red()', 'discord.Colour.dark_teal()','discord.Colour.darker_grey()', 'discord.Colour.gold()', 'discord.Colour.green()', 'discord.Colour.greyple()', 'discord.Colour.light_grey()', 'discord.Colour.lighter_grey()', 'discord.Colour.magenta()', 'discord.Colour.orange()', 'discord.Colour.purple()', 'discord.Colour.red()', 'discord.Colour.teal()']


    @commands.command(guild_only=True)
    async def kiss(self,msg,*users:discord.Member):
        """
        Sends a kiss anime gif embed message with the tagged user's names
        Command: s.kiss <@Users> (can mention multiple users)
        Example: s.kiss @Katie @Yukinno
        """
        if users:
            emb=discord.Embed(description="{} kissed {}".format(msg.author.nick,", ".join([user.nick for user in users])),colour=eval(random.choice(self.raw_color)))
            emb.set_image(url=nekos.img('kiss'))
            await msg.send(embed=emb)
        else:
            await msg.send("Please mention a user")

    @commands.command(hidden=True)
    async def add_adatus(self,msg,*,name):
        pass
        #TODO: Make the request and title submitted to the database

    @commands.command()
    async def why(self, msg):
        """
        Sends a random question starting with why
        Command: s.why
        Example: s.why
        """
        emb = discord.Embed(description=nekos.why(),colour=eval(random.choice(self.raw_color)))
        await msg.send(embed=emb)

    @commands.command(name='8ball')
    async def eball(self, msg, *, pack):
        """
        Sends a random answer for your question you ask the 8ball
        Command: s.8ball <Your question>
        Example: s.8ball Will it rain today?
        """
        dc = nekos.eightball()._dict
        emb = discord.Embed(description=dc['text'],colour=eval(random.choice(self.raw_color)))
        emb.set_image(url=dc['image'])
        await msg.send(embed=emb)

    #NSFW COMMANDS HERE
    @commands.is_nsfw()
    @commands.command()
    async def erofeet(self, msg):
        """
        Sends an anime girl's foot pointing at the screen (This command can only be used in an NSFW channel)
        Command: s.erofeet
        Example: s.erofeet
        """
        emb = discord.Embed(title='Ero Feet',colour=eval(random.choice(self.raw_color)))
        emb.set_image(url=nekos.img('erofeet'))
        await msg.send(embed=emb)


    @commands.command()
    async def avatar(self,msg):
        """
        Sends a random anime avatar picture
        Command: s.avatar
        Example: s.avatar
        """
        emb = discord.Embed(colour=eval(random.choice(self.raw_color)))
        emb.set_image(url=nekos.img('avatar'))
        await msg.send(embed=emb)



    @commands.is_nsfw()
    @commands.command()
    async def kemonomimi(self, msg):
        """
        Sends you a kemonomimi(humanoid with other body parts like horns) (This command can only be used in NSFW channel)
        Command: s.kemonomimi
        Example: s.kemonomimi
        """
        emb = discord.Embed(title='kemonomimi')
        emb.set_image(url=nekos.img('kemonomimi'))
        await msg.send(embed=emb)


    @commands.command()
    async def owoify(self, msg, *, Msg:str):
        """
        Edits the message you sent and add owo in them
        Command: s.owoify <Your message>
        Example: s.owoify Hello there (Results: Hewwo thewe)
        """
        emb = discord.Embed(title=msg.author.display_name,description=nekos.owoify(Msg))
        await msg.send(embed=emb)
        await msg.delete()


    @commands.command()
    async def randomfact(self, msg):
        """
        Get a random fact about random things
        Command: s.randomfact
        Example: s.randomfact
        """
        emb = discord.Embed(description=nekos.fact())
        await msg.send(embed=emb)

    @commands.command()
    async def textcat(self, msg):
        """
        Sends a text version of a cat face
        Command: s.textcat
        Example: s.textcat (Result: b(=^‥^=)o)
        """
        emb = discord.Embed(title=msg.author.display_name,description=nekos.textcat())
        await msg.send(embed=emb)
        await msg.delete()

    @commands.command()
    async def neko1(self, msg):
        """
        Sends a neko girl pictures in embeded format.(This one doesn't have to be in an NSFW channel)
        Command: s.neko1
        Example: s.neko1
        """
        emb = discord.Embed(title='Neko')
        emb.set_image(url=nekos.img('neko'))
        await msg.send(embed=emb)

    @commands.command(aliases=['fox-girl'])
    async def fox_girl(self, msg):
        """
        Sends you an embeded format of an anime fox girl
        Command: s.fox_girl
        Example: s.fox_girl
        """
        emb = discord.Embed(title='Fox Girl')
        emb.set_image(url=nekos.img('fox_girl'))
        await msg.send(embed=emb)

    @commands.command()
    async def hug(self, msg, *users:discord.Member):
        """
        Sends a hug GIF or image with the users that you mention
        Command: s.hug <@users> (More than 1 users can be mentioned)
        Example: s.hug @Kurusaki @Ahri @Tempest
        """
        if users:

            targets = [user.display_name for user in users]
            emb = discord.Embed(description='{} hugged {}'.format(msg.author.display_name, ', '.join(targets)))
            emb.set_image(url=nekos.img('hug'))
            await msg.send(embed=emb)
        else:
            await msg.send("Please mention a user")
    @commands.command()
    async def wallpaper(self, msg):
        """
        Sends a wallpaper
        Command: s.wallpaper
        Example: s.wallpaper
        """
        link = nekos.img('wallpaper')
        emb = discord.Embed(title='Wallpaper', url=link)
        emb.set_image(url=link)
        await msg.send(embed=emb)

    @commands.command()
    async def meow(self, msg):
        """
        Sends you an image of a cat, but without the cat fact
        Command: s.meow
        Example: s.meow
        """
        emb = discord.Embed(title='Meow')
        emb.set_image(url=nekos.img('meow'))
        await msg.send(embed=emb)

    @commands.command()
    async def tickle(self, msg, *users:discord.Member):
        """
        Sends a GIF or image of someone being tickled and adds the names of the users you mentioned to the embed
        Command: s.tickle (More than 1 users can be mentioned)
        Example: s.tickle @Tempest @Ahri @Yuno @Janna @Raka
        """
        if users:
            targets = [user.display_name for user in users]
            emb = discord.Embed(description='{} tickled {}'.format(
                msg.author.display_name, ', '.join(targets)))
            emb.set_image(url=nekos.img('tickle'))
            await msg.send(embed=emb)
        else:
            await msg.send("Please mention a user")
    @commands.command(aliases=['cat-girl','cat_girl'])
    async def gecg(self, msg):
        """
        A memee about genetically engineered Catgirls
        Command: s.gecg
        Example: s.gecg
        """
        emb = discord.Embed(title='Gecg')
        emb.set_image(url=nekos.img('gecg'))
        await msg.send(embed=emb)

    @commands.command()
    async def holo(self, msg):
        """
        Returns an image of Holo from Spice and Wolf in embeded format
        Command: s.holo
        Example: s.holo
        """
        emb = discord.Embed(title='Holo')
        emb.set_image(url=nekos.img('holo'))
        await msg.send(embed=emb)

    @commands.command()
    async def feed(self, msg, *users: discord.Member):
        """
        Return an image of an anime character feeding someone and the users you mentioned will be added in the embed
        Command: s.feed <@users>
        Example: s.feed @Janna @KowaiiNeko @Cheng Yue
        """
        if users:
            targets = [user.display_name for user in users]
            emb = discord.Embed(description='{} feed {}'.format(
                msg.author.display_name, ', '.join(targets)))
            emb.set_image(url=nekos.img('feed'))
            await msg.send(embed=emb)
        else:
            await msg.send("Please mention a user")
    @commands.command()
    async def lizard(self, msg):
        """
        Returns an image of a lizard ::)
        Command: s.lizard
        Example: s.lizard
        """
        emb = discord.Embed(title="Lizard")
        emb.set_image(url=nekos.img('lizard'))
        await msg.send(embed=emb)

    @commands.command()
    async def dog(self, msg):
        """
        Send a picture of random dog along with some facts about them
        Command: s.dog
        Example: s.dog
        """
        r = rq.Session().get('https://random.dog/woof.json')
        if r.status_code == 200:
            emb = discord.Embed(description=random.choice(
                self.facts['animals']['dogs']))
            emb.set_image(url=r.json()['url'])
            await msg.send(embed=emb)

    @commands.command(aliases=['nekogif','neko-gif'])
    async def neko_gif(self, msg):
        """
        Sends you a neko gif :D
        Command: s.neko_gif or s.nekogif or s.nekoGif
        Example: s.neko_gif or s.nekogif or s.nekoGif
        """
        emb = discord.Embed(title="Neko")
        emb.set_image(url=nekos.img('ngif'))
        await msg.send(embed=emb)

    @commands.is_nsfw()
    @commands.command()
    async def lewd(self, msg):
        """
        Sends lewd/hentai anime picutres or gif.
        Command: s.lewd (This is made to only work in NSFW channels)
        Example: s.lewd
        """
        sites = [name for name in self.lewdImages]
        ims = random.choice([1, 2])
        emb = discord.Embed()
        if ims == 1:
            emb.set_image(url=nekos.img(random.choice(self.nsfw)))

        if ims == 2:
            emb.set_image(url=random.choice(
                self.lewdImages[random.choice(sites)]['images']))

        await msg.send(embed=emb)


    @commands.command()
    async def slap(self, msg, *users: discord.Member):
        """
        Returns a slap gif and adds the name of users you mentioned in command
        Command: s.slap <@users> (Can mention more than 1 user)
        Example: s.slap @Janna @Kurusaki @Alice
        """
        if users:
            targets = [user.display_name for user in users]
            emb = discord.Embed(description='**{}** slapped **{}**'.format(msg.author.display_name, ", ".join(targets)))
            emb.set_image(url=nekos.img('slap'))
            await msg.send(embed=emb)

        else:
            await msg.send("Please mention a user")
    @commands.command()
    async def waifu(self, msg):
        """
        Returns a waifu anime girl for you
        Command: s.waifu
        Example: s.waifu
        """
        emb = discord.Embed(title='Waifu')
        emb.set_image(url=nekos.img('waifu'))
        await msg.send(embed=emb)


    @commands.command()
    async def joke(self,msg):
        """
        Sends a random joke (usually about Chuck Norris)
        Command: s.joke
        Example: s.joke
        """
        emb=discord.Embed(description=rq.get('https://geek-jokes.sameerkumar.website/api').text)
        await msg.send(embed=emb)


    @commands.command()
    async def poke(self, msg, *users: discord.Member):
        """
        Pokes the users you mentioned
        Command: s.poke <@users> (Can mention more than 1 user)
        Example: s.poke @Alice @Hana @Katie
        """
        if users:
            targets = [user.display_name for user in users]
            emb = discord.Embed(
                description="**{}** poked **{}**".format(msg.author.display_name, ", ".join(targets)))
            emb.set_image(url=nekos.img('poke'))
            await msg.send(embed=emb)
        else:
            await msg.send("Please mention a user")
    @commands.command()
    async def cat(self, msg):
        """
        Sends a cat picture along with a cat fact
        Command: s.cat
        Example: s.cat
        """
        emb = discord.Embed(description=random.choice(self.facts['animals']['cats']))
        emb.set_image(url=nekos.img('meow'))
        await msg.send(embed=emb)

    @commands.command()
    async def pi(self, msg):
        """
        Sends you a pi fact
        Command: s.pi
        Example: s.pi
        """
        emb = discord.Embed(
            title='Pi Fact', description=random.choice(self.facts['math']['pi']))
        await msg.send(embed=emb)


    @commands.command(aliases=['random-show','random_show'])
    async def randomshow(self, msg):
        """
        Send a random snow name
        Command: s.randomshow
        Example: s.randomshow
        """

        session = rq.Session()
        url = 'https://tv-v2.api-fetch.website/random/show'
        r = session.get(url)
        if r.status_code == 200:
            r_json = r.json()
            name = r_json['title']
            year = r_json['year']
            img = r_json['images']['poster']
            await msg.send("**Name**: {}\n**Year**: {}\n**Poster**: {}".format(name, year, img))
        if r.status_code != 200:
            emb = discord.Embed(title="Error {}".format(r.status_code))
            emb.set_image(url='https://http.cat/{}'.format(r.status_code))
            await msg.send(embed=emb)

    @commands.command(aliases=['random-anime','random_anime'])
    @commands.cooldown(rate=1, per=2, type=commands.BucketType.channel)
    async def randomanime(self, msg):
        """
        Send random anime
        Command: s.randomanime
        Example: s.randomanime
        """

        rData = rq.Session().get('https://tv-v2.api-fetch.website/random/anime')
        r = rData.json()
        if rData.status_code == 200:
            title = r['title']
            mal_id = r['mal_id']
            genres = r['genres']
            url2 = 'https://api.jikan.moe/anime/{}/stats/'.format(mal_id)
            r2 = rq.Session().get(url2).text
            r2j = json.loads(r2)
            summary = r2j['synopsis']
            await msg.send("**Title**: {}\n**Genres**: {}\n**Synopsis**: {}".format(title, genres, summary))
        if rData.status_code != 200:
            emb = discord.Embed(title='Error {}'.format(rData.status_code))
            emb.set_image(url='https://http.cat/{}'.format(rData.status_code))
            await msg.send(embed=emb)

    @commands.command(aliases=['random-movie','random_movie'])
    async def randommovie(self, msg):
        """
        Send a random movie
        Command: s.randommovie
        Example: s.randommovie
        """

        movie = rq.Session().get('https://tv-v2.api-fetch.website/random/movie')
        if movie.status_code == 200:
            rest = movie.text
            rq_json = json.loads(rest)
            title = rq_json['title']
            summary = rq_json['synopsis']
            runtime = rq_json['runtime']
            genres = rq_json['genres']
            gen = " ".join(genres[1:])
            await msg.send("**Title**: {}\n**Genres**: {}\n**Length*: {} Minutes\n**Synopsis**: {}".format(title, gen, runtime, summary))

        if movie.status_code != 200:
            emb = discord.Embed(title='Error {}'.format(movie.status_code))
            emb.set_image(url='https://http.cat/{}'.format(movie.status_code))
            await msg.send(embed=emb)

    @commands.is_nsfw()
    @commands.command(hidden=True, enabled=True)
    async def neko(self, msg, nsfw=None):
        """
        Send random neko picture, adding nsfw will send nsfw ones (Only works in NSFW channels)
        Command: s.neko or s.neko nsfw
        Example: s.neko or s.neko nsfw
        """
        if nsfw != None and nsfw.lower() == 'nsfw':
            nsfw = 'true'
        else:
            nsfw = 'false'
        img = rq.get(
            'https://nekos.moe/api/v1/random/image?count=1&nsfw={}'.format(nsfw))
        emb = discord.Embed(title='Neko')
        if img.status_code == 200:
            url = 'https://nekos.moe/image/{}'.format(
                img.json()['images'][0]['id'])
            emb.set_image(url=url)
            await msg.send(embed=emb)

        else:
            emb.set_image(url='https://http.cat/{}'.format(img.status_code))
            emb.set_footer(
                text='Something went wrong error {}'.format(img.status_code))

    @commands.command()
    async def fox(self, msg):
        """
        Send random fox picture
        Command: s.fox
        Example: s.fox
        """

        emb = discord.Embed(title=None)
        r = rq.Session().get('https://randomfox.ca/floof/')
        if r.status_code == 200:
            emb.set_image(url=r.json()['image'])
            await msg.send(embed=emb)
        if r.status_code != 200:
            emb = discord.Embed(title="Error {}".format(r.status_code))
            emb.set_image(url='https://http.cat/{}'.format(r.status_code))
            await msg.send(embed=emb)



    @commands.command()
    async def pfp(self,msg,*users:discord.Member):
        """
        Sends you the profile picture url of the users you mentioend 
        Command: s.pfp <@users> (Can mention multiple users)
        Example s.pfp @Katie @Yukinno
        """
        if users:
            await msg.send("{}".format([user.avatar_url for user in users]))
        else:
            await msg.send("**Please mention some user(s)**")




def setup(bot):
    bot.add_cog(Fun(bot))