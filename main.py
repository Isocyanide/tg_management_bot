def start(bot, update):
	from start import start
	start(bot, update)

def plugins(bot, update, user_data):
	from plugins import plugins
	plugins(bot, update, user_data)

def plugins_callback(bot, update, user_data):
	from plugins import plugins_callback
	plugins_callback(bot, update, user_data)

def msg_text(bot, update, user_data):
	from msg_text import msg_text
	msg_text(bot, update, user_data)

def msg_all(bot, update, user_data):
	from msg_all import msg_all
	msg_all(bot, update, user_data)

def setwelcome(bot, update):
	from welcome import setwelcome
	setwelcome(bot, update)

def rules(bot, update):
	from rules import rules
	rules(bot, update)

def setrules(bot, update):
	from rules import setrules
	setrules(bot, update)

def ban(bot, update):
	from ban import ban
	ban(bot, update)

def kick(bot, update):
	from kick import kick
	kick(bot, update)

def warn(bot,update):
	from warn import warn
	warn(bot,update)

def setwarn(bot, update):
	from warn import setwarn
	setwarn(bot, update)

def clearwarns(bot, update):
	from warn import clearwarns
	clearwarns(bot, update)

def add_filter(bot,update):
	from filters import add_filter
	add_filter(bot,update)

def filter_list(bot, update):
	from filters import filter_list
	filter_list(bot, update)

def remove_filter(bot, update):
	from filters import remove_filter
	remove_filter(bot, update)

def ud(bot, update):
	from ud import ud
	ud(bot, update)

def tl(bot, update):
	from tl import tl
	tl(bot, update)

def tts(bot, update):
	from tts import tts
	tts(bot, update)

def weeb(bot, update):
	from tts import weeb
	weeb(bot, update)

def admins(bot, update):
	from admins import admins
	admins(bot, update)

def main():
	from telegram.ext import (Updater, MessageHandler, Filters, CommandHandler,
							  ConversationHandler, CallbackQueryHandler, RegexHandler)
	import logging
	logging.basicConfig(level = logging.INFO,
						format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	updater = Updater(token="TOKEN") 

	dispatcher = updater.dispatcher

	start_handler = CommandHandler('start', start)

	plugins_handler = CommandHandler('plugins', plugins, pass_user_data = True)
	plugins_callback_handler = CallbackQueryHandler(plugins_callback, pass_user_data = True)
	
	msg_text_handler = MessageHandler(Filters.text, msg_text, pass_user_data = True)
	msg_all_handler = MessageHandler(Filters.all, msg_all, pass_user_data = True)

	setwelcome_handler = CommandHandler('setwelcome', setwelcome)
	rules_handler = CommandHandler('rules', rules)
	setrules_handler = CommandHandler('setrules', setrules)
	
	kick_handler = CommandHandler('kick', kick)
	ban_handler = CommandHandler('ban', ban)

	add_filter_handler = CommandHandler('filter',add_filter)
	filter_list_handler = CommandHandler('filters',filter_list)
	remove_filter_handler = CommandHandler('stop',remove_filter)


	warn_handler = CommandHandler('warn', warn)
	setwarn_handler = CommandHandler('setwarn', setwarn)
	clearwarn_handler = CommandHandler('clearwarns', clearwarns)

	ud_handler = CommandHandler('ud', ud)
	tl_handler = CommandHandler('tl', tl)
	tts_handler = CommandHandler('tts', tts)
	weeb_handler = CommandHandler('weeb', weeb)

	admins_handler = CommandHandler('admins', admins)

	dispatcher.add_handler(start_handler)
	dispatcher.add_handler(plugins_handler)
	dispatcher.add_handler(plugins_callback_handler)
	dispatcher.add_handler(setwelcome_handler)
	dispatcher.add_handler(rules_handler)
	dispatcher.add_handler(setrules_handler)
	dispatcher.add_handler(kick_handler)
	dispatcher.add_handler(ban_handler)
	dispatcher.add_handler(add_filter_handler)
	dispatcher.add_handler(filter_list_handler)
	dispatcher.add_handler(remove_filter_handler)
	dispatcher.add_handler(warn_handler)
	dispatcher.add_handler(setwarn_handler)
	dispatcher.add_handler(clearwarn_handler)
	dispatcher.add_handler(ud_handler)
	dispatcher.add_handler(tl_handler)
	dispatcher.add_handler(tts_handler)
	dispatcher.add_handler(weeb_handler)
	dispatcher.add_handler(admins_handler)


	dispatcher.add_handler(msg_text_handler)
	dispatcher.add_handler(msg_all_handler)
	
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()