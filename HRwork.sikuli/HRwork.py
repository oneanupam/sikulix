def OpenURL(browser_executable):
    """ Function to open a URL in chrome browser. """
    type("r", KeyModifier.WIN)       
    wait(3)       
    type(Key.DELETE)     
    wait(3)         
    type(browser_executable + Key.ENTER)        
    wait(3)        
    type(Key.UP, KeyModifier.WIN)         
    wait(3)
    type("www.naukri.com" + Key.ENTER)
    wait(10)

def HRwork():
    if exists("1531340523266.png"):
        click("1531340523266.png")

    wait(3)
    click("1531388452968.png")

    wait(3)
    type("1531340919583.png", "anupam@gmail.com")
    wait(2)
    type(Key.TAB)
    wait(2)
    type("anupam" + Key.ENTER)
    wait(5)
    type(Key.F4, KeyModifier.ALT)
    Do.popup("Thank You...!!!", "Message Box", 5)     
    
if __name__ == "__main__":
    browser_executable = "chrome.exe"
    OpenURL(browser_executable)
    HRwork()
