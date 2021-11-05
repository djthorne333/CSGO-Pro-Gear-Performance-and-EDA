from selenium import webdriver
import time
import numpy as np
import pandas as pd



driver = webdriver.Chrome(executable_path = )
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://esports.leetify.com/stats")
time.sleep(5) # Takes time load page.
aim_tab = driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[1]/div[1]/button[2]")
aim_tab.click()
time.sleep(5)
#table = driver.find_element_by_xpath("//table[@id='table_1']") #Find the table scroll into view.
first_row = driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[2]")
driver.execute_script("arguments[0].scrollIntoView(true);", first_row)
loops = 0
players_array = []
teams_array = []
hs_acc_array = []
acc_spotted_array = []
acc_all_array = []
acc_spray_array = []
counter_strafe_array = []
crosshair_placement_array = []
time_to_damage_array = []
try:
    while True:
        players = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[1]/a/div")
        teams = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[2]")
        hs_acc = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[3]")
        acc_spotted = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[4]")
        acc_all = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[5]")
        acc_spray = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[6]")
        counter_strafe = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[7]")
        crosshair_placement = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[8]")
        time_to_damage = driver.find_elements_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[9]")
        seen_rows = np.arange(len(teams))  # indexes to loop over new seen rows in this scroll loop
        for i in seen_rows:
            players_array.append(players[i].text)
            teams_array.append(teams[i].text)  # add new values in this scroll loop to total sensitivities
            hs_acc_array.append(hs_acc[i].text)
            acc_spotted_array.append(acc_spotted[i].text)
            acc_all_array.append(acc_all[i].text)
            acc_spray_array.append(acc_spray[i].text)
            counter_strafe_array.append(counter_strafe[i].text)
            crosshair_placement_array.append(crosshair_placement[i].text)
            time_to_damage_array.append(time_to_damage[i].text)
        next_button = driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/div/pagination-controls/pagination-template/ul/li[10]/a")
        next_button.click()
        time.sleep(5) #wait for load after click
        first_row = driver.find_element_by_xpath("/html/body/app-root/app-topnav-layout/app-stats/div/div/div[2]/table/tbody/tr/td[2]")
        driver.execute_script("arguments[0].scrollIntoView(true);", first_row)
        time.sleep(5) #wait for load after scroll (dont think I actually need this after scrolls, probably already loaded)
        loops+=1
        if len(teams_array) == 217: #we want the 20*10 + 17 from pages of table
            break
except Exception as e: #will get e if something else happens, kinda left over from previous code
    print(e)



print(players_array)
print(teams_array)
print(hs_acc_array)
print(acc_spotted_array)
print(acc_all_array)
print(acc_spray_array)
print(counter_strafe_array)
print(crosshair_placement_array)
print(time_to_damage_array)


print(len(teams_array))
print(loops)
print(seen_rows)
driver.quit()

array1 = np.array([teams_array, hs_acc_array, acc_spotted_array, acc_all_array, acc_spray_array,
                   counter_strafe_array, crosshair_placement_array, time_to_damage_array]).transpose()
performance_df = pd.DataFrame(array1, players_array, ['team', 'hs acc', 'acc spotted', 'acc all', 'acc spray', 'counter strafe',
                                           'crosshair_placement', 'time_to_damage'])
print(performance_df)
performance_df.to_csv()