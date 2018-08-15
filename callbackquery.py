def callback_query(bot, update, user_data):
	query = update.callback_query.data
	chat_id = update.callback_query.message.chat_id
	from plugins import plugins_callback

	plugins_callback(bot, update, user_data)