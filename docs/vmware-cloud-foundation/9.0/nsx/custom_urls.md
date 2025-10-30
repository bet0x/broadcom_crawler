---
source_url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/inventory/attribute-types/custom-urls.html
product: vmware-cloud-foundation
version: 9.0
section: NSX
breadcrumb: NSX > Custom URLs
---

# Custom URLs

Custom URLs are used in L7 access profiles as an attribute type for URL filtering,
and context profiles.

NSX allows users to configure full or partial domain or URL with
special characters. The following image depicts different elements of a URL (Uniform
Resource Locator).

![""](/content/broadcom/techdocs/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/_jcr_content/assetversioncopies/d7889f5e-4b50-45bf-8f95-bd9fe31f2611.original.png)

NSX supports the following
custom URL patterns:

- Only IANA registered Top Level
  Domain (TLD), and wildcard characters \* and ^ are supported.
- Entered URL should be a valid URL.
  For example, www...google+com will be rejected.
- Do not include http://, https://,
  ftp://, etc.
- Users must enter a domain name, but
  may optionally include URI as well. For example, google.com and google.com/news
  are valid, but /news is invalid input.
- URI must not include query
  parameters. For example, www./google.com/query?keyboard=news will be rejected.
- Special characters \* and ^ can be
  used for wildcard matching both in the domain name and the URI path. \* will
  match one or more words where as ^ will match exactly one word. For example,
  \*.google.com will match news.google.com and also local.news.google.com. However,
  ^ will only match news.google.com, but will not match local.news.google.com.
  Similarly, google.com/\* will match google.com/news and also
  google.com/news/sanjose. However, google.com/^ will only match google.com/news,
  but will not match google.com/news/sanjose.
- \* and ^ match only full words, they
  cannot be used to match partial words. For example, \*google.com cannot be used
  to match mygoogle.com. However, \*.google.com can be used to match my.google.com.
  Similarly, google.com/\*news and google.com/n\* are invalid and will be
  rejected.
- \* and ^ can appear more than once
  in the URL. For example, \*.google.\* and \*.google.com/^/news/\* are valid.
- As ^ matches only a single word,
  two ^s back to back is allowed. For example, ^.^.google.com is valid and matches
  local.news.google.com, but does not match my.local.news.google.com or
  news.google.com. Similarly, google.com/^/^ is valid and matches
  google.com/news/sanjose, but does not match google.com/news or
  google.com/news/sanjose/today.
- When entering just the domain name
  (without URI), user may enter the domain name with a / at the end or without it
  and they have different behavior. If the user enters without an ending /, then
  it is treated as a partial match. For example, \*.google.com will match
  news.google.com, news.google.com.us, news.google.com.us/,
  news.google.com.us/local, etc. If the user enters the domain name with a / at
  the end, then it is treated as an exact match. For example, \*.google.com/ will
  match news.google.com and news.google.com/, but will not match
  news.google.com.us or news.google.com/local.
- When the entered URL has a path,
  then the presence of / at the end is not treated in any special way and the URL
  is treated as an exact match. For example, google.com/news/ will only match
  google.com/news/, but will not match google.com/news or google.com/newslatest or
  google.com/news/latest.
- URL matching can be used to match
  HTTP URL (Host header + URI) or TLS SNI. If the user specified URL has a path,
  it will not match the TLS SNI. However, if TLS Inspection is enabled and the
  traffic is decrypted, then the internal HTTP URL can be used for matching URL
  with path. For example, \*.google.com and \*.google.com/ can match HTTP URL or TLS
  SNI (without TLS Inspection), but \*.google.com/news will not match TLS SNI
  (without TLS Inspection).

## Examples

| User Input | Example |
| --- | --- |
| espn.com | Matches: espn.com, espn.com/, espn.com.us, espn.com.us/, espn.com/sports, espn.com.us/sports/p Does not match: premium.espn.com |
| espn.com/ | Matches: espn.com, espn.com/ Does not match: premium.espn.com, espn.com.us, espn.com.us/, espn.com/sports, espn.com.us/sports/ |
| espn.com/sports | Matches: espn.com/sports Does not match: espn.com/sportsnba, esp.com/sports/, espn.com/sports/nba |
| espn.com/sports/ | Matches: espn.com/sports Does not match: esp.com/sports, espn.com/sports/nba |
| \*espn.com | Matches: premium.espn.com, replay.preimum.espn.com, instant.replay.premium.espn.com, premium.espn.com/, premium.espn.com.us, premium.espn.com.us/, premium.espn.com/sports, premium.espn.com.us/sports Does not match: espn.com, .espn.com |
| \*.espn.\* | Matches: www.espn.com, premium.espn.com, www.espn.us, premium.espn.com.us/, latest.espn.com/sports, www.espn.com.us/sports/ replay.premium.espn.com, instant.replay.premium.espn.com instant.replay.premium.espn.com.us/ Does not match: espn.com, www.espn |
| espn.\*.us/ | Matches: espn.news.us, espn.news.us/, espn.local.news.us Does not match: espn.us, www.espn.us, espn.news.us/sports |
| \*.espn.\*/\* | Matches: www.espn.com/sports, replay.premium.espn.com.us/sports/nba/ Does not match: www.espn.com, www.espn.com/ |
| ^.espn.com | Matches: www.espn.com, www.espn.com/, www.espn.com/sports, www.espn.com.us/ Does not match: espn.com, news.local.espn.com |
| ^.espn.^ | Matches: www.espn.com, www.espn.com/,www.espn.com.us, www.espn.com.us/sports Does not match: news.local.espn.com, www.espn.com.us |
| espn.^/ | Matches: espn.com, espn.com/ Does not match: espn.com.us, espn.com/sports |
| www.^.^.com/^/^ | Matches www.local.espn.com/sports/nba Does not match www.personal.local.espn.com/sports/nba, www.local.espn.com/sports/nba/ |