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

# An example: 11.6851 (9.9110, 13.7840) (from P5. 11.6206 (9.8050, 13.6388))

print('Increasing the sample size (n) without changing the observed probability of survival (k/n) should, in theory, '
      'result in higher precision in the model and tighter projection interval bounds.')
print('Due to some issue with the coding that I do not understand, mine did not meaningfully change. '
      'I got the same result with the original gaussian calibration files on which my code is based.')
