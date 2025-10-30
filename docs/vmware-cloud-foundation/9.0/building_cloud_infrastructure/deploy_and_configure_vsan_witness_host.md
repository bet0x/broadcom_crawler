---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/stretching-clusters/deploy-vsan-witness-host.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Deploy and Configure vSAN Witness Host
---

# Deploy and Configure vSAN Witness Host

vSAN HCI and vSAN storage stretched clusters require a witness host deployed in a vSAN witness zone, which must be different from the location of both availability zones. vSAN compute stretched cluster do not require a witness host.

You deploy the vSAN witness host using an appliance instead of using a dedicated physical ESX host as a witness host. The witness host does not run virtual machines and must run the same version of ESX as the ESX hosts in the stretched cluster. It must also meet latency and Round Trip Time (RTT) requirements.

There are separate vSAN witness appliances for vSAN OSA and vSAN ESA. You must deploy the witness appliance that matches the cluster type that you are stretching.

| Cluster Type | vSAN Witness Appliance |
| --- | --- |
| vSAN ESA | vSAN ESA appliance |
| vSAN OSA | vSAN OSA appliance |
| vSAN storage | vSAN ESA appliance |
| vSAN compute | n/a |