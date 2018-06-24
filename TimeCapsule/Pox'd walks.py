from selenium import webdriver

def replays ():
    
    # Inicialization
    browser = webdriver.Chrome('chromedriver.exe')
    browser.implicitly_wait(2) 
    replays = []
    # Login
    browser.get(r'https://hsreplay.net/games/mine/#hero=shaman')
    browser.find_element_by_xpath(r'/html/body/div/div/form/p[1]/button'
                                  ).click()
    inputbox = browser.find_element_by_xpath(r'//*[@id="accountName"]')
    inputbox.send_keys('tiago.vello@gmail.com')
    inputbox = browser.find_element_by_xpath(r'//*[@id="password"]')
    inputbox.send_keys('T31g4V2ll4')
    browser.find_element_by_xpath(r'//*[@id="submit"]').click()
    # Search
    browser.find_element_by_xpath(
             r'//*[@id="myreplays-infobox"]/div[3]/div/span[7]/div').click()
    browser.find_element_by_xpath(
             r'//*[@id="myreplays-infobox"]/div[2]/ul/li[1]').click()
    
    # input the pages from which you wish to scrap the url
    star_page = 1
    end_page = 4
    for i in range (star_page, end_page):
        # Create a url list for the replays
        for j in range (1,101):
            x=r'//*[@id="my_replays-container"]/div/div[2]/div[2]/div[2]/a[{}]'
            replays.append(browser.find_element_by_xpath(x.format(str(j))
            ).get_attribute('href'))
    # Go to the next page
    input('Press enter, after you go to the next page, to continue')
    browser.close()
    return replays

# Configure the first page manualy because selenium can't do it
def wait_for_page_configuration():
    confirmation = '0'
    while confirmation != 'y':
        confirmation = input(
            'Turn on the Event log, set the speed, rewind and press "y"')                  
replays = replays()

# Returns a data frame with the replay info
def info(replays):
    row = []
    for i in range(len(replays)):
        browser.get(replays[i])
        if i == 0:
            wait_for_page_configuration()
        get_page_info()
               
        
def get_page_info ():
    game_ended = False
    game_info = []
    while (game_ended == False):
        # add a new play to the collected information about the game if it 
        # wasn't added before
        play = browser.find_element_by_xpath(
        r'//*[@id="joust-container"]/div/div[1]/div[2]').text
        if play not in game_info:
            game_info.append(play)
        # check if game has ended
        last_play = browser.find_element_by_xpath(
        r'//*[@id="joust-container"]/div/div[1]/div[2]/div[20]').text
        if 'wins' in last_play:
            game_ended = True
    # add the rest of the plays to the collected game information
    for i in range(2,21):
        play = browser.find_element_by_xpath(
        r'//*[@id="joust-container"]/div/div[1]/div[2]/div[{}]'.format(i)).text
        game_info.append(play)
    return 0