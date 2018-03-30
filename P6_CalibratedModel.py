# Problem 6. 95% projection interval
import CalibrationClasses_P6 as Cls
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

# 11.6182 (9.9480, 13.2370); diff: 1.6702, 1.6188 (P5. 11.5433 (9.8430, 13.6979); dif: 1.7003, 2.1546)

print('Increasing the sample size (n) without changing the observed probability of survival (k/n) should, in theory, '
      'result in higher precision in the model and tighter projection interval bounds.')
print('Compared to Problem 5, this is the result that we see.')
