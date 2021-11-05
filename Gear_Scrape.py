from selenium import webdriver
import time
import numpy as np
import pandas as pd


driver = webdriver.Chrome(executable_path = )
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://prosettings.net/cs-go-pro-settings-gear-list/")
time.sleep(10) # Takes time load page.
#table = driver.find_element_by_xpath("//table[@id='table_1']") #Find the table scroll into view.
first_row = driver.find_element_by_xpath("//table[@id='table_1']/tbody/tr/td[7]")
driver.execute_script("arguments[0].scrollIntoView(true);", first_row)
loops = 0
sens_array = []
teams_array = []
players_array = []
role_array = []
mouse_array = []
mouse_hertz_array = []
dpi_array = []
edpi_array = []
zoom_sens_array = []
accel_array = []
windows_sens_array = []
raw_input_array = []
hertz_array = []
resolution_array = []
aspect_ratio_array = []
mouse_pad_array = []
try:
    while True:
        sens = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[7]") #get all we can see in this scroll
        teams = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[1]")
        players = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[2]")
        role = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[3]")
        mouse = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[4]")
        mouse_hertz = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[5]")
        dpi = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[6]")
        edpi = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[8]")
        zoom_sens = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[9]")
        accel = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[10]")
        windows_sens = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[11]")
        raw_input = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[12]")
        hertz = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[14]")
        resolution = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[16]")
        aspect_ratio = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[17]")
        mouse_pad = driver.find_elements_by_xpath("//table[@id='table_1']/tbody/tr/td[19]")
        seen_rows = np.arange(len(sens))  # indexes to loop over new seen rows in this scroll loop
        for i in seen_rows:
            sens_array.append(sens[i].text)  # add new values in this scroll loop to total sensitivities
            teams_array.append(teams[i].text)
            players_array.append(players[i].text)
            role_array.append(role[i].text)
            mouse_array.append(mouse[i].text)
            mouse_hertz_array.append(mouse_hertz[i].text)
            dpi_array.append(dpi[i].text)
            edpi_array.append(edpi[i].text)
            zoom_sens_array.append(zoom_sens[i].text)
            accel_array.append(accel[i].text)
            windows_sens_array.append(windows_sens[i].text)
            raw_input_array.append(raw_input[i].text)
            hertz_array.append(hertz[i].text)
            resolution_array.append(resolution[i].text)
            aspect_ratio_array.append(aspect_ratio[i].text)
            mouse_pad_array.append(mouse_pad[i].text)
        driver.execute_script("arguments[0].scrollIntoView(true);",sens[-1])#scroll to last row that could be seen so we can start form there next loop
        # print(sens[i].text)
        # print(teams[i].text)
        # print(players[i].text)
        # print(role[i].text)
        # print(mouse[i].text)
        # print(mouse_hertz[i].text)
        # print(dpi[i].text)
        # print(edpi[i].text)
        # print(zoom_sens[i].text)
        # print(accel[i].text)
        # print(windows_sens[i].text)
        # print(raw_input[i].text)
        # print(hertz[i].text)
        # print(resolution[i].text)
        # print(aspect_ratio[i].text)
        # print(mouse_pad[i].text)
        loops+=1
        if len(sens_array) >= 475: #we want the 475 from that table
            break
except Exception as e: #will get e if something else happens, kinda left over from previous code
    print(e)
# print(sensarray)
# print(len(sensarray))
# print(loops)
# print(seen_rows)


print(sens_array)
print(teams_array)
print(players_array)
print(role_array)
print(mouse_array)
print(mouse_hertz_array)
print(dpi_array)
print(edpi_array)
print(zoom_sens_array)
print(accel_array)
print(windows_sens_array)
print(raw_input_array)
print(hertz_array)
print(resolution_array)
print(aspect_ratio_array)
print(mouse_pad_array)

print(len(sens_array))
print(loops)
print(seen_rows)
driver.quit()

array1 = np.array([sens_array, teams_array, role_array, mouse_array, mouse_hertz_array, dpi_array, edpi_array, zoom_sens_array,
                   accel_array, windows_sens_array, raw_input_array, hertz_array, resolution_array, aspect_ratio_array, mouse_pad_array]).transpose()
gear_df = pd.DataFrame(array1, players_array, ['sens', 'teams', 'role', 'mouse', 'mouse_hertz', 'dpi', 'edpi', 'zoom_sens',
                   'accel', 'windows_sens', 'raw_input', 'hertz', 'resolution', 'aspect_ratio', 'mouse_pad'])
print(gear_df)
gear_df.to_csv()