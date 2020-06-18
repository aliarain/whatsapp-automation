from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    print("Hello World!")

schedculer = BlockingScheduler()

