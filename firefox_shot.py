from selenium import webdriver

def make_profile():
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', '127.0.0.1')
    profile.set_preference('network.proxy.socks_port', 9050)
    profile.set_preference('network.proxy.socks_version', 5)
    profile.set_preference('network.proxy.socks_remote_dns', 'true')
    profile.update_preferences()
    return profile

def shot_screen(url):
    browser.save_screenshot('tmp/'+url+'.png')


profile = make_profile()
browser=webdriver.Firefox(profile)
url="ipinfo.io"
browser.get("http://"+url)
shot_screen(url)
browser.quit()
