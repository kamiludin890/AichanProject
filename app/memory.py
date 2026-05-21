user_memory = {}


def save_memory(user_id, message):
    if user_id not in user_memory:
        user_memory[user_id] = []

    user_memory[user_id].append(message)

    if len(user_memory[user_id]) > 10:
        user_memory[user_id] = user_memory[user_id][-10:]


def get_memory(user_id):
    return "\n".join(user_memory.get(user_id, []))
