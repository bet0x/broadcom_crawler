---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/upgrading-cloud-foundation/preparing-your-vcf-9-management-components/preparing-to-upgrade-to-vmware-cloud-foundation/deploy-vcf-operations.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Deploy VCF Operations Nodes
---

# Deploy VCF Operations Nodes

Use the vSphere Client to deploy the VCF Operations primary, replica, and data nodes.

If you plan to use a custom authentication certificate, verify that you have imported your certificate into VCF Operations. See [Importing CA Certificates](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0/managing-certificates-in-vmware-vsphere-foundation/certificates/importing-ca-certificates.html). For more information about certificates in VCF Operations fleet management, see [Managing Certificates in VMware Cloud Foundation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/certificate-management-9-0.html).

Perform the following steps to deploy VCF Operations.

1. Download the VCF Operations 9.0 Install OVA files from the [Broadcom Support Portal](https://support.broadcom.com).
   1. Log in to the [Broadcom Support Portal](https://support.broadcom.com).
   2. Browse to My Downloads.
   3. Search for VMware Cloud Foundation and select VMware Cloud Foundation 9.0.
   4. Accept the terms and conditions.
   5. Select VCF Operations and download the VCF Operations Install OVA files.
2. Log in to vCenter using the vSphere Client.
3. Start the Deploy OVF Template wizard.

   On the “Select an OVF template”, specify the local location of the source VCF Operations Install OVA template and follow the prompts until you are asked to enter a name for the node.
4. Deploy nodes for VCF Operations.
5. Provide input to deploy each node.

   For Node Name, do not include nonstandard characters such as underscores (\_) in node names. If creating a multi-node cluster, use a unique name for each node.

   1. Select the size configuration. Your selection does not affect the disk size.
   2. Select the disk format:

      - Thin Provisioned
      - Thick Provisioned Lazy Zeroed
      - Thick Provisioned Eager Zeroed
   3. From the drop-down menu, select a Destination Network.
   4. Specify networking properties.

      For static IPv4 or static IPv6, specify the associated Domain Name, Domain Search Path, and Domain Name Servers values.
   5. Specify a time zone.

      You must configure all nodes with the same time zone.
   6. (optional) Specify a FIPS setting and click Next.

      To deploy a FIPS activated VCF Operations setup, check Activate FIPS Mode
   7. Review the settings and click Finish.

      After deployment, note the node FQDN or IP address.

   To create a multi-node cluster, repeat the steps to deploy each node.
6. Power on the VCF Operations appliance and wait until it bootstraps completely.
7. Create and add a primary node in VCF Operations.
8. Navigate to the name or IP address of the primary node.
   1. Click New InstallationNext.
   2. Enter and confirm a password for the admin user and click Next.

      - The admin user account name cannot be changed.
      - Passwords require a minimum of fifteen characters, one uppercase letter, one lowercase letter, one digit, and one special character.
   3. Use the certificate included with VCF Operations or to install one of your own.

      - To use the included certificate, click Use the default certificates and review the certificate information. If it meets the requirements for VCF Operations, click Next.
      - To install your own certificate, click Install a certificate.

        1. Click Browse to locate the certificate file.
        2. Click Open to load the file in the Certificate text box.
        3. Click Next
   4. Enter a name for the primary node such as ops-primary.
   5. For NTP server cluster synchronization:

      - To have VCF Operations manage its own synchronization, leave the shared IP address blank. All nodes will synchronize with the primary and replica node.
      - Or enter a URL or IP address such as nist.time.gov, and click Add.
   6. Configure VCF Operations availability.

      To install VCF Operations with availability, activate the Availability Mode and select High Availability or Continuous Availability. To continue your installation on full capacity, click Next.
   7. To add a node, click the plus sign, specify the following information:

      1. Enter the Node Name and Node Address.
      2. Select the Current Cluster Role.
      3. Click Next
   8. Click Finish.

      The administration interface appears. It takes a moment for VCF Operations to finish adding the primary node.

   After creating the primary node, you can create and add data nodes before starting the cluster or you can start a single-node cluster.
9. To start the cluster, click Start VCF Operations.

   Depending on the size of the cluster and nodes, deployment might take 10 to 30 minutes to start. Do not make any changes or perform any actions on cluster nodes while the cluster is starting.

VCF Operations 9.0 is deployed in evaluation mode. Before adding other components, assign the VCF entitlement type. See [Registering VCF Operations with VCF Business Services Console](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/register-vcf-operations.html).