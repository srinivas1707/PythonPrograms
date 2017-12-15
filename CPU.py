import multiprocessing

count=multiprocessing.cpu_count()
if count >=0:
        print count
