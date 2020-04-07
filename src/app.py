from data_sources.global_cases import GlobalCases
from lcd_driver.lcd_display_driver import lcd

data_source = GlobalCases()
lcd_display = lcd()

cases = data_source.get_total_infection_cases()

print(cases)

lcd_display.lcd_display_string("All: " + str(cases.all_cases), 1)
lcd_display.lcd_display_string("Deaths: " + str(cases.deaths), 2)
lcd_display.lcd_display_string("Recovered: " + str(cases.recovered), 3)
