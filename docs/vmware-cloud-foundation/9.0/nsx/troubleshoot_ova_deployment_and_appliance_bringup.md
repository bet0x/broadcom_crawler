---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/troubleshooting-installation-issues/troubleshoot-ova-deployment-and-appliance-bringup.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Troubleshoot OVA Deployment and Appliance Bringup
---

# Troubleshoot OVA Deployment and Appliance Bringup

## Troubleshooting OVA Failures

During deployment, if you entered incorrect configuration details, delete the appliance and redeploy with correct configuration.

- Verify that the datastore chosen for deployment is mounted on all the hosts that are members of a cluster. Redeploy and choose ESX host instead of vCenter to bypass vCenter cluster related checks.
- If proxy enabled on vCenter, edit file /etc/sysconfig/proxy and add line .\*.domainname to bypass proxy for ESX hosts. See Knowledge Base article 321922: [Unable to deploy OVF using vSphere Client in vCenter when an HTTPS Proxy is configured](https://knowledge.broadcom.com/external/article?articleNumber=321922).
- If the deployment of the appliance through the OVF tool results in the error ovf descriptor not found, view the file contents in terminal cat -A <filepath/filename> and remove hidden formatting characters. Then try again.

## Troubleshooting Issues Related to Bringing Up the Appliance

SSH to NSX Manager CLI as admin and run following commands to troubleshoot.

- Run get configuration and verify hostname/name-server/search-domain/ntp settings are correct.
- Run get services and verify all required services are running (other than nsx-message-bus, snmp, migration-coordinator). If these services are not running, try restarting the service by running restart service <service-name>.
- Run get cluster status and verify all manager cluster components are up. If any component is down, try restarting the service associated to the component by running restart service <associated-component-service-name>.
- Run get core-dumps to verify no core dumps generated in /var/log/core or /image/core. If you find any core dumps, contact VMware Support.
- Run get filesystem-stats to verify that no disk partition is full, especially those partitions that are consumed by NSX.
- Alternatively, you can run API commands to know the node and service status.

  GET api/v1/node/status

  GET api/v1/node/services