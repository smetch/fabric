# Import Fabric's API module
from fabric.api import *

env.hosts = [
]

# Set the username
env.user   = "fabric"
#env.parallel=True
env.skip_bad_hosts=True
env.timeout=4
env.warn_only=True
env.key_filename = "/home/fabric/.ssh/id_rsa"

def set_hosts(serverlist_file):
   """
        Pass line by line the contents of the field "serverlist_file"
        to fabric as the list of server names
                                            """
#   env.hosts = open('/opt/fabric/serverlist', 'r').readlines()
#   env.hosts = open('/opt/fabric/servershortlist', 'r').readlines()
   env.hosts = open((serverlist_file), 'r').readlines()

def put_script():
    """
        Push the script /usr/local/bin/mountcheck
        to remove server's /tmp folder.
                                            """
    put("/usr/local/bin/mountcheck", "/home/fabric/mountcheck", mode=755)
    run("chmod 755 /home/fabric/mountcheck")

def run_script():
    run("/home/fabric/mountcheck")
    run("rm /home/fabric/mountcheck")

def put_run():
    put_script()
    run_script()

def run_uname():
    run("/bin/uname -r")

def put_run():
    put_script()
    run_script()

def run_uname():
    run("/bin/uname -r")

def run_locate(file):
    fabtools.files.is_file(file,use_sudo=False)

def run_checkwebminrepo():
    run("yum list webmin")

def run_yumlist(package):
    run("yum list " + str(package))

def run_javaversion():
    run("java -version")

def run_getalljava():
    run("rpm -qa | grep jdk")

def run_locatestruts():
    run("locate struts")

def run_epelcheck():
    run("grep enabled /etc/yum.repos.d/epel.repo")

def run_mediamounts():
    run("grep vnuchmedia1 /etc/fstab")

def run_locatestruts():
    run("updatedb")
    run("locate struts")

def run_grepwebminstatus():
    run("grep enabled= /etc/yum.repos.d/webmin.repo")

def run_getenforce():
    run("getenforce")

def run_getresolve():
    run("more /etc/resolv.conf")

def run_clamavdbfiles():
    run("find /var/lib/clamav/ -name main*")
