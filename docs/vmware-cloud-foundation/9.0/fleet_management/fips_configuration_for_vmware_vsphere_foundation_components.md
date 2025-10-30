---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/fips-compliance-for-vcf-components/enable-fips-admin-ui.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > FIPS Configuration for VMware vSphere Foundation Components
---

# FIPS Configuration for VMware vSphere Foundation Components

You can activate Federal Information Processing Standards (FIPS) for the VCF Operations component of VMware vSphere Foundation to make your environment FIPS compliant. You can also activate firewall hardening.

## Activate FIPS

You can activate FIPS in the VCF Operations cluster at the time of installation or after VCF Operations is up and running. Adding FIPS at installation is less intrusive because the cluster has not yet started.

If the cluster is running, to activate FIPS, you must take the cluster offline.

FIPS mode is supported in Cloud Proxy. You can continue using your cloud proxy after enabling FIPS for the VCF Operations cluster.

1. In a Web browser, navigate to the master node administration interface. https://master-node-name-or-ip-address/admin.
2. Enter the VCF Operations administrator username of admin.
3. Enter the VCF Operations administrator password and click Log In.
4. Click Administrator Settings.

   The Activate FIPS button is deactivated when the cluster is running.
5. Click Activate FIPS after you take your cluster offline.

   After you activate FIPS, you cannot deactivate the FIPS mode in the current setup. To revert to a FIPS deactivated setup, you must re-deploy VCF Operations.
6. In the Are you sure you want to activate FIPS dialog box, read the note and provide your consent for enabling FIPS and then click Yes.

   After you activate FIPS, the cluster restarts and is not be available during this time. The cluster nodes are rebooted and after the cluster is online, all the nodes are FIPS activated.

## Activate Firewall Hardening

Activating firewall hardening restricts network access to internal services in VCF Operations.

1. In a Web browser, navigate to the master node administration interface. https://master-node-name-or-ip-address/admin.
2. Enter the VCF Operations administrator username of admin.
3. Enter the VCF Operations administrator password and click Log In.
4. Click Administrator Settings, and then click Security Settings from the Administrator Settings page.
5. Click Activate Firewall Hardening.