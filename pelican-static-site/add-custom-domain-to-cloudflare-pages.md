


I will set up a custom domain so I can use a domain name of my choice, instead of the domain *pages.dev*.

# Custom domain setup

I purchase and manage my domains using [hover.com](https://www.hover.com). Hover offers an easy-to-use domain fowarding service. However, after the user is forwarded from my Hover-managed domain to Cloudflare Pages, the URL displayed by the browser changes to the Cloudflare URL. I want my URL, *learningwithcode.com* to remain visible on the browser. So, I will use the more standard method of modifying DNS information.

Cloudflare wrote a good document that tells you [how to modify your domain provider's and Cloudflare's DNS information](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/) so that a URL managed by another provider will point to a Cloudflare Pages site. the procedure is summarized below:

1. Temporarily [disable DNSSEC](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/#before-you-begin) on hover.com, or at your domain registrar. Cloudflare offers link to [provider-specific instructions for disabling DNSSEC](https://help.hover.com/hc/en-us/articles/217281647-Understanding-and-managing-DNSSEC).
2. [Add your domain](https://developers.cloudflare.com/fundamentals/get-started/setup/add-site/#step-1--add-site-in-cloudflare) in the Cloudflare Dashboard
3. [Update nameservers]() on hover.com with the [CLoudflare nameserver information](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/#update-your-nameservers), or at your domain registrar
4. [Set up your SSL certificate](https://developers.cloudflare.com/ssl/get-started/) at Cloudflare Pages
5. [Re-enable DNSSEC on hover.com](https://help.hover.com/hc/en-us/articles/217281647-DNSSEC-services#:~:text=How%20to%20setup%20DNSSEC%3F%201%20Sign%20in%20to,your%20DNS%20hosting%20provider%20and%20click%20Add%20record.), or at your domain registrar.


## Temporarily disable DNSSEC on your domain

In my case, [I disabled DNSSEC on my domain at hover.com](https://help.hover.com/hc/en-us/articles/217281647-Understanding-and-managing-DNSSEC#h_f2d54352-35c2-4e7b-919b-60235407fea2).

* I signed into my [Hover control panel](https://hover.com/signin) 
* In the list of domains, I clicked on the domain I wish to configure, *learningwithcode.com*.
* In the domain's *Advanced* page, I clicked *Edit* from the DNSSEC section for current settings.
* I clicked *Clear Fields* to remove the DNSSEC.
* I clicked *Save*.

## Add your domain to Cloudflare

* I logged into my [Cloudflare dashboard](https://dash.cloudflare.com/login).
* In the top navigation bar, I clicked *Add site*.
* I entered my website’s root domain, *learningwithcode.com*, and then clicked *Add Site*.
* Select your [plan level](https://www.cloudflare.com/plans/#compare-features). I chose the Free plan level.
* Review your DNS records. When you add a new site to Cloudflare, Cloudflare automatically scans for common records and adds them to the DNS zone. The records show up under the respective zone DNS > Records page.

## Update your domain's records in your registrar's dashboard

Cloudflare assigned my domain [two nameservers](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/#update-your-nameservers). I added the Cloudflare [nameservers to the domain records](https://help.hover.com/hc/en-us/articles/217282477--Changing-your-domain-nameservers#:~:text=Adjusting%20nameservers%20for%20a%20single%20domain%201%20Sign,Save%20nameservers%20to%20push%20through%20the%20changes.%20) at my registrar, *hover.com*.

* I signed into my [Hover control panel](https://hover.com/signin) 
* In the list of domains, I clicked on the domain I wish to configure, *learningwithcode.com*.
* On the domain's *Overview* page, I went to nameservers on the left-hand side of the page and selected *Edit*.
* I entered the name server information from Cloudflare Pages in the pop-up window
* I clicked on *Save Nameservers*


## Set up an SSL Certificate for your Cloudflare Pages site

I [use *Universal SSL* for my domain at Cloudflare](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/). Cloudflare manages the SSL certificates for my domain as long as it is hosted on Cloudflare pages.

My web site it hosted by Cloudflare Pages so I automatically get Univeral SSL enabled. I don't have to change anything.

## Re-enable DNSSEC on your domain

First, get the information you need to set up DNSSEC at hover.com, or at your domain registrar:

* I logged into my [Cloudflare dashboard](https://dash.cloudflare.com/login).
* I selected my domain, *learningwithcode.com*
* I went to *DNS* > *Settings*.
* For *DNSSEC*, I clicked *Enable DNSSEC*.
* In the *Enable DNSSEC* dialog box, I took note of the values to I need to re-enableDNSSEC at hover.com. Then I closed the dialog.

Then, go to hover.com, or your domain registrar, and re-enable DNSSEC:

* I signed into my [Hover control panel](https://hover.com/signin) 
* In the list of domains, I clicked on the domain I wish to configure, *learningwithcode.com*.
* In the domain's *Advanced* page, I clicked on *Add a DNSSEC record*
* I added the settings 

## Set up custom domain for Cloudflare Pages site

To add a [custom domain for your Cloudflare Pages site](https://developers.cloudflare.com/pages/platform/custom-domains/):

* I logged into my [Cloudflare dashboard](https://dash.cloudflare.com/login).
* I selected *Workers & Pages* and selected my pages site, 
* Select your *Pages project* --> *Custom domains*.
* Select *Set up a domain*.
* I entered "learningwithcode.com" as domain to serve my Cloudflare Pages site and selected *Continue*.
  * I added a custom apex domain: *learningwithcode.com*
  * I added a custom subdomain: *www.learningwithcode.com*
