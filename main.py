from colorama import Fore, Style
import os, time

def krest():
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

def IpLogger():
 os.system("clear");
 time.sleep(0.9);
 krest();
 print("Ip Logger");


def menu():
 print(Fore.WHITE+"[ "+Fore.RED+"1"+Fore.WHITE+" ] : IpLogger");
 print(Fore.WHITE+"[ "+Fore.GREEN+"2"+Fore.WHITE+" ] : Phone Info");
 print(Fore.WHITE+"[ "+Fore.YELLOW+"3"+Fore.WHITE+" ] : IP-Location");
 print(Fore.WHITE+"[ "+Fore.BLUE+"4"+Fore.WHITE+" ] : CheckWeather");
 print(Fore.WHITE+"[ "+Fore.GREEN+"5"+Fore.WHITE+" ] : Exit");
 choice_input = input(Fore.YELLOW+"\nSelect Number : "+Fore.BLUE);
 if "1" in choice_input.lower():
  IpLogger();
 if "2" in choice_input.lower():
  PhoneInfo();

def icon():
	os.system("clear");
	time.sleep(0.4);
	print("Loading [ "+Fore.GREEN+"█"+Fore.WHITE+" ]");
	time.sleep(0.3);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"██"+Fore.WHITE+" ]");
	time.sleep(0.9);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"███"+Fore.WHITE+" ]");
	time.sleep(0.7);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"████"+Fore.WHITE+" ]");
	time.sleep(0.3);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"█████"+Fore.WHITE+" ]");
	time.sleep(0.8);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"██████"+Fore.WHITE+" ]");
	time.sleep(2);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"███████"+Fore.WHITE+" ]");
	time.sleep(0.2);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"████████"+Fore.WHITE+" ]");
	time.sleep(0.3);
	os.system("clear");
	print("Loading [ "+Fore.GREEN+"█████████"+Fore.WHITE+" ]");
	time.sleep(0.5);
	os.system("clear");
	krest();
	menu();

icon();
