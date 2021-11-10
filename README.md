# Hive-Mind 5.0.0
 
- Blue-Bumble

## How to install
- **!! Extract Hive-Mind folder to Desktop (Important! or it wont work unless you change it) !!**

> **Making your first application for twtich** 
> 
* Go to [https://dev.twitch.tv] and sign in and create a new application.
  *  Copy the client Seceret to Clients.txt by clicking "New Secret" 
  *  Copy Client ID to "App-ID.txt"
  *  OAuth redirect url should have "[http://localhost:17563]"
  *  **MAKE SURE NO SPACES IN HERE**
  
> **Add in your username** 
> 
* Copy your username to "Username.txt" (This is the username you see in your channel url like when you share it)
	*  Example "https://www.twitch.tv/th3_bumbl3" my user name would be "th3_bumbl3"
	*  **When you paste it into the "Username.txt" it should looks like this ['th3_bumbl3']**

> **Setting up Redeption ID** 

* Make a custom redemption for moving like forward, backwards, left, right, an chaotic blunder (5 in total).
* Once you have authenticated and connected (default web browser will open and say **Thanks for Authenticating with pyTwitchAPI!**
	*  From here once its running redeem you should get a response in the termial "Got Reward ID: 3dsadfsf3ac-a544-4b34-622226-eefsad542sf287ce"
	*  Edit the Core Script and scrolls down to where you find **reward_id == "reward id":**
		* Paste your reward ID to the corrilating left, right, redeption you want. so it should looks like   
		* For the #left match with left redeption in stream deck **reward_id == "3dsadfsf3ac-a544-4b34-622226-eefsad542sf287ce":**
