from selenium import webdriver
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference('network.proxy.socks_version', 5)
profile.set_preference('network.proxy.socks_remote_dns', 'true')
profile.update_preferences()
browser=webdriver.Firefox(profile)
browser.get('http://ipinfo.io/')


browser.close()
