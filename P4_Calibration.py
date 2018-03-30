# Problem 4. Calibration: Mortality probability and 95% credible interval
import CalibrationClasses_P4 as Cls
import CalibrationSettings_P4 as CalibSets
import scr.FigureSupport as Fig

# create a calibration object
calibration = Cls.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# create the histogram of the resampled mortality probabilities
Fig.graph_histogram(
    data=calibration.get_mortality_resamples(),
    title='Histogram of Resampled Mortality Probabilities',
    x_label='Mortality Probability',
    y_label='Counts',
    x_range=[CalibSets.POST_L, CalibSets.POST_U])

# Estimate of mortality probability and the posterior interval
print('Problem 4. The estimate of the mortality probability ({:.{prec}%} credible interval) is'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))

# 0.0868 (0.0718, 0.1029)
