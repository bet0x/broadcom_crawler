---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/fleet-management/scaling-up-and-scaling-out-management-nodes-in-vcf/vertical-scale-up-for-automation.html
product: vmware-cloud-foundation
version: 9.0
section: Fleet Management
breadcrumb: Fleet Management > Scale VCF Automation
---

# Scale VCF Automation

You use the fleet management appliance to scale a VCF Automation deployment. In addition to increasing the size of the environment from small to medium or medium to large, scale offers options to increase CPU and memory, and to add nodes.

1. Under Fleet ManagementLifecycleComponents, select automation for the integrated component.
2. Click the ellipses (...) and select Scale.
3. On Select Size, choose a larger target deployment type such as Medium or Large.
4. On Configure IP addresses, add the following information and click Next.

   - For Additional VIPs: Click Add IPs to your VIP pool. You can add up to two more IPs.
   - For Cluster Node IP Pool: Click to add IPs to the Cluster Node Pool. The deployed nodes host the VCF Automation containers.

     - A small deployment requires a minimum of two IPs.
     - A medium deployment requires a minimum of four IPs.
     - A large deployment requires a minimum of four IPs.
5. Click RUN PRECHECK.

   If the data validation is not successful, perform the recommended actions and run the precheck again.
6. After a successful precheck run, review the summary of your VCF Automation scale out request and click Submit.