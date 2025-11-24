import requests, os, time, json, webbrowser, datetime, sys
from colorama import init, Fore, Style

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

banner = f"""{Fore.RED}
 ███╗   ██╗██╗   ██╗██╗     ██╗         ███████╗    ██╗  ██╗
 ████╗  ██║██║   ██║██║     ██║         ╚════██║    ╚██╗██╔╝
 ██╔██╗ ██║██║   ██║██║     ██║             ██╔╝     ╚███╔╝
 ██║╚██╗██║██║   ██║██║     ██║            ██╔╝     ██╔██╗
 ██║ ╚████║╚██████╔╝███████╗███████╗       █╔╝     ██╔╝ ██╗
 ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝      ╚═╝      ╚═╝  ╚═╝
{Fore.CYAN}                Unseen.. Untraceable.. Unknown
{Fore.MAGENTA}                     Developed by Null7x © 2025
{Fore.WHITE}                          CONVERTED.. NOT DEFEATED
"""

def beep():
    print("\a" * 2)

def save_satellite_map(lat, lon, ip):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"TARGET_{ip}_{timestamp}_SATELLITE.png"

    print(f"{Fore.RED}[+] Coordinates Locked: {lat}, {lon}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[+] Opening Satellite View...{Style.RESET_ALL}")

    urls = [
        f"https://www.google.com/maps/@{lat},{lon},150m/data=!3m1!1e3",
        f"https://earth.google.com/web/@{lat},{lon},200a,1000d,35y,0h,0t,0r",
        f"https://www.bing.com/maps?cp={lat}~{lon}&lvl=19&style=a",
        f"https://satellites.pro/#{lat},{lon},19",
        f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=19/{lat}/{lon}&layers=N",
    ]

    for url in urls:
        try:
            webbrowser.open(url, new=2)
        except:
            pass

    # optional image attempt
    try:
        img_url = f"https://static.thunderforest.com/transport/{int(float(lat)*100)}/{int(float(lon)*100)}/15.png?apikey=free"
        img_data = requests.get(img_url, timeout=8)
        if img_data.status_code == 200:
            with open(filename, "wb") as f:
                f.write(img_data.content)
            print(f"{Fore.RED}[+] Satellite Snapshot Saved → {filename}{Style.RESET_ALL}")
    except:
        pass


def trace_ip(ip):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print(f"{Fore.YELLOW}[•] Locking Target: {ip} ...", end="")
    time.sleep(1.5)
    print(f"{Fore.GREEN} LOCKED!{Style.RESET_ALL}\n")

    apis = [
        f"https://ipapi.co/{ip}/json/",
        f"http://ip-api.com/json/{ip}?fields=66846719",
        f"https://ipwho.is/{ip}",
        f"https://api.ip.sb/geoip/{ip}",
        f"https://ipinfo.io/{ip}/json",
        f"https://freegeoip.app/json/{ip}"
    ]

    for api_url in apis:
        try:
            response = requests.get(api_url, timeout=8)
            if response.status_code != 200:
                continue

            data = response.json()
            if data.get("error") or data.get("success") is False or data.get("status") == "fail":
                continue

            beep()
            print(f"{Fore.GREEN}╔═══════════════════ TARGET ACQUIRED ═══════════════════╗{Style.RESET_ALL}")
            print(f"   IP           : {data.get('ip', ip)}")
            print(f"   Location     : {data.get('city','Hidden')} • {data.get('region','Hidden')} • {data.get('country_name', data.get('country','Unknown'))}")
            print(f"   ISP          : {data.get('org', data.get('isp', 'Unknown'))}")
            print(f"   ASN          : {data.get('asn', 'N/A')}")
            print(f"   Device       : {'MOBILE' if data.get('mobile', False) else 'PC/DESKTOP'}")
            print(f"   Proxy/VPN    : {'DETECTED' if data.get('proxy', data.get('hosting', False)) else 'CLEAN'}")

            lat = data.get('latitude') or data.get('lat')
            lon = data.get('longitude') or data.get('lon')
            print(f"   Coordinates  : {lat}, {lon}")

            if lat and lon:
                print(f"   Google Maps  : https://maps.google.com?q={lat},{lon}")
                print(f"   Satellite    : https://google.com/maps/@{lat},{lon},150m/data=!3m1!1e3")
                save_satellite_map(lat, lon, ip)

            print(f"   Timezone     : {data.get('timezone','UTC')} | Postal: {data.get('postal','XXXXX')}")
            print(f"{Fore.GREEN}╚══════════════════════════════════════════════════════╝{Style.RESET_ALL}")
            return

        except:
            continue

    print(f"{Fore.RED}[-] Unable to retrieve data. Try again later.{Style.RESET_ALL}")


# ========================== MAIN ==========================
try:
    print(f"{Fore.MAGENTA}[Null7x] Enter Target IP (blank = your IP):{Style.RESET_ALL}")
    target_ip = input(" >>> ").strip()

    if not target_ip:
        try:
            target_ip = requests.get("https://api.ipify.org", timeout=10).text
            print(f"{Fore.CYAN}[+] Your IP detected: {target_ip}")
        except:
            target_ip = "8.8.8.8"
            print(f"{Fore.RED}[!] No internet – using demo IP: 8.8.8.8")

    trace_ip(target_ip)

except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}\n[•] Tracer Stopped by User.")
    sys.exit(0)
