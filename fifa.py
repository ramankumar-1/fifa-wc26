from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Scrapper:
    def __init__(self, target=None):
        self.target=target
        
        # start web driver
        self.options=webdriver.EdgeOptions()
        self.options.add_argument("--headless=true")
        self.driver=webdriver.Edge(options=self.options)

    def extract(self):
        if self.target==None:
            print("mention the url to extract from.")
            return
        else:
            print("Completed Matches: \n")
            self.driver.get(self.target)
            
            # wait for web page to load
            time.sleep(3)
            match_rows=self.driver.find_elements(By.CLASS_NAME,"match-row_matchRowBody__yc8mV")
            for match_row in match_rows:
                extracted_text=match_row.text
                if "FT" in extracted_text:
                    extracted_text=extracted_text.replace("\n","")
                    team_1, team_2 = extracted_text.split("FT")
                    team_1_score=team_1[-1]
                    team_2_score=team_2[0]

                    team_1_name=team_1[:-1]
                    team_2_name=team_2[1:]
                    
                    print(f"{team_1_name} vs {team_2_name}: {team_1_score} - {team_2_score}")

                else:
                    break


    def quit(self):
        if self.driver.session_id:
            self.driver.quit()


if __name__=="__main__":
    target_url=r"https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/scores-fixtures?country=&wtw-filter=ALL"

    scrapper=Scrapper(target_url)
    scrapper.extract()
    scrapper.quit()