#1-5 had various periods, even sampling, no noise
syn_1,12.0,1.0,1.45
syn_2,12.0,1.0,3.0
syn_3,12.0,1.0,4.0
syn_4,12.0,1.0,4.925
syn_5,12.0,1.0,4.925

#6-10 had the same period as 4&5, but increasing noise
syn_6,12.0,1.0,4.925,n=5

#11-16 had the same period as 4-10 but irregular sampling 
syn_11,6 cycles, 1000 points, noise 10%
syn_12, 6 cycles, 1000 points, noise 25%
syn_13, 6 cycles, 1000 points, noise 50%
syn_14, 60 cycles, 1000 points, noise 10%
syn_15, 60 cycles, 1000 points, noise 25%
syn_16, 60 cycles, 1000 points, noise 50%

#17-20 had irregular sampling with varying number of points
syn_17, 10 cycles, 50 points,no noise
syn_18, 20 cycles, 100 points
syn_19, 50 cycles, 100 points
syn_20, 100 cycles, 100 points

#21-24 had multiple signals, irregular sampling
syn_21,12.0,5.0,1.0,18,0.5, 15 cycles, 1000 points, no noise
syn_22, 12.0,5.0,1.0,18,0.5, 30 cycles, 500 points
syn_23, 12.0,4.5,1.0,18.2,1.5, 34 cycles, 500 points
syn_24, 12.0,6.7,3.0,31.2, 2.0, 34 cycles, 500 points
