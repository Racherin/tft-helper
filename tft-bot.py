from imagesearch import * 
from pyautogui import screenshot,getActiveWindow
import sys,json
from pynput.mouse import Button, Controller
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\merta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
mouse = Controller()

with open('champions-info.json') as f :
    data = json.load(f)

with open('spots.json') as f :
    spots = json.load(f)

my_spots = spots
my_data = data
active_comp = {'name':'Brawler-Sorcerer','champs':["Malphite","Kha'Zix","Twisted Fate","Caitlyn","Vi","Blitzcrank","Cho'gath","Velkoz"]}

def scan_pool(max_gold):
    screen_shot = region_grabber((0, 0, 2160, 1440))
    scan_list = []
    detected_list=[]
    for i in range(50):   
        if int(my_data['champions'][i]['gold']) <= max_gold :
            scan_list.append(my_data['champions'][i])
    print('Scanning all pool...')
    for i in scan_list:
        im = imagesearcharea("{}".format(i['image']), 450, 950, 1500, 1115, 0.8, screen_shot) #OPTIMIZE EDILEBILIR ...
        if im[0] != -1 :
            count = imagesearch_name("{}".format(i['image']),'pool_box',0.9)
            detected_list.append(i)
    for i in detected_list :
        print(i['name'],", ",end='')
    print(" Found !")
    return detected_list
        
def check_champs(detected_list,gold):
    print('Player has :', gold,' gold.')
    buy_list=[]
    buylist_cost = 0
    for i in detected_list :
        for k in active_comp['champs'] :
            if k == i['name'] :
                buy_list.append(i)
                buylist_cost += int(i['gold'])
    print("Buy List : ",end='')
    for i in buy_list :
        if gold >= int(i['gold']) :
            print(i['name'],"({} gold), ".format(i['gold']),end ='')
            pos = imagesearch("{}".format(i['image']))
            click_image("{}".format(i['image']), pos, "left", 0.2)
            for spot in my_spots['desk'] :
                if spot['current_status'] == "empty" :
                    spot['current_status'] = i['name']
                    for arena_spot in my_spots['arena'] :
                        if arena_spot['owner'] == i['name'] and arena_spot['current_status'] == "empty":
                            move_drag((int(spot['name'].strip('spot_'))) - 1,(int(arena_spot['name'].strip('spot_'))) - 1)
                            arena_spot['current_status'] = arena_spot['owner']
                        elif arena_spot['owner'] == i['name'] and (arena_spot['current_status'] != "empty" or arena_spot['current_status'] != i['name']):
                            pyautogui.moveTo(arena_spot['x'],arena_spot['y'])
                            pyautogui.dragTo(1024, 1024,0.5)#Delete champion from arena
                            move_drag((int(spot['name'].strip('spot_'))) - 1,(int(arena_spot['name'].strip('spot_'))) - 1)
                            arena_spot['current_status'] = arena_spot['owner']
                        elif arena_spot['owner'] == i['name'] and arena_spot['current_status'] == i['name']: #NOT WORKING
                            for i in range(9,0,-1) :
                                if my_spots['desk'][i]['current_status'] == 'empty':
                                    pyautogui.moveTo(spot['x'],spot['y'],0.5)
                                    pyautogui.dragTo(my_spots['desk'][i]['x'],my_spots['desk'][i]['y'],0.5)
                            
                    break
            gold -= int(i['gold'])
        else :
            print('Not enough gold for all buy list.')
    print()
    print('Total cost of buy list :',buylist_cost)

def place_champs():
    place_list = []
    for spot in my_spots['desk']:
        if spot['current_status'] != 'empty' :
            pass

def check_gold():
    print("Gold checking")
    screen_shot = region_grabber((0, 0, 2160, 1440))
    text = pytesseract.image_to_string('test.png', config='digits')
    return text

def auto_roll()