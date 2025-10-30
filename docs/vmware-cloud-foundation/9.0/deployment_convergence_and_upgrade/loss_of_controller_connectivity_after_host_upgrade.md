---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/upgrade-the-management-domain-to-vmware-cloud-foundation-5-2/upgrading-nsx--to-version-9/manual-upgrade-to-nsx-9-by-using-upgrade-coordinator/troubleshooting-upgrade-failures-nsxt/loss-of-controller-connectivity-after-host-upgrade.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Loss of Controller Connectivity after Host Upgrade
---

# Loss of Controller Connectivity after Host Upgrade

Controller connectivity is lost after you upgrade your hosts.

After upgrading your host, when running post checks, your Node Status shows loss of connectivity to the controller.

1. Open an SSH session to the ESX host experiencing the issue and confirm that none of the three NSX controllers are in a connected state. Run the nsxcli -c get controllers command.

   Example response:

   ```
   Controller IP    Port  SSL     Status       Is Physical Master   Session State    Controller FQDN
   192.168.60.5    1235  enabled  disconnected   true                  down          nsxmgr.corp.com
   ```

   In a working configuration, two controllers display the not used status and one controller has the connected status. If the NSX Controller shows connected, refresh the UI and confirm that the status is green. If the controller shows not connected, continue to the next step.
2. Open an SSH session to one of the NSX Manager nodes as admin and run the get certificate api thumbprint command.

   The command output is a string of alphanumeric numbers that is unique to this NSX Manager.
3. On the ESX host, push the host certificate to the Management Plane:

   ```
   ESX1> nsxcli -c push host-certificate <NSX Manager IP or FQDN> username admin thumbprint <thumbprint obtained in step #1>
   ```

   When prompted, enter the admin user password for the NSX Manager. See the NSX Command-Line Interface Reference for more information.
4. Confirm the controller status is connected. 

   ```
   ESX1> nsxcli -c get controllers
   ```

   Confirm the controller connection state is green on the UI for this Transport Node.

   If this issue continues, restart the following NSX services on the ESX host:

   ```
   ESX1> /etc/init.d/nsx-opsagent restart
   ```

   ```
   ESX1> /etc/init.d/nsx-proxy restart
   ```