import numpy as np
import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord import DMChannel
from discord.utils import get
import datetime
import base64
import asyncio
from random import randint, getrandbits

from urllib import parse, request
#import re
#Note lib PyNaCl,discord,numpy

#Var
ena2 = False;
ena3 = False;

bot = commands.Bot(command_prefix='st!', description="StemTH Memewithyasart Discord Bot", pm_help = False)

#------------------------------------Start Detact or Search or Info #Whois and Info Command
@bot.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"คุณ คือ {ctx.message.author.name}")

@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles[1:]]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="StemTH Memewithyasart Discord Bot", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://doc-0o-2g-docs.googleusercontent.com/docs/securesc/q76k1r9g5glt7npdc6a7otqurraql2eo/1inlpsm4ae9oqishk880bb6ftfr98uct/1631853825000/03718221299041134716/03718221299041134716/1O5xvSI0WVktFxhoGtYiKYO4zarnz4-pV?e=download&authuser=0&nonce=toa26m3cnvuog&user=03718221299041134716&hash=qch96ipgh46d6uvgdh0q4cbfajlhjrs2")
    await ctx.send(embed=embed)

@bot.command(name="searchbyid")
async def searchbyid(ctx, id):
    user = await bot.fetch_user(str(id))
    await ctx.send(f"ตรวจพบว่าเป็นคุณ " + str(user));

#------------------------------------End Detact or Search or Info #Whois and Info Command

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def part2on(ctx):
    global ena2 
    ena2 = True;
    await ctx.send("ระบบเปิดให้ทำข้อสอบ part2 แล้ว")
    await ctx.message.add_reaction('✅')
    channel = bot.get_channel(886873924418273291)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def part3on(ctx):
    global ena3
    ena3 = True;
    await ctx.send("ระบบเปิดให้ทำข้อสอบ part3 แล้ว")
    await ctx.message.add_reaction('✅')
    channel = bot.get_channel(886873924418273291)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def part2off(ctx):
    global ena2 
    ena2 = False;
    await ctx.send("ระบบปิดให้ทำข้อสอบ part2 แล้ว")
    await ctx.message.add_reaction('✅')
    channel = bot.get_channel(886873924418273291)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def part3off(ctx):
    global ena3
    ena3 = False;
    await ctx.send("ระบบปิดให้ทำข้อสอบ part3 แล้ว")
    await ctx.message.add_reaction('✅')
    channel = bot.get_channel(886873924418273291)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def invite2(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    user = await bot.fetch_user(f"{member.id}")
    idmem = str(member.id)
    idencoded = base64.b64encode(idmem.encode())
    delbid = idencoded.decode()
    memuser = str(member)
    memuserencoded = base64.b64encode(memuser.encode())
    delbuser = memuserencoded.decode()
    accesscode = str(delbid) + "#ST*" + str(delbuser)
    urlaccesscode = str(delbid) + "%23ST*" + str(delbuser)
        
    #user = await bot.fetch_user("320865426567462912")
    embed = discord.Embed(title=f"Science Mathematics and Technology Academic Competition 1st", description="การแข่งขันวิชาการวิทยาศาสตร์คณิตศาสตร์และ เทคโนโลยี ครั้งที่ 1 ของเซิฟเวอร์ดิสคอร์ดสาธารณะ STEM THAILAND COMMUNITY", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="User ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Access Code:", value=accesscode)
    await DMChannel.send(user, embed=embed)
    await ctx.send(f"ระบบได้ส่งข้อความส่วนตัวไปยังดิสคอร์ดของคุณ {member} แล้ว");
    await DMChannel.send(user, "ลิงก์สำหรับเข้าสอบส่วนที่ 2 ปรนัยของคุณ " + str(user) + " คือ https://docs.google.com/forms/d/e/1FAIpQLSe_mjQfheoFBtbUN10Iqn4JuqnTOB5Swffw7r-oRoygUyPvRQ/viewform?usp=pp_url&entry.1986996280=" + str(urlaccesscode) + " โดยมีรหัส Access Code คือ `" + str(accesscode) + "`")
    await ctx.message.add_reaction('✅')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def invite3(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    user = await bot.fetch_user(f"{member.id}")
    idmem = str(member.id)
    idencoded = base64.b64encode(idmem.encode())
    delbid = idencoded.decode()
    memuser = str(member)
    memuserencoded = base64.b64encode(memuser.encode())
    delbuser = memuserencoded.decode()
    accesscode = str(delbid) + "#ST*" + str(delbuser)
    urlaccesscode = str(delbid) + "%23ST*" + str(delbuser)
        
    #user = await bot.fetch_user("320865426567462912")
    embed = discord.Embed(title=f"Science Mathematics and Technology Academic Competition 1st", description="การแข่งขันวิชาการวิทยาศาสตร์คณิตศาสตร์และ เทคโนโลยี ครั้งที่ 1 ของเซิฟเวอร์ดิสคอร์ดสาธารณะ STEM THAILAND COMMUNITY", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="User ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Access Code:", value=accesscode)
    await DMChannel.send(user, embed=embed)
    await ctx.send(f"ระบบได้ส่งข้อความส่วนตัวไปยังดิสคอร์ดของคุณ {member} แล้ว");
    await DMChannel.send(user, "ลิงก์สำหรับเข้าสอบส่วนที่ 3 อัตนัยของคุณ " + str(user) + " คือ https://docs.google.com/forms/d/e/1FAIpQLSdBRjavExZMFlgGEm7Le9lTysx1zv8uqDIz6TSrDTuaZQi-Ug/viewform?usp=pp_url&entry.1986996280=" + str(urlaccesscode) + " โดยมีรหัส Access Code คือ `" + str(accesscode) + "`")
    await ctx.message.add_reaction('✅')
        
#-----------------------------------------------------------------------
@bot.command(name="part2")
async def join2(ctx):
    if ena2 == True:
        member = ctx.message.author
        user = await bot.fetch_user(f"{member.id}")
        
        idmem = str(member.id)
        idencoded = base64.b64encode(idmem.encode())
        delbid = idencoded.decode()
        memuser = str(member)
        memuserencoded = base64.b64encode(memuser.encode())
        delbuser = memuserencoded.decode()
        accesscode = str(delbid) + "#ST*" + str(delbuser)
        urlaccesscode = str(delbid) + "%23ST*" + str(delbuser)
        
        #user = await bot.fetch_user("320865426567462912")
        embed = discord.Embed(title=f"Science Mathematics and Technology Academic Competition 1st", description="การแข่งขันวิชาการวิทยาศาสตร์คณิตศาสตร์และ เทคโนโลยี ครั้งที่ 1 ของเซิฟเวอร์ดิสคอร์ดสาธารณะ STEM THAILAND COMMUNITY", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="User ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)
        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Access Code:", value=accesscode)
        await DMChannel.send(user, embed=embed)
        await ctx.send(f"ระบบได้ส่งข้อความส่วนตัวไปยังดิสคอร์ดของคุณ {ctx.message.author.mention} แล้ว");
        await DMChannel.send(user, "ลิงก์สำหรับเข้าสอบส่วนที่ 2 ปรนัยของคุณ " + str(user) + " คือ https://docs.google.com/forms/d/e/1FAIpQLSe_mjQfheoFBtbUN10Iqn4JuqnTOB5Swffw7r-oRoygUyPvRQ/viewform?usp=pp_url&entry.1986996280=" + str(urlaccesscode) + " โดยมีรหัส Access Code คือ `" + str(accesscode) + "`")
        await ctx.message.add_reaction('✅')

@bot.command(name="part3")
async def join3(ctx):
    if ena3 == True:
        member = ctx.message.author
        user = await bot.fetch_user(f"{member.id}")
        
        idmem = str(member.id)
        idencoded = base64.b64encode(idmem.encode())
        delbid = idencoded.decode()
        memuser = str(member)
        memuserencoded = base64.b64encode(memuser.encode())
        delbuser = memuserencoded.decode()
        accesscode = str(delbid) + "#ST*" + str(delbuser)
        urlaccesscode = str(delbid) + "%23ST*" + str(delbuser)
        
        #user = await bot.fetch_user("320865426567462912")
        embed = discord.Embed(title=f"Science Mathematics and Technology Academic Competition 1st", description="การแข่งขันวิชาการวิทยาศาสตร์คณิตศาสตร์และ เทคโนโลยี ครั้งที่ 1 ของเซิฟเวอร์ดิสคอร์ดสาธารณะ STEM THAILAND COMMUNITY", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="User ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)
        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Access Code:", value=accesscode)
        await DMChannel.send(user, embed=embed)
        await ctx.send(f"ระบบได้ส่งข้อความส่วนตัวไปยังดิสคอร์ดของคุณ {ctx.message.author.mention} แล้ว");
        await DMChannel.send(user, "ลิงก์สำหรับเข้าสอบส่วนที่ 3 อัตนัยของคุณ " + str(user) + " คือ https://docs.google.com/forms/d/e/1FAIpQLSdBRjavExZMFlgGEm7Le9lTysx1zv8uqDIz6TSrDTuaZQi-Ug/viewform?usp=pp_url&entry.1986996280=" + str(urlaccesscode) + " โดยมีรหัส Access Code คือ `" + str(accesscode) + "`")
        await ctx.message.add_reaction('✅')

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def บอทจ๋าjoin1(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def บอทจ๋าleave1(ctx):
    await ctx.voice_client.disconnect()

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="ภูมิกำลังปวดหัวกับสิ่งนี้", url="http://memewithyasart.ml"))
    print('My bot has ready naja xd.')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://memewithyasart.ml')
        await bot.process_commands(message)
        await ctx.message.add_reaction('✅')

bot.run("Plese Edit Token here")
