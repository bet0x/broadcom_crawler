---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/tier-0-gateways/using-regular-expressions-to-match-community-lists-when-adding-route-maps.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Using Regular Expressions to Match Community Lists When Adding Route Maps
---

# Using Regular Expressions to Match Community Lists When Adding Route Maps

You can use regular expressions to define the route-map match criteria for community
lists. BGP regular expressions are based on POSIX 1003.2 regular expressions.

The following expressions are a subset of the POSIX regular expressions.

| Expression | Description |
| --- | --- |
| .\* | Matches any single character. |
| \* | Matches 0 or more occurrences of pattern. |
| + | Matches 1 or more occurrences of pattern. |
| ? | Matches 0 or 1 occurrence of pattern. |
| ^ | Matches the beginning of the line. |
| $ | Matches the end of the line. |
| \_ | This character has special meanings in BGP regular expressions. It matches to a space, comma, AS set delimiters { and } and AS confederation delimiters ( and ). It also matches to the beginning of the line and the end of the line. Therefore this character can be used for an AS value boundaries match. This character technically evaluates to (^|[,{}()]|$). |

Here are some examples for using regular
expressions in route maps:

| Expression | Description |
| --- | --- |
| ^101 | Matches routes having community attribute that starts with 101. |
| ^[0-9]+ | Matches routes having community attribute that starts with a number between 0-9 and has one or more instances of such a number. |
| .\* | Matches routes having any or no community attribute. |
| .+ | Matches routes having any community value. |
| ^$ | Matches routes having no/null community value. |