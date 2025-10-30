---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new.html
product: vmware-cloud-foundation
version: 9.0
section: Release Notes
breadcrumb: Release Notes > What's New
---

# What's New

Following are the key features and capabilities of VMware Cloud Foundation 9.0:

**One Interface to Private Cloud Operations**

VMware Cloud Foundation 9.0 offers a streamlined experience for building, operating, and securing private cloud - all from a single interface. **VCF Operations** provides a new Operate Experience, and along with the new build experiences provided by the **VCF Installer** you have quick deployment with integrated governance  to get you up and running faster, reducing setup time and complexity while ensuring compliance and operational efficiency from day one through cost management and policy enforcement.

Read More in the [VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html) What's New section.

**One Interface For A Cloud Consumption Experience**

VMware Cloud Foundation 9.0 offers a frictionless, cloud-like experience for teams consuming infrastructure—delivered through a single, unified interface. **VCF Automation** enables IT teams and Cloud Service Providers to deliver a self-service private cloud for application teams. The self-service private cloud comes built-in with a rich set of cloud services to provision VMs, Kubernetes, Networking, Volumes, Secret Store, Databases, Harbor Container Registries, External DNS, Certificates and AI workloads.

Read More in the [VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html) What’s New section.

**Run Containers, VMs and Traditional Apps Natively**

With VMware Cloud Foundation 9.0, you get a unified platform to run containers, VMs, and enterprise applications natively.

Kubernetes and virtualization are integrated out of the box, eliminating the need to assemble separate stacks. This seamless integration allows developers and IT teams to start building and running workloads right away, streamlining their workflow and enhancing productivity.

Read more in [Building Cloud Applications](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure.html).

**Sovereign, Secure and Compliant as A Platform**

VMware Cloud Foundation 9.0 is designed to meet the highest standards of data control, compliance, and resilience, ensuring organizations can operate with confidence in an era of increasing regulatory scrutiny and geopolitical uncertainty. VCF 9.0 provides data sovereignty without trade-Offs allowing you to maintain complete control over where and how data is stored, processed, and accessed while maintaining the agility of cloud operations.

Read more in [Security and Compliance](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=security_compliance_main&appid=vcf-9-0&language=&format=rendered).

**Private Cloud Cost Transparency**

VMware Cloud Foundation 9.0 brings financial clarity to private cloud, ensuring organizations can scale without runaway costs or hidden inefficiencies. VCF provides deep cost visibility allowing you to gain comprehensive financial clarity with out-of-the-box insights that go beyond infrastructure, factoring in software licensing, operational expenses, and even physical data center costs to provide a true total cost of ownership (TCO) view

Read more in [Cost and Capacity Management](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=capacity_management_main&appid=vcf-9-0&language=&format=rendered).

**Accessibility**

In VCF 9.0, all product components are updated with the NIST recommended standard for cryptographic modules, FIPS 140-2 and 140-3. VCF components such as vCenter, ESX, and NSX run in FIPS-enabled mode by default and this mode cannot be deactivated. For more information, see [FIPS Configuration for VCF Components](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcf_510&appid=vcf-9-0&language=&format=rendered).

**Licensing**

You now manage your licenses through VCF Operations across your entire fleet and can manage licenses for multiple VCF Operations instances from the VCF Business Services console ([vcf.broadcom.com](http://vcf.broadcom.com/)), a part of the Broadcom Support Portal.

1. Manage licenses and assign them to vCenter instances from VCF Operations. All hosts and components connected to a vCenter instance with an assigned license are automatically licensed from vCenter assignments.
2. VCF Operations can be connected to the VCF Business Services console for faster licensing, updates, and automated reporting. VCF Operations can also operate in disconnected mode.
3. Fewer licenses to manage.

   1. Now, instead of 11 license keys, there are only two licenses for VCF - "VMware Cloud Foundation (cores)" and "VMware vSAN (TiBs)". vSphere Foundation follows this same pattern.
   2. Multiple subscriptions pool together into a single license that can optionally be split later.
   3. All licenses can be applied into your environment by importing a single license file. For connected VCF Operations instances, the first license file will download automatically after you complete the registration.
   4. License your vCenter, ESX hosts, NSX , VCF Operations HCX, VCF Automation, and other components by assigning the license to the vCenter instance.
4. License usage must be submitted from VCF Operations every 180 days, or hosts will disconnect from the vCenter instance and new workloads cannot be started (existing workloads will not be proactively stopped). If VCF Operations is in connected mode, license usage submission is automatic but still must be confirmed in VCF Operations by clicking Update Licenses. For VCF Operations in disconnected mode, follow the steps in the documentation to submit license usage.
5. Hosts are automatically reconnected to the respective vCenter instance with full capabilities when a valid license is applied and/or license usage is submitted and license refreshed.
6. Dynamic license quantity adjustment means that license changes made in the VCF Business Services console do not require reassignment.
7. Visualize a unified view of your usage over time for your fleet in VCF Operations and across multiple VCF Operations instances in the VCF Business Services console.
8. Evaluation Mode has been extended to 90 days.
9. The license usage file only records the following license usage data points: the usage generation timestamp, utilization details for both post-version 9 and pre-version 9 licenses, the unique VCF Operations instance ID, a unique identifier for the usage report, a list of post-version 9 licenses added to VCF Operations but currently unused, any detected usage anomalies, and the active status. Note that the license usage file exclusively gathers this specific information and, for clarity, does not collect personal data and customer data.

Read more in [Licensing Overview](https://techdocs.broadcom.com/bin/gethidpage?ux-context-string=vcom_839&appid=vcf-9-0&language=&format=rendered).

**What’s New in VCF 9.0 by Component**

See more information on What’s New in VCF 9.0 listed within each component:

- [vSphere](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsphere.html)
- [vSAN](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vsan.html)
- [NSX](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-nsx.html)
- [VCF Installer](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-installer.html)
- [VCF Operations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-ops.html)
- [VCF Automation](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-automation.html)
- [VCF SDKs, APIs, and CLIs](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/release-notes/vmware-cloud-foundation-90-release-notes/platform-whats-new/whats-new-vcf-cli-api-sdk.html)