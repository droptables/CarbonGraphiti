import argparse, cbapi
from clint.textui import colored


class Launch(object):
    
    def show_logo(self):
        print colored.cyan("""
    _________             ___.                                    
    \_   ___ \_____ ______\_ |__   ____   ____                    
    /    \  \/\__  \\\_  __ \ __ \ /  _ \ /    \                   
    \     \____/ __ \|  | \/ \_\ (  <_> )   |  \                 
     \______  (____  /__|  |___  /\____/|___|  /                   
            \/     \/          \/            \/                   
            """)
        print colored.green("""
                  ________                    .__    .__  __  .__ 
                 /  _____/___________  ______ |  |__ |__|/  |_|__|
                /   \  __\_  __ \__  \ \____ \|  |  \|  \   __\  |
                \    \_\  \  | \// __ \|  |_> >   Y  \  ||  | |  |   @f4ls3_
                 \______  /__|  (____  /   __/|___|  /__||__| |__|
                        \/           \/|__|        \/             

            """)

    def show_options(self):
        self.show_logo()
        print colored.yellow("usage: ")+colored.magenta("./Carbon-Graphiti -l https://cb-server-url.com/#analyze/00001b23-0000-1fd4-01d0-d69a136419e0/1 -c cb-server.config -o output-name.json\n")

    def get_args(self):

        self.parser = argparse.ArgumentParser(description='Turns a Carbon Black process tree into a semantic graph for consumption by OpenGraphiti')
        self.parser.add_argument('-l','--link', action='store', dest="link", help="Link to Carbon Black process report link.", required=True)
        self.parser.add_argument('-c','--config-file', action='store', dest="configfile", help="Config file for Carbon Black Server settings.", required=True)
        self.parser.add_argument('-o','--output-file', action='store', dest="outputfile", help="Output file to save Semantic graph.", required=True)
        self.parser.add_argument('--cbprotection', action='store_true', dest="cbprotection", help="Integrate results from Cb Enterprise Protection file catalog", default=False)

        self.args = self.parser.parse_args()
        return self.args

    def load_config_file(self, configile):
      cfile= open(configile, "r").readlines()
      serverurl=str(cfile[0].rstrip())
      apitoken=str(cfile[1].rstrip())

      cb = cbapi.CbApi(serverurl,
               token=apitoken,
               ssl_verify=False)

      return cb

    def load_b9_config(self,configile):
      cfile= open(configile, "r").readlines()
      b9serverurl=str(cfile[2].rstrip())
      b9apitoken=str(cfile[3].rstrip())
      return (b9serverurl,b9apitoken)
