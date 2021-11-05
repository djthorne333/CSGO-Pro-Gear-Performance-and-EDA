from selenium import webdriver
import time
import numpy as np
import pandas as pd



driver = webdriver.Chrome(executable_path = )
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://thegamingsetup.com/gaming-mouse/buying-guides/mouse-size-chart-table")
time.sleep(10) # Takes time load page.
first_row = driver.find_element_by_xpath("//*[@id='tablepress-3']/tbody/tr/td[1]")
driver.execute_script("arguments[0].scrollIntoView(true);", first_row)
loops = 0
mouse_array = []
length_array = []
width_array = []
height_array = []
size_array = []
weight_array = []
type_array = []
try:
    while True:
        mouse = driver.find_elements_by_xpath("//*[@id='tablepress-3']/tbody/tr/td[1]")
        length = driver.find_elements_by_xpath("//*[@id='tablepress-3']/tbody/tr/td[2]")
        width = driver.find_elements_by_xpath("//*[@id='tablepress-3']/tbody/tr/td[3]")
        height = driver.find_elements_by_xpath("//*[@id='tablepress-3']/tbody/tr/td[4]")
        size = driver.find_elements_by_xpath("//*[@id='tablepress-3']/tbody/tr/td[5]")
        weight = driver.find_elements_by_xpath("//*[@id='tablepress-3']/tbody/tr/td[7]")
        type = driver.find_elements_by_xpath("//*[@id='tablepress-3']/tbody/tr/td[8]")
        seen_rows = np.arange(len(mouse))  # indexes to loop over new seen rows in this scroll loop
        for i in seen_rows:
            mouse_array.append(mouse[i].text)
            length_array.append(length[i].text)
            width_array.append(width[i].text)
            height_array.append(height[i].text)
            size_array.append(size[i].text)
            weight_array.append(weight[i].text)
            type_array.append(type[i].text)
        driver.execute_script("arguments[0].scrollIntoView(true);", mouse[-1])
        time.sleep(10) #wait for load after scroll
        loops+=1
        if len(mouse) == 115: #113 or 115 of em in inspect search
            break
except Exception as e: #will get e if something else happens, kinda left over from previous code
    print(e)



print(mouse_array)
print(length_array)
print(width_array)
print(height_array)
print(size_array)
print(weight_array)
print(type_array)



print(len(mouse_array))
print(loops)
print(seen_rows)
driver.quit()

array1 = np.array([length_array, width_array, height_array, size_array, weight_array, type_array]).transpose()
df1 = pd.DataFrame(array1, mouse_array, ['length', 'width', 'height', 'size', 'weight', 'type'])
print(df1)
df1.to_csv()




