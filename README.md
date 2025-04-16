
WiPwn - WiFi Cracking Tool

WiPwn is a powerful, user-friendly WiFi penetration testing tool that helps you scan, brute-force, and generate custom wordlists for cracking WiFi networks. It is designed exclusively for educational purposes and is intended to be used in environments where you have explicit permission, such as your own networks or test labs. This project is created by NullSec8 and should never be used on any network without permission.

⚠️ Important Warning:
NullSec8, the creator of this tool, absolutely condemns any malicious use of this tool. The goal of this project is to help you learn more about WiFi security, penetration testing, and brute-forcing methods in a controlled, legal, and ethical environment. Using this tool to attack networks without consent is illegal and unethical.
Features

    Scan for WiFi Networks: Discover available networks along with their security types (WPA/WPA2).

    Brute-force Attack: Crack WiFi passwords using either a custom wordlist or by generating all possible password combinations.

    Generate Custom Wordlist: Create a wordlist tailored to the SSID (WiFi network name) with common prefixes, suffixes, and special characters.

    Clear Saved WiFi Profiles: Delete saved WiFi profiles from your system to maintain privacy or cleanup after tests.

    Cross-Platform Compatibility: Works on Linux and Windows, with Windows having some limitations.

Requirements
Prerequisites

    Python 3.x: Ensure that Python 3.x is installed on your system. You can download it from Python's official website.

    Dependencies: The following Python packages are required:

        pywifi — A library for interacting with wireless interfaces.

        pyfiglet — For ASCII art banners.

        termcolor — To add color to terminal outputs.

To install the required dependencies, run:

pip install pywifi pyfiglet termcolor

Installation Instructions

    Clone the Repository: Download or clone the repository to your local machine.

git clone https://github.com/NullSec8/WiPwn.git
cd WiPwn

Install Dependencies: Make sure you have all necessary Python libraries installed.

    pip install -r requirements.txt

Running on Windows

WiPwn can work on Windows, but be aware that some features may be limited because of the way PyWiFi interacts with wireless adapters on this platform. For a smoother experience, we recommend running the tool on Linux or macOS.
Important Notes for Windows Users:

    Npcap/WinPcap: To enable network monitoring functionality, install Npcap or WinPcap. These are libraries that allow network packet capturing:

        Download Npcap

        Download WinPcap

    Run as Administrator: Ensure that you run your terminal or command prompt as Administrator to perform certain actions like scanning networks or clearing saved profiles.

    WiFi Interface: PyWiFi's support for WiFi interfaces on Windows is limited. Some operations, especially WiFi scanning, may not work as expected. For best results, consider using a Linux system.

How to Use
1. Scan for WiFi Networks

    Select this option to scan for nearby WiFi networks. The available networks will be displayed, showing their SSID (network name), security type (WPA/WPA2), and channel.

[1] Scan for networks

2. Brute-force a Network Using a Wordlist

    If you already have a wordlist (a file containing potential passwords), this option allows you to perform a brute-force attack on a network to try all passwords from the wordlist.

[2] Bruteforce a network with wordlist

3. Generate a Custom Wordlist

    This option generates a custom wordlist for cracking a network, using the network's SSID as the base and appending common prefixes, suffixes, and special characters.

[3] Generate wordlist for target

4. Brute-force Without a Wordlist (Try All Combinations)

    If you don't have a wordlist, this option tries all possible combinations of characters (up to a certain length) to guess the WiFi password.

[4] Bruteforce without wordlist (try all combinations)

5. Clear Saved WiFi Profiles

    Deletes all saved WiFi profiles from your system, which can help you clean up after testing or ensure privacy.

[5] Clear saved WiFi profiles

6. Exit

    Exit the program.

Example Usage
Step 1: Run the Program

Execute the script by running:

python wipwn.py

Step 2: Choose an Option

You will be presented with a simple, interactive menu:

[1] Scan for networks
[2] Bruteforce a network with wordlist
[3] Generate wordlist for target
[4] Bruteforce without wordlist (try all combinations)
[5] Clear saved WiFi profiles
[6] Exit

Step 3: Interact

    To scan for WiFi networks, select option 1.

    To crack a network with a wordlist, select option 2.

    To generate a custom wordlist, select option 3.

    To try all combinations for cracking, select option 4.

    To clear all saved WiFi profiles, select option 5.

Step 4: Exit the Program

Once done, you can exit the program by selecting option 6.
Troubleshooting
Common Issues

    WiFi Interface Not Detected: If your WiFi adapter isn't being recognized, ensure that it's properly connected and that you have Npcap or WinPcap installed on Windows.

    Administrator Privileges: On Windows, some actions (like scanning networks or clearing profiles) may require Administrator rights. Make sure to run your terminal or command prompt as Administrator.

    Slow Brute-Force: Brute-forcing without a wordlist can be slow due to the number of possible combinations. It is recommended to use a wordlist for faster attacks.

Windows Limitations

    PyWiFi's support for WiFi interfaces on Windows is limited, which may prevent certain features from working. Linux is recommended for full functionality.

    Windows users may need to experiment with Npcap and WinPcap to get the best results.
