import telebot
import key
import database as db
from telebot import types
import solo_database as s_db
from random import randint
import num_update as n_u
import supernum as sn
bot = telebot.TeleBot(key.key)

@bot.message_handler(content_types=['text'])
def sey_hello(message,call=False):
    if call != False:
        print('call')
        sn.add_id(call.from_user.id)
        db.check_reg(call.from_user.id, call.from_user.first_name, call.from_user.username, message.chat.id)
        print(call.from_user.id)
        if s_db.add_user(call.from_user.id):
            print(call.from_user.id)
            if s_db.get_playing(call.from_user.id) is False:
                print('Play call??',s_db.get_playing(call.from_user.id))
                buttons     = types.ReplyKeyboardMarkup()
                solo        = types.InlineKeyboardButton('Solo game 🧐')
                settings    = types.InlineKeyboardButton('Settings ⚙️')
                multiplayer = types.InlineKeyboardButton('Play with friend 👨‍👦‍👦')
                shop = types.InlineKeyboardButton('Shop 🏬')
                buttons.add(solo, multiplayer)
                buttons.add(settings)
                buttons.add(shop)
                msg         = bot.send_message(message.chat.id,'Hello {name} ✋!\n I`m Nick and i help you play in guess number 😁😁😁\n\n If you don`t know how to play in this game send me this command - /rules ⬅️ \n\n Ok, choose what interests you in the menu below. ⬇️⬇️⬇️'.format(name=call.from_user.first_name), reply_markup=buttons)
                bot.register_next_step_handler(msg, update_message)
            elif s_db.get_playing(call.from_user.id) is True:
                print('Play call??', s_db.get_playing(call.from_user.id))
                give_up     = types.InlineKeyboardMarkup()
                yes         = types.InlineKeyboardButton('Yes', callback_data='yes')
                no          = types.InlineKeyboardButton('No', callback_data='no')
                give_up.add(yes, no)
                bot.send_message(message.chat.id, "You really want to give up?", reply_markup=give_up)
            elif s_db.get_playing(call.from_user.id) is None:
                bot.send_message(message.chat.id, "Return None!!")
                s_db.get_user(message.from_user.id)
            else:
                bot.send_message(message.chat.id, "Return else!!")
                s_db.get_user(message.from_user.id)
        else:
            bot.send_message(message.chat.id, "Never end!")
    elif call is False:
        print('else')
        sn.add_id(message.from_user.id)
        db.check_reg(message.from_user.id, message.from_user.first_name, message.from_user.username,message.chat.id)
        print(message.from_user.id)
        if s_db.add_user(message.from_user.id):
            if s_db.get_playing(message.from_user.id) is False:
                    print('Play??', s_db.get_playing(message.from_user.id))
                    buttons     = types.ReplyKeyboardMarkup()
                    solo        = types.InlineKeyboardButton('Solo game 🧐')
                    settings    = types.InlineKeyboardButton('Settings ⚙️')
                    multiplayer = types.InlineKeyboardButton('Play with friend 👨‍👦‍👦')
                    shop        = types.InlineKeyboardButton('Shop 🏬')
                    buttons.add(solo,multiplayer)
                    buttons.add(settings)
                    buttons.add(shop)
                    msg         = bot.send_message(message.chat.id, 'Hello {name} ✋!\n I`m Nick and i help you play in guess number 😁😁😁\n\n If you don`t know how to play in this game send me this command - /rules ⬅️ \n\n Ok, choose what interests you in the menu below. ⬇️⬇️⬇️'.format(name=message.from_user.first_name), reply_markup=buttons)
                    bot.register_next_step_handler(msg, update_message)
            elif s_db.get_playing(message.from_user.id) is True:
                print('Play??', s_db.get_playing(message.from_user.id))
                give_up = types.InlineKeyboardMarkup()
                yes     = types.InlineKeyboardButton('Yes', callback_data='yes')
                no      = types.InlineKeyboardButton('No', callback_data='no')
                give_up.add(yes, no)
                bot.send_message(message.chat.id, "You really want to give up?", reply_markup=give_up)
            else:
                bot.send_message(message.chat.id, "Return None!!")
                s_db.get_user(message.from_user.id)
        else:
            bot.send_message(message.chat.id, "Never end!")
    else:
        bot.send_message(message.chat.id, "Unreal!")





def update_message(message):
    if message.text == 'Solo game 🧐':
        if s_db.get_playing(message.from_user.id):
            give_up = types.InlineKeyboardMarkup()
            yes     = types.InlineKeyboardButton('Yes', callback_data='yes')
            no      = types.InlineKeyboardButton('No', callback_data='no')
            give_up.add(yes, no)
            bot.send_message(message.chat.id, "You really want to give up?", reply_markup=give_up)
        else:
            s_db.play(message.from_user.id, True)
            solo_game(message)

    elif message.text == 'Play with friend 👨‍👦‍👦':
        if s_db.get_playing(message.from_user.id):
            give_up = types.InlineKeyboardMarkup()
            yes     = types.InlineKeyboardButton('Yes', callback_data='yes')
            no      = types.InlineKeyboardButton('No', callback_data='no')
            give_up.add(yes, no)
            bot.send_message(message.chat.id, "You really want to give up?", reply_markup=give_up)
        else:
            bot.send_message(message.chat.id, "Coming soon!")

    elif message.text == 'Home 🏠':
        if s_db.get_playing(message.from_user.id):
            give_up = types.InlineKeyboardMarkup()
            yes     = types.InlineKeyboardButton('Yes', callback_data='yes')
            no      = types.InlineKeyboardButton('No', callback_data='no')
            give_up.add(yes, no)
            bot.send_message(message.chat.id, "You really want to give up?", reply_markup=give_up)
        else:
            sey_hello(message, False)

    elif message.text == 'Settings ⚙️':
        if s_db.get_playing(message.from_user.id):
            give_up = types.InlineKeyboardMarkup()
            yes     = types.InlineKeyboardButton('Yes',callback_data='yes')
            no      = types.InlineKeyboardButton('No',callback_data='no')
            give_up.add(yes,no)
            bot.send_message(message.chat.id,"You really want to give up?",reply_markup=give_up)
        else:
            settings(message)

    elif message.text == 'Shop 🏬':
        if s_db.get_playing(message.from_user.id):
            give_up = types.InlineKeyboardMarkup()
            yes     = types.InlineKeyboardButton('Yes',callback_data='yes')
            no      = types.InlineKeyboardButton('No',callback_data='no')
            give_up.add(yes,no)
            bot.send_message(message.chat.id,"You really want to give up?",reply_markup=give_up)
        else:
            print('updatemessage')
            shop_nick(message)
    elif message.text == 'money':
        if s_db.get_playing(message.from_user.id):
            give_up = types.InlineKeyboardMarkup()
            yes     = types.InlineKeyboardButton('Yes',callback_data='yes')
            no      = types.InlineKeyboardButton('No',callback_data='no')
            give_up.add(yes,no)
            bot.send_message(message.chat.id,"You really want to give up?",reply_markup=give_up)
        else:
            get_money(message)
    elif message.text == 'No, back to home':
        if s_db.get_playing(message.from_user.id):
            give_up = types.InlineKeyboardMarkup()
            yes     = types.InlineKeyboardButton('Yes',callback_data='yes')
            no      = types.InlineKeyboardButton('No',callback_data='no')
            give_up.add(yes,no)
            bot.send_message(message.chat.id,"You really want to give up?",reply_markup=give_up)
        else:
            sey_hello(message, False)
    elif message.text == 'Yes, return to shop':
        if s_db.get_playing(message.from_user.id):
            give_up = types.InlineKeyboardMarkup()
            yes     = types.InlineKeyboardButton('Yes',callback_data='yes')
            no      = types.InlineKeyboardButton('No',callback_data='no')
            give_up.add(yes,no)
            bot.send_message(message.chat.id,"You really want to give up?",reply_markup=give_up)
        else:
            print('return to shop')
            print('update:::;',message.text)
            shop_nick(message)
    elif message.text == 'mom':
        mom(message)
    else:
        if s_db.get_playing(message.from_user.id):
            solo_before_update(message)
        else:
            buttons     = types.ReplyKeyboardMarkup()
            solo        = types.InlineKeyboardButton('Solo game 🧐')
            setting     = types.InlineKeyboardButton('Settings ⚙️')
            multiplayer = types.InlineKeyboardButton('Play with friend 👨‍👦‍👦')
            shop        = types.InlineKeyboardButton('Shop 🏬')
            buttons.add(solo, multiplayer)
            buttons.add(setting)
            buttons.add(shop)
            send =bot.send_message(message.chat.id, 'Please, choose correct buttons in menu below.',reply_markup=buttons)
            bot.register_next_step_handler(send, update_message)


def mom(message):
    bot.send_message(message.chat.id,'mom!')


def shop_nick(message):
    print('shop')
    print('shop:::',message.text)
    shop_btn     = types.InlineKeyboardMarkup()
    show_ran_num = types.InlineKeyboardButton('Buy SRN 🧬 35 💶',callback_data='SRN')
    show_one_num = types.InlineKeyboardButton('Buy SEN 🧫 100 💶',callback_data='SEN')
    show_two_num = types.InlineKeyboardButton('Buy STN 🦠 360 💶',callback_data='STN')
    back_to_home = types.InlineKeyboardButton('↩️', callback_data='bth')
    shop_btn.add(show_ran_num)
    shop_btn.add(show_one_num)
    shop_btn.add(show_two_num)
    shop_btn.add(back_to_home)
    send         = bot.send_message(message.chat.id,'Shop 🏬:\n\n\n Your money 💶: {money}\n\nThe following items are presented in abbreviated form:\nSRN 🧬 - Show rundom number\nSEN 🧫 - Shows the one number that you will empty\nSTN 🦠 - Show the two numbers you want to empty \n\n Press the button downstairs to buy the product.\n If you want go to home choose this in menu below.'.format(money=db.get_money(message.from_user.id,0,True)),reply_markup=shop_btn)
    bot.register_next_step_handler(send, update_message)




def solo_game(message):
    Home        = types.ReplyKeyboardMarkup()
    home        = types.InlineKeyboardButton('Home 🏠')
    settings    = types.InlineKeyboardButton('Settings ⚙️')
    Home.add(home)
    Home.add(settings)
    random      = randint(1000,9999)
    print(random)
    s_db.del_num(message.from_user.id)
    s_db.add_num(message.from_user.id, random)
    send        = bot.send_message(message.chat.id, "Ok! I guess number\n\n Now you should guess my number! \n\nOk send me the nomber you think. ",reply_markup=Home)
    bot.register_next_step_handler(send, update_message)

def after_callback(message,call = False):
    send        = bot.send_message(message.chat.id, "I am very glad that you are not ready to give up!\n\n Ok send me the number you think. \n\n\nSRN 🧬: {srn}\nSEN 🧫: {sen}\nSTN 🦠: {s_t_n}".format(
        srn     =db.get_product(call.from_user.id,True,False,False),
        s_t_n   =db.get_product(call.from_user.id,False,False,True),
        sen     =db.get_product(call.from_user.id,False,True,False)))
    bot.register_next_step_handler(send, update_message)



def solo_before_update(message, call = False):
    if call == False:
        Supernum   = types.InlineKeyboardMarkup()
        SRN        = types.InlineKeyboardButton('Use SRN 🧬', callback_data='use_srn')
        SEN        = types.InlineKeyboardButton('Use SEN 🧫', callback_data='use_sen')
        STN        = types.InlineKeyboardButton('Use STN 🦠', callback_data='use_stn')
        Supernum.add(SRN)
        Supernum.add(SEN)
        Supernum.add(STN)
        num        = s_db.get_num(message.from_user.id)
        num_player = message.text
        get_result = sn.get_result(message.from_user.id)
        if num_player.isdigit() and len(str(num_player)) == len(str(num)) and get_result != '????':
            silver, gold = n_u.get_bull(str(num), str(num_player))
            if gold == int(len(str(num))):
                s_db.play(message.from_user.id, False)
                db.win(message.from_user.id)
                sn.drop_num(message.from_user.id)
                bot.send_message(message.chat.id,'Yeah! You win! \n\nMy nomber is {num}'.format(num=num))
                sey_hello(message, False)
            else:
                sent = bot.send_message(message.chat.id,'Oh no!\n\n You don\'t get it. Please try again. \n \n You have that kind of data coming out of that number: \n\n Silver - {silver} \n Gold - {gold} \n\nSuper Number - {result}\n\n\nSRN 🧬: {srn}\nSEN 🧫: {sen}\nSTN 🦠: {s_t_n}\n\n\nI wait next number =)'.format(
                    silver=silver,
                    gold=gold,
                    result=sn.get_result(message.from_user.id),
                    srn=db.get_product(message.from_user.id, True, False, False),
                    s_t_n=db.get_product(message.from_user.id, False, False, True),
                    sen=db.get_product(message.from_user.id, False, True, False)
                ),reply_markup=Supernum)
                bot.register_next_step_handler(sent, update_message)
        else:
            sent = bot.send_message(message.chat.id, 'Mate, please send me correct four-digit number! \n\n Example: {}'.format(randint(1000,9999)))
            bot.register_next_step_handler(sent, update_message)
    else:
        Supernum = types.InlineKeyboardMarkup()
        SRN = types.InlineKeyboardButton('Use SRN 🧬', callback_data='use_srn')
        SEN = types.InlineKeyboardButton('Use SEN 🧫', callback_data='use_sen')
        STN = types.InlineKeyboardButton('Use STN 🦠', callback_data='use_stn')
        Supernum.add(SRN)
        Supernum.add(SEN)
        Supernum.add(STN)
        num = s_db.get_num(call.from_user.id)
        num_player = message.text
        if num_player.isdigit() and len(str(num_player)) == len(str(num)):
            silver, gold = n_u.get_bull(str(num), str(num_player))
            if gold == int(len(str(num))):
                s_db.play(call.from_user.id, False)
                db.win(call.from_user.id)
                sn.drop_num(call.from_user.id)
                bot.send_message(message.chat.id, 'Yeah! You win! \n\nMy nomber is {num}'.format(num=num))
                sey_hello(message, False)
            else:
                sent = bot.send_message(message.chat.id,
                                        'Oh no!\n\n You don\'t get it. Please try again. \n \n You have that kind of data coming out of that number: \n\n Silver - {silver} \n Gold - {gold} \n\nSuper Number - {result}\n\n\nSRN 🧬: {srn}\nSEN 🧫: {sen}\nSTN 🦠: {s_t_n}\n\n\nI wait next number =)'.format(
                                            silver=silver,
                                            gold=gold,
                                            result=sn.get_result(call.from_user.id),
                                            srn=db.get_product(call.from_user.id, True, False, False),
                                            s_t_n=db.get_product(call.from_user.id, False, False, True),
                                            sen=db.get_product(call.from_user.id, False, True, False)
                                        ), reply_markup=Supernum)
                bot.register_next_step_handler(sent, update_message)
        else:
            sent = bot.send_message(message.chat.id,
                                    'Mate, please send me correct four-digit number! \n\n Example: {}'.format(
                                        randint(0000, 9999)))
            bot.register_next_step_handler(sent, update_message)



def settings(message):
    Home        = types.ReplyKeyboardMarkup()
    home        = types.InlineKeyboardButton('Home 🏠')
    solo        = types.InlineKeyboardButton('Solo game 🧐')
    multiplayer = types.InlineKeyboardButton('Play with friend 👨‍👦‍👦')
    Home.add(home)
    Home.add(solo, multiplayer)
    user        = db.get_info(message.from_user.id)
    send        = bot.send_message(message.chat.id,'Your settings ⚙️: \n\nId 👊: {id}\nUsername 🤙: {un}\nName 👨‍🦰: {name}\n\n\nMoney 💶: {money}\n\n\nTotal win 🏆: {win}\nTotal number of games played 🎮: {tg} \n\n\nSRN 🧬: {srn}\nSEN 🧫: {sen}\nSTN 🦠: {s_t_n}\n\n\n If you wont back to home click on button below. ⬇️⬇️⬇️'.format(
            id  =message.from_user.id,
            un  =message.from_user.username if message.from_user.username != None else 'you haven`t username',
            name=message.from_user.first_name,
            money=user[3],
            win =user[4],
            tg  =user[5],
            srn =db.get_product(message.from_user.id,True,False,False),
            s_t_n =db.get_product(message.from_user.id,False,False,True),
            sen =db.get_product(message.from_user.id,False,True,False)),
            reply_markup=Home)
    bot.register_next_step_handler(send, update_message)






def use_sen(message):
    if message.text.isdigit() and len(message.text) == 1 and int(message.text) <= 4 and int(message.text) >= 0:
        Supernum = types.InlineKeyboardMarkup()
        SRN = types.InlineKeyboardButton('Use SRN 🧬', callback_data='use_srn')
        SEN = types.InlineKeyboardButton('Use SEN 🧫', callback_data='use_sen')
        STN = types.InlineKeyboardButton('Use STN 🦠', callback_data='use_stn')
        Supernum.add(SRN)
        Supernum.add(SEN)
        Supernum.add(STN)
        index = message.text
        num_  = s_db.get_num(message.from_user.id)
        print('num__________',num_)
        print('id..',message.from_user.id)
        user_num =sn.run_sen(message.from_user.id,int(index),num_)
        print('user_num__________', user_num)
        bot.send_message(message.chat.id,
                         'Success! 🎉🎉🎉\n\n You choose the {} number, and he turned out is {}! 😳\n\n So, now you have this result: {} ⬅️\n\n\nI wait next number =)'.format(
                             index,
                             user_num,
                             sn.get_result(message.from_user.id)), reply_markup=Supernum)
    else:
        run = randint(1000, 9999)
        index = randint(1, 4)
        send = bot.send_message(message.chat.id,'Please, send me correct one number you want to know.\n\nFor example: \n{} \nI want to find out the number :{} -> {}'.format(run,index,str(run)[index]))
        bot.register_next_step_handler(send, use_sen)






@bot.callback_query_handler(func=lambda call: True)
def call_update(call):
    if call.data:
        if call.data == 'yes':
            bot.send_message(call.message.chat.id, 'You lose! 😩\n\n My number was:{}'.format(s_db.get_num(call.from_user.id)))
            s_db.play(call.from_user.id,False)
            sn.drop_num(call.from_user.id)
            sey_hello(call.message, call)
        elif call.data == 'no':
            after_callback(call.message,call)
        elif call.data == 'SRN':
            buy_product(call.message,call.from_user.id ,35,'srn')
        elif call.data == 'SEN' :
            buy_product(call.message,call.from_user.id,100,'sen')
        elif call.data == 'STN':
            buy_product(call.message,call.from_user.id ,360,'stn')
        elif call.data == 'yes_buy':
            shop_nick(call.message)
        elif call.data == 'no_buy':
            sey_hello(call.message, call)
        elif call.data == 'bth':
            sey_hello(call.message, call)
        elif call.data == 'use_srn':
             Supernum = types.InlineKeyboardMarkup()
             SRN = types.InlineKeyboardButton('Use SRN 🧬', callback_data='use_srn')
             SEN = types.InlineKeyboardButton('Use SEN 🧫', callback_data='use_sen')
             STN = types.InlineKeyboardButton('Use STN 🦠', callback_data='use_stn')
             Supernum.add(SRN)
             Supernum.add(SEN)
             Supernum.add(STN)
             if db.get_product(call.from_user.id,True,True,False) >= 1:
                 random = randint(1,4)
                 num    = s_db.get_num(call.from_user.id)
                 number = sn.run_srn(call.from_user.id,random,num)
                 db.use_product(call.from_user.id,True,False,False)
                 call.data = ''
                 bot.send_message(call.message.chat.id,'Success! 🎉🎉🎉\n\n I choose the {} number, and he turned out is {}! 😳\n\n So, now you have this result: {} ⬅️\n\n\nI wait next number =)'.format(random,number,sn.get_result(call.from_user.id)),reply_markup=Supernum)
             else:
                 call.data = ''
                 bot.send_message(call.message.chat.id, 'You haven`t supernumber! \n\n\nSRN 🧬: {srn}\nSEN 🧫: {sen}\nSTN 🦠: {s_t_n}'.format(
                     srn =db.get_product(call.from_user.id,True,False,False),
                     s_t_n =db.get_product(call.from_user.id,False,False,True),
                     sen =db.get_product(call.from_user.id,False,True,False)))
                 solo_before_update(call.message, call)
        elif call.data == 'use_sen':
             if db.get_product(call.from_user.id,False,True,False) >= 1:
                 db.use_product(call.from_user.id,False,True,False)
                 call.data = ''
                 run = randint(1000,9999)
                 index = randint(1,4)
                 indexx = int(index) - 1
                 send     =bot.send_message(call.message.chat.id,'Ok, send me the number you want to know\n\nFor example: \n{} \nI want to find out the number :{} -> {}'.format(run,index,str(run)[indexx]))
                 bot.register_next_step_handler(send, use_sen)
             else:
                 print('sen',db.get_product(call.from_user.id,False,True,False))
                 call.data = ''
                 bot.send_message(call.message.chat.id, 'You haven`t supernumber! \n\n\nSRN 🧬: {srn}\nSEN 🧫: {sen}\nSTN 🦠: {s_t_n}'.format(
                     srn =db.get_product(call.from_user.id,True,False,False),
                     s_t_n =db.get_product(call.from_user.id,False,True,True),
                     sen =db.get_product(call.from_user.id,False,True,True)))
                 solo_before_update(call.message, call)




def buy_product(message,callback,price:int,name_product: str):
    if db.get_money(callback, price, False):
        Shop_back = types.ReplyKeyboardMarkup()
        yes  = types.InlineKeyboardButton('Yes, return to shop')
        home = types.InlineKeyboardButton('No, back to home')
        Shop_back.add(yes,home)
        print('buy_product')
        db.buy(callback,price, name_product)
        bot.send_message(message.chat.id,'Yeah, you buy it!\n\nMaybe, something else?',reply_markup=Shop_back)
    else:
        print('buy_product else')
        Home        = types.ReplyKeyboardMarkup()
        home        = types.InlineKeyboardButton('Home 🏠')
        solo        = types.InlineKeyboardButton('Solo game 🧐')
        multiplayer = types.InlineKeyboardButton('Play with friend 👨‍👦‍👦')
        Home.add(home)
        Home.add(solo, multiplayer)
        bot.send_message(message.chat.id,'You can`t buy this because you haven`t money!\n\n Your money:{} 💶 \n\n\n If you wont back to home click on button below. ⬇️⬇️⬇️'.format(db.get_money(user_id=callback,get_money=True,price=0)),reply_markup=Home)








def get_money(message):
    send = bot.send_message(message.chat.id,'How much you want to get money?')
    bot.register_next_step_handler(send, add_money)

def add_money(message):
    money = message.text
    if money.isdigit():
        db.add_money(message.from_user.id,money)
        bot.send_message(message.chat.id, 'Done!')
        sey_hello(message, False)
    else:
        send = bot.send_message(message.chat.id, 'Write correct number!')
        bot.register_next_step_handler(send, add_money)



bot.infinity_polling(True)