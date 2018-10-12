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
    type("www.github.com" + Key.ENTER)
    wait(10)
    # Close the window.
    type(Key.F4, KeyModifier.ALT)
    Do.popup("Thank You...!!!", "Message Box", 5)
    
if __name__ == "__main__":
    browser_executable = "chrome.exe"
    OpenURL(browser_executable)
