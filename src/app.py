from data_sources.global_cases import GlobalCases

data_source = GlobalCases()

print(data_source.get_total_infection_cases())
