# TweetWake - Wake up your desktop while away from home
### Want to be able to wake up your PC at home while outside your home network? TweetWake monitors your Twitter account and can send a wake-on-lan packet when a tweet is detected.

### Benefits / Use Cases
* Run on a low-power device, such as a Raspberry Pi
* Save power by letting your computer sleep when not in use
* Enable remote desktop apps to wake up and connect
* No external static IP configurations from your ISP
* Avoid network vulnerabilities associated with opening your home network to the internet


### How it Works
* Each time the script is run, it will pull the home timeline for a specified Twitter account
* If any tweets are detected in the past X minutes, send a magic packet to the specified MAC address on your home network
* Schedule as a cron job to adjust the polling interval (recommended once per minute)


### Setting up the Script
1. Create a Twitter application with your Twitter developer account.  Credentials are required to use Twitter's API
2. Copy/rename the `sample_config.py` to `config.py`
3. Edit `config.py` and add the following
   1. Twitter API credentials
   2. Twitter handle (your account that you would like to poll)
   3. The MAC address of your device to wake.  
    **Note:** This device must be on the same network and have wake-on-lan enabled in the BIOS and wake-on-magic-packet enabled in the network device driver

