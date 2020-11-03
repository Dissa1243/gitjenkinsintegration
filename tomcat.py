import psutil
running_programm = "tomcat" #Whatever the name of your programm
pythons_psutil = []
for p in psutil.process_iter():
    try:
        if p.name() == running_programm:
            pythons_psutil.append(p)
    except psutil.Error:
        pass
if pythons_psutil :
    print "It's running !!"
