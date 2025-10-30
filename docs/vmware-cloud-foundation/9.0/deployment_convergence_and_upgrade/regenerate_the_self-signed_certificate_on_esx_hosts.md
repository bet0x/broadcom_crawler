---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/deployment/deploying-a-new-vmware-cloud-foundation-or-vmware-vsphere-foundation-private-cloud-/preparing-your-environment/preparing-esx-hosts-for-vmware-cloud-foundation-or-vmware-vsphere-foundation/regenerate-the-self-signed-certificate-on-esx-hosts.html
product: vmware-cloud-foundation
version: 9.0
section: Deployment, Convergence, and Upgrade
breadcrumb: Deployment, Convergence, and Upgrade > Regenerate the Self-Signed Certificate on ESX Hosts
---

# Regenerate the Self-Signed Certificate on ESX Hosts

Once you have configured the ESX hosts' identity by providing a hostname, you must regenerate the self-signed certificate to ensure the correct common name is defined in the certificate.

During the installation of ESX, the installer generates a self-signed certificate for each ESX host, but the process is performed prior to the ESX hostname being configured. This means all ESX hosts have a common name in their self-signed certificate of  localhost.localdomain. All communication between the VCF Installer and the ESX hosts is performed securely over HTTPS and as a result it validates the identity when making a connection by comparing the common name of the certificate against the FQDN provided within the VCF Installer deployment wizard.

To ensure that the connection attempts and validation do not fail, you must manually regenerate the self-signed certificate after the hostname has been configured.

If corporate policy requires that you use external CA-signed certificates instead of VMCA-signed certificates for ESX hosts, you can add external certificates to the hosts using the [SDDC Manager API](https://developer.broadcom.com/xapis/sddc-manager-api/latest/).

1. In a web browser, log in to the ESX host using the VMware Host Client.
2. In the Actions menu, click ServicesEnable Secure Shell (SSH).
3. Log in to the ESX host using an SSH client such as Putty.
4. Regenerate the self-signed certificate by executing the following command:

   ```
   /sbin/generate-certificates
   ```
5. Reboot the ESX host.
6. Log back in to the VMware Host Client and click ServicesDisable Secure Shell (SSH) from the Actions menu.
7. Repeat this procedure for all remaining hosts.