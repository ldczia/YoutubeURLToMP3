import yt_dlp
import os
import re
import sys
from colorama import Fore, Style, init
from os import system
from time import sleep

init(autoreset=True)

YOUTUBE_URL_REGEX = re.compile(
    r'(https?://)?(www\.)?youtube\.com/watch\?v=[\w-]+'
    r'|'
    r'(https?://)?(www\.)?youtu\.be/[\w-]+',
    re.IGNORECASE
)

def yt_url_kontrol(url):
    return YOUTUBE_URL_REGEX.match(url) is not None

def yturl_to_mp3(video_url):
    while True:
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(os.getcwd(), 'output', '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,  
            }
            output_dir = os.path.join(os.getcwd(), 'output')
            os.makedirs(output_dir, exist_ok=True)

           
            sys.stderr = open(os.devnull, 'w')

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=None)
                title = info_dict.get('title', None)

          
            sys.stderr = sys.__stderr__

            print(f"{Fore.LIGHTCYAN_EX}İndirmek istediğiniz MP3 bu mu? {title}{Style.RESET_ALL}")
            print(Fore.YELLOW + "1) Evet\n2) Hayır" + Style.RESET_ALL)
            secim = input(Fore.LIGHTMAGENTA_EX + "Seçim: " + Style.RESET_ALL)

            if secim == '1':
                system("cls||clear")
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(video_url, download=True)
                    title = info_dict.get('title', None)
                system("cls||clear")
                print(f"{Fore.GREEN}MP3 dosyası oluşturuldu: '{title}.mp3'{Style.RESET_ALL}")
                print(f"{Fore.CYAN}İndirilen video başlığı: {title}{Style.RESET_ALL}") 
                break   
            elif secim == '2':
                system("cls||clear")
                print(f"{Fore.YELLOW}Hayır olarak işaretlediniz.\nBaşa döndürülüyor...{Style.RESET_ALL}")
                sleep(3)
                system("cls||clear")
                break  
            else:
                system("cls||clear")
                print(f"{Fore.RED}Geçerli bir seçim yap.{Style.RESET_ALL}")
                sleep(2)
                system("cls||clear")
                continue  

        except Exception as e:
            print(f"{Fore.RED}Hata: {str(e)}{Style.RESET_ALL}")

def yt_baslik_bul(url):
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            return info_dict.get('title', None)
    except Exception as e:
        return str(e)

def __main__():                                 
    print(f""" {Fore.LIGHTCYAN_EX}
--------------------------
 __________    __ _    
 |__  /_ _\\ \\ / // \\                         
   / / | | \\ V // _ \\                         
  / /_ | |  | |/ ___ \\                        
 /____|___| |_/_/   \\_\\                       

--------------------------
    {Style.RESET_ALL}""")
    video_url = input(Fore.LIGHTMAGENTA_EX + "[+] " + Style.RESET_ALL + Fore.YELLOW + "İndirmek istediğiniz Youtube URL adresini girin:\n\n" + Fore.LIGHTMAGENTA_EX + "[+] " + Fore.YELLOW + "Link: " + Style.RESET_ALL)
    if not yt_url_kontrol(video_url):
        print(f"{Fore.RED}Geçersiz URL. Lütfen tekrar deneyin.{Style.RESET_ALL}")
        sleep(2)
        system("cls||clear")
        __main__()
    else:
        title = yt_baslik_bul(video_url)
        system("cls||clear")
        yturl_to_mp3(video_url)
        # print(f"{Fore.CYAN}İndirilen video başlığı: {title}{Style.RESET_ALL}")

if __name__ == "__main__":
    __main__()
