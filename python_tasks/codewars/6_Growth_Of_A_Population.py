# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year
# and moreover 50 new inhabitants per year come to live in the town.
# How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
from math import ceil


# p0 - population at the beginning of the year
#
def nb_year(p0, percent, aug, p):
    years_counter = 0
    while(p0 < p):
        yearly_result = p0 * percent / 100 + aug
        p0 += yearly_result
        years_counter = years_counter + 1

    return years_counter

print(nb_year(1500, 5, 100, 5000))


    # your code