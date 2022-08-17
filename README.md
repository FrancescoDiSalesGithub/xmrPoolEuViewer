# xmrPoolEuViewer
terminal console viewer for xmrpool.eu worker status

# Installation

Install the requirements by running:

`pip3 install -r requirements.txt`

# How to use xmrPollEuViewer

If you want to check the status of your wallet on xmrpool.eu run the following command:

`python3 main.py "wallet address"`

Where wallet address is the address of your wallet. Example:

`python3 main.py asdkkgjsi43902009530493042390893043143`

# Polling

If you want to check the status of your wallet constantly, you can use the polling script.
First, make the polling.sh script executable: 
`chmod +x polling.sh`

Then as for running the script you have to pass two arguments:
* wallet address
* timeout (in seconds)

Example:
`./polling.sh adsasdar3285989328948329438329 10`

it will check the status of the wallet each 10 seconds.

