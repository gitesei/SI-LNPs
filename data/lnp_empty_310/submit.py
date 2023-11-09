import subprocess
import os

dirname = 'CPP{:.2f}_{:.2f}_{:.1f}'
for pKa in [9.41,8.46][:]:
    for m in [1.86,2.03,2.06,2.54,3.09][:3]:
        for pH in [3.0,4.0,5.0,5.8,6.6,7.4,8.0][:3]:
            print(dirname.format(m,pKa,pH))
            os.chdir(dirname.format(m,pKa,pH))
            subprocess.run(['sbatch','submit.sh'])
            os.chdir('../')
