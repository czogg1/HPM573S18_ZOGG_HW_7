# Problem 5. Projection: Mean survival and 95% projection interval
import CalibrationClasses_P4 as Cls
import CalibrationSettings_P4 as P
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
print('Problem 5. The mean survival time and {:.{prec}%} projection interval is'.format(1 - P.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(P.ALPHA, deci=4))

# 11.5433 (9.8430, 13.6979)
