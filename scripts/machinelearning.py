import sys
import os
from pathlib import Path
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from data.create_dataset import create_dataset as cd
from data.create_plots import create_plots as cp

args = sys.argv

cd().get_all_data()

if len(sys.argv) > 1:
    if args[1] == 'plot_all':
        cp().recent_monthly_change()
        cp().monthly_change()
        cp().create_pulled_graph()
        cp().create_clean_graph()
    elif args[1] == 'plot_pull':
        cp().create_pulled_graph()
    elif args[1] == 'plot_clean':
        cp().create_clean_graph()
    elif args[1] == 'plot_process':
        cp().recent_monthly_change()
        cp().monthly_change()

if len(sys.argv) > 2:
    if args[2] == "1":
        os.system('python scripts/model/model_train.py')
