import SurvivalModelClasses as Cls
import scr.SamplePathClasses as SamplePathSupport
import scr.FigureSupport as Fig

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort
ALPHA = 0.05            # significance level

# create a cohort of patients
myCohort = Cls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)

# plot the sample path
#SamplePathSupport.graph_sample_path(
#    sample_path=cohortOutcome.get_survival_curve(),
#    title='Survival Curve',
#    x_label='Time-Step (Year)',
#    y_label='Number Survived')

# plot the histogram
#Fig.graph_histogram(
#    data=myCohort.get_survival_times(),
#    title='Histogram of Patient Survival Time',
#    x_label='Survival Time (Year)',
#    y_label='Count')

# print the patient survival time
#print('Average survival time (years):', cohortOutcome.get_ave_survival_time())
#print('95% CI of average survival time (years)', cohortOutcome.get_CI_survival_time(ALPHA))


# Problem 1: Five-year survival
print('Problem 1. The proportion of patients surviving beyond 5 years:', cohortOutcome.get_5y_survival())

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
      k, 'observed events out of', n, 'participants and assumed true propability',
      p, 'is', stats.binom.pmf(p=p, n=n, k=k))

# Problem 4. Calibration ##ASK: likely same issue as above##
# In theory, run RunCalibration.py

# Problem 5. Projection
# In theory, run RunCalibratedModel.py

# Problem 6. Projection
# Repeat Problem 4 and Problem 5 with updated parameters.

