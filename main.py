
import os
from cred import TOKEN, ID
import helper
from twitchio.ext import commands,eventsub
import twitchio
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "distilgpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
prompt = f"Human:Hello. Who are you?\nAI: I am an Twitch Bot assistant. How can I help you today?\nHuman:Can you tell me about the streamer?\nAI:Sure! The streamer is a Communication Engineer streaming Fortnite.\nHuman:"

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=TOKEN, client_id=ID, nick='anisky_bot', prefix='!',token = TOKEN,
                         initial_channels=['harshtips'])
    async def event_ready(self):
        """ Runs once the bot has established a connection to Twitch. """
        print(f'Logged in as | {self.nick}')
    async def event_message(self,ctx):
        """ Runs every time a message is sent in chat. """
        global prompt
        if ctx.author.name is not None:
            print(f"Message from {ctx.author.name}: {ctx.content}")
            prompt = prompt + ctx.content + "\nAI:"
            response = helper.predict(prompt, model, tokenizer)
            #Before printing the response, clear screen and print the response
            print("\033[H\033[J")
            print(f"Response: {response}")
            await ctx.channel.send(response)

Ani = MyBot()
@Ani.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')
@Ani.command(name='bye')
async def bye(ctx):
    await ctx.send(f'Bye {ctx.author.name}!')
@Ani.command(name='help')
async def help(ctx):
    await ctx.send(f'Hello {ctx.author.name}! I am Ani. I am here to help you. Type !hello to say hello and !bye to say bye. Also, you can type !help to get this message again. Have a nice day!')
@Ani.command(name='commands')
async def commands(ctx):
    await ctx.send(f'Hello {ctx.author.name}! I am Ani. I am here to help you. Type !hello to say hello and !bye to say bye. Also, you can type !help to get this message again. Have a nice day!')
@Ani.command(name='about')
async def about(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. tipsharsha is an Communication Engineer streaming Fortnite.')
@Ani.command(name='socials')
async def socials(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. You can follow tipsharsha on Twitter: https://twitter.com/tipsharsha')
@Ani.command(name='game')
async def game(ctx, game):
    await ctx.send(f'Hello {ctx.author.name}!. tipsharsha is playing {game} right now. Enjoy the stream!')
@Ani.command(name='poll')
async def poll(ctx, *options):
    await ctx.send(f'Hello {ctx.author.name}!. tipsharsha has started a poll. The options are: {", ".join(options)}')
if __name__ == "__main__":
    # Ani.loop.run_until_complete(Ani.__ainit__())
    Ani.run()

