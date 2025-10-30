---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/creating-a-virtual-san-cluster/using-virtual-san-with-vcenter-server-appliance.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Deploying vSAN with vCenter
---

# Deploying vSAN with vCenter

With vSphere Foundation 9.0, you can use an installer to deploy a vCenter instance and host the vCenter on that cluster.

When you use the vCenter installer, ensure that you do not select Install on a new vSAN cluster option. Follow the steps in the installer wizard to complete the deployment. You can activate vSAN from the vSphere Client after deploying vCenter. For more information on vSAN bootstrap not working with the installer, see Broadcom knowledge base article [389238](https://knowledge.broadcom.com/external/article?articleNumber=389238).