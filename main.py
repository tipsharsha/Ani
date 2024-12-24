#TO-DO: Add functionality to send SUB and FOLLOWERS event to the streamer
import os
from cred import TOKEN, ID
import helper
from twitchio.ext import commands,eventsub
import twitchio
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline,AutoModelForSequenceClassification

classifier = pipeline("text-classification", model="textattack/bert-base-uncased-yelp-polarity")
model_name = "distilgpt2"
# prof_name = "AbhishekkV19/bert-base-uncased-10k-vulgarity"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
# prof_model = AutoModelForSequenceClassification.from_pretrained(prof_name)
# prof_tokenizer = AutoTokenizer.from_pretrained(prof_name)
prompt = f"Human: Hi, how are you?\nANI: I am fine. How can I help you today?\nHuman:What is the streamer playing.\nANI: The streamer is playing Fortnite right now.\nHuman:What does he do?\nANI: He is a Communication Engineer.\nHuman:What are his socials?\nANI: You can follow him on Twitter: https://twitter.com/tipsharsha\nHuman:What are his specs?\nANI: He uses a 5900HX + 16GB RAM + RTX 3050\nHuman:What is his discord?\nANI: You can join discord channel here : https://discord.gg/SsQqges4\nHuman:What is the poll?\nANI: The streamer has started a poll. The options are: Option1, Option2, Option3\nHuman:What is the game?\nANI: The streamer is playing Fortnite right now.\nHuman:Hello\nANI:Hello! How can I help you today?\nHuman:Bye\nANI:Bye! Have a nice day!"
# esbot = commands.Bot.from_client_credentials(client_id=ID, client_secret=TOKEN)
# esclient = eventsub.EventSubClient(esbot)
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=TOKEN, client_id=ID, nick='anisky_bot', prefix='!',token = TOKEN,
                         initial_channels=['harshtips'])
    def __ainit__(self):
        pass
        # self.create_task(esclient.listen(port = 4000))
    async def event_ready(self):
        """ Runs once the bot has established a connection to Twitch. """
        print(f'Logged in as | {self.nick}')
    async def event_message(self,ctx):
        """ Runs every time a message is sent in chat. """
        global prompt
        if ctx.author is not None and ctx.author.name != "harshtips":
            print(f"Message from {ctx.author.name}: {ctx.content}")
            prompt = prompt +"\n"+ctx.author.name+ctx.content + "\nANI:"
            #if it contains a ani or ANI or Ani, then predict response
            # prof_check = helper.detect_profanity(ctx.content,prof_model,prof_tokenizer)
            ad_check = helper.detect_ads(ctx.content)
            if ad_check:
                # await ctx.channel.send(f"Please refrain from using profanity or ads in the chat {ctx.author.name}!")
                message_id = ctx.tags['id']
                await ctx.channel.send(f"/delete {message_id}")
                await ctx.channel.send(f"Please refrain from using ads in the chat {ctx.author.name}!")
                await ctx.channel.timeout(ctx.author.name, 120, f"reason")
                return
            if ctx.content.lower().find("ani") != -1 or helper.determine_sentiment(ctx.content,classifier):
                response = helper.predict_response(prompt, model, tokenizer)
                #Before printing the response, clear screen and print the response
                print(f"Response: {response}")
                await ctx.channel.send(response)
            await self.handle_commands(ctx)
Ani = MyBot()
# Ani.loop.run_until_complete(Ani.__ainit__())
@Ani.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')
@Ani.command(name='bye')
async def bye(ctx):
    await ctx.send(f'Bye {ctx.author.name}!')
@Ani.command(name='help')
async def help(ctx):
    await ctx.send(f'Hello {ctx.author.name}! I am Ani. Actions you can perform: !hello, !bye, !about, !socials, !game, !poll, !specs, !discord, !streamer, !rank')
@Ani.command(name='about')
async def about(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. harshtips is an Communication Engineer streaming Fortnite.')
@Ani.command(name='socials')
async def socials(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. You can follow harshtips on Twitter: https://twitter.com/tipsharsha')
@Ani.command(name='game')
async def game(ctx, game):
    await ctx.send(f'Hello {ctx.author.name}!. harshtips is playing {game} right now. Enjoy the stream!')
@Ani.command(name='poll')
async def poll(ctx, *options):
    await ctx.send(f'Hello {ctx.author.name}!. harshtips has started a poll. The options are: {", ".join(options)}')
@Ani.command(name='specs')
async def poll(ctx, *options):
    await ctx.send(f'Hello {ctx.author.name}!. He uses a 5900HX + 16GB RAM + RTX 3050')
@Ani.command(name='discord')
async def discord(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. You can join discord channel here : https://discord.gg/SsQqges4')
@Ani.command(name='streamer')
async def streamer(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. Harsha is an Communication Engineer streaming Fortnite.')
@Ani.command(name='rank')
async def rank(ctx):
    await ctx.send(f'Hello {ctx.author.name}!. Harsha is a Diamond 1 player.')
if __name__ == "__main__":
    Ani.run()
