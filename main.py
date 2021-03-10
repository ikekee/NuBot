from vk_api.vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
import random
vk_session = VkApi(token='cffeaea983141ec8773bd5297a11ac46f64dfb9f4357d9ba71d97b5ad5e0032aea23e9564b9ae207552c6')
api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, 186515839)
for event in longpoll.listen():
    event = event.object
    print(event)
    id = event['from_id']
    name = api.users.get(user_ids=id)[0]['first_name']
    api.messages.send(

        peer_id=event['peer_id'],
        message=f"{name}, и это ты написал?",
        random_id=random.randint(0, 99999999999),
        attachment='photo36066442_457241712_66edd3998cfe69ef1b'
    )
