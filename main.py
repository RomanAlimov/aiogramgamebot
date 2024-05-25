import asyncio
import random
from asyncio import sleep

import keyboard as kb
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv
import os
load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer_photo(photo='https://yt3.ggpht.com/a/AGF-l78_k8_FDg7TrSzmliJAMnamy4fsOY8NMzDfow=s900-c-k-c0xffffffff-no-rj-mo',
                        caption='Описание об играх в боте:'
                                                 '\n1. Кости🎲 - Бросаются два кубика, один из них должен выйграть, либо сделать ничью.'
                                                 '\n'
                                                 '\n2. Угадай число🕵️‍♂️ - Ваша задача, угадать загаданное число от 1 до 10, в случае если вы '
                                                 'не угадаете за определенное кол-во попыток вы проиграете.'
                                                 '\n'
                                                 '\n3. Камень, ножницы, бумага🗿✂️📄 - Вне зависимости от географии «камень-ножницы-бумага» — это игра, '
                                                 'в которой участвуют три объекта '
                                                 'симметрично равной силы. Камень затупляет ножницы , но оборачивается '
                                                 'в бумагу и, стало быть, проигрывает ей.')

@dp.message(CommandStart())
async def clav(message: Message):
    await message.answer_photo(photo='https://helios-i.mashable.com/imagery/articles/00LDr4tdYtld9GG7EPHoiKE/images-2.fill.size_2000x1125.v1611690896.jpg',
                               caption=f'🖐Здравствуйте, рад вас видеть, {message.from_user.username}, выберите игру в которую будете играть!'
                                       f'\nЕсли вам интересно прочитать про игры в боте нажмите на /help.', reply_markup=kb.main)



@dp.message(F.text == 'Кости🎲')
async def cub(message: Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали игру: «Кости🎲».'
                                                      '\nПодробную информацию об игре, можно узнать по команде /help.')
    await bot.send_message(message.from_user.id, 'Ваш кубик: 1️⃣')

    msg = await bot.send_dice(message.from_user.id)
    value = msg.dice.value
    await sleep(5)

    msg2 = await bot.send_dice(message.from_user.id)
    value2 = msg2.dice.value
    await sleep(4)

    if value > value2:
        await bot.send_message(message.from_user.id, 'Вы победили!🎉')
    elif value < value2:
        await bot.send_message(message.from_user.id, 'Вы проиграли, попробуйте еще раз.😢')
    else:
        await bot.send_message(message.from_user.id, 'Ничья.😬')



@dp.message(F.text == 'Угадай число🕵️‍♂️')
async def ugad(message: Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали игру: «Угадай число🕵️‍♂️».'
                                                 '\nПодробную информацию об игре, можно узнать по команде /help.')
    await bot.send_message(message.from_user.id, 'Я загадал число от 1 до 10, а ваша задача отгадать его!'
                                                 '\nНапишите любое число от 1 до 10, если вы угадаете вы победите!',
                                                 reply_markup=kb.inl)
    @dp.message()
    async def ugad2(message: Message):
        global rand
        num = int(message.text)
        if 1 <= num <= 10:
            rand = random.randint(1, 10)
        if num == rand:
            await bot.send_message(message.from_user.id, 'Поздравляю, вы угадали!😀')
        elif num < rand:
            await bot.send_message(message.from_user.id, f'Мое число: {rand}, оказалось больше вашего. К сожалению вы проиграли.🙁')
        else:
            await bot.send_message(message.from_user.id,f'Вы проиграли, мое число: {rand}, оказалось меньше вашего. Попробуйте еще раз.😦')



@dp.message(F.text == 'Камень, ножницы, бумага🗿✂️📄')
async def knb(message: Message):
    await bot.send_message(message.from_user.id, 'Вы выбрали игру: «Камень, ножницы, бумага🗿✂️📄».'
                                                 '\nПодробную информацию об игре, можно узнать по команде /help.')
    await bot.send_message(message.from_user.id, 'Выберите - камень, ножницы или бумагу снизу на кнопках и мы узнаем кто из нас победил.', reply_markup=kb.kamennochbumag)

@dp.message(lambda message: message.text in ('🗿', '✂️', '📄'))
async def knb2(message: Message):
    user = message.text
    bot13 = random.choice(['🗿', '✂️', '📄'])
    if user == bot13:
        await bot.send_message(message.from_user.id, f"Вы выбрали {user} и я выбрал: {bot13}. Ничья!😬")
    elif (user == '🗿' and bot13 == '✂️') or (user == '✂️' and bot13 == '📄') or (user == '📄' and bot13 == '🗿'):
        await bot.send_message(message.from_user.id, f'😎🎉Поздравляю, вы победили, я выбрал: {bot13}')
    else:
        await bot.send_message(message.from_user.id, f'😥Увы, вы проиграли, я выбрал: {bot13}')



@dp.message(F.text == 'Главное меню')
async def tem(message: Message):
    await bot.send_message(message.from_user.id, 'Вы вернулись в главное меню.', reply_markup=kb.main)




async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен.')