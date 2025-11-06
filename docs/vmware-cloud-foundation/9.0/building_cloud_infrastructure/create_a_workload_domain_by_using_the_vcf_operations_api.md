---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/building-your-private-cloud-infrastructure/working-with-workload-domains/create-a-workload-domain-by-using-the-vcf-operations-api.html
product: vmware-cloud-foundation
version: 9.0
section: Building Cloud Infrastructure
breadcrumb: Building Cloud Infrastructure > Create a Workload Domain by Using the VCF Operations API
---

# Create a Workload Domain by Using the VCF Operations API

A workload domain adds a logical pool of compute, network, and storage infrastructure to a VCF instance. You use the VCF Operations API to customize the deployment specification by using a JSON file.

For example, the deployment wizard assumes that your ESX hosts share the same root password. If your ESX hosts have different root passwords, use the JSON specification file to deploy your environment.

In addition, if you are deploying multiple workload domains, you may find it easier to start with an existing JSON specification file and modify it for additional deployments.

The API provides additional options which are not yet available in the UI. Certain workload domain configurations, such as LACP networking or layer 3 multi-rack vSAN HCI cluster, must be deployed through the API.