---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/nsx-manager.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > NSX Manager
---

# NSX Manager

The NSX Manager provides a web-based user interface where you can manage your NSX environment. It also hosts the API server that processes API calls.

If you modify Edge nodes, Edge clusters, or transport zones, it can take up to 5 minutes for those changes to become visible in the NSX Manager interface. To synchronize changes immediately, use POST /policy/api/v1/infra/sites/default/enforcement-points/default?action=reload.

Beginning with VCF 9.0, the NSX Manager interface provides a single mode, Policy mode, for configuring resources. The Manager mode and Manager API provided by NSX 4.x and earlier are no longer supported.

## Policy API

The NSX Manager provides a Policy API to automate management activities. The Policy API is part of the NSX REST APIs and contains URIs that begin with /policy/api.

Policy API methods support partial patching of objects. This feature needs to be explicitly enabled. If enabled, you can provide the partial payload for updating the existing object using PATCH methods.

To enable the feature, use the Partial Patch Config method.

PATCH /policy/api/v1/system-config/nsx-partial-patch-config

```
{ "enable_partial_patch": "true" }
```

The default is 'false'.

For more information about using the Policy API, see the [NSX API Guide](https://developer.broadcom.com/xapis/nsx-t-data-center-rest-api/latest/).

## Security

NSX Manager has the following security features:

- NSX Manager has a built-in user account called admin, which has access rights to all resources, but does not have rights to the operating system to install software. NSX upgrade files are the only files allowed for installation.
- NSX Manager supports session timeout and automatic user logout. NSX Manager does not support session lock. Initiating a session lock can be a function of the workstation operating system being used to access NSX Manager. Upon session termination or user logout, users are redirected to the login page.
- Authentication mechanisms implemented on NSX follow security best practices and are resistant to replay attacks. The secure practices are deployed systematically. For example, sessions IDs and tokens on NSX Manager for each session are unique and expire after the user logs out or after a period of inactivity. Also, every session has a time record and the session communications are encrypted to prevent session hijacking.

You can view and change the session timeout value with the following CLI commands:

- The command get service http displays a list of values including session timeout.
- To change the session timeout value, run the following commands:

  ```
  set service http session-timeout <timeout-value-in-seconds>
  restart service ui-service
  ```