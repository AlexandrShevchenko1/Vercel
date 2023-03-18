from apscheduler.schedulers.background import BackgroundScheduler
import gdown  # or any other module you need to run the Colab notebook
import subprocess

def run_colab():
   # Download the notebook file from Google Drive using gdown
   gdown.download("https://colab.research.google.com/drive/1YobWGoCwnZqf4CFJv-X6UI2fmtEPTQCa#scrollTo=vU91ottmE1tu", "C:\Users\WA1\TradingBot")
   
   # Execute the notebook using nbconvert
   cmd = ["jupyter", "nbconvert", "--to", "notebook", "--execute", "<local file name>"]
   subprocess.run(cmd)

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(run_colab, 'interval', minutes=10)
scheduler.start()