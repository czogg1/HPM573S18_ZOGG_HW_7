# Problem 6. 95% projection interval
import CalibrationClasses as Cls
import CalibrationSettings_P6 as P
import scr.FigureSupport as Fig

# initialize a calibrated model
calibrated_model = Cls.CalibratedModel('CalibrationResults.csv')
# simulate the calibrated model
calibrated_model.simulate(P.NUM_SIM_COHORTS, P.SIM_POP_SIZE, P.TIME_STEPS)

# plot the histogram of mean survival time
Fig.graph_histogram(
    data=calibrated_model.get_all_mean_survival(),
    title='Histogram of Mean Survival Time',
    x_label='Mean Survival Time (Year)',
    y_label='Count',
    x_range=[7, 13])

# report mean and projection interval
print('Problem 6. The mean survival time and {:.{prec}%} projection interval is'.format(1 - P.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(P.ALPHA, deci=4))

# An example of output: 11.6840 (9.8772, 13.9504) versus from P5: 11.6304 (9.8366, 13.8879)

print('Increasing the sample size (n) without changing the observed probability of death (k/n) did change '
      'the estimated 95% projection interval.')
print('The projection bounds became tighter, more narrow. The mean remained unchanged.')
