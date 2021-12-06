import discord
from discord.ext import commands
from discord import FFmpegPCMAudio #импортируем библиотеку с ffmeg для записи, конвертации и передачи аудиофайлов
import youtube_dl #библиотека для работы с youtube

class music(commands.Cog): 
    def __init__(self, client):#инициализируем бота
        self.client = client 

    @commands.command()
    async def join(self, ctx): #команда присоединения
    #если пользователь не в голосовом чате вызывает это команду,
    #он получает в ответ сообщение об этом.
        if ctx.author.voice is None:
            await ctx.send('Вы не в голосовом канале!')
        voice_channel = ctx.author.voice.channel
    #если бот не в голосовом чате, то мы его присоединяем и выводим
    #сообщение с подсказкой для пользователя
        if ctx.voice_client is None:
            await voice_channel.connect()
            await ctx.send('Привет, воспользуйтесь командой !info, чтобы узнать больше!')
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command() #команда отключения бота от голосового канала
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command() #команда, включающая песню
    async def play(self, ctx, url):
        ctx.voice_client.stop() #останавливаем голос бота
        print(ctx.voice_client)
        #настройки ffmpeg (штука, которая кодирует и декодирует видео
        FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
        #формат аудио
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client #передаем в переменную vc аудио поток бота

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl: #используем youtube объект как ydl
            info = ydl.extract_info(url, download=False) #получаем информацию об объекте
            await ctx.send('Сейчас играет: ' + info.get('title')) #отправляем в чат инфу о то, что играет
            url2 = info['formats'][0]['url'] # форматируем ссылку на аудио
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            #в переменную source записываем источник, с который мы будем проигрывать
            #здесь мы используем ffmpeg (библиотеки для записи, конвертации и передачи аудиофайлов)
            vc.play(source) #проигрываем песню


    @commands.command()
    async def pause(self, ctx): #команда паузы
        ctx.voice_client.pause()
        await ctx.send('Песня поставлена на паузу!')


    @commands.command()
    async def resume(self, ctx): #команда продолжения воспроизведения
        ctx.voice_client.resume()
        await ctx.send('Продолжаю воспроизведение!')

def setup(client):
    #регистрируем коги, то есть условно добавляем команды в коллекцию команд
    client.add_cog(music(client))
