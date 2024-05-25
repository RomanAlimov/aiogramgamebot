from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Кости🎲'),
                                      KeyboardButton(text='Угадай число🕵️‍♂️'),
                                      KeyboardButton(text='Камень, ножницы, бумага🗿✂️📄')]],
                        resize_keyboard=True,
                        input_field_placeholder='Выберите игру в которую будете играть. . .')

kamennochbumag = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='🗿'),
                                      KeyboardButton(text='✂️'),
                                      KeyboardButton(text='📄'),
                                      KeyboardButton(text='Главное меню')]],
                        resize_keyboard=True)


inl = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='1'),
                                    KeyboardButton(text='2'),
                                    KeyboardButton(text='3'),
                                    KeyboardButton(text='4'),
                                    KeyboardButton(text='5'),
                                    KeyboardButton(text='6'),
                                    KeyboardButton(text='7'),
                                    KeyboardButton(text='8'),
                                    KeyboardButton(text='9'),
                                    KeyboardButton(text='10'),
                                    KeyboardButton(text='Главное меню')]],
                          resize_keyboard=True)