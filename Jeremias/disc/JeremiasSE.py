import discord
from discord.ext import commands
import os
llave = "ODgzNDQ5NjA3NDcwODcwNTM4.YTKGkA.YtvWvYm2BGZb0I0jyQjoiqtD__A"
bot = commands.Bot(command_prefix='>', description="bot2")

@bot.command()
async def say(ctx, Sen):
    if ctx.author.bot:
        await ctx.send("<"+ Sen)

#@bot.command()
#async def s(ctx, Sen):
#    if(msg.author.id != 873482817504423946):
#        if ctx.author.bot:
#            await ctx.send("lolo"+ Sen)
#@bot.event
#async def on_message(msg):
#    if(msg.author.id != 873482817504423946):
#        return
#    channel = msg.channel
#    await channel.send(msg)
#
    

    # Si el id del autor del mensaje no es el id del bot al que se debe responder, sale de la función.
    # donde dice 12345 en realidad va la id del bot al que se debe responder.


        
    # Tu código aquí
    # obtenemos el canal donde se envió el mensaje
    # esto nos permitirá enviar un mensaje al mismo canal donde se recibió el mensaje.
    #channel = message.channel
    # 

@bot.event
async def encendido():
    await bot.change_presence(activity=discord.Streamming(name='Hacking from HadesIndsutry', url='https://www.twitch.tv/jaxswarriors'))
    print("estoy encendido")
bot.run(llave)