from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time

path = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
options.add_argument("--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data")
options.add_argument('--profile-directory=Profile 2')
driver = webdriver.Chrome(path, chrome_options=options)

def round_seconds(dts):
    date = dts.split(" ")[0]
    h, m, s = [dts.split()[1].split(':')[0],
                dts.split()[1].split(':')[1],
                str(round(float(dts.split()[1].split(':')[-1])))]
    return date + ' ' + h + ':' + m + ':' + s

driver.get("https://itch.io/jams/new")

## jam information edit
jamVersion = 1
jamTitle = driver.find_element_by_name("jam[title]")
shortText = driver.find_element_by_name("jam[short_text]")
jamURL = driver.find_element_by_name("jam[slug]")
StartDate = round_seconds(str(datetime.datetime.now() + datetime.timedelta(50)))
EndDate = round_seconds(str(datetime.datetime.now() + datetime.timedelta(52)))
VotingEndDate = round_seconds(str(datetime.datetime.now() + datetime.timedelta(60)))
Descrption = driver.find_element_by_id("redactor-uuid-0")

jamTitle.send_keys("Artificial Game Jam")
shortText.send_keys("A Jam Created by an Artificial Intelligence")
jamURL.send_keys(f"aijam{str(jamVersion)}")
Descrption.send_keys(#The description. It is too long so I didn't include it here. Plus, the description might subject to change in the future)

driver.execute_script(f'document.getElementsByName("jam[start_date]")[0].value = "{StartDate}"')
driver.execute_script(f'document.getElementsByName("jam[end_date]")[0].value = "{EndDate}"')
driver.execute_script(f'document.getElementsByName("jam[voting_end_date]")[0].value = "{VotingEndDate}"')

create = driver.find_elements_by_class_name("button")[-1]
create.click()

time.sleep(1)

## jam page edit
driver.find_element_by_class_name("edit_theme_btn").click()

bg1 = driver.find_element_by_name("jam_layout[bg_color]")
bg2 = driver.find_element_by_name("jam_layout[bg_color2]")
textColor = driver.find_element_by_name("jam_layout[text_color]")
css = driver.find_element_by_name("jam_layout[css]")
save = driver.find_element_by_xpath("/html/body/div[1]/div/form/div[8]/button")
Exit = driver.find_element_by_xpath("/html/body/div[1]/div/form/div[8]/a")

bg1.send_keys(Keys.CONTROL + "a")
bg1.send_keys(Keys.DELETE)
bg1.send_keys("#11142c")

bg2.send_keys(Keys.CONTROL + "a")
bg2.send_keys(Keys.DELETE)
bg2.send_keys("#16101e")

textColor.send_keys(Keys.CONTROL + "a")
textColor.send_keys(Keys.DELETE)
textColor.send_keys("#ffffff")

css.send_keys("""
.jam_title_header{
    color: #F1EC40;
    font-family: 'Baloo Da 2', cursive;
}

.jam_body{
    border: 5px #16101E solid;
    border-radius: 3%;
}
""")

save.click()
Exit.click()


