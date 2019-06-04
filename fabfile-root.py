# Import Fabric's API module
from fabric.api import *

env.hosts = [
]

# Set the username
env.user   = "ansible"
#env.parallel=True
env.skip_bad_hosts=True
env.timeout=4
env.warn_only=True
env.key_filename = "/home/ansible/.ssh/id_rsa"

def set_hosts(serverlist_file):
   """
	Pass line by line the contents of the field "serverlist_file"
	to fabric as the list of server names
					    """
#   env.hosts = open('/root/fabric/serverlist', 'r').readlines()
#   env.hosts = open('/root/fabric/servershortlist', 'r').readlines()
   env.hosts = open((serverlist_file), 'r').readlines()

def put_script():
    """
        Push the script /opt/scripts/mountcheck
        to remove server's /tmp folder.
                                            """
    put("/opt/scripts/mountcheck", "/home/fabric/bin/mountcheck", mode=755)
    run("chmod 755 /home/fabric/bin/mountcheck")

def run_script():
    run("/home/fabric/bin/mountcheck")
    run("rm /home/fabric/bin/mountcheck")

def put_run():
    put_script()
    run_script()

def run_uname():
    run("/bin/uname -r")

def run_yumlist(package):
    run("yum list installed " + str(package))

def run_yumupdate(package):
    run("yum update -y " + str(package))

def run_yuminstall(package):
    run("sudo yum install -y " + str(package))

def run_yumremove(package):
    run("yum remove -y " + str(package))

def run_restartservice(service):
    run("sudo systemctl restart " + str(service))

def run_enableservice(service):
    run("sudo systemctl enable " + str(service))

def run_disableservice(service):
    run("sudo systemctl disable " + str(service))

def run_stopservice(service):
    run("sudo systemctl stop " + str(service))

def run_statusservice(service):
    run("sudo systemctl status " + str(service))

def run_allyumupdate():
    run("sudo yum update -y ")

def run_yumnokernel():
    run("yum -y --exclude=kernel\* update")

def run_reboot():
    run("sudo shutdown -r now")

def new_user(username, admin='no', comment="No comment provided"):
    print("New User (%s): %s" % (username, comment))
#    print(username, comment)
    pass

def add_cert():
    put("/etc/pki/tls/certs/star.systems.hosting.icfi.com.crt", "/etc/pki/tls/certs/star.systems.hosting.icfi.com.crt")
    run("chmod 644 /etc/pki/tls/certs/star.systems.hosting.icfi.com.crt")
    put("/etc/pki/tls/private/star.systems.hosting.icfi.com.key", "/etc/pki/tls/private/star.systems.hosting.icfi.com.key")
    run("chmod 600 /etc/pki/tls/private/star.systems.hosting.icfi.com.key")

def add_routetest():
    put("/root/bin/routetest", "/usr/local/bin/routetest")
    run("cod 755 /usr/local/bin/routetest")

def put_routetest():
    """
        Push the script /opt/scripts/routetest
        to remove server's /usr/local/bin/ folder.
                                            """
    put("/opt/scripts/routetest", "/usr/local/bin/routetest", mode=755)
    run("chmod 755 /usr/local/bin/routetest")

def run_vmwaretoolsupdate():
    """
	Runs sudo /usr/bin/vmware-config-tools.pl -d
					"""
    run("sudo /usr/bin/vmware-config-tools.pl -d")


def put_clamfiles():
    """
        Push the script /opt/scripts/clamscan_daily.sh
        to remote server's /usr/local/bin folder.
                                            """
    put("/opt/scripts/clamscan_daily.sh", "/usr/local/bin/clamscan_daily.sh", mode=755)
    run("chmod 755 /usr/local/bin/clamscan_daily.sh")

def run_istallclamav():
    run("yum -y install clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd")

def run_disable_rhnplugin():
    """
	edits /etc/yum/pluginconf.d/rhnplugin.conf to disable rhn to allow Subscription-manager to function correctly
					"""
    run("sed -i 's/enabled = 1/enabled = 0/g' /etc/yum/pluginconf.d/rhnplugin.conf")

def put_tomcatlog_service():
    """
	Push the files to Tomcat servers that will force the system to allow 
	read access on /var/log/tomcat at every restart.
					"""
    put("/usr/local/bin/tomcatlog.sh", "/usr/local/bin/tomcatlog.sh")
    run("chmod +x /usr/local/bin/tomcatlog.sh")
    put("/usr/lib/systemd/system/tomcatlogrights.service", "/usr/lib/systemd/system/tomcatlogrights.service")
    run("systemctl daemon-reload")
    run("systemctl enable tomcatlogrights")
    run("systemctl start tomcatlogrights")

def run_removelogline():
    """
  	removes olddir line from /etc/logrotate.d/samba file
					"""
    run("sed -i 's/olddir \/var\/log\/samba\/old/#olddir \/var\/log\/samba\/old/g' /etc/logrotate.d/samba")
    run("rm -rf /var/log/samba/old /var/log/samba/cores")

def run_startensableyumcron():
    """
	RH7 disbles and stops the yum-cron service
					"""
    put("/opt/files/rhel7/yum-cron.conf", "/home/ansible/")
    put("/opt/files/rhel7/yum-cron-hourly.conf", "/home/ansible/")
    run("sudo cp /home/ansible/yum-cron* /etc/yum/")
    run("sudo systemctl enable yum-cron")
    run("sudo systemctl restart yum-cron")

def run_stopdisableyumcron():
    """
	RH7 disbles and stops the yum-cron service
					"""
    run("systemctl disable yum-cron")
    run("systemctl stop yum-cron")

def run_rh6stopdisableyumcron():
    """
	RH6 disbles and stops the yum-cron service
					"""
    run("chkconfig off yum-cron")
    run("service yum-cron stop")

def put_etcissue():
    put("/etc/issue", "/home/ansible/issue")
    run("sudo cp /home/ansible/issue /etc/motd")

def reg_insights():
    run("sudo insights-client --register")

def putrun_satdev():
#    run("rm -f /home/ansible/sat*")
    put("/opt/files/scripts/attach-satellite-DEV.sh", "/home/ansible/")
    run("sudo chmod +x /home/ansible/attach-satellite-DEV.sh")
    run("sudo /home/ansible/attach-satellite-DEV.sh")
    run("rm -f /home/ansible/attach-satellite-DEV.sh")

def putrun_sattest():
    run("rm -f /home/ansible/sat*")
    put("/opt/files/scripts/attach-satellite-TEST.sh", "/home/ansible/")
    run("sudo chmod +x /home/ansible/attach-satellite-TEST.sh")
    run("sudo /home/ansible/attach-satellite-TEST.sh")
    run("rm -f /home/ansible/attach-satellite-TEST.sh")

def putrun_satstage():
    run("rm -f /home/ansible/sat*")
    put("/opt/files/scripts/attach-satellite-STAGE.sh", "/home/ansible/")
    run("sudo chmod +x /home/ansible/attach-satellite-STAGE.sh")
    run("sudo /home/ansible/attach-satellite-STAGE.sh")
    run("rm -f /home/ansible/attach-satellite-STAGE.sh")

def putrun_satprod():
    run("rm -f /home/ansible/sat*")
    put("/opt/files/scripts/attach-satellite-PROD.sh", "/home/ansible/")
    run("sudo chmod +x /home/ansible/attach-satellite-PROD.sh")
    run("sudo /home/ansible/attach-satellite-PROD.sh")
    run("rm -f /home/ansible/attach-satellite-PROD.sh")


def put_puppetconf():
    put("/opt/files/rhel7/puppet.conf", "/home/ansible/puppet.conf")
    run("sudo cp /home/ansible/puppet.conf /etc/puppetlabs/puppet/puppet.conf")
    run('''sudo sed -i "s/\[host\]/$HOSTNAME/g" /etc/puppetlabs/puppet/puppet.conf''')

def run_puppetagent():
    run("sudo puppet agent -tv")

def run_addsatkey():
    run("curl https://rwgovxsatlte63.icfgov.wan:9090/ssh/pubkey >> .ssh/authorized_keys")

def put_copylogs():
    put("/opt/files/scripts/copylogs.sh", "/home/ansible/copylogs.sh", mode=755)
    run("sudo cp /home/ansible/copylogs.sh /usr/local/bin/copylogs.sh")
    run("sudo chmod 755 /usr/local/bin/copylogs.sh")

def put_nessussudo():
    put("/opt/files/rhel7/rwgov_nessus_scanner", "/home/ansible/rwgov_nessus_scanner")
    run("sudo cp /home/ansible/rwgov_nessus_scanner /etc/sudoers.d/rwgov_nessus_scanner")
    run("sudo chmod 0440 /etc/sudoers.d/rwgov_nessus_scanner")
    run("rm /home/ansible/rwgov_nessus_scanner")

def put_webminciphers():
    put ("/opt/files/webmin/miniserv.conf", "/home/ansible/miniserv.conf")
    put ("/opt/files/webmin/miniserv.users", "/home/ansible/miniserv.users")
    run ("sudo cp /home/ansible/miniserv.* /etc/webmin/")
    run ("sudo chown root:bin /etc/webmin/miniserv.*")
    run ("sudo chmod 600 /etc/webmin/miniserv.*")

def kill_apachemanual():
    run ("sudo rm -f /etc/httpd/conf.d/manual.conf*")
    run ("sudo rm -rf /usr/share/httpd/manual")

def put_resolv():
    put ("/etc/resolv.conf", "/home/ansible/resolv.conf")
    run ("sudo cp /home/ansible/resolv.conf /etc/resolv.conf")
    run ("rm /home/ansible/resolv.conf")

def run_subs():
    run("sudo subscription-manager repos --enable=rhel-\*-satellite-tools-\*-rpms")

def run_tmpvar():
    run("echo 'export TMPDIR=/tmp' >> .bash_profile")

def run_abrtlist():
    run("sudo abrt-cli -a list")

def run_abrtrmall():
    run("sudo su -")
    run("abrt-cli rm /var/spool/abrt/*")

def run_rmvartmpyum():
    run("sudo rm -rf /var/tmp/yum-*")

def put_sshdconfig():
    put ("/opt/files/rhel7/sshd_config", "/home/ansible/sshd_config")
    run("sudo cp /home/ansible/sshd_config /etc/ssh/sshd_config")
    run("sudo systemctl restart sshd")

def run_remount():
    run("sudo mount -a")

def put_rhsmback():
    put("/opt/files/rhel7/rhsm/rhsm.conf.rh", "/home/ansible/rhsm.conf")
    run("sudo cp /home/ansible/rhsm.conf /etc/rhsm/")
    run("rm -f /home/ansible/rhsm.conf")

def run_subscribetoredhat():
    run("sudo subscription-manager clean")
    run("sudo subscription-manager register --username=ddonley@icfi.com --password=ddonley  --auto-attach")
    run("sudo subscription-manager repos --enable=rhel-7-server-optional-rpms")
