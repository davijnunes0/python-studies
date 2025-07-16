from pyfiglet import Figlet
import time

def main():

   f = Figlet(font="script")
   
   words = ["I wasn’t the best person—but this isn’t about you.",
            "I wasn’t a good boyfriend, but it’s not that I never loved you.",
            "I don’t live the best way, though I never truly wanted to live.",
            "I wanted you to be alive, but you’re not here.",
            "I’ve found a deeper pain now.",
            "I should have spent more time with you,",
            "and I fear I’ll make that same mistake again.",
            "I want to reach the top, but I feel like I never will."]
            
            
   
   for word in words:
   	print(f.renderText(word))
   	time.sleep(1)
            
   

if __name__ == "__main__":
   main()
