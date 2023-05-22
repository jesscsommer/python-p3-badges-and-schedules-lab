def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badge_msgs = [badge_maker(name) for name in names]
    return badge_msgs

def assign_rooms(names):
    rooms = []
    for i in range(len(names)):
        rooms.append(f'Hello, {names[i]}! You\'ll be assigned to room {i + 1}!')
    return rooms


def printer(names):
    for msg in batch_badge_creator(names):
        print(msg)
    for room in assign_rooms(names):
        print(room)