---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/nsx-tags.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >   NSX Tags
---

# NSX Tags

Tags help you to label NSX objects so
that you can quickly search or filter objects, troubleshoot and trace, and do other related
tasks.

You can create tags using both the UI and APIs. Each tag has the following two
attributes:

- Tag (refers to the tag name. It is
  required, must be unique and case-sensitive.)
- Scope (optional)

Tag scope is analogous to a key and tag name is analogous to a value. For example,
let us say, you want to label all virtual machines based on their operating system
(Windows, Mac, Linux). You can create three tags, such as Windows, Linux, and Mac, and
set the scope of each tag to OS. Other examples of tag scope can be tenant, owner, name,
and so on.

After you save a tag, you cannot update the
name and scope. However, you can unassign or remove tags from objects.

For information about the maximum number of
tags supported in NSX objects, see the
VMware Configuration Maximums tool at <https://configmax.vmware.com/home>.

Following are some of the operations that you can do with tags:

- Assign or unassign tags to an object.
- Assign or unassign a single tag to multiple objects simultaneously (supported
  only for VMs).
- View a list of all tags in the
  inventory.
- Filter the list of tags by tag name, tag source, and tag scope.
- View a list of objects that are assigned a specific tag.

When
a VM disappears from the vCenter inventory for more than 30 minutes, tags on the VM are lost. If
the same VM reappears in the vCenter inventory after 30 minutes, NSX treats it as a new VM, and you must add the tags again on the VM.
This behavior is expected and as per design. For example, this behavior is seen when
using array-based replication with VMware Live Site Recovery™.

## Use Cases of Tags

The following table describes some use cases of using tags.

| Use Case | Description |
| --- | --- |
| Manageability | - Simplify searching of objects in a large-scale inventory   management. - Provide more information to differentiate objects that share   similar or unclear names. |
| Third-party sharing and context sharing | - Annotate objects with custom information. - Allow third-party non-NSX systems to add metadata information in   an automated fashion. For example, metadata from partners,   container platforms, and so   on. - Capture attributes or properties and relationships that are   learned using NSX   discovery agent, inventory collection,   Guest Introspection, VM Tools, and so   on. |
| Security | - Create grouping membership criteria. - Specify the firewall source and destination. |
| Troubleshooting (Traceability) | - Trace a firewall rule into the logs (Rule tags) - Trace and correlate objects back to an OpenStack network. |

## System Tags

System tags are tags that are system-defined, and you cannot add, edit, or delete
them.

System Tags in Other
NSX Objects



| Objects | System Tags |
| --- | --- |
| Group | - autoPlumbing - abstractionPath - NLB-VIP\_ID - NLB-Lb-ID - NLB-Pool\_ID |
| Segment | - subnet-cidr |
| IP Address Pool  IP Address Block | - abstractionPath |

## Discovered Tags

NSX can discover and synchronize tags from the following:

- Amazon Web Services
- Microsoft Azure
- Kubernetes container clusters with
  NSX Container Plugin
  (NCP)
- Kubernetes container clusters with
  Antrea network plug-in
- OpenShift container clusters with
  NCP

Discovered tags are displayed for
workload VMs and container cluster objects. You cannot edit discovered tags in the
NSX UI.

For example:

- Tags that are added to
  container cluster objects in the Kubernetes container clusters with NCP CNI
  or Antrea CNI, and OpenShift
  container clusters with NCP CNI.

| Tag Prefix | Meaning |
| --- | --- |
| dis:aws | Tags discovered from Amazon Web Services (AWS). |
| dis:azure | Tags discovered from Microsoft Azure. |
| dis:k8s | Tags discovered from Kubernetes container clusters with NCP CNI, Antrea CNI, and OpenShift container clusters with NCP CNI. |

You can enable or disable the discovery
of AWS tags at the time of adding the AWS account. Similarly, you can enable or
disable Microsoft Azure tags at the time of adding the Microsoft Azure
subscription.