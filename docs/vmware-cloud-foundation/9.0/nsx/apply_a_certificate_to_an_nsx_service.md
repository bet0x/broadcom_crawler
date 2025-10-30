---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/certificates/apply-certificate-to-a-service.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Apply a Certificate to an NSX Service
---

# Apply a Certificate to an NSX Service

After you add a certificate to NSX, you can associate it with a service by using the Apply Certificate option.

When you associate a certificate to a service for the first time, all services in the system are available for selection. The first service applied to a certificate sets the category of that certificate. From now on, only services from the same category of the certificate will be available for selection when you use the Apply Certificate option.

You can use the Apply Certificate option when you have a unique CA-signed certificate and you want to apply such an individual certificate to the VIP and the individual API services rather than using a single consolidated certificate. Once you have applied an individual certificate to a service, you can always use the Replace Certificate option to replace that certificate when it expires.

1. Log in to NSX Manager with admin privilege.
2. Navigate to SystemCertificates.

   You see a list of all the certificates including, total certificates, certificates that are about to expire, and the certificates that are currently in use. All the certificates are arranged in different groups. You can also filter the certificates as per your requirements.
3. Select the required certificate from the list.
4. From the more option, click Apply Certificate.
5. In the Apply Certificate dialog box, select the required service/entity to apply to the certificate.
6. If a service needs to be applied to a node, the Apply Certificate dialog box displays a Node drop-down. Select the required node to apply the service/entity.
7. Click Save.