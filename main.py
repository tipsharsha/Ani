from twitchio.ext import commands
import os

from cred import TOKEN, ID


Ani = commands.Bot(irctoken= TOKEN  , client_id= ID, nick='anisky_bot' , token=TOKEN,
                   prefix = '!',initial_channels= ['tipsharsha'])

@Ani.event
async def event_ready(ctx):
    print(f'Ready | {ctx.nick}')

@Ani.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')
@Ani.command(name='bye')
async def bye(ctx):
    await ctx.send(f'Bye {ctx.author.name}!')
@Ani.command(name='help')
async def help(ctx):
    await ctx.send(f'Hello {ctx.author.name}! I am AniSky_Bot. I am here to help you. Type !hello to say hello and !bye to say bye. Also, you can type !help to get this message again. Have a nice day!')
@Ani.command(name='commands')
async def commands(ctx):
    await ctx.send(f'Hello {ctx.author.name}! I am AniSky_Bot. I am here to help you. Type !hello to say hello and !bye to say bye. Also, you can type !help to get this message again. Have a nice day!')
@Ani.command(name='about')
async def about(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. tipsharsha is an Communication Engineer streaming Fortnite.')
@Ani.command(name='socials')
async def socials(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. You can follow tipsharsha on Instagram: https://www.instagram.com/tipsharsha/ and on Twitter: https://twitter.com/tipsharsha')

@Ani.command(name = 'ban')
async def ban(ctx, user: commands.User):
    await ctx.channel.ban(user)
    await ctx.send(f'Banned {user.name}!')
    


if __name__ == "__main__":
    Ani.run()
