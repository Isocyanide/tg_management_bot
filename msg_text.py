def msg_text(bot, update, user_data):
	from filters import check_filters
	check_filters(bot, update)