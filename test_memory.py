from memory import save_message, get_history

save_message("john", "user", "hello")

history = get_history("john")

for item in history:
    print(item.user_id, item.role, item.message)