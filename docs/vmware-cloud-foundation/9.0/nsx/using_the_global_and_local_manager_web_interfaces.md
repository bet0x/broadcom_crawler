---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/using-the-gm-and-lm-ui.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Using the Global and Local Manager Web Interfaces
---

# Using the Global and Local Manager Web Interfaces

You can use the Global Manager to create
objects that are limited to one location, or span multiple locations. You can also monitor
communication details between Local Manager and Global Manager using the Location
Manager.

## Location Drop-Down Menu on Global Manager

When you log into the active Global Manager web interface, you see a Location drop-down menu in the
top navigation bar. Using this menu, you can switch between the active Global Manager and any associated Local Managers.
You can also select System > Location Manager to view
communication activity.

![Shows Global Manager drop-down menu displaying Local Manager clusters.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/0db338ee-d824-41eb-935e-831b6a44c115.original.png)

## Local and Global Objects

Objects created on a Local Manager are
local objects. Objects created from the Global Manager are global objects, though their span might not include
all available locations. You can import objects to the Global Manager using the
Location Manager.

On a Local Manager, you can see local objects, and any global objects that apply to
that location. The global objects have the following Global icon next to them:
![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/017cd101-66ae-4aa7-b868-9c8b7023c44f.original.gif).

This screenshot from the Local Manager web interface shows two segments.
The segment that has the Global icon next to it indicates that it was created on the
Global Manager. The segment that has no Global icon indicates that it was created on
the Local Manager.

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/df975e62-94b5-4af9-ad03-c47a4036e30e.original.png)

Because all objects on the Global Manager are global, there is no icon displayed when you are
logged into the active Global Manager.

## Status of Local and Global Objects

Local Managers display the status of both global and local objects. The active
Global Manager displays any objects imported from the
Local Managers. For details on importing objects from Local to Global Managers using
Location Manager, see [Monitoring NSX Federation Locations](/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/using-the-gm-and-lm-ui/monitoring-nsx-federation-locations.html#GUID-89b5803a-0ec9-4324-9867-7ffef1e8c6a0-en).

To retrieve the latest status from the
Local Managers, click Check Status for the object. To refresh
the status, click the Refresh icon.

![Displays the list of object status including the curved arrow Refresh icon.](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/bb9e9462-73a2-4d67-af56-6086b8a5e807.original.png)