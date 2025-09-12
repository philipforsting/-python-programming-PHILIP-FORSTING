TP = 2
FP = 2
FN = 11
TN = 985

acc = (TP+TN) / (TP+TN+FP+FN)

print(f"00_3_Classification accuracy: the accuracy of this model is {acc}. ")

# I consider the fire detection model to be bad. Fires are only detected in 2 out of 13 samples 
# so a more relevant formula for calculating accuracy would be TP / (TP +FN). The number of FNs 
# should be 0 or at least very close to 0 if more samples had been recorded.