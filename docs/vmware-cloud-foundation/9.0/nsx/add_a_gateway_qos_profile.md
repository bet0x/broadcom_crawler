---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/networking-settings/add-a-gateway-qos-profile.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Add a Gateway QoS Profile
---

# Add a Gateway QoS Profile

Create a QoS (quality of service)
profile for your tier-1 gateways to define limits on the traffic rates. You can specify the
permitted information rate and the burst size to set the limitations. Any traffic that does
not conform to the QoS policy, is dropped. QoS profiles can be set for both ingress and
egress traffic, for all traffic types (unicast, BUM, IPv4/IPv6). You can choose to create a
different profile for each tier-1 gateway.

- Gateway QoS profile is
  supported only on tier-1 gateways.
- QoS policies on tier-1 gateways
  apply only to north-south traffic and not to tier-1 gateway overlay segments
  or service interfaces.
- The tier-1 gateways must be in
  active-standby mode with an NSX Edge cluster.
- QoS profile is not supported on
  tier-1 gateways that are configured for distributed routing only.

1. With admin privileges, log in
   to NSX Manager.
2. Select NetworkingNetworking Profiles.
3. Click the Gateway
   QoS tab.
4. Click Add Gateway QoS
   Profiles.
5. Enter a name for the
   profile.
6. Enter the commited bandwidth
   limit that you want to set for the traffic.
7. Enter the burst size. Use the
   following guidelines for burst size.

   - B is the
     burst size in bytes.
   - R is the
     committed rate (or bandwidth) in Mbps.
   - I is the
     time interval in milliseconds, to refill or withdraw tokens(in bytes)
     from the token bucket. Use the get dataplane command
     from the NSX Edge CLI to
     retrieve the time interval, Qos\_wakeup\_interval\_ms.
     The default value for Qos\_wakeup\_interval\_ms is 50ms.
     However, this value is automatically adjusted by the dataplane based on
     the QoS configuration.

   The constraints for burst size
   are:
   - B >= R \*
     1000,000 \* I / 1000 / 8 because burst size is the
     maximum amount of tokens that can be refilled in each interval.
   - B >= R \*
     1000,000 \* 1 / 1000 / 8 because the minimum value for
     I is 1 ms, taking into account dataplane CPU
     usage among other constraints.
   - B >= MTU of
     SR port because at least the MTU-size amount of tokens
     need to be present in the token bucket for an MTU-size packet to
     pass rate-limiting check.Since the burst size needs to satisfy all three constraints, the
   configured value of burst size would
   be:

   ```
   Max (R * 1000,000 * I / 1000 / 8, R * 1000,000 * 1 / 1000 / 8, MTU)
   ```

   For example, if R = 100 Mbps, I = 50
   ms, and MTU = 1500, then

   ```
   B >= max (100 * 1000,000 * 50 / 1000/ 8, 100 * 1000,000 * 1 / 1000/ 8, 1500) = 625000 in bytes
   ```
8. Click
   Save.