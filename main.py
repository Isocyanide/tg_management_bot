filter_dict = {}
warn_dict = {}
warn_limit_dict = {}
PluginsConversationHandler = 0

# from load_database import load_database
# chats_data = load_database()

def plugins(bot, update, user_data):
	from plugins import plugins
	plugins(bot, update, user_data)

def ban(bot, update):
	from ban import ban
	ban(bot, update)

def kick(bot, update):
	from kick import kick
	kick(bot, update)

def add_filters(bot,update):
	from filters import add_filters
	add_filters(bot,update)

def Message(bot, update):
	from filters import check_filters
	check_filters(bot, update)

def filter_list(bot, update):
	from filters import filter_list
	filter_list(bot, update)

def remove_filter(bot, update):
	from filters import remove_filter
	remove_filter(bot, update)

def warn(bot,update):
	from warn import warn
	warn(bot,update)

def set_warn(bot, update):
	from warn import set_warn
	set_warn(bot, update)

def clear_warns(bot, update):
	from warn import clear_warns
	clear_warns(bot, update)

def ud(bot, update):
	from ud import ud
	ud(bot, update)

def main():
	from telegram.ext import (Updater, MessageHandler, Filters, CommandHandler,
							  ConversationHandler, CallbackQueryHandler, RegexHandler)
	import logging
	logging.basicConfig(level = logging.INFO,
						format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	updater = Updater(token="TOKEN GOES HERE")

	dispatcher = updater.dispatcher

	from plugins import plugins_callback
	global PluginsConversationHandler

	PluginsHandler = CommandHandler('plugins', plugins, pass_user_data = True)
	PluginsCallbackHandler = CallbackQueryHandler(plugins_callback, pass_user_data = True)
	filters_handler=MessageHandler(Filters.text, Message)
	
	KickHandler = CommandHandler('kick', kick)
	BanHandler = CommandHandler('ban', ban)

	add_filter_handler=CommandHandler('filter',add_filters)
	filter_list_handler=CommandHandler('filters',filter_list)
	remove_filter_handler=CommandHandler('stop',remove_filter)


	warn_handler=CommandHandler('warn', warn)
	set_warn_handler=CommandHandler('set_warn', set_warn)
	clear_warn_handler=CommandHandler('clearwarns', clear_warns)

	ud_handler=CommandHandler('ud', ud)

	dispatcher.add_handler(PluginsHandler)
	dispatcher.add_handler(PluginsCallbackHandler)
	dispatcher.add_handler(KickHandler)
	dispatcher.add_handler(BanHandler)
	dispatcher.add_handler(add_filter_handler)
	dispatcher.add_handler(filters_handler)
	dispatcher.add_handler(filter_list_handler)
	dispatcher.add_handler(remove_filter_handler)
	dispatcher.add_handler(warn_handler)
	dispatcher.add_handler(set_warn_handler)
	dispatcher.add_handler(clear_warn_handler)
	dispatcher.add_handler(ud_handler)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()