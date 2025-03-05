from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import random
import random_names
def formfill():
    cookieok = False
    attempts = 0
    emailformats = ["fn.ln","ln.fn","fnln","fn1ln"]
    emailproviders = ["gmail.com","yahoo.com","outlook.com","hotmail.com","icloud.com"]
    driver = webdriver.Firefox()
    driver.get("https://secured.heritage.org/the-doge-survey/")
    title = driver.title
    elements = [driver.find_element(By.ID,"environmental_protection_agency__5"),driver.find_element(By.ID,"federal_bureau_of_investigation__5"),driver.find_element(By.ID,"department_of_education__5"),driver.find_element(By.ID,"department_of_housing_and_urban_development__5"),driver.find_element(By.ID,"department_of_state__5"),driver.find_element(By.ID,"45_million_for_a_diversity_and_inclusion_scholarship_in_burma__very_supportive"),driver.find_element(By.ID,"3_million_for_girlcentered_climate_action_in_brazil__very_supportive"),driver.find_element(By.ID,"125_million_to_push_critical_race_theory_in_public_health_policy__very_supportive"),driver.find_element(By.ID,"280000_for_diverse_bird_watcher_groups__very_supportive"),driver.find_element(By.ID,"3267000_to_build_a_transgender_health_guide_website_meant_to_increase_access_to_genderaffirming_care_also_known_as_mutilation___very_supportive"),driver.find_element(By.ID,"do_you_believe_the_federal_government_needs_to_be_responsible_with_taxpayer_dollars_and_not_spend_more_money_than_it_takes_in_no"),driver.find_element(By.ID,"do_you_support_significant_cuts_to_the_federal_budget_to_eliminate_budget_deficits_and_pay_down_the_national_debt_no"),driver.find_element(By.ID,"do_you_believe_the_department_of_government_efficiency_doge_will_be_an_effective_tool_for_eliminating_excessive_government_spending__no")]
    starttime = datetime.now().second
    while cookieok == False:
        try:
            cookiebutton = driver.find_element(By.CLASS_NAME,"vwo-notification-bar__button")
            cookiebutton.click()
        except:
            attempts += 1
            if attempts > 1000:
                cookieok = True
            else:
                if datetime.now().second > starttime + 10:
                    cookieok = True
                else:
                    continue
        else:
            cookieok = True
    for i in elements:
        try:
            cookiebutton = driver.find_element(By.CLASS_NAME,"vwo-notification-bar__button")
            cookiebutton.click()
        except:
            i.click()
        else:
            i.click()
    firstnamefield = driver.find_element(By.ID,"first_name")
    lastnamefield = driver.find_element(By.ID,"last_name")
    emailfield = driver.find_element(By.ID,"email")
    firstname = random_names.First()
    lastname = random_names.Last()
    emailformat = random.choice(emailformats)
    emailprovider = random.choice(emailproviders)
    firstnameprocessed = "".join(char for char in firstname if char.isalnum() or char == ".").replace("hit", "sample")
    lastnameprocessed = "".join(char for char in lastname if char.isalnum() or char == ".").replace("hit", "sample")
    if emailformat == "fn.ln":
        email = f"{firstnameprocessed.lower()}.{lastnameprocessed.lower()}@{emailprovider}"
    elif emailformat == "ln.fn":
        email = f"{lastnameprocessed.lower()}.{firstnameprocessed.lower()}@{emailprovider}"
    elif emailformat == "fnln":
        email = f"{firstnameprocessed.lower()}{lastnameprocessed.lower()}@{emailprovider}"
    else:
        email = f"{firstname.lower()[0]}{lastname.lower()}@{emailprovider}"
    firstnamefield.send_keys(firstname)
    lastnamefield.send_keys(lastname)
    emailfield.send_keys(email)
    submitbutton = driver.find_element(By.ID,"lp-pom-button-122")
    submitbutton.click()
    wait(driver, 15).until_not(EC.title_is(title))
    driver.close()

while True:
    formfill()