from utility.html_util import HTMLUtil
from data_sources.cases_interface import CasesInterface
from model.cases import Cases

class GlobalCases(CasesInterface):
    def get_total_infection_cases(self) -> Cases:
        html_util = HTMLUtil()
        html_data = html_util.fetch_data("https://www.worldometers.info/coronavirus/", "div", "maincounter-number")

        cases = Cases()
        values = []
        for data_chunk in html_data:
            values.append(int(data_chunk.text.replace(',', '')))

        cases.all_cases = values[0]
        cases.deaths = values[1]
        cases.recovered = values[2]

        return cases