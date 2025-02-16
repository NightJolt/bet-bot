import env

@env.inject("selenium")
class SeleniumConfig():
    find_element_timeout = 10
    window_width = [0, 0]
    headless = False
    maximized = False

    def apply_options(options):
        if SeleniumConfig.maximized:
            options.add_argument("--start-maximized")
        if SeleniumConfig.headless:
            options.add_argument('--headless')
        if len(SeleniumConfig.window_width) > 1 and SeleniumConfig.window_width[0] > 0 and SeleniumConfig.window_width[1] > 0:
            options.add_argument(f'--window-size={SeleniumConfig.window_width[0]},{SeleniumConfig.window_width[1]}')
        # options.add_argument("user-data-dir=/tmp/tarun")
        # options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument('--proxy-server=180.183.157.159:8080')
        return options