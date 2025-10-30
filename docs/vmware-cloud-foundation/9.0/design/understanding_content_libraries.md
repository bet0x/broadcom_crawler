---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/design/design-library/vcf-automation-deployment-models(1)/organization-consumption-model/understanding-content-libraries.html
product: vmware-cloud-foundation
version: 9.0
section: Design
breadcrumb: Design > Understanding Content Libraries
---

# Understanding Content Libraries

Content Libraries contain the templates and images used to deploy workloads. They are stored in vCenter using vCenter Content Libraries, but VCF Automation takes care of replicating the libraries across multiple regions to keep the content in sync. Content libraries can be created by the provider which are classified as *shared*, and are then available for all tenants within the region(s) selected for the library. They can also be created by the tenant which are classified as *not shared*, and only accessible to the tenant that created them. Tenants can only upload items to non-shared libraries that they created.

| Design Objectives | Design Decisions |
| --- | --- |
| Define a collection of templates and objects (such as ISO images, OVA/OVF templates, vm disk files) which are replicated to all the regions where workloads are being deployed, so that end users can attach them to vSphere Namespaces where they are used to deploy workloads from the images stored in the Content Library. | There are 2 primary types of Content Library:   1. Provider-managed Content Libraries, where the Provider can define and share images or files with multiple Tenants. Tenants cannot add to or modify the images in the library. Provider-managed Content Libraries will automatically be attached to any vSphere Namespaces in the region(s) the Content Library is configured for. 2. Tenant-managed Content Libraries, which are created by the Tenant to upload their own images and files. Tenants have the option of manually assigning Content Libraries to vSphere Namespace Classes, or having them auto-attached to all vSphere Namespaces in the region(s) the Content Library is configured for. This setting cannot be modified once the Content Library has been created. When using the manual assignment method via vSphere Namespace Classes, only vSphere Namespaces created after the Content Library has been assigned in the vSphere Namespace Class will have access to it.   Content Libraries must be assigned to one or more Regions. When multiple regions are selected, the content libraries will be replicated with local copies stored in each region.  In most cases, a combination of a Provider Content Library and Tenant Content Library will be required. |