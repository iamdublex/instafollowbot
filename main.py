from selenium import webdriver
from time import sleep
from fake_useragent import UserAgent
import random
import requests
import re
import os
import 

#MADE BY DOUBLEXERROR
#https://github.com/doublexerror/instafollowbot

#get proxies list
p = open("proxies.txt")
pr = p.read()
proxies = pr.splitlines()

#input your totating proxie into #here
rproxie = "p.webshare.io:19999"

#variables
i = 0
brp = 0
#restart
restart = True
true = True

def genName():
    #customize with your own name lists (for example: top 100 names in your country)
    fNames = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Avram", "Antonije", "Agnija", "Andjelija", "Adam", "Aran", "Aleksandra", "Andjelka", "Aksentije", "Arsenije", "Aleksija", "Anica", "Aleksa", "Atanasije", "Ana", "Anka", "Aleksandar", "Acim", "Anastasija", "Antonina", "Alimpije", "Aca", "Angelina", "Andjelko", "Aco", "Andrijana", "Andrija", "Andja", "Bane", "Borivoje", "Biljana", "Borka", "Blagoje", "Borisav", "Bisenija", "Bosiljka", "Blagomir", "Borislav", "Biserka", "Branislava", "Blaza", "Bosko", "Blaginja", "Branka", "Bogdan", "Branimir", "Blagica", "Bratislava", "Bogoljub", "Bratislav", "Blazenka", "Bogomir", "Branko", "Bogdana", "Bogosav", "Bratoljub", "Bogdanka", "Borko", "Budimir", "Bozana", "Bozidar", "Budislav", "Bozidarka", "Bojan", "Buda", "Bojana", "Vasilije", "Vladislav", "Valerija", "Visnja", "Vekoslav", "Vlajko", "Varvara", "Vladanka", "Velibor", "Vlastimir", "Vasilija", "Vlastimirka", "Velimir", "Vojimir", "Veliborka", "Vojislava", "Velislav", "Vojin", "Velinka", "Vujadinka", "Veljko", "Vojislav", "Vera", "Viktorija", "Vladeta", "Vukota", "Violeta", "Vladimir", "Vuksan", "Viseslava", "Gorica", "Gojko", "Grujica", "Goca", "Golub", "Goran", "Grozdana", "David", "Dositej", "Daliborka", "Dragoslava", "Dalibor", "Dragan", "Damjanka", "Dubravka", "Damjan", "Dragisa", "Danica", "Dunja", "Danilo","Dejan", "Dragoljub", "Divna", "Desimir", "Dragomir", "Dobrila", "Despot", "Drgorad", "Dobrinka", "Dimitrije", "Dragoslav", "Dobroslavka", "Dmitar", "Dragutin", "Doris", "Dobrasin", "Drazo", "Doroteja", "Dobrivoj", "Drasko", "Dragana", "Dobrilo", "Dusan", "Draginja", "Dobrica", "Dragica", "Luka", "Stefan", "Vuk", "Lazar", "Filip", "Pavle", "Aleksa", "Nikola", "Vasilije", "Uros", "Andrej", "Petar", "Viktor", "Vukasin", "Jovan", "Mihajlo", "Kosta", "Bogdan", "Dusan", "Sofija", "Dunja", "Milica", "Sara", "Nina", "Ana", "Mila", "Masa", "Lena", "Teodora", "Helena", "Petra", "Anjda", "Andjela", "Una", "Jana", "Nikolina", "Tara", "Elena", "Anja", "Luka", "Stefan", "Vuk", "Lazar", "Filip", "Pavle", "Aleksa", "Nikola", "Vasilije", "Uros", "Andrej", "Petar", "Viktor", "Vukasin", "Jovan", "Mihajlo", "Kosta", "Bogdan", "Dusan", "Sofija", "Dunja", "Milica", "Sara", "Nina", "Ana", "Mila", "Masa", "Lena", "Teodora", "Helena", "Petra", "Anjda", "Andjela", "Una", "Jana", "Nikolina", "Tara", "Elena", "Anja"]
    characters = ["nbgd", "zemun", "04", "03", "cc", "_", "_04", "_03", "__"]
    lNames = ["Jovanovic", "Petrovic", "Nikolic", "Ilic", "Djordevic", "Pavlovic", "Markovic", "Popovic", "Stojanovic", "Zivkovic", "Jankovic", "Todorovic", "Stankovic", "Ristic", "Kostic", "Milosevic", "Cvetkovic", "Kovacevic", "Dimitrijevic", "Tomic", "Krstic", "Ivanovic", "Lukic", "Filipovic", "Savic", "Mitrovic", "Lazic", "Petkovic", "Obradovic", "Aleksic", "Radovanovic", "Lazarevic", "Vasic", "Milovanovic", "Jovic", "Stevanovic", "Milenkovic", "Milosavljevic", "Mladenovic", "Zivanovic", "Simic", "Djuric", "Nedeljkovic", "Novakovic", "Marinkovic", "Bogdanovic", "Knezevic", "Radosavljevic", "Mihajlovic", "Gajic", "Mitic", "Stefanovic", "Blagojevic", "Antic", "Vasiljevic", "Jevtic", "Djokic", "Stojkovic", "Vukovic", "Rakic", "Stanojevic", "Pesic", "Tasic", "Milic", "Milanovic", "Zdravkovic", "Grujic", "Babic", "Vuckovic", "Matic", "Peric", "Ciric", "Paunovic", "Marjanovic", "Maksimovic", "Andelkovic", "Jakovljevic", "Gavrilovic", "Veljkovic", "Tosic", "Trajkovic", "Ivkovic", "Arsic", "Miletic", "Velickovic", "Radovic", "Miljkovic", "Nesic", "Jeremic", "Radulovic", "Djurdevic", "Milojevic", "Urosevic", "Boskovic", "Trifunovic", "Bozic", "Radivojevic", "Djukic", "Milutinovic", "Stamenkovic"]

    genime = ''.join(random.choice(fNames) + random.choice(lNames))
    global genuser
    genuser = ''.join(genime + random.choice(nastavci))
    print(genuser)
    return genime

    
#generating a username
def username():
    return genuser

def generatePassword():
    #Edit in password to use into #here
    password = "lozinka1234"
    return password

def genEmail() :
    return ''.join(username() + '@mail.com')

def register():
    # fill the name value
    fullname_field = driver.find_element_by_name('fullName')
    fullname_field.send_keys(genName())

    # fill the username value
    username_field = driver.find_element_by_name('username')
    name = username()
    username_field.send_keys(name)
        
    # fill the email value
    email_field = driver.find_element_by_name('emailOrPhone')
    email_field.send_keys(genEmail())

    # fill the password value
    password_field = driver.find_element_by_name('password')
    passW = generatePassword()
    password_field.send_keys(passW)
    sleep(1)
    # submit
    submit = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button')
    submit.click()


print("Input user to follow: ")
follow = input()     
print("Input followers to add: ")   
repeat = int(input())
print("Use rotating proxies? y/n")
qrotate = input()
if qrotate == "y":
    rotate = True
if qrotate == "n":
    rotate = False


while restart:
    if i == repeat:
        break
    while true == True:
        ua = UserAgent()
        userAgent = ua.random
        var = repeat - i
        print("Followers left to add: " + str(var))
        chrome_options = webdriver.ChromeOptions()
        #headless for some reason works slower than normal.
        #chrome_options.headless = True
        chrome_options.add_argument(f'user-agent={userAgent}')
        if rotate == False:
            chrome_options.add_argument('--proxy-server=' + proxies[brp])
            print("Using Proxy: " +proxies[brp])    
        else:       
            chrome_options.add_argument('--proxy-server=' + rproxie)
            print("Using rotating proxy: " + rproxie)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.instagram.com/") 
        sleep(2)
        # Check if instagram loaded proprely.
        try:
            test = driver.find_element_by_name('fullName')
        except:
            print("Failed loading instagram.")
            break
        else:
            try:
                test = driver.find_element_by_xpath("//*[contains(text(), 'To help personalize content, tailor and measure ads')]")            
            except:
                print("Successfuly Loaded instagram")
                challenge = False
            else:
                print("Solving challenge....")
                challenge = True
        try:
            print ("Trying to register...")
            register()
        except:
            print("Something crashed here...")
            break     
        sleep(4)
        if challenge == True:
            try:
                el = driver.find_element_by_id("igCoreRadioButtonageRadioabove_18")
            except:
                print("Challenge went wrong...")
                break
            else:
                el.click()
                sleep(2)
                try:
                    nextt = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/button")
                except:
                    print("Somehow pressing next went wrong. lol")
                    break
                else:
                    nextt.click()
                    sleep(4)
        else:
            sleep(2)        
        try:
            el = driver.find_element_by_xpath("//*[contains(text(), 'Please try')]")
        except:
            print('Successfuly registered.')
            driver.get("https://www.instagram.com/" + follow)
            try:
                followb = driver.find_element_by_xpath("//*[text()='Follow']") 
            except:
                print("Something went wrong...")
            else:
                followb.click()
                print("Successfuly followed said user.")
                i+=1
                sleep(1)     
        else:
            print('Unsuccessfuly registered.')
        finally:
            break
    driver.close()
    brp+=1        
