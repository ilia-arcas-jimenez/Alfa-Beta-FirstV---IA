import discord
from discord.ext import commands
import os
llave = "ODczNDgyODE3NTA0NDIzOTQ2.YQ5ERA.CasXWBU7kd4-Op5mdwbdYCB-pUI"
bot = commands.Bot(command_prefix='>', description="bot de hacking")
#async def msfconsole(ctx):
#    await ctx.send('msfconsole')
    
@bot.command()
async def say(ctx, msg):
    await ctx.send("<"+ msg+ "dudo")
    #await ctx.message.delete()
    #await message.channel.send(message)



#@bot.command()
#async def msf(ctx, Abrirconsola):
#    if Abrirconsola == ("payloadwindows"):
#        os.system("gnome-terminal -e 'bash payloadwindows.sh'")
#        await ctx.send(Abrirconsola)
#        await ctx.send("Aqui esta el virus que has creado file:///home/kali/Desktop/payload")
#    elif Abrirconsola == ("payloadandroid"):
#        os.system("gnome-terminal -e payloadandroid.sh")
#@bot.command()
#async def msfvenom(ctx, parametros):
#    os.system("msfvenom "+ parametros)
#    await ctx.send("estos son tus parametros")
@bot.command()
async def nube(ctx):
    await ctx.send('https://hadesindustry.ddns.net')

@bot.event
async def encendido():
    await bot.change_presence(activity=discord.Streamming(name='Hacking from HadesIndsutry', url='https://www.twitch.tv/jaxswarriors'))
    print("estoy encendido")
bot.run(llave)
