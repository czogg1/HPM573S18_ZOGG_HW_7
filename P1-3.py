import SurvivalModelClasses as Cls

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort
ALPHA = 0.05            # significance level

# create a cohort of patients
myCohort = Cls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)


# Problem 1: Five-year survival
print('Problem 1. The proportion of patients surviving beyond 5 years is', cohortOutcome.get_5y_survival())

# Problem 2: Likelihood assumption
print('Problem 2. The number of participants who survived beyond 5 years in a cohort of N participants '
      'follows a binomial distribution')
print('     with parameter p equal to the true probability '
      'of surviving beyond 5 years and the parameter n equal to the number of participants in the population')

# Problem 3: Likelihood calculation ##ASK##
import scipy.stats as stats
p = 0.5
n = 573
k = 400

print('Problem 3. The likelihood of observing the result of a clinical trial with',
      k, 'observed events out of', n, 'participants and an assumed true propability of',
      p, 'is', stats.binom.pmf(p=p, n=n, k=k))
