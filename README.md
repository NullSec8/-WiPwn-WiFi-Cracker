⚡️ WiPwn – WiFi Cracking Tool

WiFi Cracking TOol for Educational WiFi Pentesting

WiPwn is a powerful, interactive, and educational tool for WiFi network penetration testing. It allows you to scan for networks, brute-force passwords, and generate custom wordlists. Created by NullSec8, strictly for ethical hacking, educational purposes, and controlled environments (your own network or authorized test labs).
⚠️ Legal Disclaimer

    ❌ Do NOT use this tool on networks you don't own or don't have explicit permission to test.
    🔒 The creator takes no responsibility for misuse. This is a tool for learning and research only.

  Project Goals

    Educate on WiFi network security

    Learn password cracking methods (wordlist and full brute-force)

    Practice ethical hacking in a legal, controlled setting

    Use in virtual labs, personal routers, or authorized testbeds

🔧 Features

    📡 Scan WiFi Networks – Detects nearby networks, their SSIDs, and security types

    🧠 Brute-force Using Wordlist – Use your own or default wordlists to attempt password cracking

    🛠️ Generate Custom Wordlists – Create targeted lists based on SSID patterns, prefixes/suffixes, etc.

    🔓 Brute-force Without Wordlist – Try all possible character combinations (slow but thorough)

    🧹 Clear Saved WiFi Profiles – Wipe stored WiFi profiles from your system for privacy

    🖥️ Cross-platform – Works on Linux and Windows (Linux recommended for full features)

⚙️ Requirements

    Python 3.x

    Python modules:

    pip install pywifi pyfiglet termcolor

📥 Installation

git clone https://github.com/NullSec8/-WiPwn-WiFi-Cracker.git
cd -WiPwn-WiFi-Cracker
pip install -r requirements.txt

🪟 Windows Notes

    Install Npcap or WinPcap to enable WiFi scanning

    Run your terminal as Administrator

    Some features may be limited due to PyWiFi constraints

    Linux or Kali Linux is highly recommended

🚀 Usage

    Run the Tool

python wipwn.py

Select an Option

    [1] Scan for networks  
    [2] Bruteforce a network with wordlist  
    [3] Generate wordlist for target  
    [4] Bruteforce without wordlist (all combinations)  
    [5] Clear saved WiFi profiles  
    [6] Exit

    Perform the Action

        Choose your target

        Launch attack or generate wordlist

        Analyze results

🧪 Example Use

Scan networks

Choose [1] to view available SSIDs

Brute-force with a custom wordlist

Choose [2], input SSID and path to your wordlist

Create a targeted wordlist

Choose [3], enter SSID, and let the script generate combinations

🧠 Troubleshooting

    WiFi Adapter Not Found: Make sure it supports monitor mode and is recognized by PyWiFi

    Admin Rights Needed: Run terminal as Administrator on Windows

    Slow Cracking: Brute-force without a wordlist is intensive – use only for short tests

    Windows Limitations: Use Linux for best compatibility and performance

🔐 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute — as long as it’s for educational, non-malicious purposes.
