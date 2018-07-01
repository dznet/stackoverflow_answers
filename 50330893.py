def feed(bot, update):
    # send reply to the user
    bot.send_message(chat_id=update.message.chat_id,
                     text="reply this message")
    # forward user message to group
    # note: group ID with the negative sign
    bot.forward_message(chat_id='-1010101001010',
                        from_chat_id=update.message.chat_id,
                        message_id=update.message.message_id)
