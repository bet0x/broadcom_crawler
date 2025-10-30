---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-monitoring-and-troubleshooting/handling-failures-and-troubleshooting-virtual-san/non-compliant-virtual-machine-objects-do-not-become-compliant-instantly.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Not Compliant Virtual Machine Objects Do Not Become Compliant Instantly
---

# Not Compliant Virtual Machine Objects Do Not Become Compliant Instantly

When you use the Check Compliance button, a virtual machine object does not change its status from Not Compliant to Compliant even though vSAN resources have become available and satisfy the virtual machine profile.

When you use force provisioning, you can provision a virtual machine object even when the policy specified in the virtual machine profile cannot be satisfied with the resources available in the vSAN cluster. The object is created, but remains in the non-compliant status.

vSAN is expected to bring the object into compliance when storage resources in the cluster become available, for example, when you add an ESX host. However, the object's status does not change to compliant immediately after you add resources.

This occurs because vSAN regulates the pace of the reconfiguration to avoid overloading the system. The amount of time it takes for compliance to be achieved depends on the number of objects in the cluster, the I/O load on the cluster and the size of the object in question. In most cases, compliance is achieved within a reasonable time.