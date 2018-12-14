# TweetWake - Wake up your desktop while away from home
### Want to be able to wake up your PC at home while outside your home network? TweetWake monitors your Twitter account and can send a wake-on-lan packet when a tweet is detected on your home timeline.

### Benefits / Use Cases
* Can run on a low-power device, such as a Raspberry Pi, allowing you to save energy by letting your desktop sleep
* Enable remote desktop apps to start up and become available
* No external static IP configurations from your ISP
* Avoid network vulnerabilities associated with opening your home network to the internet

### How it Works
* Each time the script is run, it will query Twitter pull the home timeline for a specified Twitter account
* If any tweets are detected in the past X minutes, send a magic packet to the specified MAC address on your home network
* Schedule as a cron job to adjust the polling interval (recommended once per minute)


### Setting up the Script
1. Create a Twitter application with your Twitter developer account.  Credentials are required to use Twitter's API.  [More Info](https://developer.twitter.com/en/docs/basics/apps/overview)
2. Clone the repository to a location on your machine, or the device you will run it on

#### Configuration
2. Copy/rename the file `sample_config.py` to `config.py`
3. Edit `config.py` and add the following
   1. Twitter API credentials
   2. Twitter handle (your account that you would like to poll)
   3. The MAC address of your device to wake.  
    **Note:** This device must be on the same network and have wake-on-lan enabled in the BIOS and wake-on-magic-packet enabled in the network device driver: [setup instructions](https://www.lifewire.com/wake-on-lan-4149800)
   4. Detection window in minutes.  On each run the script will check for a tweet within the past X minutes
   
#### Deployment to Raspberry Pi (Raspbian Stretch)
1. ssh into your Raspberry Pi using the devices IP address:   

`ssh pi@192.168.1.2` 


1. Make sure python3 and pip3 are installed:   

`sudo apt-get update && sudo apt-get install python3 && sudo apt-get install python3-pip`


1. If you downloaded the files to your main computer, you will need to copy them to the Raspberry Pi home directory
   1. From your main computer, navigate one folder up from the cloned repository.  You should be able to see the `tweetwake` folder
   1. Run the copy command to transfer the files to the Raspberry Pi 
   
   `scp -pr <PATH-TO-FOLDER>/tweetwake/ pi@192.168.1.2:/home/pi/tweetwake`
   
   
   1. You should now have all the same contents available in `/home/pi/tweetwake` on the Raspberry Pi
   
1.  Update your cron configuration to run the script every minute.  This appends an entry if there are existing cron jobs. This causes python3 to execute the script every minute and output the log to `/home/pi/tweetwake/log.txt`
   1. 
   
   `(crontab -l && echo "* * * * *  python3 /home/pi/tweetwake/tweetwake.py > /home/pi/tweetwake/log.txt") | crontab -`
   
     
#### Troubleshooting
* View the contents of `/home/pi/tweetwake/log.txt` for any errors using `cat log.txt`
* Ensure the script is configured to run every minute.  You can run `crontab -l` to view the file.  Ensure there is an entry: `* * * * * python3 /home/pi/twitterwake/tweetwake.py > /home/pi/twitterwake/log.txt`
* Make sure your `config.py` file has the correct credentials and settings
* Make sure your computer is enabled for wake-on-lan: [setup instructions](https://www.lifewire.com/wake-on-lan-4149800)


