## EER scikitlearn 버전 ##

from sklearn.metrics import roc_curve, auc

from utility.datasetutil import *

# 하나씩 불러서 평균으로 계산
# epoch = 390
score_path1 = r'C:\Users\8138\Desktop\best\3real_SDU_A_Proposed_best_shift_ver2.csv'

S1 = np.array(csv2list(score_path1))

labels = S1[:, 0].astype(float)
score1 = S1[:, 3:5].astype(float)

# score는 positive case던 negative case던 1가지 값만 주기
# 어차피 positive case로 계산하면 1-계산된 EER을 해야지 원하는 값 형태가 되기 때문에 되도록 negative case의 score주고 계산 진행하기
fpr, tpr, thr = roc_curve(labels, score1[:, 1], pos_label=1)

fnr = 1 - tpr
eer_threshold = thr[np.nanargmin(np.absolute((fnr - fpr)))]
EER = fpr[np.nanargmin(np.absolute((fnr - fpr)))]

print(EER)
with open(r'C:\Users\8138\Desktop\best\3real_HKPU_A_test_result_EER.txt', 'a+') as result:
    result.write(str(EER) + '\n')


'''
def make_fpr_tpr(score_path1,score_path2):
    S1 = np.array(csv2list(score_path1))
    S2 = np.array(csv2list(score_path2))

    AllS = np.concatenate((S1, S2), axis=0)

    labels = AllS[:, 0].astype(np.float)
    score1 = AllS[:, 3:5].astype(np.float)

    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    test_labels=[]
    for i in range(2):
        if i==0:
            input_label = np.where(labels == 0, 1, 0)
            test_labels.append(input_label)
        else:
            input_label = np.where(labels == 1, 1, 0)
            test_labels.append(input_label)
        fpr[i], tpr[i], _ = roc_curve(labels, score1[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    return fpr,tpr,roc_auc,test_labels,score1

fpr,tpr,roc_auc,test_labels,score1=make_fpr_tpr(score_path1,score_path2)
test_labels=np.array(test_labels)
# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(test_labels.ravel(), score1.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

fpr2,tpr2,roc_auc2,test_labels2,score2=make_fpr_tpr(score_targetpath1,score_targetpath2)
test_labels2=np.array(test_labels2)
# Compute micro-average ROC curve and ROC area
fpr2["micro"], tpr2["micro"], _ = roc_curve(test_labels2.ravel(), score2.ravel())
roc_auc2["micro"] = auc(fpr2["micro"], tpr2["micro"])


plt.figure()
lw = 2
plt.rc('font', size=15)
plt.rc('legend', fontsize=10)

plt.yticks(np.arange(0,105,5))
plt.plot(np.arange(100,0,-1), color='black',
         lw=lw, linewidth=1)
plt.plot(fpr[1]*100, tpr[1]*100, color='b',
         lw=lw,linewidth=1)
plt.plot(fpr2[1]*100, tpr2[1]*100, color='r',
         lw=lw ,linewidth=1)

plt.xlim([0, 5])
plt.ylim([95, 100])
plt.xlabel('FAR (%)')
plt.ylabel('GAR (%)')
#plt.legend(loc="lower right")

plt.savefig('EER_SDU-DB_calculation_origin_closed.png')

plt.show()

print('aaaa')
'''