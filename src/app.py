from data_sources.global_cases import GlobalCases
from lcd_driver.lcd_display_driver import lcd

data_source = GlobalCases()
lcd_display = lcd()

print(data_source.get_total_infection_cases())
lcd_display.lcd_display_string(data_source.get_total_infection_cases, 1)
