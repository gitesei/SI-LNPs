import subprocess
import os
import shutil

shutil.copyfile('state_copy.json', 'state.json')

sed_1 = f"sed -i '4609,4619d;60403,63138d;63159,63176d' state.json"
sed_2 = f"sed -i '4608s/,//;60391s/,//' state.json"
sed_3 = f"""sed -i -e 's/"id": 7/"id": 4/g' state.json"""
sed_4 = f"""sed -i -e 's/"id": 8/"id": 5/g' state.json"""
subprocess.call(sed_1,shell=True)
subprocess.call(sed_2,shell=True)
subprocess.call(sed_3,shell=True)
subprocess.call(sed_4,shell=True)
sed_5 = f"(sed -n '/reactionlist/q;p' ../state.json; sed -n '/reactionlist/,$p' state.json) > output"
sed_6 = "sed -i '60412,60429d' output"

dirname = 'CPP{:.2f}_{:.2f}_{:.1f}'
for pKa in [9.41]:
    for m in [2.03,2.06,1.86,2.54,3.09][:2]:
        for pH in [3.0,4.0,5.0,5.8,6.6,7.4,8.0][:]:
            os.chdir(dirname.format(m,pKa,pH))
            subprocess.call(sed_5,shell=True)
            subprocess.call(sed_6,shell=True)
            subprocess.call('cp output state.json',shell=True)
            os.chdir('../')
for pKa in [8.46]:
    for m in [2.03,2.06,1.86,2.54,3.09][:2]:
        for pH in [3.0,4.0,5.0,5.8,6.6,7.4,8.0][:]:
            os.chdir(dirname.format(m,pKa,pH))
            subprocess.call(sed_5,shell=True)
            subprocess.call(sed_6,shell=True)
            subprocess.call('cp output state.json',shell=True)
            os.chdir('../')
