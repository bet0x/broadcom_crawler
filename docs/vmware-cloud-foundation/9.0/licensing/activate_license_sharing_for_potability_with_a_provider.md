---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/licensing/license-sharing/license-sharing(1)/share-a-licenses-with-a-cloud-services-provider.html
product: vmware-cloud-foundation
version: 9.0
section: Licensing
breadcrumb: Licensing > Activate License Sharing for Potability with a Provider
---

# Activate License Sharing for Potability with a Provider

End customers can activate the sharing of a license for portability with a provider. The provider can then validate the license.

- Verify that the license type is Split.
- Verify that the license is eligible for sharing.
- Verify that the license is not added to a VCF Operations instance.

After sharing for portability for a license is activated, the customer shares the license ID and site ID manually with the provider. Through Broadcom APIs, the provider validates the shared licenses for legitimacy and ownership by the end customer.

1. Log in to the VCF Business Services console (vcf.broadcom.com).
2. Under License Management, navigate to the Version 9+ tab.
3. Click the vertical ellipsis next to the license.
4. Select Manage Sharing for Portability.
5. Activate the Activate Sharing for Portability toggle button.
6. Copy and send the License ID and Site ID to a provider.

After the cloud services provider or a hyperscaler completes validating the license, you can add the license to a VCF Operations instance deployed by the provider.