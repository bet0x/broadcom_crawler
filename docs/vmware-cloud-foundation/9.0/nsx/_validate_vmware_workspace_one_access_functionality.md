---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/authentication-and-authorization/integration-with-vmware-identity-manager-workspace-one-access/validate-vmware-identity-manager-functionality.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX >  Validate VMware Workspace ONE Access Functionality
---

# Validate VMware Workspace ONE Access Functionality

After configuring VMware Workspace ONE Access, validate the functionality.

Unless Workspace ONE Access is properly configured and validated, some users may receive Not Authorized (Error Code 98) messages when trying to log in.

1. Create a base64 encoding of the username and password.

   Run the following command to get the encoding and remove the trailing '\n' character. For example:

   ```
   echo -n '[email protected]:password1234!' | base64 | tr -d '\n'
   c2ZhZG1pbkBhZC5ub2RlLmNvbTpwYXNzd29yZDEyMzQhCg==
   ```
2. Verify that each user can make API call to each node.

   Use a Remote Authorization curl command: curl -k -H 'Authorization: Remote <base64 encoding string>' https://<node FQDN>/api/v1/node/aaa/auth-policy. For example:

   ```
   curl -k -H 'Authorization: Remote c2ZhZG1pbkBhZC5ub2RlLmNvbTpwYXNzd29yZDEyMzQhCg==' /
   https://tmgr1.cptroot.com/api/v1/node/aaa/auth-policy
   ```

   This returns the authorization policy settings, such as:

   ```
   {
     "_schema": "AuthenticationPolicyProperties",
     "_self": {
       "href": "/node/aaa/auth-policy",
       "rel": "self"
     },
     "api_failed_auth_lockout_period": 900,
     "api_failed_auth_reset_period": 900,
     "api_max_auth_failures": 5,
     "cli_failed_auth_lockout_period": 900,
     "cli_max_auth_failures": 5,
     "minimum_password_length": 12
   }
   ```

   If the command does not return an error, Workspace ONE Access is working correctly. No further steps are required. If the curl command returns an error, the user may be locked out.

   Account lockout policies are set set and enforced on a per node basis. If one node in the cluster has locked out a user, other nodes may have not.
3. To reset a user lockout on a node:
   1. Retrieve the authorization policy using the local NSX Manager admin user:

      ```
      curl -k -u 'admin:<password>' https://nsxmgr/api/v1/node/aaa/auth-policy
      ```
   2. Save the output to a JSON file in current working directory.
   3. Modify the file to change lockout period settings.

      For example, many of the default settings apply lockout and reset periods of 900 seconds. Change these values to enable immediate reset, such as:

      ```
      {
        "_schema": "AuthenticationPolicyProperties",
        "_self": {
          "href": "/node/aaa/auth-policy",
          "rel": "self"
        },
        "api_failed_auth_lockout_period": 1,
        "api_failed_auth_reset_period": 1,
        "api_max_auth_failures": 5,
        "cli_failed_auth_lockout_period": 1,
        "cli_max_auth_failures": 5,
        "minimum_password_length": 12
      }
      ```
   4. Apply the change to the affected node.

      ```
      curl -k -u 'admin:<password>' -H 'Content-Type: application/json' -d \
      @<modified_policy_setting.json> https://nsxmgr/api/v1/node/aaa/auth-policy
      ```
   5. Return the authorization policy settings files to its previous settings.

   This should resolve the lockout issue. If you can still make remote auth API calls, but are still unable to log in through the browser, the browser may have an invalid cache or cookie stored. Clear your cache and cookies, and try again.