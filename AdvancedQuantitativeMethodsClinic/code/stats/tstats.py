# http://iaingallagher.tumblr.com/post/50980987285/t-tests-in-python
#
# 1-sample t-test
# The 1-sample t-test is used when we want to compare a sample mean to a population mean
# (which we already know). The average British man is 175.3 cm tall. A survey recorded the
# heights of 10 UK men and we want to know whether the mean of the sample is different
# from the population mean.

from scipy import stats
one_sample_data = [177.3, 182.7, 169.6, 176.3, 180.3, 179.4, 178.5, 177.2, 181.8, 176.5]
one_sample = stats.ttest_1samp(one_sample_data, 175.3)
print "The t-statistic is %.3f and the p-value is %.3f." % one_sample

# Here we can conclude that the average height of our sample is significantly different
# (p < 0.05) from the average British male height. The return value is the result of a
# two-sided t-test and is a tuple containing the t-value and the p-value.

# Unpaired t-test
# This test compares two unrelated samples. In the example below data was collected on the
# weight (kg) of 8 elderly women and 8 elderly men. We are interested in whether the
# weights of these two samples is different.
#
female = [63.8, 56.4, 55.2, 58.5, 64.0, 51.6, 54.6, 71.0]
male = [75.5, 83.9, 75.7, 72.5, 56.2, 73.4, 67.7, 87.9]

two_sample = stats.ttest_ind(male, female)

print "The t-statistic is %.3f and the p-value is %.3f." % two_sample

# assuming unequal population variances
two_sample_diff_var = stats.ttest_ind(male, female, equal_var=False)

print "If we assume unequal variances than the t-statistic is %.3f and the p-value is %.3f." % two_sample_diff_var
