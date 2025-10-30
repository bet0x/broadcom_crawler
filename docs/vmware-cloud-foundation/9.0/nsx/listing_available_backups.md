---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/configure-backup-location/list-the-available-backups.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Listing Available Backups
---

# Listing Available Backups

The backup file server stores backups
from all the NSX Manager or Global Manager nodes. To get the list of backups so that you can find the one you
want to restore, you must run the get\_backup\_timestamps.sh script.

Use the same key size for backup and restore.
If the key size is different at time of backup and restore, the backup does not appear
in the list. Starting in NSX
3.2.1, support includes key size 256-bit, 384-bit, and 521-bit. In 3.2.0, support
includes only 256-bit key size.

The script can be found on each NSX Manager or Global Manager appliance at /var/vmware/nsx/file-store/get\_backup\_timestamps.sh. You can run this
script on any Linux machine or on the NSX appliance. As a best practice, copy this script after
installing NSX to a machine that is not an
NSX Manager or Global Manager so that you can run this script even if all the
NSX Manager or Global Manager nodes become inaccessible. If you need to restore a
backup but have no access to this script, you can install a new NSX Manager or Global Manager
node and run the script there.

You can copy the script to another machine or
to the backup file server by logging in to the NSX Manager or Global Manager as admin and running a CLI command.
For
example:

```
nsxmgr-1> copy file get_backup_timestamps.sh url scp://admin@server1/tmp/
admin@server's password:
nsxmgr-1>
```

The script is interactive and prompts you for the
information that you specified when you configured the backup file server. You can
specify the number of backups to display. Each backup is listed with a timestamp, the
NSX Manager or Global Manager node's IP address or FQDN if the NSX Manager or Global Manager
node is set up to publish its FQDN, and the node ID. For example,

```
admin@host1:/home/admin# ./get_backup_timestamps.sh 
Enter file server ip:
10.10.10.20
Enter port:
22
Enter directory path:
/home/nsx/backups
Enter number of latest backup or press Enter to list all backups:

[email protected]'s password: 
Latest backups:
[Backup timestamp; IP address/FQDN; Node id]
2019-01-22;09:16:43 nsxmgr.example.com 41893642-597b-915f-5117-7da576df4ff2
2019-01-22;09:14:42 nsxmgr.example.com 41893642-597b-915f-5117-7da576df4ff2
2019-01-22;09:13:30 nsxmgr.example.com 41893642-597b-915f-5117-7da576df4ff2
2019-01-22;09:01:52 10.10.10.77 35163642-6623-8f6d-7af0-52e03f16faed
2019-01-22;09:00:33 10.10.10.77 35163642-6623-8f6d-7af0-52e03f16faed
```