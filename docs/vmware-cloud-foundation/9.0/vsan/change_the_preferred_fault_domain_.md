---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/vsan-deployment-administration-and-monitoring/vsan-planning-and-deployment/working-with-virtual-san-stretched-cluster/mark-fault-domain-as-preferred-site.html
product: vmware-cloud-foundation
version: 9.0
section: vSAN
breadcrumb: vSAN > Change the Preferred Fault Domain 
---

# Change the Preferred Fault Domain

You can configure the Secondary site as the Preferred site. The current Preferred site becomes the Secondary site.

Objects with Data locality=Preferred policy setting always move to the Preferred fault domain. Objects with Data locality=Secondary always move to the Secondary fault domain. If you change the Preferred domain to Secondary, and the Secondary domain to Preferred, these objects move from one site to the other. This action might cause an increase in resynchronization activity. To avoid unnecessary resynchronization, you can change the Data locality setting to None before you swap the Preferred and Secondary domains. Once you swap the domains back, you can reset the Data locality.

1. Navigate to the vSAN cluster.
2. Click the Configure tab.
3. Under vSAN, click Fault Domains.
4. Select the secondary fault domain and click the Change Preferred Fault Domain icon.
5. Click Yes or Apply to confirm. 

   The selected fault domain is marked as the preferred fault domain.