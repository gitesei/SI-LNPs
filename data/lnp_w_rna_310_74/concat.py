import subprocess
import os

dirname = 'CPP{:.2f}_{:.2f}_{:.1f}'
for pKa in [8.46,9.41]:
    for m in [1.86,2.03,2.06]:
        #dirname_1 = dirname.format(m,pKa,5.8)
        #sed_command = f"(sed -n '/reactionlist/q;p' ../{dirname_1:s}/state.json; sed -n '/reactionlist/,$p' state.json) > output"
        for pH in [3.0, 4.0, 5.0, 5.8, 6.6, 7.4, 8.0][:2]:
            dirname_1 = dirname.format(2.06,pKa,4.0)
            sed_command = f"(sed -n '/reactionlist/q;p' ../{dirname_1:s}/state.json; sed -n '/reactionlist/,$p' state.json) > output"
            os.chdir(dirname.format(m,pKa,pH))
            subprocess.call(sed_command,shell=True)
            subprocess.call('cp output state.json',shell=True)
            os.chdir('../')
