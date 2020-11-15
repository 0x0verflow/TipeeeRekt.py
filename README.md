> This is only a POC! Don't use this against other people without their permission!

# TipeeeRekt.py
A tool to hack or recover a streamer's Tipeeestream account with a little bit of social enineering.

## Credits
 - Code: @0x0verflow
 - Originally found by @DavAlbert
 
## How to
### Installation
TipeeeRekt.py depends on:
   `colored,
   requests,
   json,
   sys`. 
You can install the missing packages with the following command:
   `pip install colored requests`.
   
### Usage
1) Open Burp Suite and connect it to your browser. You'll need the proxy feature later.

2) Ask the streamer you're watching to show you the URL of a frame or a scene he uses. You can do this by telling him that you've donated, but nothing is happening and you want to help to fix it.

3) Make a screenshot when he shows the end of the URL. All characters after the '#' are the apiKey.

4) Log into Tipeeestream by using a platform the streamer isn't using. While doing this, use Intercept in Burp and forward all requests until you get something looking like this:
![Burp Suite Screenshot: Tipeeestream OAuth login request](https://i.ibb.co/kxNDMDy/tipeeerekt.png)

5) Now run TipeeeRekt.py. You'll see the syntax. Just enter the data of the HTTP request and the apiKey and run the tool. Wait until it finishes.

6) Go back to Burp and turn intercept off. You'll be logged into the streamers account

7) (Optional) Go to Settings -> Management and remove your account. Now there is no more evidence that the streamer's account got hacked.

## Disclaimer
This software is for educational purposes only!
The exploit has already been reported to Tipeeestream. They said it's not an exploit, just normal usage of their API which their users are warned about.
Please ONLY use this tool to recover your own account or to troll people you've got a permission from.
**Any other usage of this tool is illegal.**

