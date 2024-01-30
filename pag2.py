import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create a list of URLs to open in incognito t
urls = [
    "https://learn.microsoft.com/en-us/?WT.mc_id=academic&wt.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/?WT.mc_id=credentials&wt.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/?WT.mc_id=training&wt.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/?WT.mc_id=docs&wt.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/?WT.mc_id=answers&wt.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/?WT.mc_id=assessments&wt.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/?WT.mc_id=shows&wt.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/training/modules/challenge-project-use-generative-ai-to-create-business-model-startup/?WT.mc_id=studentamb_262148",
    "https://techcommunity.microsoft.com/t5/educator-developer-blog/master-microsoft-fabric-your-ultimate-guide-to-certification-and/ba-p/4025137?WT.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/ai/?WT.mc_id=studentamb_262148",
    "https://learn.microsoft.com/en-us/collections/8pm3f6kdw4md?WT.mc_id=cloudskillschallenge_4ec5e79f-725d-427e-9c48-6805af903981%3Fwt.mc_id%3Dstudentamb_262148",
    "https://learn.microsoft.com/en-us/training/challenges?id=aeee6acf-22c6-46b5-996b-0e95848c138c&WT.mc_id=cloudskillschallenge_aeee6acf-22c6-46b5-996b-0e95848c138c&wt.mc_id=studentamb_262148"
]

# Create an instance of the Chrome driver with incognito mode enabled
options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)


# Open each URL in a new incognito tab
for url in urls:
    driver.execute_script(f"window.open('{url}', 'tab{len(driver.window_handles)}');")

# Wait for 5 seconds to allow the tabs to load
time.sleep(4)

# Close the tabs
for i in range(len(driver.window_handles)):
    driver.switch_to.window(driver.window_handles[i])
    driver.close()

# Quit the driver
driver.quit()

