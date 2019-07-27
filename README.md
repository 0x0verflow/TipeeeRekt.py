# TipeeeRekt.py
A tool to hack a streamer's Tipeeestream account by using a little bit of social enineering

## Credits
 - Code: 0x0verflow | http://0x0verflow.cf/
 - Exploit: Garkolym | https://www.youtube.com/channel/UCukS5iWNa60iBC60MCdETBw
 
## How to
### Installation
TipeeeRekt.py is depending on:
   `colored,
   requests,
   json,
   sys`. 
To install these python packages you can use the following commands in your command line:
   `pip install colored &&
   pip install requests &&
   pip install json &&
   pip install sys`
   
### Usage
1) Open Burp Suite and connect it to your browser. You'll need the proxy feature later.
2) Ask the streamer you're watching to show you the URL of a frame or a scene he uses. You can do this by telling him, that you've donated, but nothing is happening and you want to help to fix it.
3) Make a screenshot when he shows the end of the URL. All characters after the '#' are the apiKey.
4) Log into Tipeeestream by using a platform, the streamer isn't using. While doing this, use Intercept in Burp and forward all requests until you get something looking like this:
![Burp Suite Screenshot: Tipeeestream OAuth login request](https://i.ibb.co/kxNDMDy/tipeeerekt.png)
5) Now run TipeeeRekt.py via python on your command line. You'll see the syntax. Just enter the data of the HTTP request and the apiKey and run the tool. Wait until it finishes.
6) Go back to Burp and turn intercept off. You'll be logged into the streamers account
7) (Optional) Go to Settings -> Management and remove your account. Now there is no more evidence, that the streamers account was hacked.

## Disclaimer
This software is for educational purposes only!
The exploit was already reported to Tipeeestream by Garkolym. They said it is not an exploit, just an usage of the API.
