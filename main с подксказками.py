import discord #импортируем библиотеку дикорда
from discord.ext import commands
import music #импортируем данные из файла music

cogs = [music] #коллекция комманд для бота

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())
#создаем экземпляр нашего бота, указываем, что перед командой используется !
#в intents кладем информацию о том, что бот реагирует на любой тип событий

@client.command() #декоратор, который указывает, что это команда для бота
async def info(ctx, arg=None): #функция информации принимает в себя аргумент
    #ctx - контекст, в нем вся информация о том, где команда была вызвана и кто ее вызвал
    author = ctx.message.author #в переменную author кладем автора сообщения
    #если аргументов нет, то отправляем подсказку
    #если в аргументах есть "общая" или "команды",
    #то отправляем соответствующую информацию
    if arg == None:
        await ctx.send(f'{author.mention} Введите:\n!info общая\n!info команды')
    elif arg == 'общая':
        await ctx.send(f'{author.mention} Я - бот, позволяющий прослушивать музыку с YouTube!')
    elif arg == 'команды':
        await ctx.send(f'{author.mention} !join - подключает бота к голосовому каналу\n'
                       f'!disconnect - отсоединяет бота от голосового канала\n'
                       f'!play + ссылка на видео с YouTube - включает файл из ссылки в аудиоформате\n'
                       f'!pause - ставит песню на паузу\n'
                       f'!resume - продолжает воспроизведение')

for i in range(len(cogs)): #настройка всех команд
    cogs[i].setup(client)

client.run('OTA4NDAyMzIzNDM5NjM2NTAw.YY1Nlw.4y5TVES01mWYL3cGsh-C60eCmpk')
#Запуск бота
