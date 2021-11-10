from typing import get_args
from aiohttp.web import main
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from uuid import UUID
from ChnlPointLib import *
import pprint
import getpass


################## 
# Pathing #
################## 
user_name = str(getpass.getuser())
main_path = ("C:/Users/" + user_name + "/Desktop/Hive-Mind/")
twitch_name = print(str(open(main_path + "Username.txt", "r")))


################## 
# Authentication #
################## 

Auth = open(main_path + "App-ID.txt", "r")
#Auth = open(r"C:\Users\Big KAt\Documents\Python Projects\Twitch\Pubsubv4.0 - GUI update\App-ID.txt")
## http://localhost:1765 ##

Auth2 = open(main_path + "ClientS.txt", "r")

## https://twitchapps.com/tokengen/ ## Scope " bits:read channel:read:redemptions " ##
one = (Auth.read())
two = (Auth2.read())
twitch = Twitch( one , two )



target_scope = [AuthScope.BITS_READ, AuthScope.CHANNEL_READ_REDEMPTIONS, AuthScope.CHANNEL_READ_SUBSCRIPTIONS]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)

# this will open your default browser and prompt you with the twitch verification website
user_auth_token, refresh_token = auth.authenticate()

# add User authentication
twitch.set_user_authentication(user_auth_token, target_scope, refresh_token)


#################### 
#   Your username  #
####################

user_info = twitch.get_users(logins=twitch_name)
user_id = user_info['data'][0]['id']


#######################
# Call back user data #
#######################


#Conditions for BITS redemptions
def callback_bits(uuid: UUID, data: dict):
        print('got Bits callback' + str(uuid))
        print(data)
        pass        

#Conditions for CHANNEL POINTS redemptions
def callback_points(uuid: UUID, data: dict): # channel points system
    #print('got points callback ' + str(uuid) + str(data)) #To see a mess of unessary data dump


    #Sees ID
    #print('got points callback ' + str(uuid))
    # reward information
    reward = data['data']['redemption']['reward']
    # the ID of the reward used
    reward_id = reward['id']
    

    #conditions for when a ID matches
    print("Got Reward ID: " + reward_id)

        #Backwards
    if reward_id == "reward id":
        print("backwards")
        time.sleep(2)
        Thread(target = sounds.derp).start()
        Thread(target = functions.back).start()

        #left
    if reward_id == "reward id":
        print("left")
        time.sleep(2)
        Thread(target = sounds.derp).start()
        Thread(target = functions.left).start()

        #right
    if reward_id == "reward id":
        print("right")
        time.sleep(2)
        Thread(target = sounds.derp).start()
        Thread(target = functions.right).start()

        #forward
    if reward_id == "reward id":
        time.sleep(2)
        Thread(target = sounds.derp).start()
        Thread(target = functions.charge).start()

        #Chaotic Blunder
    if reward_id == "reward id":
        time.sleep(2)
        Thread(target = sounds.derp).start()
        Thread(target = functions.click).start()
        Thread(target = functions.scroll).start()
        Thread(target = functions.charge).start()

#Conditions for Sub subscriptions
# def callback_subs(uuid: UUID, data: dict):
#     print('got Sub callback' + str(uuid) + str(data))
#     subs = data['data']
#     print(subs)
#     pass      

#Conditions for Chat


###############
# PUBSub Core #
###############
    


# starting up PubSub
pubsub = PubSub(twitch)
pubsub.start()



# you can either start listening before or after you started pubsub.
uuid = pubsub.listen_bits(user_id, callback_bits)
uuid = pubsub.listen_channel_points(user_id, callback_points)
#uuid = pubsub.listen_channel_subscriptions(user_id, callback_subs)
#uuid = pubsub.listen_chat_moderator_actions(user_id,)
input('We are listening for redeems but to close press ENTER...')

# you do not need to unlisten to topics before stopping but you can listen and unlisten at any moment you want
pubsub.unlisten(uuid)
pubsub.stop()



