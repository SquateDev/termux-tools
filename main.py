from colorama import Fore, Style
import os, time

def menu():
 print(Fore.WHITE+"[ "+Fore.RED+"1"+Fore.WHITE+" ] : IpLogger");
 print(Fore.WHITE+"[ "+Fore.GREEN+"2"+Fore.WHITE+" ] : Phone Info");
 print(Fore.WHITE+"[ "+Fore.YELLOW+"3"+Fore.WHITE+" ] : IP-Location");
 print(Fore.WHITE+"[ "+Fore.BLUE+"4"+Fore.WHITE+" ] : CheckWeather");
 print(Fore.WHITE+"[ "+Fore.PURPLE+"5"+Fore.WHITE+" ] : Exit");
 choice_input = input(Fore.YELLOW+"\nSelect Number : "+Fore.BLUE);
def icon():
	os.system("clear");
	time.sleep(1);
	print("Loading [ "+Fore.GREEN+"█"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"██"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"███"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"████"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"█████"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"██████"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"███████"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"████████"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"█████████"+Fore.WHITE+" ]");
	time.sleep(1);
	os.system("clear");
	icon_img = """
         ██
         ██
     ██████████
         ██
         ██
         ██
         ██
         ██
	""";
	print(Fore.RED+icon_img);
	menu();

icon();
