import cbapi
from clint.textui import colored

class GetProcessReport(object):

    @staticmethod
    def Run(cb,link):
        print colored.yellow("[*] Getting process report.")
        reportid=link.split("/")[-2:][0]
        segment=link.split("/")[-2:][1]
        print colored.green("[+] Completed.\n")
        return cb.process_events(reportid, segment)