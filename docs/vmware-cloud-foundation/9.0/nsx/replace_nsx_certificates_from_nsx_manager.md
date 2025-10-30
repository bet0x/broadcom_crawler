---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/replacing-certificates/replace-certificates-through-nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Replace NSX Certificates from NSX Manager
---

# Replace NSX Certificates from NSX Manager

You can replace self-signed or CA-signed appliance certificates from the NSX Manager. You can only replace certificates that have private key and are valid. You cannot replace a certificate that belongs to a service-certificate category.

You can replace the self-signed certificates for the following service types:

- MGMT\_CLUSTER (aka VIP)
- CBM\_CLUSTER\_MANAGER
- K8S\_MSG\_CLIENT
- CBM\_CORFU
- CCP
- APH\_TN
- LOCAL\_MANAGER
- GLOBAL\_MANAGER
- APH (aka APH\_AR)
- API
- WEB\_PROXY

Note that starting from NSX 4.2, some certificates have been consolidated. When you replace such a certificate, ensure that the replacing certificate must either have a wild-card SAN entry that matches all the nodes in the cluster and the VIP or it must have as many SAN entries that match the VIP and the individual node addresses.

Going forward, use '[Apply Certificate](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/apply-certificate-to-a-service.html#GUID-946551a7-12cb-4d2f-9e78-dac25051f01e-en_GUID-13838CE4-95A7-4DA2-8BC6-A57A6478474F)' when you want to assign individual certificates to services that have been consolidated previously so that they become individual certificates again or to consolidate certificates that have been previously separated. After the de-consolidation of a certificate, use 'Replace Certificate' to renew it or replace it when it has expired.

1. With admin privileges, log in to NSX Manager.
2. Navigate to SystemCertificates.

   You see a list of all the certificates including, total certificates, certificates that are about to expire, and the certificates that are currently in use. All the certificates are arranged in different groups. You can also filter the certificates as per your requirements.
3. To replace multiple certificates, perform the following steps:
   1. Select the certificates you want to replace, and click ActionsReplace Certificates.
   2. In the Replace Certificates dialog box, for each certificate select the required option:

      - Auto-generate Self Signed Certificate: Replaces the old certificate with a auto-generated self-signed certificate. This is the default option.
      - Import Certificates: Imports signed certificates to replace the old certificate. You need to select this option from the drop-down menu.
      - Generate Self Signed Certificate: Provides an option to create a self-signed certificate to replace the old certificate. You need to select this option from the drop-down menu.
   3. Click Save.
4. To replace PI certificates, perform the following steps:
   1. Select the PI certificate that you want to replace.
   2. From the more option, click Replace Certificate.
   3. In the Replace Certificate dialog box, select the PI certificate from the drop-down menu.
   4. Click Save.