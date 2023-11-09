import subprocess
import os

dirname = 'CPP{:.2f}_{:.2f}_{:.1f}'
for pKa in [9.41,8.46][:1]:
    #for m in [2.06,2.12,2.22,2.26,2.41,2.54,2.64,2.8,2.93,3.03][:2]:
    #for m in [2.12, 2.22, 2.26, 2.41, 2.64, 2.8, 2.93]:
    for m in [1.86,2.03,2.06,2.22,2.26,2.54,2.80,2.93,3.03,3.09][3:]:
        for pH in [3.0,4.0,5.0,5.8,6.6,7.4,8.0][:]:
            print(dirname.format(m,pKa,pH))
            os.chdir(dirname.format(m,pKa,pH))
            subprocess.run(['sbatch','submit.sh'])
            os.chdir('../')
