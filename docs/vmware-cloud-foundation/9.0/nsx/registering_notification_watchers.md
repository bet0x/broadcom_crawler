---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/system-monitoring/registering-notification-watchers.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Registering Notification Watchers
---

# Registering Notification Watchers

You can register a watcher that will receive notifications based on specific
criteria.

To register a watcher, you can invoke the following API.

POST /api/v1/notification-watcher

After adding a watcher, you must register a
notification\_id (feature\_name.notification\_name) with a watcher\_id and specify
notifications that the watcher should receive. Note that without the registration, the
watcher will not receive any notifications. Invoke the following APIs with the required
request parameters to register notification\_id and to specify notifications. For more
information on NSX Notification APIs, see
NSX API Guide.

- PUT
  /api/v1/notification-watchers/<watcher-id>
- POST
  /api/v1/notification-watchers/<watcher-id>/notifications?action=add\_uri\_filters
  with the following request parameters:

  - notification\_id: A
    string identifying feature\_name.notification\_name to indicate a
    notification that watcher is interested in receiving for the URI
    identified by the feature\_name.notification\_name.
  - uri\_filters: Optional
    list of URIs to filter notifications based on its policy path. When
    specifying uri\_filters, you can also use \* as a wildcard character
    instead of a specific value.

    For example, if the
    notification\_id is group.change\_name, the uri\_filter pattern is
    /policy/api/v1/infra/domains/<domain>/groups/<group>.
    You can specify the pattern as
    /policy/api/v1/infra/domains/domain1/groups/group2 to get
    notifications specific to domain1 and group2. Alternatively, you
    can also specify the pattern
    /policy/api/v1/infra/domains/domain2/groups/\* to get
    notifications for all groups in domain2 or specify it as
    /policy/api/v1/infra/domains/\*/groups/\* to get notifications for
    all groups in all domains.

The following table lists the feature names and their respective URIs.

| Feature Name | Feature Description | Notification Name | Notification Description | URI |
| --- | --- | --- | --- | --- |
| group | Notifications supported by NS Group feature. | change\_notification | Group notification, <domain> identifies the domain name and <group> identifies group name. | /policy/api/v1/infra/domains/<domain>/groups/<group> |
| monitoring | Notifications supported by the monitoring feature. | alarm | Alarm notifications. <alarm-id> identifies an alarm instance. A notification is sent whenever an alarm instance is created or deleted and when the alarm instance is updated. | /api/v1/alarms/<alarm-id> |
| alarm\_status\_change\_notification | Alarm notifications. <alarm-id> identifies an alarm instance. A notification is sent whenever an alarm instance is created and when the status property value of an alarm instance is updated. | /api/v1/alarms/<alarm-id> |
| notification | Notifications supported by notification framework. | watcher | Platform notification to convey updates to watcher configuration. <watcher-id> identifies the watcher. | /api/v1/notification-watchers/<watcher-id> |
| watcher\_notification | Platform notification to convey updates to notifications. <watcher-id> identifies the watcher. | /api/v1/notification-watchers/<watcher-id>/notifications |
| service\_config | Notifications supported by Service Config feature. | change\_notification | Service config notification. <domain> identifies the domain name, <policy> identifies the endpoint policy, and <rule> identifies the endpoint rule. This notification is generated when a service config used in endpoint rule is updated or when UPM Profile is updated. | /policy/api/v1/infra/domains/<domain>/endpoint-policies/<policy>/endpoint-rules/<rule> |
| service\_insertion | Notifications supported by Service Insertion module.  Currently Service Insertion module supports notifications for Service Profile, Service Instance Runtime, and Policy Groups. | instance\_runtime\_notification | Service Instance Runtime notification. <service-id> identifies the service, <service-instance-id> identifies the service instance. Notification will be sent for deployed and undeployed operations. | /api/v1/serviceinsertion/services/<service-id>/service-instances/<service-instance-id>/instance-runtimes |
| profile\_notification | Service Profile change notification. <service-reference> identifies the service name and <service-profile> identifies profile name. Notification will be sent for profile create, update, and delete. | /policy/api/v1/infra/service-references/<service-reference>/service-profiles/<service-profile> |
| profile\_chain\_mapping\_notification | Service Profile Chain Mapping notification. <service-reference> identifies the service name and <service-profile> identifies profile name. The notification will be sent when a profile is added or removed as a part of a service chain. | /policy/api/v1/infra/service-references/<service-reference>/service-profiles/<service-profile>/service-chain-mappings |
| profile\_nsgroups\_notification | Service Profile NSGroups notification. <service-reference> identifies the service name and <service-profile> identifies profile name. This notification gets triggered whenever an east-west rule containing nsgroups gets added or deleted with the particular profile. | /policy/api/v1/infra/service-references/<service-reference>/service-profiles/<service-profile>/group-associations |
| instance\_nsgroups\_notification | Service Instance NSGroups notification. <service-id> identifies the service name and <service-instance-id> identifies service instance. This notification gets triggered whenever a north-south rule containing nsgroups gets added or deleted with the particular instance. | /api/v1/serviceinsertion/services/<service-id>/service-instances/<service-instance-id>/group-associations |