---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/preparing-to-upgrade-to-vmware-cloud-foundation/install-the-vcf-operations-fleet-management-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploy the VCF Operations fleet management Appliance
---

# Deploy the VCF Operations fleet management Appliance

Use vCenter to deploy the VCF Operations fleet management appliance.

Perform the following steps to deploy the VCF Operations fleet management appliance.

1. Download the VCF Operations fleet management OVA from the [Broadcom Support Portal](https://support.broadcom.com).
   1. Log in to the [Broadcom Support Portal](https://support.broadcom.com).
   2. Browse to My Downloads.
   3. Search for VMware Cloud Foundation and select VMware Cloud Foundation 9.0.
   4. Accept the terms and conditions.
   5. Select VCF Operations and download the VCF Operations fleet management appliance OVA.
2. Log in to vCenter using the vSphere Client.
3. Start the Deploy OVF Template wizard.

   On the “Select an OVF template”, specify the local location of the source VCF Operations fleet management OVA template.
4. Configure the fleet management appliance.
5. Follow prompts until you are asked to enter a name for the node. 
   1. For Compute Resource

      Provide the storage or datastore where the appliance will be deployed.
   2. Select and configure a network for the appliance.

      - Hostname. Do not include nonstandard characters such as underscores (\_) in node names. Always use the FQDN.
      - Initial Root Password. The password must be 15 characters or more.
      - Initial Admin Password. The password must be 15 characters or more.
      - Select Enable SSH service on the appliance.
      - Select Enable firstboot for vrlcm.
      - Select Join CEIP.
      - Host Network Default Gateway. Specify the gateway to which the appliance will connect.
      - Domain Name. Specify the Domain Name of the appliance. This is not the hostname. For example, if the hostname is opslcm.ops.com, ops.com is the domain name.
      - Domain Search Path. Typically the same as the domain name.
      - Network 1 IP address. IP address of the virtual appliance. Should resolve to the FQDN of the appliance.
      - Network 1 IP NetMask. Netmask of the virtual appliance.
   3. Review the Settings and click Finish.
6. Power on the fleet management appliance and wait until it bootstraps completely.