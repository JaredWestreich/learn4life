fall_winter_students = 7800
spring_summer_students = fall_winter_students / 0.7 - fall_winter_students
total_students = fall_winter_students + spring_summer_students

cost_per_class = 250

seniors_rate = 0.65
adult_rate = 1
subsidy_rate = 0.2

adult_proportion = 0.62
seniors_proportion = 0.36
subsidy_proportion = 0.02

adult_fee_increase = 0.5
seniors_fee_increase = 1.3
subsidy_fee_increase = 0

adult_drop_rate = 0.25
seniors_drop_rate = 0.5
subsidy_drop_rate = 0

this_year_adult_revenue = total_students * adult_proportion * adult_rate * cost_per_class
next_year_adult_revenue = this_year_adult_revenue * (1 + adult_fee_increase) * (1 - adult_drop_rate)

this_year_seniors_revenue = total_students * seniors_proportion * seniors_rate * cost_per_class
next_year_seniors_revenue = this_year_seniors_revenue * (1 + seniors_fee_increase) * (1 - seniors_drop_rate)

this_year_subsidy_revenue = total_students * subsidy_proportion * subsidy_rate * cost_per_class
next_year_subsidy_revenue = this_year_subsidy_revenue * (1 + subsidy_fee_increase) * (1 - subsidy_drop_rate)

this_year_revenue = this_year_adult_revenue + this_year_seniors_revenue + this_year_subsidy_revenue
next_year_revenue = next_year_adult_revenue + next_year_seniors_revenue + next_year_subsidy_revenue

revnue_increase = next_year_revenue - this_year_revenue